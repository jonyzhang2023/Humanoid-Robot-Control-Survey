---
outline: deep
---

# 方向二：人-场景交互 (HSI)

### 5.1 方向概述

人-场景交互（Human-Scene Interaction, HSI）研究人形机器人/虚拟角色与 3D 场景中家具、楼梯、地面等静态元素的物理交互。这一方向正从**动画/虚拟角色生成**走向**真实机器人部署**，核心挑战在于：（1）生成符合物理规律的全身接触运动；（2）泛化到未见过的场景布局；（3）弥合仿真与真实部署的差距。

> 📖 综述 [A Survey on Human Interaction Motion Generation](https://arxiv.org/abs/2503.11755) 系统梳理了人-人、人-物、人-场景交互的运动生成进展。ICCV 2025 专门设立了 [Human-Robot-Scene Interaction and Collaboration Workshop](https://human-robot-scene.github.io/)。

### 5.2 关键论文深度解析

#### 5.2.1 UniHSI — 统一人-场景交互

| 项目 | 内容 |
|------|------|
| **论文** | [*UniHSI: Unified Human-Scene Interaction via Prompted Chain-of-Contacts*](https://arxiv.org/abs/2309.07918) |
| **发表** | ICLR 2024 |
| **日期** | 2023.09 |

**核心方法**：提出**接触链（Chain-of-Contacts）**作为统一的交互表示——将复杂的人-场景交互分解为一系列身体部位与场景物体之间的接触事件序列。

**关键创新**：
- **LLM 驱动的任务规划**：使用大语言模型将自然语言指令（如"坐在椅子上"）转化为接触链序列
- **物理仿真控制**：基于 AMP 框架训练 RL 策略，执行接触链指定的交互
- **统一范式**：同一框架支持坐、躺、靠、上楼梯等多种交互类型

**成果**：在 PartNet 和 ScanNet 场景中验证了多样化的人-场景交互生成能力。

#### 5.2.2 PhysHSI — 真实世界人形-场景交互

| 项目 | 内容 |
|------|------|
| **论文** | [*PhysHSI: Real-World Generalizable and Natural Humanoid-Scene Interaction System*](https://arxiv.org/abs/2502.07747) |
| **机构** | 上海交通大学 |
| **日期** | 2025.02 |

**核心突破**：将 HSI 从虚拟角色扩展到**真实人形机器人**。

**系统架构**：
1. **训练流水线**：基于 AMP 的仿真训练，学习场景条件下的全身运动策略
2. **场景感知模块**：实时物体定位与场景理解，持续更新交互目标
3. **Sim-to-Real 迁移**：域随机化 + 严格的对齐评估协议

**关键发现**：
- 仅在仿真中训练的策略可以在真实人形机器人上执行椅子就座、物品拾取等交互
- 场景感知模块的持续定位能力对泛化到新场景至关重要
- 动态物体追踪和交互仍然是主要挑战

#### 5.2.3 SceneDiffuser — 场景条件扩散生成

| 项目 | 内容 |
|------|------|
| **论文** | [*SceneDiffuser: Efficient and Controllable Driving Simulation via Consistent Scene Diffusion*](https://arxiv.org/abs/2306.07870) |
| **发表** | ICCV 2023 |
| **日期** | 2023.06 |

**核心方法**：使用条件扩散模型在 3D 场景中生成人体姿态和运动序列。将场景几何和语义信息作为条件注入扩散过程，实现场景感知的人体运动规划。

### 5.3 HSI 技术演进

| 阶段 | 时间 | 方法 | 特点 |
|------|------|------|------|
| **数据驱动生成** | 2020–2022 | PROX、PLACE、POSA | 从数据学习人体在场景中的合理放置 |
| **物理仿真交互** | 2023–2024 | UniHSI、AMP-HSI | 物理引擎中训练 RL 策略执行交互 |
| **真实机器人部署** | 2025– | PhysHSI | 仿真策略迁移到真实人形平台 |
| **扩散模型生成** | 2023– | SceneDiffuser、TRUMANS | 条件扩散模型生成场景交互运动 |

### 5.4 核心技术挑战

#### 5.4.1 接触建模

HSI 的核心难点在于**频繁的接触状态切换**：行走→坐下→站起的过程中，接触点从脚底→臀部→脚底切换，每次切换都引入不连续的动力学变化。

**解决方案演进**：
- **早期**：显式接触规划（预定义接触序列）
- **UniHSI**：接触链提示（Chain-of-Contacts），由 LLM 生成
- **PhysHSI**：隐式接触学习，RL 策略自动发现接触策略

#### 5.4.2 场景泛化

| 挑战 | 当前方法 | 局限 |
|------|---------|------|
| 未见家具形状 | 点云条件化 | 语义理解不足 |
| 不同场景布局 | 坐标变换 + 重定位 | 路径规划与交互解耦 |
| 动态场景 | 持续感知 + 重规划 | 计算延迟大 |

### 5.5 前沿论文全景

| 论文 | 会议/时间 | 核心贡献 | 链接 |
|------|----------|---------|------|
| [PROX](https://arxiv.org/abs/1912.02923) | ICCV 2019 | 场景约束的人体形状与姿态估计 | [arXiv](https://arxiv.org/abs/1912.02923) |
| [PLACE](https://arxiv.org/abs/2008.05570) | 3DV 2020 | 场景中人体的合理放置 | [arXiv](https://arxiv.org/abs/2008.05570) |
| [POSA](https://arxiv.org/abs/2108.07945) | CVPR 2022 | 基于接触的场景交互姿态生成 | [arXiv](https://arxiv.org/abs/2108.07945) |
| [COINS](https://arxiv.org/abs/2211.11836) | CVPR 2023 | 可组合的人-物-场景交互合成 | [arXiv](https://arxiv.org/abs/2211.11836) |
| [SceneDiffuser](https://arxiv.org/abs/2306.07870) | ICCV 2023 | 场景条件扩散模型的运动生成 | [arXiv](https://arxiv.org/abs/2306.07870) |
| [**UniHSI**](https://arxiv.org/abs/2309.07918) | ICLR 2024 | 统一接触链 + LLM 任务规划 | [arXiv](https://arxiv.org/abs/2309.07918) |
| [TRUMANS](https://arxiv.org/abs/2407.11094) | ECCV 2024 | 实时用户引导的场景交互运动合成 | [arXiv](https://arxiv.org/abs/2407.11094) |
| [InterScene](https://arxiv.org/abs/2405.04219) | 2024.05 | 语言指导的 3D 场景交互运动生成 | [arXiv](https://arxiv.org/abs/2405.04219) |
| [**PhysHSI**](https://arxiv.org/abs/2502.07747) | 2025.02 | 真实世界人形-场景交互系统 | [arXiv](https://arxiv.org/abs/2502.07747) |
| [HSI Survey](https://arxiv.org/abs/2503.11755) | 2025.03 | 人类交互运动生成综合综述 | [arXiv](https://arxiv.org/abs/2503.11755) |

### 5.6 方向小结

| 特征 | 描述 |
|------|------|
| **优势** | 直接服务家庭/办公场景部署；LLM 赋能的任务规划使自然语言交互成为可能 |
| **局限** | 真实部署刚起步（PhysHSI 是首个）；动态场景交互仍然困难；接触动力学 sim-to-real 差距大 |
| **趋势** | 从动画生成 → 机器人部署；从预定义交互 → LLM 驱动的开放式交互；多模态场景理解与交互规划融合 |
| **代表方法** | UniHSI, PhysHSI, SceneDiffuser, TRUMANS, COINS |
