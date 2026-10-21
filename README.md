# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集三类应用型内容：

1. **AI 投资与金融工具**：投资、交易、资产配置、行情/财务数据、资金流、回测与策略。
2. **Vibe Coding**：Coding Agent、代码库理解、工作流自动化、工作学习与开发能力增强。
3. **AI Infra**：vLLM、SGLang、推理服务、KV Cache、PD 分离、部署、RAG/Agent 基础设施、评测与可观测性。

项目满足 **Star ≥ 100**，或**近 7 天增长 ≥ 20 Star**；新库创建 7 天内达到 20 Star 也会立即进入榜单。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。当天多次运行会合并去重，不覆盖已收集内容。最近 90 天完整日报见 [`archive/index.md`](archive/index.md)，更早内容转入精简月度历史；搜索词和阈值可在 [`config.yaml`](config.yaml) 调整。

---

# AI 应用研究日报 · 2026-10-21

本期新增：**0 篇论文**（其中 0 篇找到可能的代码）和 **2 个 GitHub 项目**。

## AI 投资与交易论文

本期没有发现通过严格双重筛选的新论文。


## GitHub 金融与交易工具

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [gbeced/basana](https://github.com/gbeced/basana) | A Python async and event driven framework for algorithmic trading, with a focus on crypto currencies. | 871 | — | Python | 近期活跃 |
| [The-Knowledge-Graph-Guys/vault-ld](https://github.com/The-Knowledge-Graph-Guys/vault-ld) | Vault-LD: an open spec for Markdown vaults as linked data. YAML-LD frontmatter + a shared `@context` = an RDF knowledge graph. Prose for humans and LLMs, triples for machines. | 240 | — | Python | 近期活跃 |


## Vibe Coding · 工作与学习增强

新增 **6 篇论文**（1 篇找到代码）和 **4 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-20 | [AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](https://arxiv.org/abs/2610.28589) | Xinxin Liu, Bingxin Xu, Wenrui Bao 等 | — |
| 2026-10-20 | [S-Agent 2.0: Spatial Reasoning with a General Coding Agent](https://arxiv.org/abs/2610.28354) | Rui Gong, Ruoyu Wang, Yalun Dai 等 | — |
| 2026-10-20 | [Knowledge as Code](https://arxiv.org/abs/2610.27693) | Martin Monperrus | — |
| 2026-10-19 | [REM: What to Store, When to Recall, What to Forget in Experience Memory for Coding Agents](https://arxiv.org/abs/2610.27377) | Xinyi Lisa Chen, Pedro Herrero-Vidal, Xiaohan Chen 等 | — |
| 2026-10-19 | [Unsupervised Tool Evolution for Coding Agents in Data-Lake Analytics](https://arxiv.org/abs/2610.27327) | Yuqing Yang, Yurong Liu, Deqing Fu 等 | — |
| 2026-10-19 | [ReuF2F: Benchmarking Coding Agents on Formalized Undergraduate Research Problems](https://arxiv.org/abs/2610.27046) | Zeyu Zheng, Yiyang Liu, Yuyang Zhao 等 | [arXiv 页面](https://github.com/cmu-l3/reuF2F) |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [dominikmartn/harp](https://github.com/dominikmartn/harp) | Run many Claude Code and Codex agents side by side, in one sidebar that tells you which one needs you. An unofficial fork of Warp. | 361 | — | Rust | 新项目 |
| [Tongyi-MAI/OpenGCUA](https://github.com/Tongyi-MAI/OpenGCUA) | An open-source stack for generalist computer-use agents, combining code execution, GUI interaction, and cross-device control. | 360 | — | HTML | 新项目 |
| [Jehuge/prompt-collection](https://github.com/Jehuge/prompt-collection) | AI 编程 / vibe coding 提示词收集（中文 + 英文原文） | 24 | — |  | 新项目 |
| [morethanrealio/brambit](https://github.com/morethanrealio/brambit) | Open-source engine for personal AI assistants that chat on web, WhatsApp, Telegram, email and Slack, with memory, connectors, sandboxed code, hosted apps and scheduled routines. Bring your own LLM. | 20 | — | JavaScript | 新项目 |


## AI Infra · 推理部署与应用基础设施

新增 **6 篇论文**（2 篇找到代码）和 **7 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-20 | [Cache Engineering for Agents](https://arxiv.org/abs/2610.28577) | Tianyu Fu, Ruoxi Wang, Zihan Min 等 | [论文链接](https://github.com/thu-nics/AKV) |
| 2026-10-20 | [Beyond the Point Mass: Acceptance-Derived Weights and Distributional Losses for Speculative Decoding](https://arxiv.org/abs/2610.28355) | Tianyu Wu, Zhuohan Wang, Jonathan Geuter 等 | [arXiv 页面](https://github.com/Lucas-TY/D-PAL-SpecForge) |
| 2026-10-20 | [Local Inference of LLMs on Long Contexts: A Data Systems Perspective](https://arxiv.org/abs/2610.28223) | Mattias Dürrmeier, Alberto Lerner | — |
| 2026-10-20 | [How Developers Configure LLM Inference: A Large-Scale Study of Real-World Practices](https://arxiv.org/abs/2610.27945) | Nada Zine, Matias Martinez, Romain Rouvoy 等 | — |
| 2026-10-20 | [ProVe: Proposer-Verifier Decoding](https://arxiv.org/abs/2610.27815) | Ziqi Jin, Weiwen Xu, Jiaxi Li 等 | — |
| 2026-10-19 | [DStill: Trajectory Consistency Distillation for Accelerated One-Step Drafting in Block Diffusion Speculative Decoding](https://arxiv.org/abs/2610.27379) | Shreyas Kulkarni, Uttam Gurram, Madhav Kanda 等 | — |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [eagle-hq/EAGLE-4](https://github.com/eagle-hq/EAGLE-4) | Official Inference Code of EAGLE-4 | 363 | — | Python | 新项目 |
| [T-Crypt/berth](https://github.com/T-Crypt/berth) | Decides who gets your GPU. Chat, image and voice engines lease the card in turn instead of grabbing it, so two of them never load at once and crash each other. One Go binary, nothing else to install. | 113 | — | Go | 新项目 |
| [xLLM-AI/xllm-service](https://github.com/xLLM-AI/xllm-service) | A flexible serving framework that delivers efficient and fault-tolerant LLM inference for clustered deployments. | 100 | +1 | C++ | 近期活跃 |
| [hongfaqiu/strata-manager](https://github.com/hongfaqiu/strata-manager) | Strata Manager makes Niko1221/Strata, the local LLM inference engine, easier to set up and use. Manage local models and services, monitor hardware and API usage, chat and tune inference. Open-source desktop app for Windows / Linux x64. | 30 | +24 | Rust | 新项目 |
| [happyme531/open_rknpu2_lm_infer](https://github.com/happyme531/open_rknpu2_lm_infer) | Fully open-source, high-performance LLM inference engine for the RK3588 NPU | 26 | — | Rust | 新项目 |
| [vcruz305/DSV4.1-Flash-1017-EXL3-Spark-recipe](https://github.com/vcruz305/DSV4.1-Flash-1017-EXL3-Spark-recipe) | DSV4.1-Flash-1017 SAGE EXL3 (1.62 bpw) on one DGX Spark with vLLM: DSpark MTP, cold-expert ATS alias, tile-K 16 MoE, memory guard, measured 31-34 tok/s | 25 | — | Python | 新项目 |
| [Sheltercosmo/Rilldex-RL-Studio](https://github.com/Sheltercosmo/Rilldex-RL-Studio) | RL observability for LLM agents: behavior maps, native trainer metrics, rollout investigations, and Python/SQL analysis. | 23 | — | Python | 新项目 |


> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。

