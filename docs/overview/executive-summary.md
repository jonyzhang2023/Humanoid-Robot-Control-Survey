---
outline: deep
---

# 执行摘要

**人形机器人运动控制（Humanoid Robot Motion Control）** 是实现通用人形机器人的核心技术挑战——让双足类人平台在复杂、非结构化的真实世界环境中，安全、灵活、自然地执行多样化运动任务。这一领域融合了控制理论、强化学习、计算机视觉和生物力学，其终极目标是赋予机器人类人级别的运动智能。

**截至 2026 年 2 月，人形机器人运动控制已经历三次范式跃迁：**

| 阶段 | 时间 | 代表工作 | 核心特征 |
|------|------|---------|---------| 
| **传统控制时代** | 2000–2018 | ASIMO、Atlas（液压）、全身控制 (WBC)、ZMP 步态规划 | 基于模型的轨迹优化与逆运动学，依赖精确建模 |
| **Sim-to-Real 突破** | 2019–2023 | [Sim-to-Real RL](https://arxiv.org/abs/2004.10190)、[DeepMimic](https://arxiv.org/abs/1804.02717)、[AMP](https://arxiv.org/abs/2104.02180)、[DWL](https://arxiv.org/abs/2408.14472) | 大规模并行仿真 + 深度强化学习 + 域随机化，策略从仿真直接部署到真实机器人 |
| **基础模型时代** | 2024– | [ExBody2](https://arxiv.org/abs/2412.13196)、[HumanPlus](https://arxiv.org/abs/2406.10454)、[OmniH2O](https://arxiv.org/abs/2406.08858)、[SONIC](https://sonic-humanoid.github.io/)、[PhysHSI](https://arxiv.org/abs/2502.07747) | 行为基础模型（BFM），从海量人体运动数据预训练通用控制策略，零样本或快速适配多种任务 |

**六大标志性事件定义了当前格局：**

1. **Boston Dynamics Atlas 电动化（2024.4）**：从液压到全电驱动的转型，标志着人形机器人从实验室走向商业化部署的关键一步，新 Atlas 具备前所未有的灵活性和关节活动范围。

2. **Sim-to-Real 运动控制全面突破（2024–2025）**：[ExBody2](https://arxiv.org/abs/2412.13196)（Unitree G1/H1 全身表达性控制）、[HumanPlus](https://arxiv.org/abs/2406.10454)（单 RGB 摄像头实时全身模仿）、[OmniH2O](https://arxiv.org/abs/2406.08858)（VR/语音/RGB 多模态遥操作）等工作验证了从大规模人体运动数据训练通用全身控制器的可行性。

3. **感知移动大规模验证（2025）**：[HPC](https://arxiv.org/abs/2503.01048)（人形感知控制器，在雪地、碎石、楼梯等 7 种户外地形验证）、[DPL](https://arxiv.org/abs/2510.13809)（纯深度感知人形运动），实现了从盲策略到视觉感知的跨越。

4. **人-场景交互系统化（2024–2025）**：[UniHSI](https://arxiv.org/abs/2309.07918)（ICLR 2024，统一人-场景交互框架）和 [PhysHSI](https://arxiv.org/abs/2502.07747)（真实世界可泛化人形-场景交互系统）将 HSI 从动画生成推进到真实机器人部署。

5. **移动操作（Loco-Manipulation）爆发（2025–2026）**：[VIRAL](https://arxiv.org/abs/2411.09838)（视觉 Sim-to-Real 移动操作框架）、[TRILL](https://arxiv.org/abs/2309.15013)（VR 遥操作+深度模仿学习）、[Coordinated Manipulation](https://arxiv.org/abs/2511.17981) 等工作将上半身灵巧操控与下半身稳定行走统一在一个框架中。

6. **行为基础模型（BFM）兴起（2025–2026）**：[BFM Survey](https://arxiv.org/abs/2412.07539) 系统梳理了从大规模运动数据预训练行为基础模型的技术路线，NVIDIA [GR00T N1](https://arxiv.org/abs/2503.14734) 和 [SONIC](https://sonic-humanoid.github.io/) 等工作验证了通用人形控制器的 zero-shot 泛化能力。

**当前最活跃的五个交叉前沿：**
1. **通用全身控制 × 行为基础模型** → 一个策略控制所有运动（ExBody2、SONIC、BFM）← **2026 年最活跃方向**
2. **感知移动 × 复杂地形** → 自适应地形感知与鲁棒行走（HPC、DPL、DWL）
3. **HSI × 真实部署** → 从动画到机器人的场景交互（PhysHSI、SceneDiffuser）
4. **HOI × 移动操作** → 双手灵巧操控 + 全身协调（VIRAL、TRILL、H2O）
5. **感知导航 × VLA** → 语义理解驱动的长程自主导航（LLM-Nav、NaVILA）
