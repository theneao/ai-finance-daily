# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集三类应用型内容：

1. **AI 投资与金融工具**：投资、交易、资产配置、行情/财务数据、资金流、回测与策略。
2. **Vibe Coding**：Coding Agent、代码库理解、工作流自动化、工作学习与开发能力增强。
3. **AI Infra**：vLLM、SGLang、推理服务、KV Cache、PD 分离、部署、RAG/Agent 基础设施、评测与可观测性。

项目满足 **Star ≥ 100**，或**近 7 天增长 ≥ 20 Star**；新库创建 7 天内达到 20 Star 也会立即进入榜单。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。当天多次运行会合并去重，不覆盖已收集内容。最近 90 天完整日报见 [`archive/index.md`](archive/index.md)，更早内容转入精简月度历史；搜索词和阈值可在 [`config.yaml`](config.yaml) 调整。

---

# AI 应用研究日报 · 2026-10-15

本期新增：**0 篇论文**（其中 0 篇找到可能的代码）和 **1 个 GitHub 项目**。

## AI 投资与交易论文

本期没有发现通过严格双重筛选的新论文。


## GitHub 金融与交易工具

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [polytutor-ai/polymarket-black-scholes-hft-bot](https://github.com/polytutor-ai/polymarket-black-scholes-hft-bot) | High-frequency Polymarket trading bot for crypto Up/Down markets, using Black-Scholes and TWAP probability models, Chainlink and multi-exchange price feeds, fee-aware EV, and risk management. | 20 | — | Python | 新项目 |


## Vibe Coding · 工作与学习增强

新增 **15 篇论文**（1 篇找到代码）和 **2 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-14 | [Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents](https://arxiv.org/abs/2610.20344) | Yuyao Ge, Shenghua Liu, Peizhong Gao 等 | — |
| 2026-10-14 | [Maximising Transparency in Context Compaction Improves Retention of Facts and Commitments for Lightweight Coding Agents](https://arxiv.org/abs/2610.20116) | Felix Woolford | — |
| 2026-10-14 | [The Code of Theseus: Can Agents Rebuild Software from Recovered Design Documents?](https://arxiv.org/abs/2610.20068) | Cezar Sas, Sandra Mitrović, Fabio Barth 等 | — |
| 2026-10-14 | [What Coding Agents Leave Unsaid: Measuring Task-State Gaps Between Execution and Reports](https://arxiv.org/abs/2610.20003) | Guoyang Xu, Rui Zhang, Xiuyu Wu 等 | — |
| 2026-10-14 | [Temporal Adaptive Fine-Tuning for Code Comprehension](https://arxiv.org/abs/2610.19970) | Alex Wolf, Pooja Rani, Harald C. Gall | — |
| 2026-10-14 | [ReproBAIT: Can coding agents build their own biological AI tools?](https://arxiv.org/abs/2610.19810) | Shiv Muthupandiyan, Tolga H. Dur, Mac Walker 等 | — |
| 2026-10-14 | [JevCoder: When Does Decision Delegation Pay Off in Code Repair?](https://arxiv.org/abs/2610.19596) | Jiahao Zhang, Yifan Zhang, Yu Huang | — |
| 2026-10-13 | [How Far Can Coding Agents Go in Visual Generation?](https://arxiv.org/abs/2610.19025) | Hengguang Zhou, Yuanhao Ban, Jiaqi Feng 等 | — |
| 2026-10-13 | [The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery](https://arxiv.org/abs/2610.18933) | Robert Tjarko Lange, Luca Grillotti, Yutaro Yamada 等 | [ID 命中](https://github.com/SakanaAI/AI-Scientist-v3) |
| 2026-10-11 | [SpecForge: Recursive Self-Improvement for Coding Agents via Behavioral Specifications](https://arxiv.org/abs/2610.15708) | Yutong Cheng, Haifeng Chen, Peng Gao 等 | — |
| 2026-10-11 | [ANTE: Anticipate, Then Execute -- Learning Internal World Models for Coding Agents from Verified Beliefs](https://arxiv.org/abs/2610.15368) | Yi Ge, Kangrui Ruan, Jifan Chen 等 | — |
| 2026-10-10 | [ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling](https://arxiv.org/abs/2610.15166) | Xinge Peng, Zhen Fang, Ruibing Wang 等 | — |
| 2026-10-10 | [When the Approved File Is Unchanged: Authority-Set Integrity for Deployment and Coding-Agent Approvals](https://arxiv.org/abs/2610.15137) | Md Imran Hossen | — |
| 2026-10-10 | [TurnCost: Turns, Not Observations: Cache-Aware Loop Engineering for Coding Agents](https://arxiv.org/abs/2610.15093) | Pramod Kumar, Raj Kumar Pandey | — |
| 2026-10-10 | [Do Modifications Made by Coding Agents Make Subsequent Software Maintenance Harder?](https://arxiv.org/abs/2610.14768) | Ruwei Pan, John Zhang, Linhao Wu 等 | — |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [liyupi/ai-promo-video-maker](https://github.com/liyupi/ai-promo-video-maker) | 一句话让 AI 帮你做产品宣传片！把产品名或网址告诉 Cursor、Claude Code、Codex 等 AI 编程工具，它会自己调研产品、画出多种风格样图让你挑选、截取 4K 真实页面、按音乐节拍卡点剪辑、生成 AI 旁白并逐句转写校验、自动审图，最后交付一支 4K 商业宣传视频和可在线播放的网页版。App、网站、SaaS、开源项目、课程、AI 模型都能做，你只需确认需求、试听配乐。不用学剪辑软件，也不用花钱找外包。基于 Remotion + ElevenLabs，可直接克隆使用，也能一键安装为 Agent Skill。 | 273 | — | Python | 新项目 |
| [Betterfans-link/betterfans-mcp](https://github.com/Betterfans-link/betterfans-mcp) | MCP server for the BetterFans Link SDK, the OnlyFans API. Gives AI coding assistants access to OnlyFans API documentation, guides, and code examples. | 29 | — | TypeScript | 新项目 |


## AI Infra · 推理部署与应用基础设施

新增 **15 篇论文**（2 篇找到代码）和 **0 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-14 | [FOLD: Position-Free Far Memory with Local Order for Long-Context Speculative Decoding](https://arxiv.org/abs/2610.20392) | Shuxuan Li, Jialiang Kang, Yanghao Zhou 等 | — |
| 2026-10-14 | [TreeSpark: Learning to Draft the Trees You Verify for Speculative Decoding](https://arxiv.org/abs/2610.20175) | Jihao Zhao, Qianyu Jiang, Shuaishuai Zu 等 | — |
| 2026-10-14 | [Not All Criteria Matter: Importance-Aware Criteria Weighting for Rubric-Based LLM Evaluation](https://arxiv.org/abs/2610.19915) | Haocheng Yang, Licheng Pan, Yiming Dong 等 | — |
| 2026-10-14 | [MAPLE: A Multi-Axis Parametric Knowledge Extraction Lens for LLM Evaluation](https://arxiv.org/abs/2610.19827) | Minsuh Joo, Youna Kim, Choonghyun Park 等 | — |
| 2026-10-14 | [PN-Mix: Pair-Norm Guided Mixed-Precision Key Cache Quantization for Efficient Long-Output LLM Inference](https://arxiv.org/abs/2610.19605) | Gil Jae Song, Sungjoo Yoo | — |
| 2026-10-13 | [CacheSmith: Accurate RAG Serving under Latency SLOs with Adaptive KV Reuse](https://arxiv.org/abs/2610.18925) | Xinyue Ma, Damin Lee, Aashaka Shah 等 | — |
| 2026-10-12 | [FORGE: Procedural Weight Generation for Sparse MoE Inference](https://arxiv.org/abs/2610.16890) | Chanyoung Moon, Travis Pence, Daisuke Yamada 等 | — |
| 2026-10-11 | [Lightweight Scheduling Policies for Continuously Batched LLM Serving Across GPU Architectures](https://arxiv.org/abs/2610.15899) | Ashman Mehra, Akshan Agarwal, Aryeh Carmi | — |
| 2026-10-11 | [Native Dual Pools or Shared Paging? Memory Organization for Concurrent Hybrid LLM Serving](https://arxiv.org/abs/2610.15755) | Dongwook Kang | — |
| 2026-10-11 | [To Cache or Not to Cache: Understanding and Mitigating Safety Incompatibility in Cross-Model KV Cache Reuse](https://arxiv.org/abs/2610.15721) | Zhiwei Lin, Jiahao Liu, Yan Liu 等 | [arXiv 页面](https://github.com/Snakinya/VReparo) |
| 2026-10-11 | [Context-Aware Precision Scheduling for Small Language Models](https://arxiv.org/abs/2610.15640) | Mukund Athmaram, Manoj Rao, Liang Ma | — |
| 2026-10-11 | [The Price of Precision: A Calibrated Cost Model for Mixed-Precision LLM Serving](https://arxiv.org/abs/2610.15629) | Mukund Athmaram, Manoj Rao, Liang Ma | — |
| 2026-10-11 | [Approximation Algorithms for Dual-Memory Request Scheduling in Disaggregated LLM Inference](https://arxiv.org/abs/2610.15579) | Xin Wang, Hong Shen, Hui Tian 等 | — |
| 2026-10-11 | [CacheLink: Functional KV Transport for Zero-Prefill Cross-Model Context Handoff](https://arxiv.org/abs/2610.15509) | Haomiao Qiu, Yining Tang, Zijia Song 等 | — |
| 2026-10-11 | [SpecFit: Not All Draft Tokens Cost the Same in Offloaded MoE Inference](https://arxiv.org/abs/2610.15417) | Hongliang Cao, Xiuyu Li, Siqi Wang 等 | [论文链接](https://github.com/Chlience/SpecFit) |


### GitHub 项目

本期没有发现符合条件的新项目。


> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。

