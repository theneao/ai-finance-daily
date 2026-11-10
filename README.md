# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集 AI 投资研究、金融 Agent、交易框架、金融工具和交易游戏。论文源结合 arXiv 与 [Hugging Face Trending Papers](https://huggingface.co/papers/trending)，仅筛选 AI 投资交易研究，按 arXiv ID 去重；Trending 中重新走热的旧论文也可收录，保留原发表日期与 HF 社区热度。

**[📚 完整热门项目总榜（全部历史项目 · Star 排名 · 分类导航）](HOT_PROJECTS.md)** · **[月度总结](archive/index.md)**

热门总榜不限制项目创建时间，收录 **Star > 100** 且**近三年有代码更新**的非归档项目，包括历史 Star > 1,000 的成熟项目；每天随日报刷新，按 Star 降序排列。分类包括 Agent、交易框架（回测/语言）、工具（看板/数据源/创意）、游戏、论文研究，市场标签区分美股、A股、虚拟货币、期货、因子。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。首页保留当日日报；历史内容每月仅一份 Markdown，月内累计去重更新，不再保存逐日日报文件。`data/` 中 JSON 用于累计和去重，不是逐日归档。日报仍允许近 7 天增长 ≥ 20 Star 的新项目，总榜采用严格 Star > 100 门槛。检索范围和阈值见 [`config.yaml`](config.yaml)。

---

# AI 应用研究日报 · 2026-11-10

本期新增：**7 篇论文**（其中 4 篇找到可能的代码）和 **0 个 GitHub 项目**。

## AI 投资与交易论文

| 日期 | 论文 | 作者 | 代码 | 市场/因子 | 来源/热度 |
|---|---|---|---|---|---|
| 2026-11-09 | [Diversification Across Predictors: Heterogeneous Ensemble Learning for Cross-Sectional Return Prediction](https://arxiv.org/abs/2611.12389) | Danning Li | — | 因子 | arXiv |
| 2026-11-07 | [A Bayesian oriented exploration and reinforcement learning in continuous-time mean-variance portfolio optimization](https://arxiv.org/abs/2611.10759) | Kexin Chen, Xiang Yu, Shanshan Zhao | — | 未明确（需查文档） | arXiv |
| 2026-11-07 | [M3FT: Micro-Macro-Micro Reasoning for Multi-Agent Cryptocurrency Perpetual Futures Trading](https://arxiv.org/abs/2611.10586) | Jiashun Wang, Beile Wang, Guangyan Gan 等 | — | 虚拟货币、期货 | arXiv |
| 2025-12-01 | [AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://arxiv.org/abs/2512.10971) | Tianyu Fan, Yuhao Yang, Yangqin Jiang 等 | [HF 社区代码候选](https://github.com/HKUDS/AI-Trader) | A股、虚拟货币、期货 | [HF Trending](https://huggingface.co/papers/2512.10971) · 👍 13 |
| 2025-09-14 | [Trading-R1: Financial Trading with LLM Reasoning via Reinforcement   Learning](https://arxiv.org/abs/2509.11420) | Yijia Xiao, Edward Sun, Tong Chen 等 | [HF 社区代码候选](https://github.com/TauricResearch/Trading-R1) | 未明确（需查文档） | [HF Trending](https://huggingface.co/papers/2509.11420) · 👍 5 |
| 2025-08-02 | [Kronos: A Foundation Model for the Language of Financial Markets](https://arxiv.org/abs/2508.02739) | Yu Shi, Zongliang Fu, Shuo Chen 等 | [HF 社区代码候选](https://github.com/shiyu-coder/Kronos) | 未明确（需查文档） | [HF Trending](https://huggingface.co/papers/2508.02739) · 👍 65 |
| 2024-12-28 | [TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138) | Yijia Xiao, Edward Sun, Di Luo 等 | [HF 社区代码候选](https://github.com/tauricresearch/tradingagents) | 未明确（需查文档） | [HF Trending](https://huggingface.co/papers/2412.20138) · 👍 164 |


## GitHub 金融与交易工具

本期没有发现符合条件的新项目。


> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。

