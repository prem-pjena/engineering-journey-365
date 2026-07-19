# 🧠 Deep Research Report: Model Architecture, ML Fundamentals & Hardware for Agentic AI Engineer

**Source:** Gemini Deep Research (Jul 19, 2026)
**Key Takeaway:** AI Engineer orchestrates foundation models — does NOT train them from scratch

---

## 🎯 Role Clarification

| Role | What They Do | Am I This? |
|------|-------------|------------|
| **Data Scientist** | Exploratory analysis, statistical modeling, custom predictive models | ❌ No |
| **ML Engineer** | Infrastructure to train/validate/deploy models at scale (MLOps, distributed training) | ❌ No |
| **AI Engineer** | Consumes pre-trained models via APIs, builds RAG, agents, orchestration | ✅ YES |

> "An AI Engineer does not need to master custom gradient descent implementations; they must master prompt engineering, API latency optimization, and backend orchestration."

---

## 🔴 Critical Updates to Study Plan

### What the Report CONFIRMS about our plan

| Our Plan Says | Report Confirms |
|--------------|-----------------|
| LangGraph + FastAPI are most important | ✅ "Orchestration is the primary deliverable" |
| RAG > Fine-tuning | ✅ RAG in 35.9% of JDs, Fine-tuning in only 8.5% |
| Skip training CNNs/RNNs from scratch | ✅ "Gradient descent: Skip mathematical implementation" |
| Focus on deployed production systems | ✅ "Production readiness separates junior from senior" |

### What We Need to ADD based on this report

| New Insight | Priority | Where to Add in Plan |
|------------|----------|---------------------|
| **AWS Bedrock** — serverless model access, enterprise compliance | 🔴 Must-Know | Add to Phase 5 (Production) |
| **vLLM inference engine** — PagedAttention, continuous batching | 🔴 Must-Know | Add to Phase 5 (Production) |
| **Constrained Decoding** — Outlines/XGrammar for guaranteed JSON output | 🔴 Must-Know | Add to Phase 2 (Structured Output day) |
| **Redis Semantic Caching** — cache repeated LLM queries | 🟡 Good-to-Have | Add to Phase 6 (System Design) |
| **KV Cache & VRAM capacity planning** | 🟡 Good-to-Have | Add to Phase 6 (Cost tracking day) |
| **Quantization (INT8/INT4)** for cost optimization | 🟡 Good-to-Have | Mention during deployment days |
| **Sampling params** (temp, top-k, top-p) — used on EVERY API call | 🔴 Must-Know | Already in Phase 1 (LLM APIs day) |

---

## 📊 Prioritization Matrix (from Report)

| Topic | Relevance | Depth Needed | Our Plan Status |
|-------|-----------|-------------|-----------------|
| Supervised vs Unsupervised | 3/10 | Concept | ✅ Already covered lightly |
| ML Pipelines | 4/10 | Concept | ✅ Don't need to add |
| Bias-Variance Tradeoff | 5/10 | Concept | ✅ In interview prep phase |
| Gradient Descent | 2/10 | Skip | ✅ Already skipped |
| Transformer Architecture (QKV) | 7/10 | Concept | ✅ In interview prep phase |
| Tokenization (BPE) | 8/10 | Implementation | ⚠️ Add to LLM APIs day |
| KV Cache / VRAM | 9/10 | Expert | ⚠️ Add to deployment phase |
| Quantization (INT8/FP16) | 9/10 | Implementation | ⚠️ Add to deployment phase |
| Fine-tuning (LoRA) | 5/10 | Concept | ✅ Already low priority |
| Sampling (temp, top-k, top-p) | 10/10 | Expert | ⚠️ Add dedicated coverage |
| MoE / Router Models | 8/10 | Implementation | ✅ Already in agent design |
| Speculative Decoding | 6/10 | Concept | ⚪ Nice-to-know |
| Continuous Batching | 8/10 | Concept | ⚪ Mention in vLLM context |
| AWS Bedrock | 9/10 | Master | 🔴 Must ADD to plan |
| ECS Fargate | 9/10 | Master | 🔴 Already in plan |
| pgvector tuning | 9/10 | Master | 🔴 Already in plan |
| Redis Semantic Cache | 8/10 | Implementation | 🟡 Add to system design |
| Constrained Decoding | 10/10 | Expert | 🔴 Must ADD to plan |

---

## 🔥 Key Interview Answers to Memorize

### "Why RAG over Fine-tuning?"
> "I view RAG and fine-tuning as complementary. RAG solves the knowledge problem by fetching real-time, auditable facts. Fine-tuning solves the behavior problem. Given modern context windows, I start with few-shot prompting and multi-agent routing. I only escalate to LoRA when prompting hits a latency or context-limit bottleneck."

### "Explain the Transformer architecture"
> "Self-attention has quadratic time complexity — extremely long agent prompts cause TTFT to spike. When I design RAG prompts, I limit context window size and place critical instructions at the end to ensure attention gives them the highest computational weight."

### "How do you optimize LLM costs?"
> "I architect compound AI systems. A fast SLM like Llama 3 8B acts as a semantic router — simple queries hit cached responses or specialized extractors, only complex reasoning tasks escalate to frontier models like Claude. This drastically reduces cost and latency."

### "How do you ensure structured JSON output?"
> "I implement constrained decoding at the engine level using Outlines/XGrammar. This compiles Pydantic schemas into finite-state machines that apply logit masks during inference, guaranteeing 100% type-safe JSON outputs."

### "What AWS services for AI?"
> "I default to Bedrock for serverless model access with zero infra management. I deploy FastAPI backends on ECS Fargate for persistent streaming connections. I use Aurora pgvector for RAG to keep vectors and relational data co-located with ACID compliance."

---

## 🛠️ Practical Changes to Implement

### Changes to Current Code/Practice

1. **When calling LLM APIs**, always specify and document:
   - Temperature, top_p, max_tokens
   - Why you chose those values

2. **When building structured output**, use Pydantic + constrained decoding concept:
   ```python
   from pydantic import BaseModel
   
   class ExtractionResult(BaseModel):
       name: str
       amount: float
       date: str
   ```

3. **When deploying**, think in terms of:
   - VRAM requirements for model size
   - KV cache growth with context length
   - Quantization for cost reduction

4. **When designing agents**, use the router pattern:
   - Fast cheap model for intent classification
   - Expensive model only for complex reasoning
