---
outline: deep
---

# 什么是世界模型？

### 2.1 定义

World Model（世界模型）是一种 AI 系统，它学习对环境的内部表示，能够模拟环境在给定动作下的演变过程，从而使智能体通过"想象未来"进行规划，而非仅靠即时感知做出反应。

核心思想可追溯至认知科学家 Kenneth Craik（1943）在《The Nature of Explanation》中提出的"心智模型"概念——人脑构建外部世界的"小比例模型"来预测事件。在 AI 领域，这一思想被重新定义为：**学习环境的压缩时空表示，用于预测、规划和决策**。

具体而言，世界模型能够：

1. **编码当前状态**：将高维观测（如像素、点云、传感器数据）压缩为紧凑的内部表征
2. **预测未来状态**：给定当前状态和行动，预测下一个状态（即 $P(s_{t+1} | s_t, a_t)$）
3. **模拟后果**：通过迭代预测，在"想象"中评估不同行动序列的长期影响
4. **支持规划**：利用上述能力在内部模拟中搜索最优策略，而无需与真实环境交互

### 2.2 核心数学框架

世界模型的核心可以形式化为一个状态转移函数的学习问题：

$$\hat{s}_{t+1} = f_\theta(s_t, a_t)$$

其中 $s_t$ 是时刻 $t$ 的状态表示，$a_t$ 是行动，$f_\theta$ 是参数化的世界模型。

在更一般的概率框架下：

$$p_\theta(s_{t+1} | s_t, a_t)$$

世界模型学习的是状态转移的条件分布。

在更真实的**部分可观测**场景（POMDP）中，智能体无法直接观察完整状态 $s_t$，只能获得观测 $o_t$。此时世界模型需要额外维护一个**信念状态** $b_t$：

$$b_t = \text{Encoder}(o_{1:t}, a_{1:t-1}), \quad \hat{b}_{t+1} = f_\theta(b_t, a_t)$$

Dreamer 系列的 RSSM 即遵循此范式，使用确定性路径 $h_t$ 和随机状态 $z_t$ 联合表示信念。在实践中，根据预测空间和建模方式的不同，这一框架衍生出多种变体：

| 范式 | 预测目标 | 代表方法 |
|------|---------|---------|
| **显式动力学模型** | 预测潜在状态向量 $s_{t+1}$ | Dreamer 系列（RSSM）、TD-MPC2 |
| **生成式模型** | 预测像素/token $o_{t+1}$ | Sora、Genie、DIAMOND |
| **联合嵌入预测** | 预测表征向量 $z_{t+1}$（丢弃不可预测细节） | JEPA（I-JEPA、V-JEPA） |
| **隐式世界模型** | 不显式预测，通过辅助损失对齐未来表征 | FLARE、TD-MPC |

### 2.3 世界模型 vs. 相关概念

| 概念 | 区别 |
|------|------|
| **视频生成模型** | 生成视觉上逼真的视频，但不一定理解物理规律或支持行动控制。关键争议见 [From Generative Engines to Actionable Simulators](https://arxiv.org/abs/2601.15533) |
| **模拟器（Simulator）** | 基于手工编码的物理/规则引擎；世界模型是从数据中学习的 |
| **数字孪生** | 特定物理系统的精确复制；世界模型是通用的、可泛化的 |
| **语言模型** | 在文本空间中建模序列分布，可能隐含地学习了某些世界知识（参见 [Othello-GPT](https://arxiv.org/abs/2210.13382)、[LLM Represent Space and Time](https://arxiv.org/abs/2310.02207)） |
| **NeRF / 3DGS** | 神经辐射场和 3D 高斯溅射是**静态场景的 3D 表示方法**，可作为世界模型的空间表征组件（如 [3D and 4D World Modeling](https://arxiv.org/abs/2509.07996)），但它们本身不建模动力学或时间演化 |

### 2.4 为什么世界模型如此重要？

- **样本效率**：在想象中训练策略，大幅减少真实环境交互次数（DreamerV3 用想象训练首次从零收集 Minecraft 钻石 — [🎬 官方演示](https://danijar.com/project/dreamerv3/) · [GitHub](https://github.com/danijar/dreamerv3)）
- **安全性**：在内部模拟中测试危险场景，无需真实试错（GAIA-1 在虚拟环境模拟驾驶场景 — [🎬 Wayve 官方博客](https://wayve.ai/thinking/scaling-gaia-1/)）
- **泛化能力**：一个好的世界模型可以生成无限多样的训练场景（[Cosmos-Drive-Dreams](https://arxiv.org/abs/2506.09042) — [🎬 NVIDIA 演示](https://research.nvidia.com/labs/toronto-ai/cosmos-drive-dreams/)）
- **通向 AGI 的关键路径**：LeCun 认为世界模型是实现自主机器智能的核心组件；[DreamZero](https://arxiv.org/abs/2602.15922) 证明世界模型可作为零样本策略（[🎬 项目主页](https://dreamzero-world-action-model.github.io/)）

### 2.5 当前局限性

世界模型虽然前景广阔，但仍面临若干根本性挑战（[From Generative Engines to Actionable Simulators](https://arxiv.org/abs/2601.15533)）：

1. **长时预测误差累积**：多步展开后预测质量快速衰减，这是自回归模型的固有缺陷（[A Comprehensive Survey on World Models for Embodied AI](https://arxiv.org/abs/2510.16732)）
2. **物理理解的脆弱性**：视觉逼真度 ≠ 物理理解——模型可生成逼真视频但违反基本物理约束（如物体穿模、重力异常）
3. **分布外泛化失败**：在未见过的场景或动力学条件下，世界模型的预测可靠性急剧下降
4. **评估困难**：缺乏统一的评估框架来衡量世界模型是否"真正理解"了世界规律（参见 [Simulating the Visual World: A Roadmap](https://arxiv.org/abs/2511.08585)）
5. **计算成本高昂**：大规模视频世界模型训练需要数千 GPU 天，限制了学术界的参与
