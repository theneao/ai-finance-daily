# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集三类应用型内容：

1. **AI 投资与金融工具**：投资、交易、资产配置、行情/财务数据、资金流、回测与策略。
2. **Vibe Coding**：Coding Agent、代码库理解、工作流自动化、工作学习与开发能力增强。
3. **AI Infra**：vLLM、SGLang、推理服务、KV Cache、PD 分离、部署、RAG/Agent 基础设施、评测与可观测性。

项目满足 **Star ≥ 100**，或**近 7 天增长 ≥ 20 Star**；新库创建 7 天内达到 20 Star 也会立即进入榜单。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。当天多次运行会合并去重，不覆盖已收集内容。最近 90 天完整日报见 [`archive/index.md`](archive/index.md)，更早内容转入精简月度历史；搜索词和阈值可在 [`config.yaml`](config.yaml) 调整。

---

# AI 应用研究日报 · 2026-11-02

本期新增：**0 篇论文**（其中 0 篇找到可能的代码）和 **2 个 GitHub 项目**。

## AI 投资与交易论文

本期没有发现通过严格双重筛选的新论文。


## GitHub 金融与交易工具

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [fonrex/fonrex](https://github.com/fonrex/fonrex) | Financial data, unlocked. | 78 | +70 | Python | 近期活跃 |
| [Jokejoker-designer/QUANTSMART](https://github.com/Jokejoker-designer/QUANTSMART) | A local workspace for testing strategies and building your own quantitative algorithms. Strategy Cards, historical replay, traceable validation and an optional MT5 connector. | 20 | — | TypeScript | 新项目 |


## Vibe Coding · 工作与学习增强

新增 **2 篇论文**（0 篇找到代码）和 **2 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-30 | [Migrating a Legacy Scientific Application with an AI Coding Agent: NICAM from Fortran to Kokkos](https://arxiv.org/abs/2610.41313) | Xuanzhengbo Ren, Takashi Shimokawabe, Hisashi Yashiro | — |
| 2026-10-29 | ["Shall We Approve?" Consequence-Aware Approval for Autonomous Coding Agents](https://arxiv.org/abs/2610.40753) | Weiheng Wu, Junkai Chen, Zhensu Sun 等 | — |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [benjitaylor/skills](https://github.com/benjitaylor/skills) | Skills for AI coding agents. | 569 | — | TypeScript | 新项目 |
| [actionow-ai/vvv](https://github.com/actionow-ai/vvv) | 一次构建视频模板，多次复用：给 Claude Code、Codex 等 25+ 个 Agent 的开源可编辑婚礼视频模板与 Agent Skill。Build a video template once, reuse it across coding agents. | 513 | — | Python | 新项目 |


## AI Infra · 推理部署与应用基础设施

新增 **6 篇论文**（1 篇找到代码）和 **1 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-30 | [Flide: Accelerating Decision Inference with Exact State Forking](https://arxiv.org/abs/2610.42148) | Bobo Li, Jiajia Song, Hao Fei 等 | [标题匹配](https://github.com/OmniJev/Flide) |
| 2026-10-30 | [HiState: Hierarchical Prefix Cache Management for Hybrid LLM Serving in Agentic Workloads](https://arxiv.org/abs/2610.41508) | Zaifeng Pan, Lucas Wang, Xinwei Qiang 等 | — |
| 2026-10-30 | [KV-Cache Patching: Tracing How and Where Fine-Tuned Behaviors Arise](https://arxiv.org/abs/2610.41480) | Jonas Loos, Oliver Eberle | — |
| 2026-10-30 | [LEAP: Efficient LLM Inference Scheduling with Generalizable Length Prediction](https://arxiv.org/abs/2610.41359) | Kwan Yan, Jialun Zhong, Yanzeng Li | — |
| 2026-10-30 | [TraceSpec: Understanding and Improving Speculative Decoding for LLM Agents](https://arxiv.org/abs/2610.41177) | Jihao Zhao, Shuaishuai Zu, Pengfei Li 等 | — |
| 2026-10-30 | [ARK: Avoiding Routing Collisions for KV Cache Transfer in Disaggregated LLM Inference](https://arxiv.org/abs/2610.41160) | Hung-Chun Lin, Ting-Wei Hsu, Chung-En Ho 等 | — |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [Leonccaa/ReVolta](https://github.com/Leonccaa/ReVolta) | Stable, high-throughput inference server for multi-GPU NVIDIA V100 (SM70): Qwen3.8 Flash-Next with AWQ / NVFP4, multimodal input, CPU/disk KV offload, and MTP or DFlash2 speculative decoding. | 31 | +22 | Python | 新项目 |


> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。

