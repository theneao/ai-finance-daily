# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集三类应用型内容：

1. **AI 投资与金融工具**：投资、交易、资产配置、行情/财务数据、资金流、回测与策略。
2. **Vibe Coding**：Coding Agent、代码库理解、工作流自动化、工作学习与开发能力增强。
3. **AI Infra**：vLLM、SGLang、推理服务、KV Cache、PD 分离、部署、RAG/Agent 基础设施、评测与可观测性。

项目满足 **Star ≥ 100**，或**近 7 天增长 ≥ 20 Star**；新库创建 7 天内达到 20 Star 也会立即进入榜单。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。当天多次运行会合并去重，不覆盖已收集内容。最近 90 天完整日报见 [`archive/index.md`](archive/index.md)，更早内容转入精简月度历史；搜索词和阈值可在 [`config.yaml`](config.yaml) 调整。

---

# AI 应用研究日报 · 2026-10-19

本期新增：**0 篇论文**（其中 0 篇找到可能的代码）和 **1 个 GitHub 项目**。

## AI 投资与交易论文

本期没有发现通过严格双重筛选的新论文。


## GitHub 金融与交易工具

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [fidetolabs/qanat](https://github.com/fidetolabs/qanat) | A data platform for investment research. Ingests financial data sources and computes point-in-time financial metrics for valuation and screening. Delivered as an MCP server. | 315 | — | Python | 近期活跃 |


## Vibe Coding · 工作与学习增强

新增 **6 篇论文**（2 篇找到代码）和 **2 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-16 | [HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents](https://arxiv.org/abs/2610.23479) | Hongcheng Gao, Alex Zhou, Jay Zhu 等 | [论文链接](https://github.com/HexaFuture/HexaShell) |
| 2026-10-16 | [MetaCurate: Evolving Curation Filters for High-Quality Agentic Coding Data](https://arxiv.org/abs/2610.23134) | Donghoon Kim, Seunghyuk Oh, Kevin Galim 等 | — |
| 2026-10-16 | [Trojan Horse: Automated Repository Poisoning against Coding Agents](https://arxiv.org/abs/2610.23109) | Xiao Yang, Jinchang Hou, Jiawei Chen 等 | — |
| 2026-10-16 | [From Approval to Abuse: Privilege Escalation Attacks on Harness-Protected Coding Agents](https://arxiv.org/abs/2610.22987) | Xianglin Yang, Yechao Zhang, Jiahao Liu 等 | — |
| 2026-10-16 | [Self-Evolving Coding Agents via Harness-Policy Optimization](https://arxiv.org/abs/2610.22791) | Zhepei Wei, Wenlin Yao, Baolin Peng 等 | [ID 命中](https://github.com/MSR-Orchard/Self-HPO) |
| 2026-10-15 | [TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://arxiv.org/abs/2610.22732) | Aaron J. Li, Weijia Xu, Chandan Singh 等 | — |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [alchaincyf/huashu-motion](https://github.com/alchaincyf/huashu-motion) | 让你的agent一键直出商业级产品宣传片：会作曲，能指着画面改。Commercial-grade launch films by your coding agent — point at the frame to change it. | 518 | — | JavaScript | 新项目 |
| [KnifeLemon/Droidline](https://github.com/KnifeLemon/Droidline) | Android automation from code. Test your apps on real phones, script the tasks you repeat, run a shelf of phones, or let an AI agent use one, from Python, Node.js, the CLI, HTTP or Appium clients. No ADB, no USB cable, no root. | 265 | — | Go | 新项目 |


## AI Infra · 推理部署与应用基础设施

新增 **5 篇论文**（0 篇找到代码）和 **2 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-16 | [DLite: History-free Speculative Decoding for Agentic AI](https://arxiv.org/abs/2610.23787) | Jiaming Xu, Hanzhen Wang, Tianlang Zhao 等 | — |
| 2026-10-16 | [BS-Spec: BFP-Based Bit-Sharing for Self-Speculative LLM Decoding with LUT-Driven Mixed-Precision Acceleration](https://arxiv.org/abs/2610.22877) | Jiwoo Kim, Gunho Park, Sunwoo Yoo 等 | — |
| 2026-10-16 | [Stealthy Poisoning Attacks via Reused KV Cache of Reasoning](https://arxiv.org/abs/2610.22873) | L. Zhu, Y. Jung, S. Szyller | — |
| 2026-10-15 | [MemLLM: End-to-end In-Storage Acceleration of On-device Retrieval-Augmented Generation using Precomputed KV Caches](https://arxiv.org/abs/2610.22579) | Seungkwan Kang, Hyungseok Ko, Heemin Kim 等 | — |
| 2026-10-15 | [On the SPOT: Enhancing Speculative Decoding for Diffusion Language Models via Commit-Order Prediction](https://arxiv.org/abs/2610.22543) | Eliezer Shlomi, Eliron Rahimi, Avi Mendelson 等 | — |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [Elevatormusic/DeepSeek-V4.1-Flash-1017-EXL3-TensorFold-2x-DGX-Spark](https://github.com/Elevatormusic/DeepSeek-V4.1-Flash-1017-EXL3-TensorFold-2x-DGX-Spark) | DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw on 2x NVIDIA DGX Spark (GB10) with TensorFold: 2.1-2.3x the vLLM kit's decode speed. | 27 | — | Python | 新项目 |
| [eliasbiondo/antirion](https://github.com/eliasbiondo/antirion) | ⚡ The fastest open-source AI gateway — one Rust binary with a built-in console to route, secure, budget and observe every LLM call across OpenAI, Anthropic, Gemini, Bedrock and more. | 25 | — | Rust | 新项目 |


> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。

