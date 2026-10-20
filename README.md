# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集三类应用型内容：

1. **AI 投资与金融工具**：投资、交易、资产配置、行情/财务数据、资金流、回测与策略。
2. **Vibe Coding**：Coding Agent、代码库理解、工作流自动化、工作学习与开发能力增强。
3. **AI Infra**：vLLM、SGLang、推理服务、KV Cache、PD 分离、部署、RAG/Agent 基础设施、评测与可观测性。

项目满足 **Star ≥ 100**，或**近 7 天增长 ≥ 20 Star**；新库创建 7 天内达到 20 Star 也会立即进入榜单。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。当天多次运行会合并去重，不覆盖已收集内容。最近 90 天完整日报见 [`archive/index.md`](archive/index.md)，更早内容转入精简月度历史；搜索词和阈值可在 [`config.yaml`](config.yaml) 调整。

---

# AI 应用研究日报 · 2026-10-20

本期新增：**3 篇论文**（其中 0 篇找到可能的代码）和 **1 个 GitHub 项目**。

## AI 投资与交易论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-19 | [Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents](https://arxiv.org/abs/2610.26438) | Mengxiao Wang, Nitesh Saxena | — |
| 2026-10-19 | [ACE-Trader: Adversarial Co-Evolution for Generator-Critic Trading Systems](https://arxiv.org/abs/2610.25847) | Chang Zhou, Jiarun Zhou, Xingtong Yu 等 | — |
| 2026-10-16 | [From SEC Filings to Financial Signals: Evaluating LLMs on Stock Market Reactions and Analyst Forecasts](https://arxiv.org/abs/2610.24268) | Shengkun Wang, Taoran Ji, Linhan Wang 等 | — |


## GitHub 金融与交易工具

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [JKorf/Bitfinex.Net](https://github.com/JKorf/Bitfinex.Net) | C#/.NET client library for the Bitfinex.com cryptocurrency exchange REST and WebSocket APIs, supporting Spot and Futures trading and market data with strongly typed models. | 100 | — | C# | 近期活跃 |


## Vibe Coding · 工作与学习增强

新增 **12 篇论文**（3 篇找到代码）和 **4 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-19 | [FOMTools: Development and AI-Assisted Code Generation for First-Order Methods](https://arxiv.org/abs/2610.26743) | Vinit Ranjan, Daniel Deza, Anushka Acharya 等 | — |
| 2026-10-19 | [When Coding Agents Outpace Review: Evaluating PRD-Driven Development in Mature Enterprise Repositories](https://arxiv.org/abs/2610.26394) | Tianqi Liu, Yandong Guan, Songze Li 等 | [论文链接](https://github.com/TianqiLiu1/PACE-Bench) |
| 2026-10-19 | [From Code to Playable Systems: CEGame-Bench for Long-Horizon Game Creation Agents](https://arxiv.org/abs/2610.26098) | Zixuan Dong, Yanghai Wang, Hanyan Bian 等 | — |
| 2026-10-19 | [Policy Search in Code Space for Multi-Agent Pathfinding](https://arxiv.org/abs/2610.25946) | Matthias Eder, Pantelis Emmanouil, Vivek Farias 等 | — |
| 2026-10-19 | [SWE-Residual: Evaluating Starting-State Robustness of Coding Agents](https://arxiv.org/abs/2610.25899) | Jinze Li, Weijie Liu, Jinfeng Xu 等 | — |
| 2026-10-19 | [FrontierRefactor: Benchmarking Multi-Scale Performance-Oriented Codebase Refactoring](https://arxiv.org/abs/2610.25834) | Shijian Wang, Fanqing Meng, Jiajun Chen 等 | — |
| 2026-10-19 | [OpenSaC: A Python Library for Search as Code in Deep Research Agents](https://arxiv.org/abs/2610.25779) | Qi Liu, Jiaxin Mao, Fengbin Zhu 等 | [arXiv 页面](https://github.com/liuqi6777/OpenSaC) |
| 2026-10-19 | [How Effectively Do Security Skills Guide Coding Agents in Vulnerability Detection in Linux Kernel?](https://arxiv.org/abs/2610.25705) | Haoran Xue, Nikta Akbarpour, Gias Uddin 等 | — |
| 2026-10-18 | [Over-Defense in Coding Agents Begins at Silent Forks](https://arxiv.org/abs/2610.24949) | Hanjun Luo, Xuecheng Liu, Xiucheng Zhang 等 | [论文链接](https://github.com/Astarojth/silent-forks) |
| 2026-10-17 | [Teaching Code Agents to Ask Without Leaking Private Code](https://arxiv.org/abs/2610.24824) | Wenjia Jiang, Jieke Shi, Zhensu Sun 等 | — |
| 2026-10-16 | [Cortex: A Fixed-Point Theory of Governed Coding Agents - Technical Report](https://arxiv.org/abs/2610.24255) | Marius-Constantin Dinu, Florian Zeba | — |
| 2026-10-16 | [SWE-Bench Pro V2: A Cleaner, Harder-to-Game Coding Benchmark](https://arxiv.org/abs/2610.24206) | Soham Dan, Jeff Da, Sanyam Bhutani 等 | — |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [UnderleveledBuilder/awesome-short-drama-skills](https://github.com/UnderleveledBuilder/awesome-short-drama-skills) | AI 短剧 · 漫剧 Skill（技能包）精选：剧本、改编、分镜、Seedance / 可灵 / MiniMax 视频提示词，千问、豆包、龙虾 OpenClaw、WorkBuddy、Claude Code、Codex 等智能体可用 \| Curated agent skills for AI short drama, micro drama / microdrama, vertical drama and manju (AI comic drama): screenwriting, storyboards, Seedance / Kling / MiniMax video prompts | 312 | — | HTML | 新项目 |
| [EL4CTEO/blender-skills](https://github.com/EL4CTEO/blender-skills) | Professional Blender 5.2 workflows as Agent Skills for Claude Code, Codex, Gemini CLI, Copilot and Cursor: modeling, UVs, PBR, baking, rigging, animation, export and QA. | 291 | — | Python | 新项目 |
| [eecs498-aase/materials](https://github.com/eecs498-aase/materials) | Lecture and lab slides for EECS 498 AASE (Applied Agentic Software Engineering), UMich Fall 2026 | 231 | — | Python | 近期活跃 |
| [mustafacagri/vibe-usage](https://github.com/mustafacagri/vibe-usage) | See the quota left on Claude Code, Codex, Cursor and Antigravity, launch the tool that has room and hand a task over. Windows tray, macOS menu bar and CLI. | 23 | — | TypeScript | 新项目 |


## AI Infra · 推理部署与应用基础设施

新增 **12 篇论文**（2 篇找到代码）和 **3 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-19 | [SARP: An On-SSD Index for KVCache with Fast Prefix Matching and Recovery](https://arxiv.org/abs/2610.26849) | Jun Kong, Qi Lin, Zhichao Cao | — |
| 2026-10-19 | [Tandem: Serving Hybrid Linear-Attention GUI Agents on Mobile NPUs](https://arxiv.org/abs/2610.26660) | Zhuomin Chen, Jingchao Ni, Xu Zheng 等 | — |
| 2026-10-19 | [MX-Like Tensor Core for LLM Inference with NPU Integration via Hardware-Software Co-Design Exploration](https://arxiv.org/abs/2610.26083) | Zijun Zhao, Ruichu Ao, Stef Cuyckens 等 | — |
| 2026-10-18 | [System X: An LLM Decision Model That Replies from Its Own KV Cache](https://arxiv.org/abs/2610.25456) | Syed Usama Khalid Bukhari, Syed Safwan Khalid, Muhammad Aamir | — |
| 2026-10-18 | [MOSAIC: Multi-Objective Search for Allocating Inference Cache Across LLM Decoder Layers](https://arxiv.org/abs/2610.25431) | Sravanth Kodavanti, Manjunath Arveti | — |
| 2026-10-18 | [Visual Cache Reuse for Efficient Multimodal Inference](https://arxiv.org/abs/2610.25136) | Shuheng Gao, Yuankai Fan, Jiaqiang Ma 等 | — |
| 2026-10-18 | [Conjugate Compilation: Self-Improving Agentic Co-Compilation for Speculative Decoding](https://arxiv.org/abs/2610.25012) | Annabelle Sujun Tang, Rohan Mahapatra, Christopher Priebe 等 | — |
| 2026-10-18 | [When Does Better Acceptance Pay? A Controlled Study of Speculative Decoding](https://arxiv.org/abs/2610.24993) | Yongchao Long, Chunrui Zheng, Yuxuan Zhou 等 | [arXiv 页面](https://github.com/longyongchao/SpecLab) |
| 2026-10-17 | [PV-Decoding: Progressive Verification Decoding with Decode Gating for Diffusion Language Models](https://arxiv.org/abs/2610.24722) | Renxi Liu, Yiming Li, Shengyin Sun 等 | — |
| 2026-10-17 | [TideKV: Delayed KV Eviction via Layer-Wise Chunked Prefill for Memory-Efficient Long-Context LLM Inference](https://arxiv.org/abs/2610.24499) | Yu Wang, Zhu Wang, Ning Hu 等 | — |
| 2026-10-17 | [FlashMap: Flow Map Speculative Decoding](https://arxiv.org/abs/2610.24365) | Jeff Shen, Zhejian Zhou, Ryan Lee 等 | [arXiv 页面](https://github.com/al-jshen/flashmap) |
| 2026-10-16 | [KVCompass: A Discovery Plane for Internet-Scale Prefix Cache Sharing in LLM Serving](https://arxiv.org/abs/2610.24179) | Shiyi Ling, Fei Fang, Chen Qian | — |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [MemTensor/MemT-1.0](https://github.com/MemTensor/MemT-1.0) | Official repository for MemT-1.0 | 94 | — | Python | 新项目 |
| [surya-koritala/condor](https://github.com/surya-koritala/condor) | Qwen3.8-Flash-Next (180B MoE) on one 12-16 GB NVIDIA GPU, Linux or Windows. Own engine, own compression. | 30 | — | HTML | 新项目 |
| [Lowaltitudeflight/local-llm-tuning-guide](https://github.com/Lowaltitudeflight/local-llm-tuning-guide) | A decision library for running local LLMs on multi-GPU machines without NVLink: parallelism, communication, quantization, speculative decoding, KV cache. Every conclusion carries its evidence grade and reproducible conditions. | 21 | — | Python | 新项目 |


> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。

