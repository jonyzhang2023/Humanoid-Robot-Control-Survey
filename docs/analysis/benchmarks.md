---
outline: deep
---

# 评估基准景观

世界模型评估正在从"单维度指标"走向"多维度综合基准"。以下是截至 2026 年 2 月的主要评估基准：

| 基准 | 时间 | 评估目标 | 核心维度 | 链接 |
|------|------|---------|---------|------|
| [**WorldSimBench**](https://arxiv.org/abs/2410.18072) | 2024.10 | 视频生成世界模拟器 | 显式感知 + 隐式推理 | [arXiv](https://arxiv.org/abs/2410.18072) |
| [**EWMBench**](https://arxiv.org/abs/2405.13503) | 2024.05 | 具身世界模型 | 物理交互预测 | [arXiv](https://arxiv.org/abs/2405.13503) |
| [**WorldModelBench**](https://arxiv.org/abs/2504.12579) | 2025.04 | 多模态世界模型 | 感知、推理、规划统一评估 | [arXiv](https://arxiv.org/abs/2504.12579) |
| [**WorldArena**](https://arxiv.org/abs/2501.18622) | 2025.01 | 交互式智能体评估 | 智能体在世界模型中的表现 | [arXiv](https://arxiv.org/abs/2501.18622) |
| [**WorldBench**](https://arxiv.org/abs/2504.18308) | 2025.04 | LLM 世界知识 | 常识推理、空间推理 | [arXiv](https://arxiv.org/abs/2504.18308) |
| [**4DWorldBench**](https://arxiv.org/abs/2601.15655) | 2026.01 | 4D 时空理解 | 3D + 时间维度预测 | [arXiv](https://arxiv.org/abs/2601.15655) |
| [**PhysBench**](https://arxiv.org/abs/2406.10170) | 2024.06 | 物理推理 | 刚体/流体/材料等物理规律 | [arXiv](https://arxiv.org/abs/2406.10170) |
| [**PhysGame**](https://arxiv.org/abs/2412.01800) | 2024.12 | 游戏物理理解 | 视频生成模型的游戏物理表现 | [arXiv](https://arxiv.org/abs/2412.01800) |
| [**VGBench**](https://arxiv.org/abs/2309.16292) | 2023.09 | 视频生成质量 | FVD、IS、CLIP-Sim 等 | [arXiv](https://arxiv.org/abs/2309.16292) |
| [**RoboBench (Dojo)**](https://arxiv.org/abs/2501.05600) | 2025.01 | 机器人世界模型 | 操作任务成功率 | [arXiv](https://arxiv.org/abs/2501.05600) |
| [**DriveArena**](https://arxiv.org/abs/2408.00415) | 2024.08 | 自动驾驶闭环 | 规划安全性、合规性 | [arXiv](https://arxiv.org/abs/2408.00415) |

**评估维度演进**：

1. **第一代（~2023）**：FVD、FID 等视觉质量指标 → 只关注"生成的像不像"
2. **第二代（2024）**：物理一致性 + 因果推理 → 关注"理解了没有"（PhysBench、WorldSimBench）
3. **第三代（2025–2026）**：交互性 + 动作可控 + 闭环评估 → 关注"能不能用"（WorldArena、4DWorldBench）
