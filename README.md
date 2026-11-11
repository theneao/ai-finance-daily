# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集 AI 投资研究、金融 Agent、交易框架、金融工具和交易游戏。论文源结合 arXiv 与 [Hugging Face Trending Papers](https://huggingface.co/papers/trending)，仅筛选 AI 投资交易研究，按 arXiv ID 去重；Trending 中重新走热的旧论文也可收录，保留原发表日期与 HF 社区热度。

**[📚 完整热门项目总榜（全部历史项目 · Star 排名 · 分类导航）](HOT_PROJECTS.md)** · **[本月月报](archive/2026-11.md)** · **[历月归档](archive/index.md)**

最近更新 2026-11-12（北京时间）。

热门总榜每天刷新，按 Star 降序排列。**500–999 Star** 须近一年有代码更新且 Star 增长 **≥ 30%**。**1,000 Star 及以上**须近三年有代码更新。分类包括 Agent、交易框架（回测/语言）、工具（看板/数据源/创意）、游戏、论文研究，市场标签区分美股、A股、虚拟货币、期货、因子。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。首页展示当月累计月报，每天合并去重，按月保存一份 Markdown。`data/` 中 JSON 用于累计和去重，不是逐日归档。月报新增项目须 **Star ≥ 200**，且近半年有代码更新或 Star 增长 **≥ 30%**。涨幅按窗口内最早一条有效 Star 快照与当前值比较，缺少历史快照时无法验证增长。项目名称、简介、topics、README 和论文标题、摘要会进行政治敏感主题筛选，检查不可用的仓库暂缓展示。同时排除 `.github`/个人主页仓库、资源导航合集及超过 400 字符的冗长简介仓库，优先展示可使用的项目。检索范围和阈值见 [`config.yaml`](config.yaml)。

---

## 热门项目 · Star ≥ 500

按 Star 降序，按分类直接展示各类前 10 个项目；[查看全部热门项目](HOT_PROJECTS.md)。

### Agent

| 项目 | 简介 | ⭐ | 半年内已观测涨幅 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | TradingAgents: Multi-Agents LLM Financial Trading Framework | 122052 | +0.1%（自 2026-11-11） | Python | Agent | 未明确（需查文档） | Agent |
| [openbq-org/OpenBB](https://github.com/openbq-org/OpenBB) | Open Data Platform for analysts, quants and AI agents. | 75336 | +0.0%（自 2026-11-11） | Python | Agent | 虚拟货币、期货 | Agent |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。  LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | 70025 | +0.5%（自 2026-11-11） | Python | Agent | 未明确（需查文档） | Agent |
| [microsoft/qlib](https://github.com/microsoft/qlib) | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://github.com/microsoft/RD-Agent to automate R&D process. | 50217 | +0.0%（自 2026-11-11） | Python | Agent | 未明确（需查文档） | Agent |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | "Vibe-Trading: Your Personal Trading Agent" | 38048 | +3.4%（自 2026-10-27） | Python | Agent | 未明确（需查文档） | Agent |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 410 Claude Code skills & agent skills & plugins (120+ Agents, custom commands, 410+ skills, customizable references, scripts)for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — engineering, marketing, product, compliance, C-level advisory, research, business operations, commercial & finance, and your daily productivity skills. | 29639 | +0.0%（自 2026-11-11） | Python | Agent | 未明确（需查文档） | Agent |
| [virattt/dexter](https://github.com/virattt/dexter) | An autonomous agent for deep financial research | 27815 | -0.0%（自 2026-11-11） | TypeScript | Agent | 未明确（需查文档） | Agent |
| [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | "AI-Trader: 100% Fully-Automated Agent-Native Trading"   | 23235 | +0.0%（自 2026-11-11） | Python | Agent | 未明确（需查文档） | Agent |
| [stefan-jansen/machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading) | Code for Machine Learning for Trading, 3rd edition — from data sourcing to live execution. | 21786 | +1.0%（自 2026-10-27） | Jupyter Notebook | Agent | 未明确（需查文档） | Agent |
| [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | Open source software that helps you create and deploy high-frequency crypto trading bots | 21168 | — | Python | Agent | 虚拟货币 | Agent |

### 交易框架

| 项目 | 简介 | ⭐ | 半年内已观测涨幅 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [vnpy/vnpy](https://github.com/vnpy/vnpy) | 基于Python的开源量化交易平台开发框架 | 46341 | — | Python | 交易框架 | 未明确（需查文档） | 回测：需查文档 |
| [mementum/backtrader](https://github.com/mementum/backtrader) | Python Backtesting library for trading strategies | 23717 | +0.0%（自 2026-11-11） | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [QuantConnect/Lean](https://github.com/QuantConnect/Lean) | Lean Algorithmic Trading Engine by QuantConnect (Python, C#) | 22488 | +0.0%（自 2026-11-11） | C# | 交易框架 | 未明确（需查文档） | 回测：需查文档 |
| [myhhub/stock](https://github.com/myhhub/stock) | stock股票.获取股票数据,计算股票指标,筹码分布,识别股票形态,综合选股,选股策略,股票验证回测,股票自动交易,支持PC及移动设备。 | 15128 | +0.2%（自 2026-11-11） | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [yutiansut/QUANTAXIS](https://github.com/yutiansut/QUANTAXIS) | QUANTAXIS 支持任务调度 分布式部署的 股票/期货/期权  数据/回测/模拟/交易/可视化/多账户 纯本地量化解决方案 | 11359 | +0.0%（自 2026-11-11） | Python | 交易框架 | 期货 | 回测：明确提及 |
| [StockSharp/StockSharp](https://github.com/StockSharp/StockSharp) | Algorithmic trading and quantitative trading open source platform to develop trading robots (stock markets, forex, crypto, bitcoins, and options). | 11091 | — | C# | 交易框架 | 虚拟货币 | 回测：明确提及 |
| [kernc/backtesting.py](https://github.com/kernc/backtesting.py) | 🔎 📈 🐍 💰  Backtest trading strategies in Python. | 9226 | +0.0%（自 2026-11-11） | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [Jakeschincariol/day-trader-skill](https://github.com/Jakeschincariol/day-trader-skill) | 11 Claude skills for day trading: scan thousands of charts, track breaking news, time every entry and exit, and replay every outcome before you risk a dollar. | 6948 | +1.8%（自 2026-11-11） | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [ricequant/rqalpha](https://github.com/ricequant/rqalpha) | A extendable, replaceable Python algorithmic backtest && trading framework supporting multiple securities | 6871 | +0.5%（自 2026-10-27） | Python | 交易框架 | 期货 | 回测：明确提及 |
| [Mathieu2301/TradingView-API](https://github.com/Mathieu2301/TradingView-API) | 📈 Get real-time stocks from TradingView | 5866 | +1.8%（自 2026-10-27） | TypeScript | 交易框架 | 虚拟货币 | 回测：明确提及 |

### 工具

| 项目 | 简介 | ⭐ | 半年内已观测涨幅 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade) | Free, open source crypto trading bot | 56771 | — | Python | 工具 | 虚拟货币 | 分析/策略工具 |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Kronos: A Foundation Model for the Language of Financial Markets | 47626 | +0.0%（自 2026-11-11） | Python | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [ccxt/ccxt](https://github.com/ccxt/ccxt) | A unified trading API with more than 100 crypto exchanges and prediction markets in JavaScript / TypeScript / Python / C# / PHP / Go / Java / Rust | 44860 | — | Python | 工具 | 虚拟货币 | 数据源 |
| [akfamily/akshare](https://github.com/akfamily/akshare) | AKShare is an elegant and simple financial data interface library for Python, built for human beings! 开源财经数据接口库 | 23302 | +0.0%（自 2026-11-11） | Python | 工具 | A股、期货 | 数据源 |
| [quantopian/zipline](https://github.com/quantopian/zipline) | Zipline, a Pythonic Algorithmic Trading Library | 20230 | +0.0%（自 2026-11-11） | Python | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [bbfamily/abu](https://github.com/bbfamily/abu) | 阿布量化交易系统(股票，期权，期货，比特币，机器学习) 基于python的开源量化交易，量化投资架构 | 19168 | +0.0%（自 2026-11-11） | Python | 工具 | 虚拟货币、期货 | 分析/策略工具 |
| [xcanwin/KeepChatGPT](https://github.com/xcanwin/KeepChatGPT) | 这是一款提高ChatGPT的数据安全能力和效率的插件。并且免费共享大量创新功能，如：自动刷新、保持活跃、数据安全、取消审计、克隆对话、言无不尽、净化页面、展示大屏、拦截跟踪、日新月异、明察秋毫等。让我们的AI体验无比安全、顺畅、丝滑、高效、简洁。 | 14890 | +0.0%（自 2026-11-11） | JavaScript | 工具 | 未明确（需查文档） | 数据源 |
| [wechat-article/wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter) | 一款在线的 微信公众号文章批量下载 工具，支持导出阅读量与评论数据，无需搭建任何环境，可通过 在线网站 使用，支持 docker 私有化部署和 Cloudflare 部署。  支持下载各种文件格式，其中 HTML 格式可100%还原文章排版与样式。 | 13151 | +0.0%（自 2026-11-11） | TypeScript | 工具 | 未明确（需查文档） | 数据源 |
| [daniulive/SmarterStreaming](https://github.com/daniulive/SmarterStreaming) | 业内为数不多致力于极致体验的超强全自研跨平台(windows/linux/android/iOS)流媒体内核，通过模块化自由组合，支持实时RTMP推流、RTSP推流、RTMP播放器、RTSP播放器、录像、多路流媒体转发、音视频导播、动态视频合成、音频混音、直播互动、内置轻量级RTSP服务等，比快更快，业界真正靠谱的超低延迟直播SDK(延迟低至100~200ms)。 | 11172 | +0.0%（自 2026-11-11） | Java | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [chaitin/PandaWiki](https://github.com/chaitin/PandaWiki) | PandaWiki 是一款 AI 大模型驱动的开源知识库搭建系统，帮助你快速构建智能化的 产品文档、技术文档、FAQ、博客系统，借助大模型的力量为你提供 AI 创作、AI 问答、AI 搜索等能力。 | 10496 | +0.0%（自 2026-11-11） | TypeScript | 工具 | 未明确（需查文档） | 分析/策略工具 |

### 游戏

| 项目 | 简介 | ⭐ | 半年内已观测涨幅 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [kingston-csj/jforgame](https://github.com/kingston-csj/jforgame) | jforgame是一个一站式游戏服务器开发框架。包含游戏服务器开发所需要的各种组件，比如socket服务端与客户端，高性能线程模型，自定义二进制消息编解码，自定义orm工具，异步持久化方案，游戏热更新，配置表自动化仓库，游戏通用工具等等，同时提供大量业务案例以供学习。亦可用于其他socket应用，例如及时聊天等。 | 1102 | +0.0%（自 2026-11-11） | Java | 游戏 | 未明确（需查文档） | 游戏 |

### 论文研究

| 项目 | 简介 | ⭐ | 半年内已观测涨幅 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [UFund-Me/Qbot](https://github.com/UFund-Me/Qbot) | [🔥updating ...] AI 自动量化交易机器人(完全本地部署) AI-powered Quantitative Investment Research Platform. 📃 online docs: https://ufund-me.github.io/Qbot   ✨ :news: qbot-mini: https://github.com/Charmve/iQuant | 18798 | -0.0%（自 2026-11-11） | Jupyter Notebook | 论文研究 | 虚拟货币 | 论文研究 |
| [polakowo/vectorbt](https://github.com/polakowo/vectorbt) | The research engine that gives you an unfair advantage. Run thousands of trading ideas before others finish one. | 9817 | +2.8%（自 2026-10-27） | Python | 论文研究 | 虚拟货币 | 论文研究 |
| [Drakkar-Software/OctoBot](https://github.com/Drakkar-Software/OctoBot) | Free open source crypto trading bot to automate AI, Grid, DCA and TradingView strategies on Binance, Hyperliquid and 15+ exchanges, with a simple interface. | 6927 | +0.9%（自 2026-10-27） | Python | 论文研究 | 虚拟货币 | 论文研究 |
| [hugo2046/QuantsPlaybook](https://github.com/hugo2046/QuantsPlaybook) | 量化研究-券商金工研报复现 | 6874 | +0.0%（自 2026-11-11） | Jupyter Notebook | 论文研究 | 未明确（需查文档） | 论文研究 |
| [Superalgos/Superalgos](https://github.com/Superalgos/Superalgos) | Free, open-source crypto trading bot, automated bitcoin / cryptocurrency trading software, algorithmic trading bots. Visually design your crypto trading bot, leveraging an integrated charting system, data-mining, backtesting, paper trading, and multi-server crypto bot deployments. | 5786 | — | JavaScript | 论文研究 | 虚拟货币 | 论文研究 |
| [cybergeekgyan/Quant-Developers-Resources](https://github.com/cybergeekgyan/Quant-Developers-Resources) | Resources to Prepare for Quant Developers/ Quantitative Researcher/ Quantitative Trader/ Quant Analyst/ Software Engineers in Quant Trading Firms, HFTs and Hedge Funds | 4142 | +5.1%（自 2026-09-19） | Python | 论文研究 | 未明确（需查文档） | 论文研究 |
| [mpquant/Ashare](https://github.com/mpquant/Ashare) | 股票行情实时数据接口-A股,完全免费的沪深证券股票数据-中国股市,python最简封装的API接口,包含日线,历史K线,分时线,分钟线,全部实时采集，系统包括新浪腾讯双数据核心采集获取，自动故障切换，STOCK数据格式成DataFrame格式,可用来查询研究量化分析，股票程序自动化交易系统.为量化研究者在数据获取方面极大地减轻工作量，更加专注于策略和模型的研究与实现。 | 3939 | +0.0%（自 2026-11-11） | Python | 论文研究 | A股 | 论文研究 |
| [AI4Finance-Foundation/FinRL-Trading](https://github.com/AI4Finance-Foundation/FinRL-Trading) | FinRL-X: An AI-Native Modular Infrastructure for Quantitative Trading | 3932 | +6.0%（自 2026-09-18） | Python | 论文研究 | 未明确（需查文档） | 论文研究 |
| [hello245m/free-stockdb](https://github.com/hello245m/free-stockdb) | 面向 A 股日K、分钟K与ETF分钟数据的本地量化引擎，集成增量同步、本地缓存、复权、批量查询、回测与指标计算。 | 3160 | +0.0%（自 2026-11-11） | HTML | 论文研究 | A股 | 论文研究 |
| [weslynn/AlphaTree-graphic-deep-neural-network](https://github.com/weslynn/AlphaTree-graphic-deep-neural-network) | AI Roadmap:机器学习(Machine Learning)、深度学习(Deep Learning)、对抗神经网络(GAN），图神经网络（GNN），NLP，大数据相关的发展路书(roadmap), 并附海量源码（python，pytorch）带大家消化基本知识点，突破面试，完成从新手到合格工程师的跨越，其中深度学习相关论文附有tensorflow caffe官方源码，应用部分含推荐算法和知识图谱 | 3027 | +0.0%（自 2026-11-11） |  | 论文研究 | 未明确（需查文档） | 论文研究 |


---

## AI 金融月报 · 2026-11

本月累计收录 **17 篇论文**（其中 6 篇找到可能的代码）和 **89 个 GitHub 项目**。

### AI 投资与交易论文

| 日期 | 论文 | 作者 | 代码 | 市场/因子 | 来源/热度 |
|---|---|---|---|---|---|
| 2026-11-10 | [Online-Adaptive Fuzzy Cognitive Maps for Neuro-symbolic Financial Forecasting](https://arxiv.org/abs/2611.13388) | Brandon Rodriguez, Abel Deulofeu, Olaoluwa Adigun | — | 美股、因子 | arXiv |
| 2026-11-09 | [Diversification Across Predictors: Heterogeneous Ensemble Learning for Cross-Sectional Return Prediction](https://arxiv.org/abs/2611.12389) | Danning Li | — | 因子 | arXiv |
| 2026-11-07 | [M3FT: Micro-Macro-Micro Reasoning for Multi-Agent Cryptocurrency Perpetual Futures Trading](https://arxiv.org/abs/2611.10586) | Jiashun Wang, Beile Wang, Guangyan Gan 等 | — | 虚拟货币、期货 | arXiv |
| 2026-11-07 | [A Bayesian oriented exploration and reinforcement learning in continuous-time mean-variance portfolio optimization](https://arxiv.org/abs/2611.10759) | Kexin Chen, Xiang Yu, Shanshan Zhao | — | 未明确（需查文档） | arXiv |
| 2026-11-06 | [Towards Robust Reinforcement Learning Market Making: Lessons from Loss Function Experimentation](https://arxiv.org/abs/2611.09012) | Siddharth Nand, Bora Guney | — | 未明确（需查文档） | arXiv |
| 2026-11-06 | [TailDART: Compute-Efficient Foundation Models for Financial Time-Series Forecasting](https://arxiv.org/abs/2611.09176) | Chiang Qin Zhi, Ranjan Satapathy, Erik Cambria 等 | — | 未明确（需查文档） | arXiv |
| 2026-11-04 | [Constrained defined-contribution pension management: A reparameterized neural network approach](https://arxiv.org/abs/2611.06495) | Yueman Feng, Wenyuan Li | — | 因子 | arXiv |
| 2026-11-03 | [LENS: Reliability-Aware Stock Prediction via LLM-Extracted Priors and News-Driven Semantic Graphs](https://arxiv.org/abs/2611.04217) | Hao Zhou, Tiejun Ma, Luis Felipe Costa Sperb | — | 美股 | arXiv |
| 2026-11-03 | [Mitigating Return Drag and Regime Whipsaws in Sector Rotation: An Asymmetric Downside-Aware Nested Clustered Optimization Framework](https://arxiv.org/abs/2611.05310) |  Supriadi | [arXiv 页面](https://github.com/obo-cloud/sp500-asymmetric-nco) | 美股 | arXiv |
| 2026-11-03 | [Generative Modeling for Cascading Extremes via Autoregressive Transformers](https://arxiv.org/abs/2611.05728) | Miguel de Carvalho, Myung Won Lee, Jordan Richards 等 | — | 期货 | arXiv |
| 2026-11-01 | [LLM-Enhanced Multimodal House Price Prediction using Structured, Textual, and Visual Features](https://arxiv.org/abs/2611.01615) | Khandokar Md. Rahat Hossain, Souvik Das, Tahsina Hashem 等 | [arXiv 页面](https://github.com/rh2975/LLM-VLM-HousePrice) | 未明确（需查文档） | arXiv |
| 2026-10-31 | [AStockArena: Beyond Returns, Can We Entrust Real Capital to the Decisions of Financial Agents?](https://arxiv.org/abs/2611.00515) | Zeyu Liu, Sing Kwong Lai, Xuanzhi Feng 等 | — | A股 | arXiv |
| 2026-10-31 | [Entropy-Regularized Reinforcement Learning for the Regime-Switching Consumption-Investment Problem](https://arxiv.org/abs/2611.01046) | Congde Hu, Danping Li, Xun Li 等 | — | 未明确（需查文档） | arXiv |
| 2025-12-01 | [AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://arxiv.org/abs/2512.10971) | Tianyu Fan, Yuhao Yang, Yangqin Jiang 等 | [HF 社区代码候选](https://github.com/HKUDS/AI-Trader) | A股、虚拟货币、期货 | [HF Trending](https://huggingface.co/papers/2512.10971) · 👍 13 |
| 2025-09-14 | [Trading-R1: Financial Trading with LLM Reasoning via Reinforcement   Learning](https://arxiv.org/abs/2509.11420) | Yijia Xiao, Edward Sun, Tong Chen 等 | [HF 社区代码候选](https://github.com/TauricResearch/Trading-R1) | 未明确（需查文档） | [HF Trending](https://huggingface.co/papers/2509.11420) · 👍 5 |
| 2025-08-02 | [Kronos: A Foundation Model for the Language of Financial Markets](https://arxiv.org/abs/2508.02739) | Yu Shi, Zongliang Fu, Shuo Chen 等 | [HF 社区代码候选](https://github.com/shiyu-coder/Kronos) | 未明确（需查文档） | [HF Trending](https://huggingface.co/papers/2508.02739) · 👍 65 |
| 2024-12-28 | [TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138) | Yijia Xiao, Edward Sun, Di Luo 等 | [HF 社区代码候选](https://github.com/tauricresearch/tradingagents) | 未明确（需查文档） | [HF Trending](https://huggingface.co/papers/2412.20138) · 👍 164 |


### GitHub 金融与交易工具

| 项目 | 简介 | ⭐ | 半年内已观测涨幅 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade) | Free, open source crypto trading bot | 56733 | — | Python | 工具 | 虚拟货币 | 分析/策略工具 |
| [ccxt/ccxt](https://github.com/ccxt/ccxt) | A unified trading API with more than 100 crypto exchanges and prediction markets in JavaScript / TypeScript / Python / C# / PHP / Go / Java / Rust | 44847 | — | Python | 工具 | 虚拟货币 | 数据源 |
| [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | Open source software that helps you create and deploy high-frequency crypto trading bots | 21144 | — | Python | Agent | 虚拟货币 | Agent |
| [StockSharp/StockSharp](https://github.com/StockSharp/StockSharp) | Algorithmic trading and quantitative trading open source platform to develop trading robots (stock markets, forex, crypto, bitcoins, and options). | 11085 | — | C# | 交易框架 | 虚拟货币 | 回测：明确提及 |
| [Superalgos/Superalgos](https://github.com/Superalgos/Superalgos) | Free, open-source crypto trading bot, automated bitcoin / cryptocurrency trading software, algorithmic trading bots. Visually design your crypto trading bot, leveraging an integrated charting system, data-mining, backtesting, paper trading, and multi-server crypto bot deployments. | 5781 | — | JavaScript | 论文研究 | 虚拟货币 | 论文研究 |
| [FinMind/FinMind](https://github.com/FinMind/FinMind) | Open Data, more than 50 financial data. 提供超過 50 個金融資料(台股為主)，每天更新 https://finmind.github.io/ | 2881 | — | HTML | 工具 | 未明确（需查文档） | 数据源 |
| [TA-Lib/ta-lib](https://github.com/TA-Lib/ta-lib) | Technical analysis library: indicators and candlestick patterns, batch and streaming, native in C, Rust, Java, C#... and more | 1732 | — | C | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [visualHFT/VisualHFT](https://github.com/visualHFT/VisualHFT) | VisualHFT Terminal: open-source observability and decision terminal for electronic trading desks. Live Level 2 order books, microstructure analytics, and quantitative execution monitoring. | 1216 | — | C# | 工具 | 未明确（需查文档） | 看板、数据源 |
| [HammerGPT/Hyper-Alpha-Arena](https://github.com/HammerGPT/Hyper-Alpha-Arena) | AI Trading platform for Hyperliquid & Binance Futures AI 自动交易平台，支持 Hyperliquid 和币安合约 | 1198 | — | Python | 交易框架 | 虚拟货币、期货 | 回测：需查文档 |
| [Finnhub-Stock-API/finnhub-python](https://github.com/Finnhub-Stock-API/finnhub-python) | Finnhub Python API Client. Finnhub API provides institutional-grade financial data to investors, fintech startups and investment firms. We support real-time stock price, global fundamentals, global ETFs holdings and alternative data. https://finnhub.io/docs/api | 1097 | — | Python | 工具 | 未明确（需查文档） | 数据源 |
| [51bitquant/binance_grid_trader](https://github.com/51bitquant/binance_grid_trader) | Binance_grid_trader is a grid strategy bot trading with Binance Spot and Binance Futures Exchange. you can use it to trade any pair in Binance Exchange. Binance_grid_trader是一个币安网格策略软件, 目前支持币安现货，USDT合约和币币合约。 | 991 | — | Python | 工具 | 虚拟货币、期货 | 数据源 |
| [51bitquant/howtrader](https://github.com/51bitquant/howtrader) | Howtrader: A crypto quant framework for developing, backtesting, and executing your own trading strategies. Seamlessly integrates with TradingView and other third-party signals. Simply send a post request to automate trading and order placement. Supports Binance and Okex exchanges. | 972 | — | Python | 交易框架 | 虚拟货币 | 回测：明确提及 |
| [ailabx/agilab](https://github.com/ailabx/agilab) | AgiLab(Agi实验室)，专注于将前沿AI技术落地：量化投资，多智能体落地，科研自动化。 | 971 | — | Python | Agent | 未明确（需查文档） | Agent |
| [dromara/dante-cloud](https://github.com/dromara/dante-cloud) | 🐉 Dante Cloud 是支持阻塞式与响应式服务并行的微服务云原生基座和面向AI Agent开发的智能基座，基于领域驱动模型（DDD）设计，以高质量代码与低安全漏洞为核心，高度模块化、组件化，覆盖IoT设备认证、国家等保三级、接口国密数字信封加密等多层次安全体系，并提供多租户解决方案。独创“一套代码实现微服务和单体架构灵活切换”，赋能企业级智能应用构建。🔝🔝点个star 持续关注更新！ | 969 | — | Java | Agent | 未明确（需查文档） | Agent |
| [Leo4815162342/dukascopy-node](https://github.com/Leo4815162342/dukascopy-node) | ✨ Download historical and real-time price tick data for Crypto, Stocks, ETFs, CFDs, Forex via CLI and Node.js ✨ | 963 | — | TypeScript | 交易框架 | 虚拟货币 | 回测：明确提及 |
| [sensorsdata/sa-sdk-javascript](https://github.com/sensorsdata/sa-sdk-javascript) | 神策数据官方 Web JavaScript 埋点 SDK，是一款轻量级用于 Web 端和 H5 端的数据采集埋点 SDK。使用原生 JavaScript 技术实现代码埋点、全埋点、可视化全埋点、网页热力图和触达图等功能。 | 958 | — | JavaScript | 工具 | 未明确（需查文档） | 看板、数据源 |
| [jianweiweng05/qsx-strategy-score](https://github.com/jianweiweng05/qsx-strategy-score) | Free strategy scorecard for trading backtests. Detect overfitting, weak edge, drawdown risk, and random-timing luck from returns, equity curves, or trade logs. | 928 | — | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [rush86999/atom](https://github.com/rush86999/atom) | Atom Agent, Open-Source Governed AI Agent Platform for Self-Hosted Automation | 915 | — | Python | Agent | 未明确（需查文档） | Agent |
| [sdcoffey/techan](https://github.com/sdcoffey/techan) | Technical Analysis Library for Golang | 905 | — | Go | 工具 | 虚拟货币 | 分析/策略工具 |
| [KylinMountain/TradingAgents-AShare](https://github.com/KylinMountain/TradingAgents-AShare) | A 股多智能体智能投研系统 — 基于 TradingAgents 架构，15 名 AI Agent 模拟机构协作与实时辩论对抗，全流程可视化，支持 OpenClaw / Claude Code 集成，Docker 一键部署。 | 899 | — | Python | Agent | A股 | Agent |
| [hananedupouy/LLMs-in-Finance](https://github.com/hananedupouy/LLMs-in-Finance) | LLMs in Finance - Generative AI - AI Agents  | 896 | — | Jupyter Notebook | Agent | 未明确（需查文档） | Agent |
| [jwangkun/claude-for-financial-services-cn](https://github.com/jwangkun/claude-for-financial-services-cn) |  63 个 Claude Skills，为 A 股金融从业者而生  基于 Anthropic 官方 claude-for-financial-services 深度适配国内市场，现已开源。 | 889 | — | Python | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [xingwudao/xquant-beginner](https://github.com/xingwudao/xquant-beginner) | 《XQuant：人人都是量化交易员》量化交易入门与自学开源书：用 AI 和 Python 从零跑通策略回测、风险评估、交易执行和因子研究。 | 888 | — | TypeScript | 论文研究 | 因子 | 论文研究 |
| [NewLifeX/NewLife.Redis](https://github.com/NewLifeX/NewLife.Redis) | High performance redis client, support NETCore/. NET4. 0/. NET4. 5. It is specially optimized for big data and message queue. The average daily consumption of online single application is 10 billion. 高性能Redis客户端，支持.NETCore/.NET4.0/.NET4.5，为大数据与消息队列而特别优化，线上单应用日均100亿调用量 | 879 | — | C# | 工具 | 未明确（需查文档） | 数据源 |
| [TencentBlueKing/bk-job](https://github.com/TencentBlueKing/bk-job) | 蓝鲸作业平台（Job）是一套运维基础操作管理系统，具备海量任务并发处理能力。除了支持脚本执行、文件分发、定时任务等一系列基础运维场景以外，还支持通过流程调度能力将零碎的单个任务组装成一个自动化作业流程；而每个作业都可做为一个原子节点，提供给上层或周边系统/平台使用，实现调度自动化。 | 875 | — | Java | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [zgsfsec/Full-Chain-Sentinel-System](https://github.com/zgsfsec/Full-Chain-Sentinel-System) | 全链哨兵，是集Web 渗透、安卓 App 安全测试、iOS APP安全测试、攻防批量打点、自动化应急响应、开源漏洞监测为一体的网络安全 Agent，用于安全服务交付自动化辅助，禁止用于非法用途。 | 869 | — | TypeScript | Agent | 未明确（需查文档） | Agent |
| [Adamant-im/adamant-tradebot](https://github.com/Adamant-im/adamant-tradebot) | Free self-hosted liquidity bot for token issuers who want to improve CEX market quality without sending tokens, funds, or API keys to a third-party market maker. | 863 | — | JavaScript | 工具 | 虚拟货币 | 数据源 |
| [gazbert/bxbot](https://github.com/gazbert/bxbot) | A simple Bitcoin trading bot written in Java. | 863 | — | Java | 工具 | 虚拟货币 | 数据源 |
| [KunMoe/kun-touchgal-next](https://github.com/KunMoe/kun-touchgal-next) | TouchGal 是一个一站式 Galgame 文化社区。提供Galgame 论坛、Galgame 下载等服务。承诺永久免费, 高质量。为Galgame 爱好者提供一片净土！ | 849 | — | TypeScript | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [huanyuejue/Fluent-Steam-Lua](https://github.com/huanyuejue/Fluent-Steam-Lua) | 基于 WPF + Fluent Design 开发的现代化轻量级 Steam Lua 入库管理工具，目前仅适配OpenSteamTool | 844 | — | C# | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [liudf0716/xfrpc](https://github.com/liudf0716/xfrpc) | xfrpc 是一个轻量级的 FRP 客户端，完美兼容 frps，采用 C 语言实现，专为 OpenWRT 和物联网等资源受限系统优化设计。它针对 ROM 和 RAM 空间有限的设备，提供高效的内网穿透解决方案。xfrpc 集成了xDPI（深度包检测）功能，增强了安全性，有效防止内网穿透中因恶意嗅探导致的安全威胁，确保数据传输和网络访问的可靠保护。购买下面的链接中的服务支持我的开源 | 844 | — | C | 工具 | 未明确（需查文档） | 数据源 |
| [AsyncAlgoTrading/aat](https://github.com/AsyncAlgoTrading/aat) | Asynchronous, event-driven algorithmic trading in Python and C++ | 843 | — | C++ | 交易框架 | 虚拟货币 | 回测：明确提及 |
| [Heerozh/spectre](https://github.com/Heerozh/spectre) | GPU-accelerated Factors analysis library and Backtester | 831 | — | Python | 交易框架 | 因子 | 回测：明确提及 |
| [Yohann0617/oci-helper](https://github.com/Yohann0617/oci-helper) | 基于 Oracle OCI SDK 🐢 开发的 web 端可视化甲骨文云助手（Y探长），目前实现的功能有：批量添加多个租户配置、更改实例配置、引导卷配置、一键开启免费AMD实例下行500Mbps、一键更新、一键救援/缩小硬盘、附加ipv6、安全列表、实时流量查询（分钟级别）、根据多个 CIDR 网段更换实例公共IP、多租户同时批量抢机、Cloud Shell 控制台、断点续抢、备份恢复、日志实时查看、消息通知、MFA登录验证、更新 Cloudflare DNS 记录、TG 机器人操作等功能。 | 823 | — | Java | 工具 | 未明确（需查文档） | 看板 |
| [garagesteve1155/PowerTrader_AI](https://github.com/garagesteve1155/PowerTrader_AI) | Fully automated crypto trading powered by a custom price prediction AI and a structured/tiered DCA system. Website at PowerTrader.net | 820 | — | Python | 工具 | 虚拟货币 | 分析/策略工具 |
| [gadicc/yahoo-finance2](https://github.com/gadicc/yahoo-finance2) | Unofficial API for Yahoo Finance with CLI, MCP and Agent Skill | 815 | — | HTML | Agent | 未明确（需查文档） | Agent |
| [dragon1086/prism-insight](https://github.com/dragon1086/prism-insight) | AI-based stock analysis and trading system | 807 | — | Python | Agent | 未明确（需查文档） | Agent |
| [edmcouncil/fibo](https://github.com/edmcouncil/fibo) | The Financial Industry Business Ontology (FIBO) defines the sets of things that are of interest in financial business applications and the ways that those things can relate to one another. In this way, FIBO can give meaning to any data (e.g., spreadsheets, relational databases, XML documents) that describe the business of finance. | 799 | — | Shell | 工具 | 未明确（需查文档） | 数据源 |
| [twelvedata/twelvedata-python](https://github.com/twelvedata/twelvedata-python) | Twelve Data Python Client - Financial data API & WebSocket | 793 | — | Python | 工具 | 虚拟货币 | 数据源 |
| [AUTO-MAS-Project/AUTO-MAS](https://github.com/AUTO-MAS-Project/AUTO-MAS) | 多脚本多配置统一管理与自动化工具 \| 轻松管理大量脚本并存储多个用户配置、设计自动化任务流、监看脚本日志，大幅提高自动化代理效率与稳定性！ | 788 | — | Python | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [taniman/profit-trailer](https://github.com/taniman/profit-trailer) | The most advanced crypto trading bot | 784 | — | Shell | 工具 | 虚拟货币 | 分析/策略工具 |
| [YoungCan-Wang/WyckoffTradingAgent](https://github.com/YoungCan-Wang/WyckoffTradingAgent) | Open-source Wyckoff trading agent and AI stock screener for volume-price analysis, A-share screening, CLI workflows, and MCP tools.灵感来自秋生trader @Hoyooyoo | 773 | — | Python | Agent | A股 | Agent |
| [liangdabiao/make-prompt-seedance2](https://github.com/liangdabiao/make-prompt-seedance2) | 一句话：试错成本越来越高，提示词的重要性从来没有像今天这样大。seedance2结构化提示语和通用SKILL，整合了 Seedance 2.0（字节跳动 AI 视频生成模型）的结构化提示词使用方法，帮助用户快速上手并创作出高质量的视频内容。包含 16+ 个模板和 8+ 个示例 \| 带货广告\| TVC广告\| 真人实拍视频效果 | 759 | — |  | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | 我希望全世界都能使用这个系统，实现AI的真正0门槛，人人都能体验到AI带来的好处，而并不只是掌握在少数人手里。支持上千种垂直场景，支持AI模型定制化和AI算法定制化开发 深度融合，赋能万物智视：EasyAIoT 构筑了物联网设备（尤其是海量摄像头）的高效接入与管控网络。我们深度融合流媒体实时传输技术与前沿人工智能（AI），打造一体化服务核心。这套方案不仅打通了异构设备的互联互通，更将高清视频流与强大的AI解析引擎深度集成，赋予监控系统“智能之眼”——精准实现人脸识别、异常行为分析、风险人员布控周界入侵检测。 | 758 | — | Python | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [quant-king299/EasyXT](https://github.com/quant-king299/EasyXT) | EasyXT是基于miniqmt中xtquant的二次开发封装库，旨在简化xtquant的使用，提供更友好的API接口。通过统一的接口设计、智能参数处理和完善的错误处理，让量化交易开发变得更加简单高效。 | 756 | — | Python | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [binance/binance-connector-js](https://github.com/binance/binance-connector-js) | A simple connector to Binance Public API | 755 | — | TypeScript | 工具 | 虚拟货币 | 数据源 |
| [ling-0729/KHunter](https://github.com/ling-0729/KHunter) | KHunter 是一套开箱即用的A股量化交易系统，集数据管理、策略选股、择时交易、风险控制、回测验证于一体，为个人投资者提供从数据到交易的全流程量化解决方案。 | 738 | — | Python | 交易框架 | A股 | 回测：明确提及 |
| [yangfeng20/ai-job](https://github.com/yangfeng20/ai-job) | 找工作，用AI工作猎手！让AI帮您找工作！【DeepSeek+ChatGpt】赋能，ai助理作为您的求职者分身7*24小时在线找工作，并结合您的简历信息定制化回复。批量投递，自动发送简历，交换联系方式。hr拒绝挽留。高意向邮件通知，让您不错过每一份工作机会。BOSS直聘 | 727 | — | Java | Agent | 未明确（需查文档） | Agent |
| [alleyway/add-tradingview-alerts-tool](https://github.com/alleyway/add-tradingview-alerts-tool) | Automated entry of TradingView alerts for bot trading tools such as 3Commas, Alertatron, CryptoHopper, etc. | 723 | — | TypeScript | 工具 | 虚拟货币 | 分析/策略工具 |
| [electkismet/eltdx](https://github.com/electkismet/eltdx) | 通达信A股行情协议 Python 库，MCP，支持快照、分时、逐笔、K 线、集合竞价、特殊指标等接口。适合作为量化数据源，支持其他语言通过HTTP或WebSocket调用 | 717 | — | Python | 工具 | A股 | 数据源 |
| [rosemarycox5334-debug/AlphaMaster](https://github.com/rosemarycox5334-debug/AlphaMaster) | MT5 factor mining, backtest, and web training UI | 716 | — | Python | 交易框架 | 因子 | 回测：明确提及 |
| [GMGNAI/gmgn-skills](https://github.com/GMGNAI/gmgn-skills) | GMGN OpenAPI skills for AI Agent — query tokens, wallets, and market data, and execute on-chain trades across Solana, BSC, and Base. | 711 | — | Python | Agent | 虚拟货币 | Agent |
| [TheFourGreatErrors/alpha-rptr](https://github.com/TheFourGreatErrors/alpha-rptr) | A trading bot for automated algorithmic trading on Binance Futures, Bybit, BitMEX and FTX written in python. | 711 | — | Python | 工具 | 虚拟货币、期货 | 分析/策略工具 |
| [alpacahq/alpaca-backtrader-api](https://github.com/alpacahq/alpaca-backtrader-api) | Alpaca Trading API integrated with backtrader  | 705 | — | Python | 交易框架 | 美股 | 回测：明确提及 |
| [sensorsdata/sa-sdk-ios](https://github.com/sensorsdata/sa-sdk-ios) | 神策数据官方 iOS 埋点 SDK，是一款轻量级用于 iOS 端的数据采集埋点 SDK。神策分析 iOS SDK 不仅有代码埋点功能，还通过使用运行时机制（Runtime）中的相关技术实现 iOS 端的全埋点（无埋点、无码埋点、无痕埋点、自动埋点）、点击图、可视化全埋点。 | 703 | +0.0%（自 2026-11-11） | Objective-C | 工具 | 未明确（需查文档） | 看板、数据源 |
| [casual-silva/NewsCrawl](https://github.com/casual-silva/NewsCrawl) | 狠心开源企业级舆情新闻爬虫项目：支持任意数量爬虫一键运行、爬虫定时任务、爬虫批量删除；爬虫一键部署；爬虫监控可视化;  配置集群爬虫分配策略；👉 现成的docker一键部署文档已为大家踩坑  an enterprise-grade public opinion news crawler project: supports one-click operation of any number of crawlers, scheduled crawler tasks, batch deletion of crawlers; one-click deployment of crawlers  | 690 | +0.0%（自 2026-11-11） | Python | 工具 | 未明确（需查文档） | 看板、数据源 |
| [banbox/banbot](https://github.com/banbox/banbot) | a high-performance, easy-to-use, multi-symbol, multi-strategy, multi-period, multi-account event-driven trading bot | 688 | +0.0%（自 2026-11-11） | Go | 工具 | 虚拟货币 | 分析/策略工具 |
| [LucivHuang/heimdallr-sdk](https://github.com/LucivHuang/heimdallr-sdk) | A lightweight front-end monitoring sdk/一款简单易用、轻量化、插件化的前端监控sdk | 686 | +0.0%（自 2026-11-11） | TypeScript | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [zjn-zjn/ice](https://github.com/zjn-zjn/ice) | Rule engine/process engine, committed to solving flexible and complex hard-coded problems, for complex/flexibly changing business, provide a new abstract orchestration solution that is lightweight, high-performance and provides visual operation pages. Java规则引擎-ice，针对复杂/灵活变动业务，提供一个新的抽象编排解决方案，轻量级，高性能并提供可视化操作页面 | 679 | +0.0%（自 2026-11-11） | Go | 工具 | 未明确（需查文档） | 看板 |
| [VarunS2002/Python-NSE-Option-Chain-Analyzer](https://github.com/VarunS2002/Python-NSE-Option-Chain-Analyzer) | The NSE has a website which displays the option chain in near real-time. This program retrieves this data from the NSE site and then generates useful analysis of the Option Chain for the specified Index or Stock. It also continuously refreshes the Option Chain and visually displays the trend in various indicators useful for Technical Analysis. | 673 | +0.0%（自 2026-11-11） | Python | 工具 | 期货 | 数据源 |
| [Quantweb3-com/NexusTrader](https://github.com/Quantweb3-com/NexusTrader) | NexusTrader is a professional-grade open-source quantitative trading platform designed by Scott Zhang | 671 | +0.0%（自 2026-11-11） | Python | 交易框架 | 虚拟货币 | 回测：需查文档 |
| [CuriousLearnerDev/TrafficEye](https://github.com/CuriousLearnerDev/TrafficEye) |  This tool is designed to help penetration testers and network administrators identify potential security threats, especially those targeting web applications such as SQL injection, XSS, and WebShells. Its modular desig 该工具适用于 HW 蓝队对网络流量的深入分析，帮助安全研究人员、渗透测试人员及网络管理员等专业人士识别潜在的安全威胁，尤其是针对 Web 应用的攻击（如 SQL 注入、XSS、WebShell 等）。其模块化设计使用户能够根据实际需求自由选择并定制各类功能模块 | 661 | +0.0%（自 2026-11-11） |  | 论文研究 | 未明确（需查文档） | 论文研究 |
| [bi-box/Median](https://github.com/bi-box/Median) | 一个功能密度极高的，安装包仅200kb的极致轻量化浏览器 | 655 | +0.3%（自 2026-11-11） | Java | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [SecNN/AiScan-N](https://github.com/SecNN/AiScan-N) | AiScan-N 来了！这是一款基于人工智能驱动的Ai自动化网络安全（运维）工具，专注于网络安全评估、漏洞扫描、运维、应急响应、渗透测试自动化，Ai大模型工具集【CLI Agent】 ，Ai驱动的安全检测技术，提升安全测试（运维）效率，专为企业和个人用户打造，尤其适合初学者（小白）快速上手使用，让你轻松迈入智能安全攻防时代！适用场景 ：如（红队演练、CTF比赛、Web应用渗透测试、内网横向移动、密码破解与暴力攻击、流量分析与威胁检测、APT攻击模拟、漏洞赏金挑战等场景）🎥演示视频（文章中）：https://mp.weixin.qq.com/s/7lsUdbrxkDy4P5pZhEWv7Q | 652 | +0.0%（自 2026-11-11） |  | Agent | 未明确（需查文档） | Agent |
| [TauricResearch/Trading-R1](https://github.com/TauricResearch/Trading-R1) | Trading-R1: Agentic Finance Research | 648 | +1.4%（自 2026-11-11） | Python | Agent | 未明确（需查文档） | Agent |
| [QuantJourneyOrg/quantjourney-bt](https://github.com/QuantJourneyOrg/quantjourney-bt) | QuantJourney Backtester | 645 | +0.0%（自 2026-11-11） | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [henrylin99/quantitative_analysis](https://github.com/henrylin99/quantitative_analysis) | 量化分析 | 638 | +0.0%（自 2026-11-11） | Python | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [TimeCopilot/timecopilot](https://github.com/TimeCopilot/timecopilot) | TimeCopilot: the Agentic Forecasting Framework. Built on LLMs and Time Series Foundation Models, it lets you forecast, cross-validate, and detect anomalies using multiple foundation models through a single API. From finance and energy to web analytics, TimeCopilot turns natural-language queries into production-ready forecasts. | 638 | — | Python | Agent | 未明确（需查文档） | Agent |
| [billpwchan/futu_algo](https://github.com/billpwchan/futu_algo) | Futu Algorithmic Trading Solution (Python) 基於富途OpenAPI所開發量化交易程序 | 624 | +0.0%（自 2026-11-11） | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [sarim2000/pennywiseai-tracker](https://github.com/sarim2000/pennywiseai-tracker) | PennyWise automatically reads transaction SMS messages and transforms them    into organized financial data with on-device AI assistance. No manual   entry, no cloud processing, complete privacy. | 623 | +0.0%（自 2026-11-11） | Kotlin | 工具 | 未明确（需查文档） | 数据源 |
| [mingli30119/stock-analysis](https://github.com/mingli30119/stock-analysis) | 一句话搞定个股分析 | 620 | +0.0%（自 2026-11-11） | Python | 工具 | A股 | 数据源 |
| [nooperpudd/ctpwrapper](https://github.com/nooperpudd/ctpwrapper) | 上海期货交易所CTP接口 Shanghai Future CTP Interface  CTP Python API Wrapper | 620 | +0.0%（自 2026-11-11） | Python | 工具 | 期货 | 数据源 |
| [agentpit-io/hunter-community](https://github.com/agentpit-io/hunter-community) | HunterCode · Community Edition · 腾讯 WorkBuddy 金融版的开源本地替代方案 · open-source, local alternative to Tencent WorkBuddy Finance Edition · 多智能体投研终端 A股/港股/美股 · 推理在你机器上跑 · 仓位不出你硬盘 · BYOK · Apache 2.0 · docker compose 自托管 | 609 | +0.0%（自 2026-11-11） | Python | Agent | A股 | Agent |
| [physercoe/starquant](https://github.com/physercoe/starquant) | a light-weighted, integrated trading/backtesting system/platform（综合量化交易回测系统/平台） | 609 | +0.0%（自 2026-11-11） | C++ | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [xxd763795151/kafka-console-ui](https://github.com/xxd763795151/kafka-console-ui) | 一款快捷易用的轻量级kafka可视化管理平台 | 606 | +0.0%（自 2026-11-11） | Vue | 工具 | 未明确（需查文档） | 看板 |
| [rnikitin/QuantNavigator](https://github.com/rnikitin/QuantNavigator) | An extensible harness for quantitative research. Product vision and roadmap. | 239 | — |  | 论文研究 | 虚拟货币 | 论文研究 |
| [WyrmSpongeHaul/quant-trading-bot](https://github.com/WyrmSpongeHaul/quant-trading-bot) | Quant Trading Bot 2026 - Full working installer with advanced trading algorithms, ready to run on your desktop. | 200 | — |  | 工具 | 虚拟货币、期货 | 分析/策略工具 |
| [ralphtradesz/trading-hub](https://github.com/ralphtradesz/trading-hub) | Plataforma de trading gratis y de código abierto para Mac (con guía para portarla a Windows con Claude): footprint, DOM, backtesting anti-sobreoptimización y estrategias con IA. 100 % local. | 138 | — | C# | 交易框架 | 虚拟货币、期货 | 回测：明确提及 |
| [duhu2000/dsh-mcp-connector](https://github.com/duhu2000/dsh-mcp-connector) | MCP Connector for DeepSeek Harness: a data marketplace connecting enterprise, financial, legal, patent and research data. Manage authorization, search tools and troubleshoot MCP connections. Supports OAuth, API keys and HTTP/stdio. | 104 | — | JavaScript | 论文研究 | 未明确（需查文档） | 论文研究 |
| [git-wallet/gitwallet](https://github.com/git-wallet/gitwallet) | GitWallet — non-custodial multi-chain crypto wallet for Android. 14 blockchains, AI assistant, trading bot. Keys stay on your phone. | 59 | — | JavaScript | 工具 | 虚拟货币 | 分析/策略工具 |
| [Stratumgreawning7/MemeCoin-Sniper-Bot](https://github.com/Stratumgreawning7/MemeCoin-Sniper-Bot) | Crypto Meme Coin Sniper Bot for Automated Trading, New Token Sniping, Meme Token Launch Detection, Smart Filtering, Fast Execution, Multi-Chain Crypto Trading & Windows Trading Software | 58 | — |  | 工具 | 虚拟货币 | 分析/策略工具 |
| [Beingfluresurrect/Solana-token-sniper](https://github.com/Beingfluresurrect/Solana-token-sniper) | Solana token sniper for Raydium V4 and Pump.fun. Bypass mempool with Jito MEV bundles, auto-skip honeypots and rugpulls, and secure profits with trailing stops. High-winrate crypto trading bot. | 51 | — | Rust | Agent | 虚拟货币 | Agent |
| [SapphireFarCzar/A.W.-rpocket-team-Stratgies-Indicator](https://github.com/SapphireFarCzar/A.W.-rpocket-team-Stratgies-Indicator) | A.W. Strategy: a rules-based intraday futures strategy for TradingView (market structure, order flow, GEX levels), with an automated options-data pipeline and a paper-trading research bot. | 42 | — | HTML | 论文研究 | 期货 | 论文研究 |
| [ZevFlashthorn/adaq-rpocket-team](https://github.com/ZevFlashthorn/adaq-rpocket-team) | AdaQ (Ada Quant) is an AI-powered quantitative trading platform for equities and digital crypto assets. | 42 | — | HTML | 交易框架 | 虚拟货币 | 回测：需查文档 |
| [andyboss1995/ritmex-bot](https://github.com/andyboss1995/ritmex-bot) | Bun/TypeScript multi-exchange perpetuals trading bot + HK momentum strategy | 39 | — | TypeScript | 工具 | 虚拟货币、期货 | 分析/策略工具 |
| [WolfZorace44832/Orderflow-Claude-skill-resocket](https://github.com/WolfZorace44832/Orderflow-Claude-skill-resocket) | Evidence-graded order-flow & footprint skill for Claude. Reads footprint, DOM, profile and CVD screenshots, separates what’s measured from what’s inferred, and shows what flow is actually useful for, without making trade calls. | 39 | — | HTML | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [DegreeApprentice/Ton-token-sniper-bot](https://github.com/DegreeApprentice/Ton-token-sniper-bot) | TON token sniper bot for STON.fi and DeDust DEX. Auto-skip scam tokens and honeypots, secure profits with trailing stops. High-frequency crypto trading bot for The Open Network. Toncoin | 35 | — |  | 工具 | 虚拟货币 | 分析/策略工具 |
| [leftamber/CEXTrader-Grid-Dca-Automation-Bot-Platform](https://github.com/leftamber/CEXTrader-Grid-Dca-Automation-Bot-Platform) | Open-source Grid + DCA trading bot for crypto. Supports Binance, Bybit, OKX, Hyperliquid, dYdX, Bitget. Advanced customization, OrderBook, risk management, Web UI and backtesting. | 22 | — | Python | 交易框架 | 虚拟货币 | 回测：明确提及 |
| [Jokejoker-designer/QUANTSMART](https://github.com/Jokejoker-designer/QUANTSMART) | A local workspace for testing strategies and building your own quantitative algorithms. Strategy Cards, historical replay, traceable validation and an optional MT5 connector. | 20 | — | TypeScript | 工具 | 未明确（需查文档） | 分析/策略工具 |


> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。

