# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集三类应用型内容：

1. **AI 投资与金融工具**：投资、交易、资产配置、行情/财务数据、资金流、回测与策略。
2. **Vibe Coding**：Coding Agent、代码库理解、工作流自动化、工作学习与开发能力增强。
3. **AI Infra**：vLLM、SGLang、推理服务、KV Cache、PD 分离、部署、RAG/Agent 基础设施、评测与可观测性。

项目满足 **Star ≥ 100**，或**近 7 天增长 ≥ 20 Star**；新库创建 7 天内达到 20 Star 也会立即进入榜单。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。当天多次运行会合并去重，不覆盖已收集内容。最近 90 天完整日报见 [`archive/index.md`](archive/index.md)，更早内容转入精简月度历史；搜索词和阈值可在 [`config.yaml`](config.yaml) 调整。

---

# AI 应用研究日报 · 2026-11-08

本期新增：**0 篇论文**（其中 0 篇找到可能的代码）和 **4 个 GitHub 项目**。

## AI 投资与交易论文

本期没有发现通过严格双重筛选的新论文。


## GitHub 金融与交易工具

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [rnikitin/QuantNavigator](https://github.com/rnikitin/QuantNavigator) | An extensible harness for quantitative research. Product vision and roadmap. | 239 | — |  | 近期活跃 |
| [ZevFlashthorn/adaq-rpocket-team](https://github.com/ZevFlashthorn/adaq-rpocket-team) | AdaQ (Ada Quant) is an AI-powered quantitative trading platform for equities and digital crypto assets. | 42 | — | HTML | 新项目 |
| [SapphireFarCzar/A.W.-rpocket-team-Stratgies-Indicator](https://github.com/SapphireFarCzar/A.W.-rpocket-team-Stratgies-Indicator) | A.W. Strategy: a rules-based intraday futures strategy for TradingView (market structure, order flow, GEX levels), with an automated options-data pipeline and a paper-trading research bot. | 42 | — | HTML | 新项目 |
| [DegreeApprentice/Ton-token-sniper-bot](https://github.com/DegreeApprentice/Ton-token-sniper-bot) | TON token sniper bot for STON.fi and DeDust DEX. Auto-skip scam tokens and honeypots, secure profits with trailing stops. High-frequency crypto trading bot for The Open Network. Toncoin | 35 | — |  | 新项目 |


## Vibe Coding · 工作与学习增强

新增 **0 篇论文**（0 篇找到代码）和 **5 个项目**。

### 论文

本期没有发现通过严格双重筛选的新论文。


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [stablyai/orca](https://github.com/stablyai/orca) | Orca lets you run a fleet of coding agents (e.g. Claude Code, Codex) with your own subscription. Available on desktop, mobile and remote runtime. | 118751 | — | TypeScript | 近期活跃 |
| [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage) | World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio. | 78374 | — | Python | 近期活跃 |
| [aa1143/NamiAgent](https://github.com/aa1143/NamiAgent) | 零基础入门 AI Agent 的基础教程。不只是教程，也是一个能在本地跑起来的 Agent：读写文件、执行命令、MCP、长期记忆，自带网页端看清每一步。从 100 行最小循环开始，一课加一个能力，最后拆解 Claude Code、Codex 等主流 Agent | 415 | — | Python | 新项目 |
| [jmanico/grim-prompter](https://github.com/jmanico/grim-prompter) | Threat modeling for AI coding agents: point Claude Code, Codex or any agent at your repo and get an evidence-traced threat model. 36 architectures, 29 methods, MIT. | 388 | — |  | 新项目 |
| [switch-dimension/deepseek-superagent-guide](https://github.com/switch-dimension/deepseek-superagent-guide) | A guide that teaches an AI coding assistant DeepSeek's superagent pattern and how to set it up with Claude Code or OpenCode | 20 | — |  | 新项目 |


## AI Infra · 推理部署与应用基础设施

新增 **9 篇论文**（1 篇找到代码）和 **0 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-31 | [Multi-Turn Semantic Caching for Low-Cost LLM Serving](https://arxiv.org/abs/2611.01077) | Baran Atalar, Selly Beyene, Xutong Liu 等 | — |
| 2026-10-31 | [Ripple: Deadline-Aware CPU-GPU Sharing for Embodied Inference](https://arxiv.org/abs/2611.01067) | Jiadong Zhang, Xiaosong Ma | — |
| 2026-10-31 | [RTP-LLM: Building an Evolvable and Reliable LLM Inference Engine at Alibaba Scale](https://arxiv.org/abs/2611.00967) | Jiarui Guo, Zhi Zhang, Boyu Tan 等 | — |
| 2026-10-31 | [TVP: TV is Almost All You Need for Speculative Decoding](https://arxiv.org/abs/2611.00588) | Aaryam Sharma | [标题匹配](https://github.com/KentoNishi/awesome-all-you-need-papers) |
| 2026-10-31 | [BitLLM: Efficient Low-Bit, Conversion-Hiding LLM Decoding on Mobile GPUs](https://arxiv.org/abs/2611.00547) | Hangyu Zheng, Zhihao Shu, Kunxiong Zhu 等 | — |
| 2026-10-31 | [Weights That Stay: On-Chip Megakernels for Serial Heads in Speculative Decoding](https://arxiv.org/abs/2611.00506) | Xinwei Qiang, Ziyi Xu, Zaifeng Pan 等 | — |
| 2026-10-31 | [te-comp: A Complete MLIR Compiler Generating Self-Contained C Inference Engines for MCUs](https://arxiv.org/abs/2611.03710) | Van Chan Ngo | — |
| 2026-10-30 | [Rethinking KV Cache Eviction for Agentic LLM Serving](https://arxiv.org/abs/2611.00391) | Jiakun Fan, Han Meng, Yuxuan Xia 等 | — |
| 2026-10-30 | [C3: Speech-Guided KV Retrieval for Long-Context SpeechLLM Inference](https://arxiv.org/abs/2611.00333) | Dancheng Liu, Markus Müller, Rupak Vignesh Swaminathan 等 | — |


### GitHub 项目

本期没有发现符合条件的新项目。


> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。

