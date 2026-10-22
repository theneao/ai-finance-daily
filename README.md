# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集三类应用型内容：

1. **AI 投资与金融工具**：投资、交易、资产配置、行情/财务数据、资金流、回测与策略。
2. **Vibe Coding**：Coding Agent、代码库理解、工作流自动化、工作学习与开发能力增强。
3. **AI Infra**：vLLM、SGLang、推理服务、KV Cache、PD 分离、部署、RAG/Agent 基础设施、评测与可观测性。

项目满足 **Star ≥ 100**，或**近 7 天增长 ≥ 20 Star**；新库创建 7 天内达到 20 Star 也会立即进入榜单。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。当天多次运行会合并去重，不覆盖已收集内容。最近 90 天完整日报见 [`archive/index.md`](archive/index.md)，更早内容转入精简月度历史；搜索词和阈值可在 [`config.yaml`](config.yaml) 调整。

---

# AI 应用研究日报 · 2026-10-22

本期新增：**1 篇论文**（其中 0 篇找到可能的代码）和 **1 个 GitHub 项目**。

## AI 投资与交易论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-21 | [Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](https://arxiv.org/abs/2610.30113) | Houde Qian, Zheng Jiang, Wenyi Li 等 | — |


## GitHub 金融与交易工具

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [ChungKit-WAN/Quant-research-lab-v0.1.0](https://github.com/ChungKit-WAN/Quant-research-lab-v0.1.0) | Python framework for monthly sector ETF allocation and multifactor stock backtesting, with transaction-cost accounting and separate Chinese and English research reports. | 51 | — | Python | 新项目 |


## Vibe Coding · 工作与学习增强

新增 **11 篇论文**（6 篇找到代码）和 **4 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-21 | [SWE-DIVE: Multi-Turn Coding Agent Evaluation with Dynamic User Simulation](https://arxiv.org/abs/2610.30047) | Lorenz Brehme, Benjamin Steenhoek, Ruth Breu | [论文链接](https://github.com/lorenzbrehme/swe-dive_usersim) |
| 2026-10-21 | [PAUSE: Search-Free Steering of Coding Agents Before Their First Source-Code Edit](https://arxiv.org/abs/2610.29870) | Viral Patel, Boyin Tan, Jason Xue 等 | — |
| 2026-10-21 | [Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents](https://arxiv.org/abs/2610.29869) | Arshan Dabirsiaghi | [arXiv 页面](https://github.com/pixee/flat-compaction-attacks-oct-2027) |
| 2026-10-21 | [UserSWE: Evaluating Coding Agents in Multi-Turn Conversations with Dynamic Users](https://arxiv.org/abs/2610.29822) | Zhan-Yu Wu, Ji Luo, Alyssa Wu 等 | — |
| 2026-10-21 | [Benchmarking Coding Agents for System-Level Performance Optimization](https://arxiv.org/abs/2610.29695) | Yanze Zhang, Maggie Yongqi Guan, Shudong Liu 等 | [论文链接](https://github.com/zyzcjnb/microperf) |
| 2026-10-21 | [Do Coding Agents Understand Why Systems Crash---and Why They Don't?](https://arxiv.org/abs/2610.29332) | Chenxi Huang, Haonan Wang, Jinghe Zhang 等 | — |
| 2026-10-21 | [Recursive Self-Improvement on a Budget: Scoring Code Edits Before They Run](https://arxiv.org/abs/2610.29121) | Erfan Darzi, Sree Bhargavi Balija, Sheng He | — |
| 2026-10-21 | [GenXR-Bench: Benchmarking Coding Agents for Interactive XR Development](https://arxiv.org/abs/2610.29014) | William Huang, David Li, Xiang 'Anthony' Chen 等 | [arXiv 页面](https://github.com/whuang37/genxr-bench) |
| 2026-10-20 | [Back Up Before You Regret: Measuring Backup Awareness and Automating Backup in Coding Agents](https://arxiv.org/abs/2610.28934) | Xu Li, Simon Yu, Minzhou Pan 等 | [ID 命中](https://github.com/CHATS-lab/BackUpper) |
| 2026-10-19 | [Who Approved This? Coding Agents, Human Accounts, and Merge-Gate Evidence at a Fintech Startup](https://arxiv.org/abs/2610.28683) | Adam Manji | — |
| 2026-10-16 | [Who Verifies the Builder? Toward Independent Assurance for Agent-Produced Software](https://arxiv.org/abs/2610.28667) | Sion Israel Sion, Alain April | [arXiv 页面](https://github.com/besionisrael/assure-harness) |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [refly-ai/refly](https://github.com/refly-ai/refly) | The first open-source agent skills builder. Define skills by vibe workflow, run on Claude Code, Cursor, Codex & more. Build Clawdbot 🦞· APIs for Lovable · Bots for Slack & Lark/Feishu · Skills are infrastructure, not prompts. | 7536 | — | TypeScript | 近期活跃 |
| [sahibzada-allahyar/Formal-Verification-RSI](https://github.com/sahibzada-allahyar/Formal-Verification-RSI) | Formal verification for AI: a Lean 4 + Dafny proof checker that catches fake AI proofs (reward hacking), and verified recursive self-improvement (RSI) for coding agents. AI for math, physics and software engineering. | 2850 | — | Python | 近期活跃 |
| [aicodeking/pandacode](https://github.com/aicodeking/pandacode) | PandaCode: a calm desktop workspace for coding agents | 420 | — | Rust | 新项目 |
| [zita-ch/supermimic_vibed](https://github.com/zita-ch/supermimic_vibed) | vibe coded supermimic within 1h, LAFAN passed within 1.5 gpuh training | 97 | — | Python | 新项目 |


## AI Infra · 推理部署与应用基础设施

新增 **9 篇论文**（0 篇找到代码）和 **3 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-21 | [HAWK: Heterogeneity-Aware KV Cache Transfer for Efficient GPU-NPU Phase-Disaggregated LLM Inference](https://arxiv.org/abs/2610.29873) | Junhyeok Park, Jungeun Yoon, Kyungmin Kim 等 | — |
| 2026-10-21 | [UlaCache: Unified Logical Addressing for Sparse LLM Serving](https://arxiv.org/abs/2610.29820) | Isaac Zhu, Alan Cao, Hugh Yin 等 | — |
| 2026-10-21 | [RISK-KV: Quality-Aware Selective KV Cache Reconstruction for Distributed LLM Inference](https://arxiv.org/abs/2610.29544) | Wang Yuekai | — |
| 2026-10-21 | [RCSD: Reinforcement and Continual Learning for Domain-Specific Speculative Decoding](https://arxiv.org/abs/2610.29527) | Mingkang Liu, Weiming Meng, Peipei Jiao 等 | — |
| 2026-10-21 | [Cache Locally, Recompute Selectively for Streaming Video Understanding](https://arxiv.org/abs/2610.29229) | Junhyeok Lee, Sangyoon Lee, Jaeho Lee | — |
| 2026-10-21 | [Resuming Vision-Language Inference across Onboard Interruptions](https://arxiv.org/abs/2610.29183) | Xiaolong Huang, Yinyuan Zhang, Daliang Xu 等 | — |
| 2026-10-20 | [Is 2:4 Sparsity Still Worth It? Semi-Structured Sparsity versus Quantization in LLM Inference](https://arxiv.org/abs/2610.28947) | Xiuyi Qin | — |
| 2026-10-19 | [Benchmarking the Quantum Leap: Auditing LLM Evaluation for Quantum Code Generation](https://arxiv.org/abs/2610.28678) | Ethan Seefried, Romit Ghosh, Sharmin Afrose 等 | — |
| 2026-10-17 | [Accelerating CPU Speculative Decoding via Unified Graph Execution and Transactional KV Isolation](https://arxiv.org/abs/2610.28671) | Zhangdie Yuan | — |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [qiniu/xhub](https://github.com/qiniu/xhub) | A self-hosted AI gateway for enterprises. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails, load balancing, and logging [Bedrock, Azure, OpenAI, Anthropic, OpenAI, VertexAI, vLLM, Nvidia NIM] | 68 | — | TypeScript | 新项目 |
| [ahtx/kindi](https://github.com/ahtx/kindi) | A custom LLM inference engine for the NVIDIA Quadro K420: Ternary-Bonsai-2-2B at 20+ tokens/s with an OpenAI-compatible server | 28 | — | Python | 新项目 |
| [yaya-sy/specspeech](https://github.com/yaya-sy/specspeech) | Speculative Decoding for fast ASR and TTS inference | 24 | — | Python | 新项目 |


> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。

