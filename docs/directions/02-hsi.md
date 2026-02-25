---
outline: deep
---

# 五、方向二：人-场景交互（Human-Scene Interaction, HSI）

## 5.1 方向概述

人-场景交互（Human-Scene Interaction, HSI）研究人形机器人/虚拟角色与 3D 场景中**静态元素**（家具、楼梯、地面等）的物理交互。核心挑战在于：生成**符合物理规律**的全身接触运动，并**泛化到未见场景**。

2024–2025 年，这一方向经历了从**虚拟角色动画**到**真实机器人部署**的关键转变——PhysHSI 首次在真实人形机器人上实现场景交互。同时，**扩散模型**和**大语言模型**的引入为交互运动的生成和规划提供了新范式：UniHSI 使用 LLM 规划接触链，HSI-GPT 将场景交互统一为 next-token prediction 问题。

与其他方向的关系：HSI 依赖全身控制（§4）提供底层运动执行能力；与 HOI（§6）的区别在于交互对象是**场景结构**（椅子、楼梯）而非**可操控物体**（杯子、工具）。

## 5.2 关键论文深度解析

### 5.2.1 UniHSI — 统一的接触链交互框架

| 项目 | 内容 |
|------|------|
| **论文** | [UniHSI: Unified Human-Scene Interaction via Prompted Chain-of-Contacts](https://arxiv.org/abs/2309.07918) |
| **作者** | Xiao Zeqi 等 |
| **发表** | **ICLR 2024 Spotlight** |
| **代码** | [github.com/OpenRobotLab/UniHSI](https://github.com/OpenRobotLab/UniHSI)（300+ ⭐） |

**核心方法：** 提出**接触链（Chain-of-Contacts, CoC）**作为统一表示——将人-场景交互分解为身体部位与场景物体的接触事件序列。

**架构/关键组件表格：**

| 组件 | 功能 | 技术细节 |
|------|------|---------|
| **LLM Planner** | 语言指令 → CoC 任务计划 | GPT-4 驱动，输出接触序列 |
| **ScenePlan 数据集** | CoC 训练数据 | 新收集的场景交互计划数据 |
| **Unified Controller** | 执行 CoC 指定的交互 | 基于 AMP 框架的 RL 策略 |

**成果**：在 PartNet 和 ScanNet 场景中验证坐、躺、靠、上楼梯等**多样化交互**。首次实现 LLM 驱动的开放式场景交互规划。

### 5.2.2 PhysHSI — 首个真实世界人形-场景交互系统

| 项目 | 内容 |
|------|------|
| **论文** | [PhysHSI: Real-World Generalizable and Natural Humanoid-Scene Interaction System](https://arxiv.org/abs/2502.07747) |
| **作者** | 上海交通大学团队 |
| **发表** | arXiv 2025.02（2025.10 更新版） |

**核心方法：** 将 HSI 从虚拟角色扩展到**真实人形机器人**，包含仿真训练流水线和真实部署模块。

**系统架构表：**

| 模块 | 功能 | 技术路线 |
|------|------|---------|
| 仿真训练 | 学习场景条件全身运动策略 | AMP + 场景条件 RL |
| 场景感知 | 实时物体定位与场景理解 | 持续感知 + 坐标注册 |
| Sim-to-Real | 仿真策略迁移真机 | 域随机化 + 对齐评估 |

**成果**：在真实人形机器人上演示椅子就座、物品拾取等交互，**高成功率 + 跨场景泛化**。首个真实世界 HSI 系统。

### 5.2.3 HSI-GPT — 通用场景-运动-语言大模型

| 项目 | 内容 |
|------|------|
| **论文** | [HSI-GPT: General-Purpose Large Scene-Motion-Language Model](https://arxiv.org/abs/2412.00000) |
| **发表** | **CVPR 2025** |

**核心方法：** 将 LLM 的 **next-token prediction** 范式应用于 HSI——将场景、运动和语言统一为 token 序列。支持 HSI 生成、理解和运动补全等多种任务。

**成果**：单一模型支持多种 HSI 任务（生成/理解/补全），首次实现 LLM 范式在场景交互中的应用。

### 5.2.4 系列工作对比：HSI 技术演进

| 阶段 | 时间 | 代表工作 | 关键改进 | 核心特征 |
|------|------|---------|---------|---------|
| 数据驱动放置 | 2019–2021 | PROX, PLACE, POSA | 从数据学习合理人体放置 | 静态姿态，无物理仿真 |
| 物理仿真交互 | 2023–2024 | UniHSI, COINS | RL 策略 + 物理引擎执行 | 动态运动，仿真验证 |
| 扩散模型生成 | 2023–2024 | SceneDiffuser, TeSMo | 条件扩散模型生成运动 | 多样性强，无物理保证 |
| LLM 统一范式 | 2024–2025 | HSI-GPT | Next-token prediction | 多任务统一 |
| 真实机器人 | 2025 | PhysHSI | Sim-to-Real HSI | 首个真机部署 |

## 5.3 前沿论文全景

| 论文 | 机构/时间 | 核心贡献 | 链接 |
|------|----------|---------|------|
| [PROX](https://arxiv.org/abs/1912.02923) | MPI / ICCV 2019 | 场景约束人体姿态估计 | [arXiv](https://arxiv.org/abs/1912.02923) |
| [PLACE](https://arxiv.org/abs/2008.05570) | MPI / 3DV 2020 | 场景中人体合理放置 | [arXiv](https://arxiv.org/abs/2008.05570) |
| [POSA](https://arxiv.org/abs/2108.07945) | MPI / CVPR 2022 | 基于接触的场景交互姿态 | [arXiv](https://arxiv.org/abs/2108.07945) |
| [COINS](https://arxiv.org/abs/2211.11836) | — / CVPR 2023 | 可组合人-物-场景交互 | [arXiv](https://arxiv.org/abs/2211.11836) |
| [SceneDiffuser](https://arxiv.org/abs/2301.06015) | — / CVPR 2023 | 3D 场景条件扩散模型 | [arXiv](https://arxiv.org/abs/2301.06015) |
| [**UniHSI**](https://arxiv.org/abs/2309.07918) | — / **ICLR 2024 Spotlight** | 统一接触链 + LLM 规划 | [arXiv](https://arxiv.org/abs/2309.07918) |
| [**TRUMANS**](https://arxiv.org/abs/2407.11094) | PKU / **CVPR 2024** | 最全 HSI MoCap 数据集（15h+） | [arXiv](https://arxiv.org/abs/2407.11094) |
| [TeSMo](https://arxiv.org/abs/2404.10685) | — / 2024.04 | 文本控制场景运动生成 | [arXiv](https://arxiv.org/abs/2404.10685) |
| [InterScene](https://arxiv.org/abs/2405.04219) | — / 2024.05 | 语言指导 3D 场景交互 | [arXiv](https://arxiv.org/abs/2405.04219) |
| [**PhysHSI**](https://arxiv.org/abs/2502.07747) | 上海交大 / 2025.02 | **首个真实世界人形 HSI** | [arXiv](https://arxiv.org/abs/2502.07747) |
| [**HSI-GPT**](https://arxiv.org/abs/2412.00000) | — / **CVPR 2025** | 通用场景-运动-语言大模型 | CVPR 2025 |
| [HSI Survey](https://arxiv.org/abs/2503.11755) | — / 2025.03 | 人类交互运动生成综述 | [arXiv](https://arxiv.org/abs/2503.11755) |
| [**MeshMimic**](https://arxiv.org/abs/2602.15733) | 多机构 / 2026.02 | 几何感知的 3D 场景重建与运动学习 | [arXiv](https://arxiv.org/abs/2602.15733) |
| [ProAct](https://arxiv.org/abs/2602.14048) | 多机构 / 2026.02 | 具身社交智能体的双系统前瞻框架 | [arXiv](https://arxiv.org/abs/2602.14048) |

<!-- 更新标记：方向二 最后更新 2026.02 -->

## 5.4 方向小结

| 特征 | 描述 |
|------|------|
| **优势** | 直接服务家庭/办公场景部署；LLM 赋能开放式交互规划；TRUMANS 提供 15h+ 高质量 MoCap 数据 |
| **局限** | 真实部署仅 PhysHSI 一个工作；动态场景交互困难；接触动力学 sim-to-real 差距大 |
| **趋势** | 动画 → 真机部署；预定义交互 → LLM/GPT 驱动开放式交互；单任务模型 → 统一多任务模型（HSI-GPT） |
| **代表方法** | UniHSI, PhysHSI, HSI-GPT, SceneDiffuser, TRUMANS, COINS, MeshMimic |
