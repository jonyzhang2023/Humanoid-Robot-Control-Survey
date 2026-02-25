---
outline: deep
---

# 方向五：LLM 作为与增强世界模型

### 8.1 方向概述

这一方向探索三个核心问题：（1）LLM 是否隐含地学习了世界模型？（2）如何将 LLM 显式地用作世界模型进行规划？（3）Agent + World Model 如何协同？

> 📖 最新综述 [LLMs Meet World Models: A Survey](https://arxiv.org/abs/2501.11417) 系统梳理了 LLM 与世界模型交叉领域的全部工作。[From Masks to Worlds](https://arxiv.org/abs/2510.20668) 从统一架构视角分析了序列模型如何演化为世界模型。

**"LLM 是否具有世界模型"** 的争论目前尚无定论。支持方指出 Othello-GPT 等实验证据表明序列模型可涌现因果性世界表征；反对方则认为这种涌现可能只是特定任务中的统计捷径，并不等同于对物理世界的结构性理解。多模态 LLM（GPT-4o、Gemini 2.0）进一步模糊了边界——它们在视觉推理中展现了部分空间理解，但在物理推理任务中仍频繁失败。

### 8.2 关键论文深度解析

#### 8.2.1 Othello-GPT — 序列模型中涌现世界表征

| 项目 | 内容 |
|------|------|
| **论文** | [*Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task*](https://arxiv.org/abs/2210.13382) |
| **发表** | **ICLR 2023, Notable Top 5%** |

**实验设计**：训练一个 GPT 变体预测黑白棋（Othello）的合法走法——模型对游戏规则完全无先验知识。

**关键发现**：
1. 使用**非线性探针**揭示模型内部涌现出了棋盘状态的表征
2. **干预实验**：修改内部表征会因果地改变预测的合法走法
3. 探针恢复棋盘状态的错误率仅 0.01%

**里程碑意义**：**序列模型在 next-token 预测中可以涌现出因果性世界模型**的最重要证据之一。

#### 8.2.2 RAP — 推理即规划

| 项目 | 内容 |
|------|------|
| **论文** | [*Reasoning with Language Model is Planning with World Model*](https://arxiv.org/abs/2305.14992) |
| **发表** | **EMNLP 2023** |

**方法**：将 LLM 同时用作**世界模型**（预测状态转移）和**智能体**（选择行动），使用**蒙特卡洛树搜索（MCTS）**在 LLM 生成的世界状态上进行战略性探索。

**成果**：LLaMA-33B + RAP 在计划生成任务中**超越 GPT-4 + CoT 33%**。

#### 8.2.3 Voyager / DEPS — LLM Agent 中的世界建模

| 项目 | 内容 |
|------|------|
| **论文** | [*Voyager: An Open-Ended Embodied Agent with LLMs*](https://arxiv.org/abs/2305.16291) / [*DEPS: Describe, Explain, Plan and Select*](https://arxiv.org/abs/2302.01560) |
| **发表** | **Voyager: NeurIPS 2023 Spotlight** / **DEPS: ICLR 2024** |

**核心思路**：LLM 不直接担当世界模型，而是在 **Agent 循环** 中通过自然语言描述环境状态、生成代码技能、并将执行反馈迭代地纳入"世界知识"。Voyager 在 Minecraft 中自动发现 63 种物品，覆盖科技树 15.3×；DEPS 引入"描述→解释→计划→选择"四步框架，将成功率提升 2× 以上。

**范式意义**：**Code-as-World-Model** ——LLM 将世界知识编码为可执行程序而非隐式参数，天然支持组合泛化、可验证性和终生学习。这一范式在 [WALL-E 2.0](https://arxiv.org/abs/2504.15785) 中被进一步发展为神经符号学习框架。

### 8.3 关键议题：LLM 是否真正具有世界模型？

这一问题是该方向最核心的学术争论，值得专门讨论。

**支持观点（Emergentist）**：
- **涌现证据**：Othello-GPT 显示序列模型可以在无监督训练中涌现棋盘状态表征（§8.2.1）；Llama-2 中可提取空间坐标和时间信息的线性探针
- **理论论证**：[Affordances Enable Partial WM](https://arxiv.org/abs/2602.10390)（DeepMind, 2026）理论证明——任何成功的语言条件 Agent 必然拥有基于 affordance 的部分世界模型
- **社会认知**：[On Emergent Social WMs](https://arxiv.org/abs/2602.10298)（2026）发现 LLM 涌现出心智理论与语用推理能力

**质疑观点（Skepticist）**：
- **统计捷径**：涌现表征可能只是特定任务中的统计相关，不具有跨域鲁棒性
- **物理推理脆弱**：即使 GPT-4o/Gemini 2.0 等多模态 LLM，在简单物理推理（如"球滚下斜坡后去向何方"）中错误率仍超 40%
- **缺乏时空一致性**：LLM 对空间和时间的理解是碎片化的，不满足世界模型所需的状态转移一致性
- **幻觉问题**：世界模型需要忠实模拟而非"合理编造"，而 LLM 的幻觉本质与此矛盾

**折中立场**：LLM 习得了**语义层面的部分世界知识**（常识推理、因果语言、社会认知），但缺乏**物理层面的接地**（空间几何、动力学、接触力学）。将 LLM 的语义知识与视觉/物理世界模型融合（如 LAW 框架、LWM）是当前最有前景的方向。

### 8.4 前沿论文全景

| 论文 | 会议/时间 | 核心贡献 | 链接 |
|------|----------|---------|------|
| **隐含世界表征** | | | |
| [LLM 表征空间与时间](https://arxiv.org/abs/2310.02207) | 2023.10 | Llama-2 学习到空间坐标和时间信息的线性表征 | [arXiv](https://arxiv.org/abs/2310.02207) |
| [从词模型到世界模型](https://arxiv.org/abs/2306.12672) | 2023.06 | LLM 翻译为概率程序，贝叶斯推理实现世界推理 | [arXiv](https://arxiv.org/abs/2306.12672) |
| [Affordances Enable Partial WM](https://arxiv.org/abs/2602.10390) | DeepMind, 2026.02 | 理论证明语言条件 Agent 必然拥有基于 affordance 的部分世界模型 | [arXiv](https://arxiv.org/abs/2602.10390) |
| [On Emergent Social WMs](https://arxiv.org/abs/2602.10298) | 2026.02 | LLM 中涌现的社会世界模型——心智理论与语用推理 | [arXiv](https://arxiv.org/abs/2602.10298) |
| **LLM 作为规划世界模型** | | | |
| [语言模型遇见世界模型](https://arxiv.org/abs/2305.10626) | 2023.05 | 具身经验微调 LM，物理推理提升 64.28% | [arXiv](https://arxiv.org/abs/2305.10626) |
| [LAW 框架](https://arxiv.org/abs/2312.05230) | NeurIPS 2023 Tutorial | 语言模型(L)、智能体模型(A)、世界模型(W) 三位一体 | [arXiv](https://arxiv.org/abs/2312.05230) |
| [LLM-Sim](https://arxiv.org/abs/2406.06485) | ACL 2024 | 语言模型作为文本世界模拟器 | [arXiv](https://arxiv.org/abs/2406.06485) |
| [WebDreamer](https://arxiv.org/abs/2411.06559) | 2024.11 | LLM 是否是互联网的世界模型 | [arXiv](https://arxiv.org/abs/2411.06559) |
| [WorldLLM](https://arxiv.org/abs/2506.06725) | 2025.06 | 好奇心驱动的理论构建改善 LLM 世界建模 | [arXiv](https://arxiv.org/abs/2506.06725) |
| **LLM Agent + 世界模型** | | | |
| [Voyager](https://arxiv.org/abs/2305.16291) | NeurIPS 2023 Spotlight | 开放式具身 Agent，LLM 生成代码技能 + 自动课程学习 | [GitHub](https://github.com/MineDojo/Voyager) [![Stars](https://img.shields.io/github/stars/MineDojo/Voyager?style=social)](https://github.com/MineDojo/Voyager) |
| [DEPS](https://arxiv.org/abs/2302.01560) | ICLR 2024 | 描述-解释-计划-选择四步框架，成功率提升 2× | [arXiv](https://arxiv.org/abs/2302.01560) |
| [WALL-E 2.0](https://arxiv.org/abs/2504.15785) | 2025.04 | 神经符号学习改善基于世界模型的 LLM Agent | [arXiv](https://arxiv.org/abs/2504.15785) |
| [RL World Model for LLM Agents](https://arxiv.org/abs/2602.05842) | 2026.02 | 面向 LLM Agent 的强化世界模型学习 | [arXiv](https://arxiv.org/abs/2602.05842) |
| **多模态 & 长上下文** | | | |
| [LWM](https://arxiv.org/abs/2402.08268) | UC Berkeley, 2024 | 基于 RingAttention 的百万 token 视频+语言世界模型 | [GitHub](https://github.com/LargeWorldModel/LWM) [![Stars](https://img.shields.io/github/stars/LargeWorldModel/LWM?style=social)](https://github.com/LargeWorldModel/LWM) |

### 8.5 方向小结

| 特征 | 描述 |
|------|------|
| **核心范式** | ① 隐式涌现（Othello-GPT → 探针发现内部世界态）② 显式规划（RAP → LLM 作 MDP 转移函数）③ Agent 协同（Voyager → Code-as-WM） |
| **优势** | 利用 LLM 的海量常识与语义知识；支持自然语言交互；Code-as-WM 天然可组合可验证；Agent+WM 范式形成闭环 |
| **局限** | 物理推理仍脆弱（简单直觉物理错误率 > 40%）；幻觉与忠实模拟矛盾；缺乏时空一致性；推理成本高 |
| **核心洞察** | LLM 拥有**语义世界模型**（常识、因果语言、社会认知）但缺乏**物理世界模型**（几何、动力学、接触）；两者融合（LAW/LWM 范式）是关键突破点 |
| **未来方向** | 多模态 LLM 与物理模拟器融合；Code-as-WM 的形式化验证；从 Agent 经验中自主构建世界模型（WorldLLM） |
| **开放问题** | "LLM 是否真正具有世界模型"仍是开放性问题——§8.3 的折中共识为当前学界主流 |
