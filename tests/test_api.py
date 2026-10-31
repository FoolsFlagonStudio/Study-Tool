import os

os.environ["STUDYTOOL_DB"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

from studytool.content import topics  # noqa: E402
from studytool.core.problem import get_problem  # noqa: E402
from studytool.main import app, history  # noqa: E402

client = TestClient(app)


def test_every_outline_topic_has_a_generator():
    missing = [t for t, info in topics().items() if not info["has_generator"]]
    assert not missing


def test_module_content_served():
    course = client.get("/api/course").json()
    for section in course["sections"]:
        for module in section["modules"]:
            text = client.get(f"/api/modules/{module['id']}/content").text
            assert text.startswith("---") and "# Module" in text
            for topic in module["topics"]:
                assert f"## {topic['heading']}" in text, topic


def test_quiz_check_and_stats_round_trip():
    history.reset()
    quiz = client.get("/api/quiz", params={"topics": "laws-of-exponents,square-roots", "count": 6, "mode": "mc", "seed": 1}).json()
    problems = quiz["problems"]
    assert len(problems) == 6
    for item in problems:
        assert "answer" not in item and item["format"] == "mc" and len(item["choices"]) == 4
        answer = get_problem(item["id"]).spec.answer
        result = client.post("/api/check", json={"problem_id": item["id"], "format": "mc", "response": answer}).json()
        assert result["correct"] and result["explanation"]

    stats = client.get("/api/stats").json()
    assert stats["attempts"] == 6 and stats["accuracy"] == 1


def test_invalid_input_is_not_recorded():
    history.reset()
    item = client.get("/api/quiz", params={"topics": "combining-like-terms", "count": 1, "mode": "input"}).json()["problems"][0]
    result = client.post("/api/check", json={"problem_id": item["id"], "format": "input", "response": "x +* )"}).json()
    assert result["valid"] is False and result["answer"] is None
    assert client.get("/api/stats").json()["attempts"] == 0


def test_unsimplified_answer_gets_feedback():
    problem = get_problem("multiplying-polynomials:3")
    unexpanded = problem.spec.prompt.split("$")[1]  # the product as written, e.g. (x + 1)(...)
    typed = unexpanded.replace("{", "(").replace("}", ")").replace("^", "^").replace("\\", "")
    result = client.post("/api/check", json={"problem_id": problem.id, "format": "input", "response": typed, "record": False}).json()
    assert result["correct"] is False and "Multiply everything out" in result["feedback"], (typed, result)


def test_adaptive_weights_favor_missed_topics():
    from studytool.quiz import topic_weights

    stats = {"a": {"recent_accuracy": 1.0}, "b": {"recent_accuracy": 0.2}}
    weights = topic_weights(["a", "b", "c"], stats)
    assert weights["b"] > weights["c"] > weights["a"]


def test_preview():
    assert client.post("/api/preview", json={"text": "x^(3/4)"}).json()["latex"] == "x^{\\frac{3}{4}}"
    assert client.post("/api/preview", json={"text": "import os"}).json()["error"]
