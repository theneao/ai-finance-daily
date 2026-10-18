# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集三类应用型内容：

1. **AI 投资与金融工具**：投资、交易、资产配置、行情/财务数据、资金流、回测与策略。
2. **Vibe Coding**：Coding Agent、代码库理解、工作流自动化、工作学习与开发能力增强。
3. **AI Infra**：vLLM、SGLang、推理服务、KV Cache、PD 分离、部署、RAG/Agent 基础设施、评测与可观测性。

项目满足 **Star ≥ 100**，或**近 7 天增长 ≥ 20 Star**；新库创建 7 天内达到 20 Star 也会立即进入榜单。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。当天多次运行会合并去重，不覆盖已收集内容。最近 90 天完整日报见 [`archive/index.md`](archive/index.md)，更早内容转入精简月度历史；搜索词和阈值可在 [`config.yaml`](config.yaml) 调整。

---

# AI 应用研究日报 · 2026-10-18

本期新增：**0 篇论文**（其中 0 篇找到可能的代码）和 **0 个 GitHub 项目**。

## AI 投资与交易论文

本期没有发现通过严格双重筛选的新论文。


## GitHub 金融与交易工具

本期没有发现符合条件的新项目。


## Vibe Coding · 工作与学习增强

新增 **10 篇论文**（4 篇找到代码）和 **7 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-09 | [Returning to Development States: When Full Sandbox Snapshots Help Coding Agents](https://arxiv.org/abs/2610.13841) | Daniel Thi Graviet, Tanmay Shah | — |
| 2026-10-09 | [(When) Should a Software Factory be Lights-off? Benchmarking Code Review Agents on Bug Detection](https://arxiv.org/abs/2610.13668) | Chenyang Yang, Hao He, Ti-Chung Cheng 等 | — |
| 2026-10-09 | [AgentSWE: Can Coding Agents Build the Agent You Actually Want?](https://arxiv.org/abs/2610.13361) | Jiahao Wang, Hongjin Qian, Yuyang Hu 等 | [arXiv 页面](https://github.com/VectorSpaceLab/AgentSWE) |
| 2026-10-09 | [SWE-Critix: Post-Training Generalist Verifiers for Assessing Coding-Agent Trajectories](https://arxiv.org/abs/2610.13356) | Jiajun Hu, Chun Yong Chong | [标题匹配](https://github.com/SWE-Critix/SWE-Critix) |
| 2026-10-09 | [Quality, Not Just Outcome: A Structural Scoring Framework for Selecting Coding-Agent Trajectories for Supervised Fine-Tuning](https://arxiv.org/abs/2610.13152) | Sida Li, Yuanxin Liu, Shicheng Li 等 | — |
| 2026-10-09 | [TestSuiteBench: Coding Agents Struggle to Generate Strong Test Suites from Specifications](https://arxiv.org/abs/2610.13065) | Kazuki Egashira, Niels Mündler-Sasahara, Mark Niklas Müller 等 | — |
| 2026-10-09 | [Co-Modifying Application Code and Deployment Infrastructure: A Causal Study of AI Agent Pull Requests](https://arxiv.org/abs/2610.12849) | Mohammad Wathiq Soualhi, Basem Suleiman | — |
| 2026-10-08 | [SWEeper-Bench: Can Agents Discover Bugs in Interactive Software?](https://arxiv.org/abs/2610.14096) | Yang Yao, Haozhe Chen, Bingyi Kang 等 | [ID 命中](https://github.com/zlab-princeton/sweeper-bench) |
| 2026-10-08 | [SWE-Duel: Towards a Self-Scaling Arena for Coding Agents](https://arxiv.org/abs/2610.12569) | Wei Minn, Zhensu Sun, Lwin Khin Shar 等 | [ID 命中](https://github.com/sweduel/SWE-Duel) |
| 2026-10-08 | [Fly-by-Code: Embodied Coding Agents for Aerial Manipulation with Active Visual and Physical Feedback](https://arxiv.org/abs/2610.12549) | Jaewoo Lee, Jeongyeon Seo, Sihyun Cho 等 | — |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) | Ears for coding agents: let AI hear, review and make sound. CPU-only, open source. | 701 | — | Python | 新项目 |
| [Gathin23/tv-vibehack](https://github.com/Gathin23/tv-vibehack) | Your TV, minus the ads. Debloat any Android TV over ADB and give it a clean, tvOS-inspired launcher. Built in an afternoon with Claude Code. | 421 | — | Java | 新项目 |
| [SakanaAI/AI-Scientist-v3](https://github.com/SakanaAI/AI-Scientist-v3) | The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery | 339 | — | Python | 新项目 |
| [reason-machines/reason-network](https://github.com/reason-machines/reason-network) | Reason Network: your team's coding agents, talking to each other. The engine behind `reason network`. | 269 | — | Rust | 新项目 |
| [Graphicle-AI/graphicle](https://github.com/Graphicle-AI/graphicle) | Code graph and memory for your coding agents, in one Rust program. For Claude Code, Codex, Cursor and any MCP client. | 264 | — | Rust | 新项目 |
| [Entelligence-AI/agentplay](https://github.com/Entelligence-AI/agentplay) | Replay your coding agent sessions as a map and a timeline | 243 | — | Python | 新项目 |
| [jatechan/ai-data-extractor](https://github.com/jatechan/ai-data-extractor) | Free open-source extractor for AI coding assistant chat histories. Supports Claude Code, Cursor, Windsurf, Aider, Cline/Roo Code and more | 217 | — | Python | 新项目 |


## AI Infra · 推理部署与应用基础设施

新增 **15 篇论文**（6 篇找到代码）和 **3 个项目**。

### 论文

| 日期 | 论文 | 作者 | 代码 |
|---|---|---|---|
| 2026-10-10 | [SAFE-KV: Causal Suffix Repair for Behavior-Preserving Non-Prefix KV Cache Reuse in RAG](https://arxiv.org/abs/2610.15186) | Xingjian Zhang | [arXiv 页面](https://github.com/XingjianZhang-dev/safe-kv) |
| 2026-10-10 | [Energy-Aware Agentic Orchestration for Multi-Site Service Deployment](https://arxiv.org/abs/2610.14793) | Rodrigo Moreira, Alisson Chaves, Larissa F. Rodrigues Moreira 等 | — |
| 2026-10-10 | [Accelerating Cross-Model LLM Inference via Attention Map Reuse](https://arxiv.org/abs/2610.14688) | Zhan Jin, Yuze Luo, Bin Cui 等 | [论文链接](https://github.com/PKU-DAIR/MapFlow) |
| 2026-10-10 | [Vesta: Queueing-Aware LLM Scheduling for Real-World Workloads](https://arxiv.org/abs/2610.14686) | Lancheng Zou, Bowen Li, Wei Mao 等 | — |
| 2026-10-10 | [Dissecting the Carbon-SLO Tension in Geo-Distributed LLM Serving](https://arxiv.org/abs/2610.14571) | Burak Topcu, Musa Cim, Zuhal Ozturk 等 | [arXiv 页面](https://github.com/topcuburak/carbon-slo-at-geoscale) |
| 2026-10-10 | [KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization](https://arxiv.org/abs/2610.14448) | Sihwan Park, Sung-Yub Kim, Doohyuk Jang 等 | — |
| 2026-10-10 | [Frustratingly Easy Agentic RAG via Portable Skills: A Case Study in Customer Support](https://arxiv.org/abs/2610.14428) | Istok Bako, Bonan Min, Tiffany Shao 等 | — |
| 2026-10-09 | [Simulate Before You Scale: High-Fidelity LLM Inference Planning Without GPUs](https://arxiv.org/abs/2610.14255) | Dipanwita Guhathakurta, Mert Toslali, Srinivasan Parthasarathy 等 | — |
| 2026-10-09 | [ReplaySSM: Cache SSM Inputs, Not State](https://arxiv.org/abs/2610.13778) | Ze-Wei Liou, Harris Nover, Amey Naik 等 | [arXiv 页面](https://github.com/Johnny-Liou/ReplaySSM) |
| 2026-10-09 | [Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy](https://arxiv.org/abs/2610.13708) | Naji Alazhar, Wassel Alazhar | — |
| 2026-10-09 | [AMLworld-Compact: Importance-Weighted Downsampling for Cost-Effective LLM Evaluation and Error Diagnosis](https://arxiv.org/abs/2610.13627) | Natapong Nitarach, Phume Ngampornsukswadi, Pittawat Taveekitworachai 等 | [论文链接](https://github.com/nat-nischw/AMLworld-Compact) |
| 2026-10-09 | [Lossless Inference Acceleration for ASR via EAGLE-Style Speculative Decoding](https://arxiv.org/abs/2610.13506) | Sen Zhang, Xianghu Yue, Yiming Chen 等 | — |
| 2026-10-09 | [Taking Tokenization off the Host for Agentic LLM Serving](https://arxiv.org/abs/2610.13325) | Mohammad Siavashi, Pascal Schwinte, Ali Banaei 等 | — |
| 2026-10-09 | [S$^3$R: Fast and Faithful RL Rollouts via Self-Sparse Speculative Decoding](https://arxiv.org/abs/2610.13202) | Yuhang He, Hongyu Ge, Zihan Lin 等 | — |
| 2026-10-09 | [KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse](https://arxiv.org/abs/2610.13060) | Taiga Ikeda, Daisuke Miyashita, Jun Deguchi | [论文链接](https://github.com/taiga333/eval-kv-repurpose) |


### GitHub 项目

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 类型 |
|---|---|---:|---:|---|---|
| [microsoft/autogen](https://github.com/microsoft/autogen) | A programming framework for agentic AI | 61454 | — | Python | 近期活跃 |
| [justxor/deepseek-local-guide-ru](https://github.com/justxor/deepseek-local-guide-ru) | 🐋 Полный гайд на русском: как установить и запустить DeepSeek локально (V4, R1) на ПК, Mac и сервере — Ollama, llama.cpp, LM Studio, vLLM, Open WebUI, API, RAG, агенты, fine-tuning, лучшие фишки | 59 | — | Shell | 新项目 |
| [xp2001-coder/zero2vllm](https://github.com/xp2001-coder/zero2vllm) | llm-inference | 20 | — | Python | 新项目 |


> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。

