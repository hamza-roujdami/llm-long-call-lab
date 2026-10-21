# 📄 The Anti-Framework Agent Blueprint

An architectural reference and implementation manual for building production-grade AI agents using **Anthropic’s engineering philosophy**. 

This repository demonstrates how to bypass heavy, over-abstracted third-party orchestration frameworks in favor of **lean, code-first harnesses, strict context engineering, and protocol-level primitives**.

---

## 📌 Executive Summary

The industry is currently suffering from an over-abstraction crisis. While developers rush to wrap LLMs in complex state-graph frameworks, internal engineering data from labs like Anthropic highlights a simpler truth: **Smarter underlying models require fewer software abstractions.**

When frameworks attempt to manage every state transition, tool call, and memory buffer, they introduce unpredictable latency, debugging nightmares, and token bloat. 

This project implements the **Lean Harness Blueprint**:
1. **The LLM is just an engine**—it handles stateless reasoning and tool selection.
2. **Your code is the drive-shaft**—a simple, explicit local loop that executes tools and manages state dynamically.
3. **Decoupled Architecture**—separating the reasoning layer (The Brain) from the execution sandbox (The Hands).

---

## 🧭 Core Architectural Philosophy

To build highly effective agents that mirror Anthropic's production systems, we decouple our agent architecture into three isolated, independent tiers:

```
Traditional Approach:  [Your Code] ──> [Heavy Framework Graph] ──> [Rigid State Engine] ──> LLM
Anthropic Approach:    [Your Code] ──> [Lean Code Loop (Harness)] ──> [Dynamic Context] ──> LLM
```

*   🧠 **The Brain (Stateless Harness):** A lightweight loop responsible *only* for calling the LLM API, checking for tool requests, and appending raw outputs. It holds no complex in-memory state objects.
*   🛠️ **The Hands (Isolated Sandbox):** An entirely separate microVM, container, or package where tools actually run. The Brain commands the Hands, but the tools never have direct access to your primary application environment or root credentials.
*   💾 **The Session Log (Append-Only Memory):** Conversations and state transitions are tracked externally as a flat chronological event log, ensuring the harness remains modular and easy to trace.

---

## 🔄 The 5 Production Workflow Patterns

Anthropic’s core framework research explicitly states that open-ended, fully autonomous "figure it out" loops fail in production environments due to compounding errors and high token costs. Instead, we constrain agent intelligence within **5 predictable design patterns**:

### 1. Prompt Chaining
Splits a massive task into linear sub-steps where Call A's output directly feeds Call B's prompt. This is ideal for sequential data transformation pipelines.

### 2. Routing
A fast, specialized LLM call classifies user intent and routes execution to a dedicated code branch. This is heavily utilized for customer service triage or multi-domain analysis.

### 3. Parallelization
Distributes sub-tasks to independent LLM calls simultaneously, aggregating results at the end. This pattern accelerates deep web-searching or multi-angle code reviews.

### 4. Orchestrator-Workers
A central "Manager" LLM dynamically breaks a loose problem into tasks and spawns worker scripts. This handles complex, multi-file software engineering tasks natively.

### 5. Evaluator-Optimizer
A Generator script creates a draft, and a separate **Skeptical Evaluator** rejects or approves it with feedback. This handles coding against strict specifications or writing formal documents.

> 💡 **Core Invariant:** *Agents are historically bad judges of their own outputs. Separating the Generation logic from the Evaluation logic is non-negotiable for deterministic results.*

---

## 🧠 Context Engineering Specifications

Prompt engineering is dead; **Context Engineering** is the true bottleneck of production-grade agents. Anthropic views the prompt window as a dynamic, volatile cache that must be micro-managed.

### 1. The Context Reset (Mitigating Context Anxiety)
When a long-running agent session drags on, the context window fills up with historical tool noise. Anthropic discovered that frontier models exhibit **context anxiety** when the window fills—they wrap up work prematurely, ignore system rules, or become overly passive.
*   **The Fix:** Avoid traditional continuous text appending. Instead, implement a **Context Reset**. 
*   **Mechanism:** Periodically wipe the context window completely clean and start a fresh API session. Pass the current state forward using a highly condensed progress state file rather than raw chat history.

### 2. Agent-Computer Interface (ACI) Design Guidelines
When writing functions for an LLM to call, you are building an API for a neural network, not a human developer.
*   **Consolidated over Granular:** Do not give your agent 50 micro-API endpoints. Give them a few high-impact tools that handle data processing and aggregation natively on the backend.
*   **High-Signal Strings:** Tools must never return abstract, raw database outputs (like IDs). They must return descriptive, semantic text strings so the model natively comprehends what occurred.
*   **Forced Truncation:** Hardcode strict pagination and truncation mechanisms directly into your database or web reader tool codes to guarantee a rogue search doesn't blow past your token budget.