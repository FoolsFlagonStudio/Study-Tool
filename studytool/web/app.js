"use strict";

/* Study Tool frontend: plain JS, no build step.
   Views: Practice (setup -> quiz -> results), Notes, Progress. */

const $ = (sel, root = document) => root.querySelector(sel);
const el = (tag, attrs = {}, ...children) => {
  const node = document.createElement(tag);
  for (const [key, val] of Object.entries(attrs)) {
    if (key === "class") node.className = val;
    else if (key === "html") node.innerHTML = val;
    else if (key.startsWith("on")) node.addEventListener(key.slice(2), val);
    else if (val !== false && val != null) node.setAttribute(key, val === true ? "" : val);
  }
  for (const child of children.flat()) {
    if (child != null) node.append(child.nodeType ? child : document.createTextNode(child));
  }
  return node;
};

const store = {
  get(key, fallback) {
    try { const raw = localStorage.getItem(`studytool:${key}`); return raw == null ? fallback : JSON.parse(raw); }
    catch { return fallback; }
  },
  set(key, val) {
    try { localStorage.setItem(`studytool:${key}`, JSON.stringify(val)); } catch { /* private mode */ }
  },
};

async function api(path, options = {}) {
  const res = await fetch(path, {
    headers: options.body ? { "Content-Type": "application/json" } : {},
    ...options,
    body: options.body ? JSON.stringify(options.body) : undefined,
  });
  if (!res.ok) {
    const detail = await res.json().catch(() => ({}));
    throw new Error(typeof detail.detail === "string" ? detail.detail : `Request failed (${res.status})`);
  }
  return res.headers.get("content-type")?.includes("json") ? res.json() : res.text();
}

/* ---------------------------------------------------------------- markdown + math */

function slug(text) {
  return text.toLowerCase().replace(/<[^>]+>/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
}

function tex(source, displayMode = false) {
  return katex.renderToString(source, { displayMode, throwOnError: false });
}

const CALLOUT_TITLES = {
  tip: "Tip", warning: "Watch out", example: "Example", note: "Note", info: "Why this matters",
  abstract: "Steps", check: "Show answer",
};

/** Markdown with $math$, $$display math$$ and Obsidian-style callouts. */
function renderMarkdown(source, { inline = false } = {}) {
  const saved = [];
  const keep = (html) => `%%K${saved.push(html) - 1}%%`;

  let text = source.replace(/^---\n[\s\S]*?\n---\n/, ""); // front matter
  text = text.replace(/\\\$/g, "%%DOLLAR%%");
  text = text.replace(/\$\$([\s\S]+?)\$\$/g, (_, m) => keep(tex(m.trim(), true)));
  text = text.replace(/\$([^$\n]+?)\$/g, (_, m) => keep(tex(m)));

  if (!inline) text = renderCallouts(text, keep);

  let html = inline ? marked.parseInline(text) : marked.parse(text);
  html = html.replace(/<p>(%%K\d+%%)<\/p>/g, "$1");
  for (let pass = 0; pass < 3 && html.includes("%%K"); pass++) {
    html = html.replace(/%%K(\d+)%%/g, (_, i) => saved[Number(i)]);
  }
  return html.replace(/%%DOLLAR%%/g, "$");
}

function renderCallouts(text, keep) {
  const lines = text.split("\n");
  const out = [];
  for (let i = 0; i < lines.length; i++) {
    const head = lines[i].match(/^>\s*\[!(\w+)\]([-+]?)\s*(.*)$/);
    if (!head) { out.push(lines[i]); continue; }
    const body = [];
    while (i + 1 < lines.length && lines[i + 1].startsWith(">")) body.push(lines[++i].replace(/^>\s?/, ""));
    const [, type, fold, title] = head;
    const label = title || CALLOUT_TITLES[type] || type;
    const inner = marked.parse(body.join("\n"));
    const html = fold === "-"
      ? `<details class="callout c-${type}"><summary>${marked.parseInline(label)}</summary>${inner}</details>`
      : `<div class="callout c-${type}"><div class="callout-title">${marked.parseInline(label)}</div>${inner}</div>`;
    out.push("", keep(html), "");
  }
  return out.join("\n");
}

/* ---------------------------------------------------------------- state */

const state = {
  course: null,
  topics: {},         // id -> topic
  modules: [],
  quiz: null,         // { problems, index, results, startedAt, timeLimit, exam, ... }
  notesModule: null,
};

/* ---------------------------------------------------------------- routing */

function show(view) {
  for (const section of document.querySelectorAll(".view")) section.hidden = section.id !== `view-${view}`;
  for (const link of document.querySelectorAll("[data-view]")) {
    link.toggleAttribute("aria-current", link.dataset.view === view);
    if (link.dataset.view === view) link.setAttribute("aria-current", "page");
  }
  if (view === "progress") renderProgress();
  if (view === "notes" && !state.notesModule) openNotes(state.modules[0].id);
}

function route() {
  const [view, ...rest] = location.hash.slice(1).split("/");
  if (view === "notes" && rest[0]) {
    show("notes");
    openNotes(rest[0], rest[1]);
    return;
  }
  show(["practice", "notes", "progress"].includes(view) ? view : "practice");
}

/* ---------------------------------------------------------------- setup */

function selectedTopics() {
  return [...document.querySelectorAll("#topic-picker input[data-topic]:checked")].map((box) => box.dataset.topic);
}

function renderSetup() {
  const saved = new Set(store.get("topics", []));
  const picker = $("#topic-picker");
  picker.replaceChildren();
  for (const module of state.modules) {
    const boxes = module.topics.map((topic) =>
      el("label", {},
        el("input", { type: "checkbox", "data-topic": topic.id, checked: saved.has(topic.id), onchange: saveSetup }),
        topic.title));
    const toggle = el("button", {
      class: "quiet", type: "button",
      onclick: () => {
        const inputs = picker.querySelectorAll(`[data-module="${module.id}"] input`);
        const allOn = [...inputs].every((i) => i.checked);
        inputs.forEach((i) => { i.checked = !allOn; });
        saveSetup();
      },
    }, "Select all");
    picker.append(el("div", { class: "picker-module", "data-module": module.id },
      el("header", {}, el("h3", {}, `Module ${module.number} `, el("span", {}, module.title)), toggle),
      el("div", { class: "topic-grid" }, boxes)));
  }

  const current = $("#current-module");
  current.replaceChildren(...state.modules.map((m) => el("option", { value: m.id }, `Module ${m.number}: ${m.title}`)));
  current.value = store.get("currentModule", state.modules[state.modules.length - 1].id);
  current.onchange = saveSetup;

  $("#count").value = store.get("count", 10);
  const mode = store.get("mode", "mixed");
  const radio = document.querySelector(`input[name="mode"][value="${mode}"]`);
  if (radio) radio.checked = true;
  $("#adaptive").checked = store.get("adaptive", false);
  const exam = examSettings();
  $("#exam-count").value = exam.count;
  $("#exam-minutes").value = exam.minutes;
  $("#exam-target").value = exam.target;
  for (const input of document.querySelectorAll("#setup input")) input.addEventListener("change", saveSetup);
}

function saveSetup() {
  store.set("topics", selectedTopics());
  store.set("currentModule", $("#current-module").value);
  store.set("count", Number($("#count").value) || 10);
  store.set("mode", document.querySelector('input[name="mode"]:checked').value);
  store.set("adaptive", $("#adaptive").checked);
  store.set("exam", {
    count: clamp(Number($("#exam-count").value) || 30, 5, 100),
    minutes: clamp(Number($("#exam-minutes").value) || 60, 5, 240),
    target: clamp(Number($("#exam-target").value) || 80, 1, 100),
  });
}

function examSettings() {
  return { count: 30, minutes: 60, target: 80, ...store.get("exam", {}) };
}

function clamp(val, lo, hi) {
  return Math.min(hi, Math.max(lo, val));
}

function quizCount() {
  return clamp(Number($("#count").value) || 10, 1, 50);
}

/** Seconds as m:ss (or h:mm:ss). */
function clock(totalSeconds) {
  const secs = Math.max(0, Math.round(totalSeconds));
  const h = Math.floor(secs / 3600);
  const m = Math.floor((secs % 3600) / 60);
  const s = String(secs % 60).padStart(2, "0");
  return h ? `${h}:${String(m).padStart(2, "0")}:${s}` : `${m}:${s}`;
}

async function startQuiz({ topics, adaptive, mode, count, kind = "custom", timeLimit = null, target = null, errorEl = $("#setup-error") }) {
  errorEl.textContent = "";
  if (!topics.length) {
    errorEl.textContent = "Pick at least one topic to practice.";
    return;
  }
  try {
    const params = new URLSearchParams({ topics: topics.join(","), count, mode, adaptive });
    const { problems } = await api(`/api/quiz?${params}`);
    state.quiz = {
      problems, topics, kind, timeLimit, target,
      exam: kind === "exam",
      index: 0,
      results: [],
      startedAt: Date.now(),
      questionStartedAt: Date.now(),
      finished: false,
      timedOut: false,
    };
    location.hash = "practice";
    $("#setup").hidden = true;
    $("#results").hidden = true;
    $("#quiz").hidden = false;
    $("#quit").textContent = state.quiz.exam ? "Finish exam now" : "End quiz";
    startTimer();
    renderQuestion();
  } catch (err) {
    errorEl.textContent = err.message;
  }
}

function coveredTopics() {
  const current = $("#current-module").value;
  const upTo = state.modules.findIndex((m) => m.id === current);
  return state.modules.slice(0, upTo + 1).flatMap((m) => m.topics.map((t) => t.id));
}

/* ---------------------------------------------------------------- quiz */

let timerHandle = null;

function elapsedSeconds() {
  return (Date.now() - state.quiz.startedAt) / 1000;
}

function startTimer() {
  clearInterval(timerHandle);
  tick();
  timerHandle = setInterval(tick, 1000);
}

function tick() {
  const quiz = state.quiz;
  if (!quiz || quiz.finished) return;
  const elapsed = elapsedSeconds();
  const timer = $("#timer");
  const pace = $("#pace");
  if (!quiz.timeLimit) {
    timer.textContent = clock(elapsed);
    pace.textContent = "";
    return;
  }
  const left = quiz.timeLimit - elapsed;
  timer.textContent = `${clock(left)} left`;
  timer.classList.toggle("low", left < Math.min(600, quiz.timeLimit / 6));
  if (left <= 0) {
    quiz.timedOut = true;
    showResults();
    return;
  }
  // Pace: each question gets an equal share of the time limit.
  const budget = quiz.timeLimit / quiz.problems.length;
  const done = quiz.results.filter(Boolean).length;
  const behind = elapsed - (done + 1) * budget;
  const ahead = done * budget - elapsed;
  pace.classList.toggle("behind", behind > 0);
  pace.textContent = behind > 0 ? `${clock(behind)} behind pace` : ahead > 0 ? `${clock(ahead)} ahead of pace` : "On pace";
}

function renderBubbles() {
  const { problems, index, results, exam } = state.quiz;
  $("#bubbles").replaceChildren(...problems.map((_, i) => {
    const result = results[i];
    let cls = "";
    let label = i === index ? "current" : "not answered";
    if (result?.skipped) { cls = "skipped"; label = "skipped"; }
    else if (result && exam) { cls = "answered"; label = "answered"; }
    else if (result) { cls = result.correct ? "right" : "wrong"; label = result.correct ? "correct" : "missed"; }
    if (i === index && !result) cls = "current";
    return el("li", { class: `bubble ${cls}`, "aria-label": `Question ${i + 1}, ${label}` }, String(i + 1));
  }));
}

function renderQuestion() {
  const { problems, index, exam } = state.quiz;
  const problem = problems[index];
  const topic = state.topics[problem.topic];
  const last = index === problems.length - 1;
  state.quiz.questionStartedAt = Date.now();
  renderBubbles();
  tick();

  const sheet = $("#question");
  sheet.replaceChildren();
  sheet.append(
    el("div", { class: "question-meta" },
      el("span", {}, problem.topic_title),
      topic && !exam ? el("a", { href: `#notes/${topic.module}/${slug(topic.heading)}` }, "Read the notes on this") : null),
    el("div", { class: "prompt", html: renderMarkdown(problem.prompt) }),
  );

  const actions = el("div", { class: "actions" });
  const label = exam ? (last ? "Finish exam" : "Next question") : "Check answer";
  const checkBtn = el("button", { class: "primary", type: "button", disabled: true }, label);
  const notice = el("p", { class: "notice", role: "alert" });
  let getResponse;

  if (problem.format === "mc") {
    let picked = null;
    const buttons = problem.choices.map((choice, i) => {
      const btn = el("button", {
        class: "choice", type: "button", role: "radio", "aria-checked": "false",
        onclick: () => {
          picked = choice;
          buttons.forEach((b) => b.setAttribute("aria-checked", String(b === btn)));
          checkBtn.disabled = false;
        },
      }, el("span", { class: "bubble", "aria-hidden": "true" }, "ABCD"[i]), el("span", { class: "choice-text", html: renderMarkdown(choice, { inline: true }) }));
      btn.dataset.choice = choice;
      return btn;
    });
    sheet.append(el("div", { class: "choices", role: "radiogroup", "aria-label": "Answer choices" }, buttons));
    getResponse = () => picked;
  } else {
    const input = el("input", {
      class: "answer-input", type: "text", autocomplete: "off", spellcheck: "false",
      "aria-label": "Your answer", placeholder: problem.input_hint || "Type your answer",
    });
    const preview = el("div", { class: "preview", "aria-live": "polite" });
    let debounce;
    input.addEventListener("input", () => {
      checkBtn.disabled = !input.value.trim();
      clearTimeout(debounce);
      debounce = setTimeout(async () => {
        if (!input.value.trim()) { preview.replaceChildren(); return; }
        const { latex, error } = await api("/api/preview", { method: "POST", body: { text: input.value } });
        preview.innerHTML = latex ? `Reads as ${tex(latex)}` : error ? `<span>${error}</span>` : "";
      }, 250);
    });
    sheet.append(el("div", { class: "answer-row" }, input, preview));
    getResponse = () => input.value;
    setTimeout(() => input.focus(), 0);
  }

  checkBtn.addEventListener("click", () => submitAnswer(problem, getResponse(), { sheet, actions, notice, checkBtn }));
  actions.append(checkBtn);
  if (exam) {
    actions.append(el("button", {
      class: "quiet", type: "button",
      onclick: () => {
        state.quiz.results[state.quiz.index] = { skipped: true, correct: false, problem, seconds: questionSeconds() };
        advance();
      },
    }, "Skip"));
  }
  sheet.append(notice, actions);
}

function questionSeconds() {
  return (Date.now() - state.quiz.questionStartedAt) / 1000;
}

async function submitAnswer(problem, response, ui) {
  if (response == null || !String(response).trim()) return;
  const quiz = state.quiz;
  const seconds = questionSeconds();
  ui.checkBtn.disabled = true;
  let result;
  try {
    result = await api("/api/check", { method: "POST", body: { problem_id: problem.id, format: problem.format, response, seconds } });
  } catch (err) {
    ui.notice.textContent = err.message;
    ui.checkBtn.disabled = false;
    return;
  }
  if (state.quiz !== quiz || quiz.finished) return; // time ran out while checking
  if (!result.valid) {
    ui.notice.textContent = result.feedback;  // couldn't read it - let them fix it, no penalty
    ui.checkBtn.disabled = false;
    return;
  }
  ui.notice.textContent = "";
  quiz.results[quiz.index] = { ...result, problem, response, seconds };

  if (quiz.exam) {
    advance();  // exam conditions: no feedback until the end
    return;
  }

  if (problem.format === "mc") {
    for (const btn of ui.sheet.querySelectorAll(".choice")) {
      btn.disabled = true;
      if (btn.dataset.choice === result.answer) btn.classList.add("is-answer");
      else if (btn.dataset.choice === response) btn.classList.add("is-wrong");
    }
  } else {
    ui.sheet.querySelector(".answer-input").readOnly = true;
  }

  const grade = el("div", { class: `grade ${result.correct ? "" : "wrong"}`, role: "status" },
    el("p", { class: "grade-mark" }, result.correct ? "✓ Nice." : "✗ Not quite."),
    result.feedback ? el("p", { class: "feedback" }, result.feedback) : null,
    result.correct ? null : el("p", { html: `Answer: ${renderMarkdown(result.answer, { inline: true })}` }),
    el("div", { html: renderMarkdown(result.explanation) }));
  ui.sheet.insertBefore(grade, ui.notice);

  const last = quiz.index === quiz.problems.length - 1;
  const next = el("button", { class: "primary", type: "button", onclick: last ? showResults : nextQuestion }, last ? "See results" : "Next question");
  ui.actions.replaceChildren(next);
  next.focus();
  renderBubbles();
}

function advance() {
  if (state.quiz.index === state.quiz.problems.length - 1) showResults();
  else nextQuestion();
}

function nextQuestion() {
  state.quiz.index += 1;
  renderQuestion();
  window.scrollTo({ top: 0 });
}

function endQuiz() {
  clearInterval(timerHandle);
  state.quiz = null;
  $("#quiz").hidden = true;
  $("#results").hidden = true;
  $("#setup").hidden = false;
}

function examVerdict({ score, target, duration, timeLimit, timedOut }) {
  const problems = [];
  if (score * 100 < target) problems.push(`below your ${target}% target`);
  if (timedOut) problems.push("ran out of time");
  else if (duration > timeLimit) problems.push("over the time limit");
  return problems.length
    ? { ready: false, text: `Not there yet: ${problems.join(" and ")}.` }
    : { ready: true, text: `Exam-ready pace: ${target}% target met with ${clock(timeLimit - duration)} to spare.` };
}

function showResults() {
  const quiz = state.quiz;
  if (!quiz || quiz.finished) return;
  quiz.finished = true;
  clearInterval(timerHandle);

  const { problems, results, timeLimit, timedOut, exam, target } = quiz;
  const duration = timeLimit ? Math.min(elapsedSeconds(), timeLimit) : elapsedSeconds();
  const answered = results.filter((r) => r && !r.skipped);
  const right = answered.filter((r) => r.correct).length;
  const score = right / problems.length;
  const unanswered = problems.length - answered.length;
  const timed = results.filter((r) => r && !r.skipped && r.seconds != null);
  const avgSeconds = timed.length ? timed.reduce((sum, r) => sum + r.seconds, 0) / timed.length : null;

  // Every question counts toward the topic score; unanswered ones as misses.
  const byTopic = {};
  problems.forEach((problem, i) => {
    const r = results[i];
    const entry = (byTopic[problem.topic] ??= { title: problem.topic_title, right: 0, total: 0, seconds: [] });
    entry.total += 1;
    entry.right += r?.correct ? 1 : 0;
    if (r && !r.skipped && r.seconds != null) entry.seconds.push(r.seconds);
  });
  const missed = problems.map((problem, i) => ({ problem, r: results[i] })).filter(({ r }) => !r?.correct);
  const missedTopics = [...new Set(missed.map(({ problem }) => problem.topic))];

  const timeLine = timeLimit
    ? timedOut
      ? `Time ran out with ${unanswered} ${unanswered === 1 ? "question" : "questions"} unanswered.`
      : `Finished in ${clock(duration)} of ${clock(timeLimit)}, with ${clock(timeLimit - duration)} to spare.`
    : `Finished in ${clock(duration)}.`;
  const paceLine = avgSeconds != null
    ? `Average ${clock(avgSeconds)} per question${timeLimit ? ` (the limit allows ${clock(timeLimit / problems.length)})` : ""}.`
    : "";
  const verdict = exam ? examVerdict({ score, target, duration, timeLimit, timedOut }) : null;

  const box = $("#results");
  box.replaceChildren(
    el("div", { class: "results-head" },
      el("div", { class: "score", "aria-label": `Score: ${right} out of ${problems.length}` }, `${right}/${problems.length}`),
      el("div", {},
        el("h1", {}, right === problems.length ? "Clean sheet." : missed.length ? "Here's what to work on." : "Quiz finished."),
        el("p", { class: "muted" }, `${Math.round(score * 100)}% correct. ${timeLine} ${paceLine}`),
        verdict ? el("p", { class: `verdict ${verdict.ready ? "ready" : "not-ready"}` }, verdict.text) : null)),
    el("table", { class: "breakdown" },
      el("thead", {}, el("tr", {}, el("th", {}, "Topic"), el("th", {}, "Score"), el("th", {}, "Avg time"), el("th", {}, ""))),
      el("tbody", {}, Object.entries(byTopic).map(([id, t]) => {
        const topic = state.topics[id];
        const avg = t.seconds.length ? t.seconds.reduce((a, b) => a + b, 0) / t.seconds.length : null;
        return el("tr", {},
          el("td", {}, t.title),
          el("td", { class: "num" }, `${t.right} / ${t.total}`),
          el("td", { class: "num" }, avg != null ? clock(avg) : ""),
          el("td", {}, t.right < t.total && topic ? el("a", { href: `#notes/${topic.module}/${slug(topic.heading)}` }, "Review notes") : ""));
      }))),
    missed.length ? el("h2", {}, exam ? "Missed and unanswered questions" : "Missed questions") : null,
    missed.length ? el("ol", { class: "missed" }, missed.map(({ problem, r }) =>
      el("li", {},
        el("div", { class: "label" }, problem.topic_title),
        el("div", { html: renderMarkdown(problem.prompt) }),
        el("p", {}, el("span", { class: "label" }, "You answered "),
          !r || r.skipped
            ? el("span", { class: "muted" }, r?.skipped ? "(skipped)" : "(not reached)")
            : el("span", { html: problem.format === "mc" ? renderMarkdown(r.response, { inline: true }) : escapeHtml(r.response) })),
        r?.answer
          ? [el("p", { html: `<span class="label">Answer </span>${renderMarkdown(r.answer, { inline: true })}` }),
             exam ? el("div", { class: "muted", html: renderMarkdown(r.explanation) }) : null]
          : el("p", {}, el("button", { class: "quiet", type: "button", onclick: (e) => revealAnswer(problem, e.currentTarget) }, "Show the answer"))))) : null,
    el("div", { class: "actions" },
      missedTopics.length ? el("button", {
        class: "primary", type: "button",
        onclick: () => startQuiz({ topics: missedTopics, adaptive: true, mode: "mixed", count: Math.max(5, missedTopics.length * 2), kind: "review" }),
      }, "Practice the missed topics") : null,
      el("button", { type: "button", onclick: endQuiz }, "Back to quiz setup")),
  );
  $("#quiz").hidden = true;
  box.hidden = false;
  window.scrollTo({ top: 0 });

  if (!answered.length) return; // abandoned before answering anything - don't log it
  api("/api/sessions", {
    method: "POST",
    body: {
      kind: quiz.kind, topics: quiz.topics, question_count: problems.length,
      answered: answered.length, correct: right, duration_seconds: duration,
      time_limit_seconds: timeLimit, timed_out: timedOut,
    },
  }).catch(() => { /* history is best-effort */ });
}

/** Unanswered questions have no checked answer yet - fetch it without logging an attempt. */
async function revealAnswer(problem, button) {
  const fmt = problem.format;
  const probe = fmt === "mc" ? problem.choices[0] : "0";
  const result = await api("/api/check", { method: "POST", body: { problem_id: problem.id, format: fmt, response: probe, record: false } });
  button.parentElement.replaceWith(
    el("p", { html: `<span class="label">Answer </span>${renderMarkdown(result.answer ?? "", { inline: true })}` }),
    el("div", { class: "muted", html: renderMarkdown(result.explanation ?? "") }));
}

function escapeHtml(text) {
  return String(text).replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));
}

/* ---------------------------------------------------------------- notes */

async function openNotes(moduleId, anchor) {
  const module = state.modules.find((m) => m.id === moduleId) || state.modules[0];
  const body = $("#notes-body");
  if (state.notesModule !== module.id) {
    const markdown = await api(`/api/modules/${module.id}/content`);
    body.innerHTML = renderMarkdown(markdown);
    for (const heading of body.querySelectorAll("h2")) heading.id = slug(heading.textContent);
    state.notesModule = module.id;
  }
  renderModuleList(module, body);
  if (anchor) document.getElementById(anchor)?.scrollIntoView();
  else window.scrollTo({ top: 0 });
}

function renderModuleList(active, body) {
  const list = $("#module-list");
  list.replaceChildren(el("h2", {}, "Modules"), el("ol", {}, state.modules.map((m) => {
    const item = el("li", {}, el("a", { href: `#notes/${m.id}`, "aria-current": m.id === active.id ? "true" : "false" }, `${m.number}. ${m.title}`));
    if (m.id === active.id) {
      item.append(el("ol", { class: "toc" }, [...body.querySelectorAll("h2")].map((h) =>
        el("li", {}, el("a", { href: `#notes/${m.id}/${h.id}` }, h.textContent)))));
    }
    return item;
  })));
}

/* ---------------------------------------------------------------- progress */

async function renderProgress() {
  const box = $("#progress-body");
  const [stats, { sessions: exams }] = await Promise.all([api("/api/stats"), api("/api/sessions?kind=exam&limit=20")]);
  if (!stats.attempts) {
    box.replaceChildren(el("div", { class: "empty" },
      el("p", {}, "Nothing here yet. Finish a quiz and your accuracy and timing for each topic show up here."),
      el("a", { href: "#practice" }, "Start practicing")));
    return;
  }
  const weak = stats.topics.filter((t) => t.attempts && t.recent_accuracy < 0.7).map((t) => t.topic);
  const pct = (val) => `${Math.round(val * 100)}%`;

  box.replaceChildren(
    el("div", { class: "summary" },
      el("div", {}, el("strong", {}, String(stats.attempts)), el("span", {}, "questions answered")),
      el("div", {}, el("strong", {}, pct(stats.accuracy)), el("span", {}, "correct overall")),
      el("div", {}, el("strong", {}, String(stats.days_studied.length)), el("span", {}, stats.days_studied.length === 1 ? "day studied" : "days studied")),
      el("div", {}, el("strong", {}, String(streak(stats.days_studied))), el("span", {}, "day streak"))),
    weak.length ? el("p", {},
      el("button", {
        class: "primary", type: "button",
        onclick: () => startQuiz({ topics: weak, adaptive: true, mode: "mixed", count: quizCount(), kind: "review" }),
      }, `Practice ${weak.length} weak ${weak.length === 1 ? "topic" : "topics"}`)) : null,
    renderExamHistory(exams),
    ...state.modules.map((module) => el("div", {},
      el("h2", {}, `Module ${module.number}: ${module.title}`),
      el("table", { class: "breakdown topic-table" },
        el("thead", {}, el("tr", {}, el("th", {}, "Topic"), el("th", {}, "Last 20"), el("th", {}, "All time"), el("th", {}, "Avg time"), el("th", {}, "Answered"))),
        el("tbody", {}, stats.topics.filter((t) => t.module === module.id).map((t) => el("tr", {},
          el("td", {}, t.title),
          el("td", { class: "num" }, t.attempts
            ? [el("span", { class: `meter ${t.recent_accuracy < 0.7 ? "low" : ""}`, "aria-hidden": "true" }, el("i", { style: `width:${pct(t.recent_accuracy)}` })), pct(t.recent_accuracy)]
            : el("span", { class: "muted" }, "Not started")),
          el("td", { class: "num" }, t.attempts ? pct(t.accuracy) : ""),
          el("td", { class: "num" }, t.avg_seconds != null ? clock(t.avg_seconds) : ""),
          el("td", { class: "num" }, String(t.attempts)))))))),
    el("p", {}, resetButton()),
  );
}

function renderExamHistory(exams) {
  const { target } = examSettings();
  if (!exams.length) {
    return el("div", {},
      el("h2", {}, "Practice exams"),
      el("p", { class: "muted" }, "Take a practice exam to track your score and finishing time together. Both have to be there on exam day."));
  }
  const recent = exams.slice(0, 3);
  const avgScore = recent.reduce((sum, e) => sum + e.score, 0) / recent.length;
  const spare = recent.map((e) => (e.time_limit_seconds ?? e.duration_seconds) - e.duration_seconds);
  const avgSpare = spare.reduce((a, b) => a + b, 0) / spare.length;
  const anyTimedOut = recent.some((e) => e.timed_out);
  const date = (iso) => new Date(iso).toLocaleDateString(undefined, { month: "short", day: "numeric" });

  return el("div", {},
    el("h2", {}, "Practice exams"),
    el("p", {},
      `Last ${recent.length === 1 ? "exam" : `${recent.length} exams`}: ${Math.round(avgScore * 100)}% average`,
      anyTimedOut ? ", and time ran out at least once." : `, finishing with ${clock(avgSpare)} to spare on average.`),
    el("table", { class: "breakdown exam-history" },
      el("thead", {}, el("tr", {}, el("th", {}, "Date"), el("th", {}, "Score"), el("th", {}, "Time used"), el("th", {}, "Per question"), el("th", {}, "Result"))),
      el("tbody", {}, exams.map((e) => {
        const limit = e.time_limit_seconds ?? e.duration_seconds;
        const verdict = examVerdict({ score: e.score, target, duration: e.duration_seconds, timeLimit: limit, timedOut: e.timed_out });
        const used = Math.min(1, e.duration_seconds / limit);
        return el("tr", {},
          el("td", {}, date(e.finished_at)),
          el("td", { class: "num" }, `${Math.round(e.score * 100)}% (${e.correct}/${e.question_count})`),
          el("td", { class: "num" },
            el("span", { class: `meter ${e.timed_out || used > 0.95 ? "low" : ""}`, "aria-hidden": "true" }, el("i", { style: `width:${Math.round(used * 100)}%` })),
            `${clock(e.duration_seconds)} / ${clock(limit)}`),
          el("td", { class: "num" }, e.answered ? clock(e.duration_seconds / e.answered) : ""),
          el("td", { class: verdict.ready ? "verdict ready" : "verdict not-ready" }, verdict.ready ? "Ready" : e.timed_out ? "Ran out of time" : e.score * 100 < target ? "Below target" : "Over time"));
      }))));
}

function streak(days) {
  const set = new Set(days);
  const day = new Date();
  const iso = (d) => d.toISOString().slice(0, 10);
  if (!set.has(iso(day))) day.setUTCDate(day.getUTCDate() - 1);
  let count = 0;
  while (set.has(iso(day))) { count += 1; day.setUTCDate(day.getUTCDate() - 1); }
  return count;
}

function resetButton() {
  let armed = false;
  const btn = el("button", {
    class: "quiet", type: "button",
    onclick: async () => {
      if (!armed) { armed = true; btn.textContent = "Click again to erase all progress"; return; }
      await api("/api/stats", { method: "DELETE" });
      renderProgress();
    },
  }, "Reset progress");
  return btn;
}

/* ---------------------------------------------------------------- keyboard */

document.addEventListener("keydown", (event) => {
  if ($("#quiz").hidden || event.target.matches("input, select, textarea") || event.metaKey || event.ctrlKey) return;
  const index = "1234abcd".indexOf(event.key.toLowerCase()) % 4;
  const choices = [...document.querySelectorAll("#question .choice:not(:disabled)")];
  if (choices.length && "1234abcd".includes(event.key.toLowerCase())) choices[index]?.click();
});

document.addEventListener("keydown", (event) => {
  if (event.key !== "Enter" || $("#quiz").hidden || event.target.matches("button")) return;
  const btn = $("#question .actions button:not(:disabled)");
  if (btn) { event.preventDefault(); btn.click(); }
});

/* ---------------------------------------------------------------- boot */

async function init() {
  state.course = await api("/api/course");
  state.modules = state.course.sections.flatMap((s) => s.modules);
  for (const module of state.modules) for (const topic of module.topics) state.topics[topic.id] = topic;

  renderSetup();
  $("#start-custom").addEventListener("click", () => {
    saveSetup();
    startQuiz({
      topics: selectedTopics(),
      adaptive: $("#adaptive").checked,
      mode: document.querySelector('input[name="mode"]:checked').value,
      count: quizCount(),
    });
  });
  $("#start-daily").addEventListener("click", () => {
    saveSetup();
    startQuiz({ topics: coveredTopics(), adaptive: true, mode: "mixed", count: quizCount(), kind: "daily" });
  });
  $("#start-exam").addEventListener("click", () => {
    saveSetup();
    const exam = examSettings();
    startQuiz({
      topics: coveredTopics(), adaptive: false, mode: "mixed", count: exam.count, kind: "exam",
      timeLimit: exam.minutes * 60, target: exam.target, errorEl: $("#exam-error"),
    });
  });
  $("#quit").addEventListener("click", () => (state.quiz.exam || state.quiz.results.some(Boolean) ? showResults() : endQuiz()));

  window.addEventListener("hashchange", route);
  route();
}

init().catch((err) => {
  document.querySelector("main").prepend(el("p", { class: "error" }, `Couldn't load the course: ${err.message}. Is the server running?`));
});
