# Study Tool

Practice math by topic with an unlimited supply of generated questions, checked by a computer algebra system, alongside notes for every topic.

It started as a way to study for a precalculus course: take a generated practice quiz every day, learn the next topic, and repeat until exam day. The content and the engine are kept separate, so new courses and topics can be added without changing the app.

## What it does

- **Unlimited practice.** Every topic has a generator that builds a fresh problem from a random seed, so you never run out of questions or memorize answers.
- **Multiple choice or typed answers.** Wrong choices come from real mistakes (forgetting the middle term of $(x+a)^2$, distributing a minus sign to only the first term, adding exponents instead of multiplying), so a wrong pick tells you something.
- **Answers checked by math, not string matching.** Typed answers go through [SymPy](https://www.sympy.org): `2(x+3)`, `2x+6` and `6 + 2*x` are all the same answer. When a question asks for a specific form, an equivalent but unfinished answer gets told what's missing ("multiply everything out", "the radicand 72 still has a perfect square factor").
- **Daily review.** A quiz across everything covered so far, weighted toward the topics you miss most.
- **Practice exams.** Exam conditions: a countdown (60 minutes by default), a pace indicator, no feedback until you finish, and an automatic finish when time runs out. Each exam is judged on score *and* time, so a perfect score that runs over the limit doesn't count as ready.
- **Notes for every topic.** Lessons in Markdown with LaTeX, rendered with KaTeX, linked from every question.
- **Progress tracking.** Accuracy and average time per topic, plus a history of practice exams, so weak and slow spots are easy to see and drill.

## Running it

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
uvicorn studytool.main:app --reload
```

Then open <http://localhost:8000>. Your history is stored locally in `data/history.db`.

Run the tests with `pytest`. The generator tests build 80 problems for every topic and check that the right answer is accepted (typed and multiple choice), every wrong choice is rejected, and generation is reproducible.

## How it works

```
content/precalc/          course outline (course.json) + one Markdown lesson per module
studytool/
  core/
    problem.py            Problem + Spec models, the generator registry
    checker.py            parses typed answers, checks equivalence and answer form
    symbols.py            shared symbols and LaTeX helpers
  generators/             one generator per topic, grouped by module
  quiz.py                 picks topics (with adaptive weighting), seeds and formats
  history.py              SQLite attempt log
  main.py                 FastAPI app
  web/                    frontend: plain HTML/CSS/JS, KaTeX and marked vendored for offline use
docs/problem-types.md     generator specs: templates, answer formats, common mistakes
```

**Problems are stateless.** A problem's id is `"<topic>:<seed>"`, and generators are deterministic, so the server never stores a quiz. To check an answer it rebuilds the problem from the id.

**Adding a topic** takes a generator function and one line in `course.json`:

```python
@generator("square-roots", "Square roots")
def square_roots(rng: random.Random) -> Spec:
    root = rng.randint(2, 15)
    return Spec(
        prompt=f"Find $\\sqrt{{{root * root}}}$.",
        answer=f"${root}$",
        kind="numbers",
        expected=[root],
        distractors=[[-root], [root, -root], [2 * root]],
        explanation=f"${root}^2 = {root * root}$, and $\\sqrt{{\\ }}$ means the positive root.",
    )
```

The registry handles the rest: shuffling choices, removing distractors that turn out to be equivalent to the answer, and filling in near-misses if a generator comes up short.

## API

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/api/course` | Course outline: sections, modules, topics |
| `GET` | `/api/modules/{id}/content` | Lesson Markdown for a module |
| `GET` | `/api/quiz?topics=a,b&count=10&mode=mixed&adaptive=true` | Generate a quiz (answers not included) |
| `POST` | `/api/check` | Check an answer, log the attempt, return the explanation |
| `POST` | `/api/preview` | Render typed input as LaTeX while you type |
| `GET` | `/api/stats` | Accuracy and average time per topic, days studied |
| `POST` | `/api/sessions` | Log a finished quiz or exam (score, duration, time limit) |
| `GET` | `/api/sessions?kind=exam` | Practice exam history |

Interactive docs are at `/docs` while the server is running.

## Course content

Everything in `content/` is original writing: explanations, examples and practice questions written for this project. Topic coverage follows a typical precalculus sequence.

Current coverage, Section 1 (Foundations of Algebra and Functions):

1. Polynomials and Exponents
2. Algebraic Expressions and Equations
3. Functions and Composition
4. Inverse Functions
