---
outline: deep
---

# 方向一：基于强化学习的世界模型

### 4.1 方向概述

这是世界模型最经典的研究路线。核心思想是：**在潜在空间中学习环境动力学模型，然后在"想象"的轨迹中训练策略**，从而大幅提升样本效率。从 Schmidhuber（1989）到 Dreamer4（2025），这条路线持续 36 年不断演进，始终是世界模型研究最坚实的理论基础。

### 4.2 关键论文深度解析

#### 4.2.1 World Models（Ha & Schmidhuber, 2018）— 奠基之作

| 项目 | 内容 |
|------|------|
| **论文** | [*Recurrent World Models Facilitate Policy Evolution*](https://arxiv.org/abs/1803.10122) |
| **作者** | David Ha（Google Brain），Jürgen Schmidhuber（NNAISENSE / IDSIA） |
| **发表** | NeurIPS 2018 |

**三组件架构（V-M-C）：**

| 组件 | 模型 | 功能 | 参数量 |
|------|------|------|--------|
| **V（视觉）** | 变分自编码器 (VAE) | 将 64×64 像素帧压缩为潜在向量 $z_t \in \mathbb{R}^{32}$ | ~430 万 |
| **M（记忆）** | MDN-RNN（LSTM + 混合密度网络） | 预测未来潜在状态：$P(z_{t+1} \mid a_t, z_t, h_t)$ | ~42-170 万 |
| **C（控制器）** | 单层线性层 | 将 $[z_t, h_t]$ 映射到动作 $a_t$；用 CMA-ES 进化策略训练 | **867-1088** |

**核心创新：**
- **梦境训练（Dream Training）**：智能体完全在潜在空间的"梦境"中训练，无需与真实环境交互
- **温度控制（$\tau$）**：调节世界模型的随机性，防止智能体利用模型缺陷
- **极简控制器**：将复杂性移入 V 和 M，使 C 极度精简（仅 ~1000 参数），可用进化策略训练

**成果**：CarRacing-v0 得分 906 ± 21（首次解决该任务），VizDoom Take Cover 得分 1092 ± 556（完全在梦境中训练）。

#### 4.2.2 Dreamer 系列技术演进（2020–2025）

| 版本 | 年份 | 论文 | 关键改进 | 重要成果 |
|------|------|------|---------|---------|
| **DreamerV1** | 2020 | [arXiv:1912.01603](https://arxiv.org/abs/1912.01603) | 在学习到的世界模型中使用 Actor-Critic 学习行为，替代进化策略 | 多个连续控制任务 SOTA |
| **DreamerV2** | 2021 | [arXiv:2010.02193](https://arxiv.org/abs/2010.02193) | 引入离散表征（categorical representations），从连续高斯切换到 32×32 one-hot 向量 | Atari 达到人类水平 |
| **DreamerV3** ⭐ | 2023 | [arXiv:2301.04104](https://arxiv.org/abs/2301.04104) | 基于 symlog 预测、percentile scaling 等归一化技术，**单一配置跨所有域** | 150+ 任务最优；Minecraft 首个从零挖钻石；**Nature 2025** |
| **Dreamer4** | 2025 | [arXiv:2509.24527](https://arxiv.org/abs/2509.24527) | 可扩展的世界模型内训练智能体，突破 DreamerV3 的规模限制 | 扩展性验证 |

**DreamerV3 核心方法**：学习环境的世界模型（RSSM），然后在想象轨迹中训练 actor-critic。关键在于使用 categorical representations 和一系列归一化技术，使同一套超参数可以跨越 Atari、DMControl、Minecraft 等完全不同的任务域。

**里程碑意义**：DreamerV3 发表于 **Nature (2025)**，标志着世界模型 RL 方法获得了最高级别的学术认可。其在 Minecraft 中从零收集钻石（需要长达 20,000+ 步的远视探索）是 AI 领域的标志性挑战。

#### 4.2.3 TD-MPC2 — 隐式世界模型

| 项目 | 内容 |
|------|------|
| **论文** | [*TD-MPC2: Scalable, Robust World Models for Continuous Control*](https://arxiv.org/abs/2310.16828) |
| **发表** | ICLR 2024 |
| **代码** | [github.com/nicklashansen/tdmpc2](https://github.com/nicklashansen/tdmpc2) [![Stars](https://img.shields.io/github/stars/nicklashansen/tdmpc2?style=social)](https://github.com/nicklashansen/tdmpc2) |

**核心方法**：在学习到的**隐式（无解码器）世界模型**的潜在空间中进行局部轨迹优化（模型预测控制）。与 Dreamer 系列不同，TD-MPC2 不重建观测——完全在潜在空间中规划。

**关键发现**：
- 单一 3.17 亿参数智能体可跨 80 个任务
- 智能体能力随模型和数据规模增长，验证了世界模型的缩放定律
- 104 个在线 RL 任务中表现一致

#### 4.2.4 DIAMOND — 扩散世界模型

| 项目 | 内容 |
|------|------|
| **论文** | [*Diffusion for World Modeling: Visual Details Matter in Atari*](https://arxiv.org/abs/2405.12399) |
| **发表** | NeurIPS 2024 Spotlight |
| **代码** | [github.com/eloialonso/diamond](https://github.com/eloialonso/diamond) [![Stars](https://img.shields.io/github/stars/eloialonso/diamond?style=social)](https://github.com/eloialonso/diamond) |

**核心洞察**：离散 token 化会**丢弃对 RL 性能至关重要的视觉细节**。DIAMOND 使用连续扩散替代离散 token 进行环境模拟。

**成果**：Atari 100k 平均人类归一化得分 **1.46**——世界模型训练智能体的新 SOTA。还可作为 CS:GO 的交互式神经游戏引擎。

### 4.3 前沿论文全景

| 论文 | 会议/时间 | 核心贡献 | 链接 |
|------|----------|---------|------|
| [MuZero](https://arxiv.org/abs/1911.08265) | Nature 2020 | 学习的模型用于搜索规划，无需环境规则，统治棋类与 Atari | [arXiv](https://arxiv.org/abs/1911.08265) |
| [IRIS](https://arxiv.org/abs/2209.00588) | ICLR 2023 Top 5% | Transformer 世界模型，将动力学学习转化为序列建模问题 | [GitHub](https://github.com/eloialonso/iris) |
| [STORM](https://arxiv.org/abs/2310.09615) | 2023 | Transformer+随机 VAE，单卡 4.3h 训练达 126.7% 人类水平 | [arXiv](https://arxiv.org/abs/2310.09615) |
| [SafeDreamer](https://arxiv.org/abs/2307.07176) | ICLR 2024 | 安全约束融入 Dreamer 框架，近零代价性能 | [arXiv](https://arxiv.org/abs/2307.07176) |
| [Diffusion Forcing](https://arxiv.org/abs/2407.01392) | NeurIPS 2024 | 独立逐 token 噪声训练范式，统一自回归与全序列扩散 | [arXiv](https://arxiv.org/abs/2407.01392) |
| [MoSim](https://arxiv.org/abs/2504.07095) | CVPR 2025 | 推动 RL 中世界模型的极限 | [arXiv](https://arxiv.org/abs/2504.07095) |
| [Dreamer4](https://arxiv.org/abs/2509.24527) | 2025.09 | 可扩展的世界模型内训练智能体 | [arXiv](https://arxiv.org/abs/2509.24527) |
| WIMLE | ICLR 2026 | 基于 IMLE 的不确定性感知世界模型 | — |
| Horizon Imagination | ICLR 2026 | 扩散世界模型中的高效策略训练 | — |
| [Mixture-of-World Models](https://arxiv.org/abs/2602.01270) | 2026.02 | 混合世界模型：模块化潜在动态扩展多任务 RL | [arXiv](https://arxiv.org/abs/2602.01270) |
| [ObjectZero](https://arxiv.org/abs/2601.07823) | 2026.01 | 对象中心世界模型结合蒙特卡洛树搜索 | [arXiv](https://arxiv.org/abs/2601.07823) |
| [Event-Aware WM](https://arxiv.org/abs/2601.14134) | 2026.01 | 事件感知世界模型提升 MBRL 样本效率 | [arXiv](https://arxiv.org/abs/2601.14134) |

### 4.4 方向小结

| 特征 | 描述 |
|------|------|
| **优势** | 样本效率高、理论清晰、可直接用于策略学习 |
| **局限** | 通常限于特定任务域，难以处理极复杂的开放世界 |
| **趋势** | 从 RSSM → Transformer → 扩散模型演进；正在与大规模视频生成方法融合，走向通用化；安全约束日益受到关注 |
| **代表方法** | Dreamer 系列、TD-MPC2、DIAMOND、IRIS、MuZero |
