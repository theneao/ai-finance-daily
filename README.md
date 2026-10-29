# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集三类应用型内容：

1. **AI 投资与金融工具**：投资、交易、资产配置、行情/财务数据、资金流、回测与策略。
2. **Vibe Coding**：Coding Agent、代码库理解、工作流自动化、工作学习与开发能力增强。
3. **AI Infra**：vLLM、SGLang、推理服务、KV Cache、PD 分离、部署、RAG/Agent 基础设施、评测与可观测性。

项目满足 **Star ≥ 100**，或**近 7 天增长 ≥ 20 Star**；新库创建 7 天内达到 20 Star 也会立即进入榜单。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。当天多次运行会合并去重，不覆盖已收集内容。最近 90 天完整日报见 [`archive/index.md`](archive/index.md)，更早内容转入精简月度历史；搜索词和阈值可在 [`config.yaml`](config.yaml) 调整。

---

# AI 应用研究日报 · 2026-10-29

本期新增：**0 篇论文**（其中 0 篇找到可能的代码）和 **0 个 GitHub 项目**。

## AI 投资与交易论文

本期没有发现通过严格双重筛选的新论文。


## GitHub 金融与交易工具

本期没有发现符合条件的新项目。


## Vibe Coding · 工作与学习增强

新增 **7 篇论文**（0 篇找到代码）和 **2 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-26 | [Continue or Restart? The Limits of Early Failure Prediction in Coding Agents](https://arxiv.org/abs/2610.35971) | Srinath Srinivasan, Lunxiao Li, Tim Menzies 等 | — |
| 2026-10-25 | [From GPU to TPU with Coding Agents: What Works, What Fails, and What It Costs?](https://arxiv.org/abs/2610.34422) | Hui Sun, Anderson Uchôa, Wesley K. G. Assunção | — |
| 2026-10-25 | [NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names](https://arxiv.org/abs/2610.34253) | Chieh-Yuan Chang, Guan-Wei Chen, Chia-Yi Hsu 等 | — |
| 2026-10-25 | [RoboDuo: Attempt, Check and Atomic Recovery through Code for Vision-Language-Action Models](https://arxiv.org/abs/2610.34108) | Jie Wang, Bo Zhang, Renzhi Lu 等 | — |
| 2026-10-25 | [Securing Agent-Generated Code with Its Own Development History](https://arxiv.org/abs/2610.34098) | Prateek Kumar Rajput, Shahzeb Khan, El-Hacen Diallo 等 | — |
| 2026-10-25 | [How Do Small Coding Agents Use Code Graphs and Embeddings?](https://arxiv.org/abs/2610.33958) | Saurav Bellam | — |
| 2026-10-24 | [Developers as Managers of AI Agents: A Workplace Shadowing Study](https://arxiv.org/abs/2610.33588) | Yi-Hung Chou, June Hyung Kim, Vasisht Kartik 等 | — |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail) | Vibe code with pi in a lightweight, real IDE that customises itself around the way you work — The Vibe You Need | 5357 | — | TypeScript | 近期活跃 |
| [andyhuo520/vibe-knowledge](https://github.com/andyhuo520/vibe-knowledge) | Vibe 知识大赏：一个知识点 → 一条有旁白、每句有出处的精品知识短片（Claude Code skill · 44 套风格 · 代码逐帧成片） | 103 | — | JavaScript | 新项目 |


## AI Infra · 推理部署与应用基础设施

新增 **0 篇论文**（0 篇找到代码）和 **4 个项目**。

### 论文

本期没有发现通过严格双重筛选的新论文。


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [I-You-Dream/NL2SQL_GRPO](https://github.com/I-You-Dream/NL2SQL_GRPO) | 使用 GRPO（通用奖励近端优化）微调 LLM 实现 Text-to-SQL 转换。基于 Qwen2.5-Coder-7B-Instruct 模型，使用 unsloth + vllm 加速训练和推理。 | 25 | — | Python | 新项目 |
| [xxPcy/PharmaLLM-Agent](https://github.com/xxPcy/PharmaLLM-Agent) | Medical LLM agent and MRI segmentation workspace built on PharmaLLM, with LangGraph, vLLM, and BEU-Net. | 24 | — | Python | 新项目 |
| [nsbradley88/talus-public](https://github.com/nsbradley88/talus-public) | Rust LLM inference engine tuned for AMD Strix Halo (gfx1151): a fork of Strata with ggml/llama.cpp-derived HIP kernels. Five models on one 128 GB machine. | 21 | — | Rust | 新项目 |
| [SRN0129/Agenttrust](https://github.com/SRN0129/Agenttrust) | Enterprise Zero-Trust Security, Cascading Delegation, Human Approvals & Verifiable Audit Infrastructure for Autonomous AI Agents | 20 | — | TypeScript | 新项目 |


> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。

