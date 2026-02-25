---
outline: deep
---

# 十二、评估基准景观

## 12.1 核心评估基准

| 基准 | 侧重方向 | 评估维度 | 链接 |
|------|---------|---------|------|
| **HumanoidBench** | 全身控制 (D1) | 27 个任务，H1/Digit 平台 | [Project](https://humanoid-bench.github.io/) |
| **Isaac Lab Humanoid** | 行走 (D4) | 速度跟踪、能耗、稳定性 | [GitHub](https://github.com/isaac-sim/IsaacLab) |
| **AMASS MoCap 跟踪** | 运动模仿 (D1) | MPJPE、加速度误差、成功率 | [AMASS](https://amass.is.tue.mpg.de/) |
| **TRUMANS** | 场景交互 (D2) | 接触合理性、穿透率、交互多样性 | [PKU](https://pku.ai/trumans) |
| **RoboCasa** | 家庭操控 (D3) | 24 任务成功率 | [GitHub](https://github.com/robocasa/robocasa) |
| **DexGraspNet** | 灵巧抓取 (D3) | 抓取成功率、多样性 | [GitHub](https://github.com/PKU-EPIC/DexGraspNet) |

## 12.2 评估指标

| 类别 | 指标 | 描述 |
|------|------|------|
| **运动质量** | MPJPE (mm) | 关节位置平均误差 |
| | Accel Error | 加速度误差，衡量运动平滑度 |
| | Foot Sliding | 脚滑量，衡量地面接触质量 |
| | Success Rate (%) | 跟踪成功率（不跌倒比例） |
| **控制性能** | Vel Tracking Error | 速度指令跟踪误差 |
| | CoT (Cost of Transport) | 单位距离能耗 |
| | Push Recovery (N) | 抗推击能力 |
| | Terrain Success (%) | 特定地形通过率 |
| **Sim-to-Real** | Gap (%) | 仿真与真实性能差距 |

## 12.3 评估维度演进

| 代际 | 时间 | 特征 | 代表 |
|------|------|------|------|
| **第一代** | ~2022 | 仿真中简单成功率 | MuJoCo Humanoid-v4 |
| **第二代** | 2023–2024 | 运动质量 + 多任务 | HumanoidBench |
| **第三代** | 2025–2026 | 真实世界综合评估 | HPC 7 地形 / VIRAL 真机 |

> ⚠️ **关键挑战**：缺乏统一的跨方向评估标准——不同工作使用不同仿真、平台和指标。建立"人形运动控制的 ImageNet"是社区亟需推动的工作。

<!-- 更新标记：评估基准 最后更新 2026.02 -->
