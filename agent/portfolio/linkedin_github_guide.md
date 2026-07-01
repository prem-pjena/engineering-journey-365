# 🌐 LinkedIn & GitHub Branding Guide (v2)

**Purpose:** Build a professional brand from Day 1 that grows with my skills. Daily GitHub commits + weekly LinkedIn posts = maximum visibility.

---

## 🔄 Daily Commit Workflow

**Goal:** At least 1 meaningful commit to GitHub every single day. Even on busy days, push *something*.

### End-of-Day Checklist (15 min)

```bash
cd /Users/prem/Documents/Generative\ AI/Future

# 1. Check what changed
git status

# 2. Stage everything meaningful
git add -A

# 3. Commit with proper prefix
# feat:     New learning task or program built
# fix:      Bug fix or error correction
# docs:     README, notes, documentation updates
# chore:    Maintenance, folder structure
# test:     Adding tests
# refactor: Improving existing code
git commit -m "feat: Day X — [concept learned]"

# 4. Push to GitHub
git push origin main
```

### What Counts as a Daily Commit

| Day Type | Minimum Commit | Example |
|----------|---------------|---------|
| **Learning Day** | Today's tasks + notes | `feat: Day 4 — logical operators, nested conditions` |
| **Project Day** | Feature or fix on project | `feat: add hybrid search pipeline with RRF fusion` |
| **Review/Retention Day** | Updated agent files | `docs: weekly test results, skill tracker update` |
| **Busy Day (5 min)** | Update README or agent status | `docs: Day X summary, updated current status` |
| **Sick/Off Day** | Update badge + push | `chore: update day counter badge` |

**Non-negotiable:** A green square on GitHub every day. Even 1 line changed counts.

---

## 👤 GitHub Profile

### Setup Checklist
- [x] Profile photo (professional, clear face)
- [ ] Bio: *"Building Agentic AI Systems | Python · LangChain · AWS | 365-day public engineering journey"*
- [ ] Bio link to [engineering-journey-365](https://github.com/prem-pjena/engineering-journey-365)
- [ ] Pin repositories: `engineering-journey-365` + current portfolio project
- [ ] Add contribution graph widget to profile README
- [ ] Enable GitHub Actions for project CI/CD

### Profile README (`prem-pjena/README.md`)
```markdown
### 👋 Hi, I'm Prem

🔨 Building Agentic AI Systems · Python · LangChain · LangGraph · AWS

📆 On a **365-day public engineering journey** → [engineering-journey-365](https://github.com/prem-pjena/engineering-journey-365)

🚀 Past: AI Engineering Intern @ SkillVeda
🎯 Target: FAANG-grade Agentic AI Backend Engineer

📈 Daily commits · Weekly LinkedIn posts · Building in public
```

### Commit Rules (Enforced Daily)
```
feat:     New learning task or project feature
fix:      Bug fix or error correction
docs:     README, notes, journal updates
chore:    Maintenance, folder cleanup
test:     Adding unit/integration tests
refactor: Code improvement without behavior change
```

### Repository Structure (Public Face)
```
engineering-journey-365/
├── README.md                  ← Journey overview, badges
├── Month-01/
│   ├── Day-01/
│   │   ├── README.md          ← What I learned + errors
│   │   ├── task_01.py
│   │   └── task_02.py
│   ├── Day-02/
│   └── ...
├── Month-02/
└── ...
```

---

## 💼 LinkedIn Profile

### Setup Checklist
- [x] Professional photo (same as GitHub)
- [ ] **Headline:** *"AI Backend Engineer | Building Agentic AI Systems | AWS · LangChain · Python"*
- [ ] **About section:** "Building in public — following a 12-month roadmap from intern to FAANG-grade AI Backend Engineer. Sharing lessons learned, projects built, and mistakes made along the way."
- [ ] **Featured section:** Pin `engineering-journey-365` + portfolio project repos
- [ ] **Skills:** Python, LangChain, LangGraph, AWS, FastAPI, PostgreSQL, Docker, System Design
- [ ] **Experience:** SkillVeda internship with detailed bullet points (quantified results)
- [ ] **Licenses & Certifications:** Add once earned

---

## 📅 12-Month LinkedIn Content Calendar

**Post every Sunday.** Each post takes 10-15 minutes. Template at the bottom.

| Week | Theme | Post Title Idea |
|------|-------|----------------|
| **Month 1: Python + DSA** | | |
| Week 1 | Python basics + Calculator | "Day 1 of 365: I wrote my first Python program" |
| Week 2 | Conditionals + Decision Making | "From if/else to decision trees — learning to code logic" |
| Week 3 | Logical Operators + Loops | "How logical operators power real-world systems" |
| Week 4 | Functions + Lists | "The week my Python code stopped being ugly" |
| **Month 2: Python Deep Dive** | | |
| Week 5 | OOP + Classes | "I finally understood OOP — here's what clicked" |
| Week 6 | File I/O + Error Handling | "Writing code that doesn't crash: error handling patterns" |
| Week 7 | ML Basics | "What I learned about ML that no tutorial taught me" |
| Week 8 | CLI Tool Project | "I built my first CLI tool and published it on PyPI" |
| **Month 3: Distributed Systems** | | |
| Week 9 | async/await + Event Loops | "Understanding async/await changed how I think about code" |
| Week 10 | Message Queues (SQS) | "What happens when your API needs to talk to another service?" |
| Week 11 | Docker | "I containerized my first app — Docker explained simply" |
| Week 12 | Redis + Caching | "Caching: The single easiest performance win" |
| **Month 4: Classical ML + Backend** | | |
| Week 13 | FastAPI + PostgreSQL | "Building my first production backend" |
| Week 14 | Docker Compose | "Multi-service apps with Docker Compose" |
| Week 15 | XGBoost | "What most AI courses don't teach you about ML" |
| Week 16 | Task Scheduling (Celery) | "Background jobs: Why synchronous code isn't enough" |
| **Month 5: Backend Deep Dive** | | |
| Week 17 | JWT Auth + Middleware | "Securing APIs with JWT — the right way" |
| Week 18 | Event-Driven Architecture | "Request-response is dead — long live events" |
| Week 19 | Linux for Engineers | "5 Linux commands every backend engineer should know" |
| Week 20 | Project 1 Complete | "Ship it: Lessons from deploying my first project" |
| **Month 6: AI + LangChain + RAG** | | |
| Week 21 | LangChain Basics | "My first week with LangChain — mental model shift" |
| Week 22 | Embeddings + Vector DBs | "How do computers understand meaning? Embeddings explained" |
| Week 23 | RAG Architecture | "Building a system that reads documents and answers questions" |
| Week 24 | Hybrid Search | "Why pure vector search isn't enough" |
| **Month 7: Advanced RAG + Eval** | | |
| Week 25 | LangSmith + Eval Pipelines | "How to know if your AI system is actually good" |
| Week 26 | CI/CD for AI | "I put my AI pipeline through CI/CD — here's what broke" |
| Week 27 | Project 2 Complete | "I built a production RAG pipeline. Here's the architecture." |
| Week 28 | Halfway Reflection | "182 days of building in public — lessons learned" |
| **Month 8: Agentic AI + LangGraph** | | |
| Week 29 | LangGraph + State Machines | "My agent can now make decisions. Here's how." |
| Week 30 | MCP (Model Context Protocol) | "MCP: The protocol that changes how AI connects to tools" |
| Week 31 | Human-in-the-Loop | "Why your AI agent needs a human supervisor" |
| Week 32 | Agent Design Patterns | "3 agent architectures I built this month" |
| **Month 9: Multi-Agent + MCP** | | |
| Week 33 | Multi-Agent Systems | "When one AI isn't enough: multi-agent patterns" |
| Week 34 | Custom MCP Servers | "I built custom MCP servers for GitHub and Slack" |
| Week 35 | Agent Security | "Prompt injection is real — here's how to defend" |
| Week 36 | Project 3 Complete | "My multi-agent system can use APIs autonomously" |
| **Month 10: Inference + Optimization** | | |
| Week 37 | BPE Tokenizer | "I built a BPE tokenizer from scratch — here's what I learned" |
| Week 38 | vLLM + Continuous Batching | "How FAANG serves LLMs at scale" |
| Week 39 | AWS Inferentia | "Running LLMs on specialized hardware" |
| Week 40 | System Design Patterns | "CAP theorem, caching, and rate limiting explained" |
| **Month 11: Full-Stack Platform** | | |
| Week 41 | Project 4 Architecture | "Designing a full-stack agentic platform on AWS" |
| Week 42 | AWS Production Deploy | "From localhost to production: my AWS deployment checklist" |
| Week 43 | Cost Optimization | "How I reduced my AWS bill by 60%" |
| Week 44 | Open Source Contribution | "My first open source PR got merged — here's how" |
| **Month 12: Interview Prep** | | |
| Week 45 | AI System Design | "How I prep for AI System Design interviews" |
| Week 46 | ML Fundamentals | "Transformers, attention, and BPE — explained for engineers" |
| Week 47 | Behavioral Stories | "My SkillVeda internship taught me more than any course" |
| Week 48 | Final Reflection | "365 days. 4 projects. Here's the resume it built." |

---

## 📝 LinkedIn Post Template

### Learning Post (Months 1-5)
```
🚀 Day [X] of 365: [What I learned]

This week I learned [concept] and built [specific thing].

Key takeaways:
1️⃣ [Insight 1 — specific, technical]
2️⃣ [Insight 2 — what surprised you]
3️⃣ [Insight 3 — how it connects to real systems]

⚡ Real-world connection:
[Connect this learning to SkillVeda work or FAANG interview topic]

#Python #EngineeringJourney365 #LearningInPublic #BackendEngineering
```

### Project Post (Months 6-12)
```
🔨 I just shipped [Project Name]

What it does:
[1-2 sentence description]

Tech stack:
Python · [Framework] · [AWS Service] · [Other]

Architecture highlight:
[One interesting architectural decision]

📊 Results:
[Eval metric or performance number]

🔗 [GitHub link]

#AI #RAG #LangChain #AWS #EngineeringJourney365
```

### Reflection Post (End of Month)
```
📆 [Month X] of 12 — Complete

What I learned this month:
✅ [Topic 1]
✅ [Topic 2]
✅ [Topic 3]
✅ [Topic 4]

Current skill scores:
Python: [X]/10 | DSA: [X]/10 | AI/ML: [X]/10 | AWS: [X]/10

Biggest mistake this month:
[Honest mistake — shows growth mindset]

Next month's focus:
[Upcoming topics]

#EngineeringJourney365 #BuildingInPublic #AI #Backend
```

---

## 🌍 Open Source Contribution Roadmap

**Start:** Month 7+ (after RAG project is solid)

### Phase 1 — Contribution Basics (Month 7-8)
- Find 3-5 repos I use daily (LangChain, LangGraph, FastAPI, etc.)
- Read CONTRIBUTING.md and good-first-issue labels
- Start with documentation PRs (typos, better examples)
- Learn the PR workflow: fork → branch → commit → PR → review → merge

### Phase 2 — Code Contributions (Month 9-10)
- Fix small bugs in LangChain/LangGraph community packages
- Add test cases for uncovered code paths
- Contribute to open-source MCP server implementations
- Build reputation through consistent, quality PRs

### Phase 3 — Meaningful Contributions (Month 11-12)
- Add features to agent frameworks (LangGraph tools, MCP servers)
- Contribute to evaluation tooling (LangSmith, DeepEval)
- Create a small open-source tool related to agent workflows
- Use contributions as interview talking points

### Target Repos
| Repo | Why | Contribution Type |
|------|-----|------------------|
| `langchain-ai/langgraph` | Core agent framework | Docs, tests, tools |
| `modelcontextprotocol/servers` | MCP ecosystem | New server implementations |
| `fastapi/fastapi` | Backend framework | Docs, bug fixes |
| `vllm-project/vllm` | Inference engine | Docs, integrations |
| `confident-ai/deepeval` | LLM evaluation | Tests, integrations |

---

## 📊 GitHub Presence Metrics (Target)

| Metric | Month 1 | Month 3 | Month 6 | Month 9 | Month 12 |
|--------|---------|---------|---------|---------|----------|
| **Commits** | 30+ | 90+ | 180+ | 270+ | 365+ |
| **Contribution Streak** | 7 days | 30 days | 90 days | 180 days | 365 days |
| **Repositories** | 1 | 2 | 3 | 4 | 5 |
| **Stars** | 0 | 5+ | 20+ | 50+ | 100+ |
| **Followers** | 0 | 5+ | 20+ | 50+ | 100+ |
| **Open Source PRs** | 0 | 0 | 1-2 | 5+ | 10+ |
