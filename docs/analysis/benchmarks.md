---
outline: deep
---

# 评估基准景观

人形机器人运动控制的评估正在从单一成功率指标走向多维度综合评估。以下是截至 2026 年 2 月的主要评估基准和方法。

### 16.1 评估基准

| 基准/环境 | 侧重 | 评估维度 | 链接 |
|----------|------|---------|------|
| **Isaac Lab Humanoid** | 仿真行走基准 | 速度跟踪、能耗、稳定性 | [GitHub](https://github.com/isaac-sim/IsaacLab) |
| **MuJoCo Humanoid-v4** | 经典仿真基准 | 前进速度、能耗效率 | [Gym](https://gymnasium.farama.org/) |
| **AMASS MoCap 跟踪** | 运动模仿评估 | MPJPE、加速度误差、成功率 | [AMASS](https://amass.is.tue.mpg.de/) |
| **SceneDiff Bench** | 场景交互运动 | 穿透率、接触合理性、运动质量 | — |
| **RoboCasa** | 家庭场景操控 | 24 任务成功率 | [GitHub](https://github.com/robocasa/robocasa) |
| **DexGraspNet** | 灵巧抓取 | 抓取成功率、多样性 | [GitHub](https://github.com/PKU-EPIC/DexGraspNet) |

### 16.2 评估指标

#### 运动质量指标

| 指标 | 全称 | 描述 |
|------|------|------|
| **MPJPE** | Mean Per Joint Position Error | 关节位置平均误差（mm） |
| **Accel Error** | Acceleration Error | 加速度误差，衡量运动平滑度 |
| **FS** | Foot Sliding | 脚滑量，衡量地面接触质量 |
| **Success Rate** | — | 跟踪成功率（不跌倒的时间比例） |
| **Penetration** | — | 身体与场景/物体的穿透率 |

#### 控制性能指标

| 指标 | 描述 |
|------|------|
| **Velocity Tracking Error** | 速度指令跟踪误差（m/s） |
| **CoT** (Cost of Transport) | 单位距离能耗，衡量运动效率 |
| **Push Recovery** | 抗推击能力（能承受的最大外力） |
| **Terrain Success Rate** | 通过特定地形的成功率 |
| **Sim-to-Real Gap** | 仿真与真实性能的差距 |

### 16.3 评估维度演进

1. **第一代（~2022）**：仿真中的简单成功率——能走就行
2. **第二代（2023–2024）**：运动质量指标——不仅要走，还要走得自然（MPJPE、foot sliding）
3. **第三代（2025–2026）**：真实世界综合评估——多地形通过率、操控成功率、长时稳定性

> ⚠️ **评估的关键挑战**：当前缺乏统一的、跨方向的人形机器人运动控制评估标准。不同工作使用不同的仿真环境、机器人平台和评估指标，使横向对比困难。建立"人形机器人运动控制的 ImageNet"是社区亟需推动的工作。
