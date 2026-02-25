---
outline: deep
---

# 发展历程与里程碑时间线

### 3.1 早期奠基（2000–2017）

| 年份 | 工作 | 作者/机构 | 贡献 |
|------|------|----------|------|
| 2000 | **ASIMO** | Honda | 首个能够流畅行走、上下楼梯的人形机器人，采用 ZMP（零力矩点）步态规划 |
| 2004 | ZMP 步态规划综述 | Vukobratović 等 | 系统化 ZMP 理论，成为经典动态行走方法 |
| 2013 | [Atlas（液压）](https://www.bostondynamics.com/atlas) | Boston Dynamics | DARPA 机器人挑战赛平台，液压驱动，展示了极端环境下的运动能力 |
| 2016 | [Whole-Body Control (WBC)](https://arxiv.org/abs/1607.07718) | IHMC 等 | 全身控制框架成熟，支撑 Atlas 在 DRC 决赛中的表现 |
| 2017 | [Cassie](https://arxiv.org/abs/1801.08093) | Agility Robotics | 首个专为 RL 控制设计的双足平台，奠定仿真到实机迁移基础 |

### 3.2 Sim-to-Real 浪潮（2018–2023）

| 年份 | 工作 | 作者/机构 | 贡献 |
|------|------|----------|------|
| 2018 | [**DeepMimic**](https://arxiv.org/abs/1804.02717) ⭐ | Peng 等（UC Berkeley） | **里程碑论文**：通过参考运动模仿的强化学习，首次实现物理仿真中的高质量类人运动（翻跟头、武术动作） |
| 2019 | [Sim-to-Real RL for Locomotion](https://arxiv.org/abs/2004.10190) | Lee 等（ETH Zurich） | 四足机器人 Sim-to-Real，域随机化 + 教师-学生蒸馏框架影响深远 |
| 2021 | [**AMP**](https://arxiv.org/abs/2104.02180) ⭐ | Peng 等（UC Berkeley） | 对抗运动先验（Adversarial Motion Priors）：用 GAN 判别器替代手工奖励，从少量 MoCap 数据学习自然运动风格 |
| 2022 | [PHC](https://arxiv.org/abs/2205.02194) | Luo 等 | 永续人形控制器（Perpetual Humanoid Control）：长时间稳定的物理仿真运动跟踪 |
| 2023 | [**DWL**](https://arxiv.org/abs/2408.14472) ⭐ RSS 2024 最佳论文入围 | He 等（CMU） | 去噪世界模型学习——通过学习一个世界模型对传感器噪声去噪，显著提升真实人形运动鲁棒性 |
| 2023 | [H2O](https://arxiv.org/abs/2309.14025) | Tairan He 等（CMU） | Human-to-Humanoid：仅用 RGB 摄像头的实时全身遥操作框架 |
| 2023 | [UniHSI](https://arxiv.org/abs/2309.07918) | Xiao 等 | **ICLR 2024**：统一人-场景交互框架，通过接触链提示实现多样化交互 |

### 3.3 基础模型时代（2024–2026）

| 日期 | 工作 | 机构 | 贡献 |
|------|------|------|------|
| 2024.04 | [**Electric Atlas**](https://www.bostondynamics.com/atlas) ⭐ | Boston Dynamics | Atlas 从液压转向全电驱动，标志性产业变革 |
| 2024.06 | [**HumanPlus**](https://arxiv.org/abs/2406.10454) ⭐ | Stanford | 单 RGB 摄像头全身模仿 + 自主学习系统，Humanoid Shadowing Transformer（33 DoF） |
| 2024.06 | [**OmniH2O**](https://arxiv.org/abs/2406.08858) ⭐ | CMU / UC San Diego | 通用人-人形全身遥操作+自主框架，支持 VR / 语音 / RGB 多模态控制接口 |
| 2024.08 | [ExBody](https://arxiv.org/abs/2402.01338) | 上海 AI Lab | 表达性全身控制，从大规模 MoCap 数据学习丰富运动 |
| 2024.11 | [**VIRAL**](https://arxiv.org/abs/2411.09838) | NVIDIA | 视觉 Sim-to-Real 人形移动操作框架，纯仿真训练零样本部署 |
| 2024.12 | [**ExBody2**](https://arxiv.org/abs/2412.13196) ⭐ | 上海 AI Lab | 进阶版表达性全身控制：教师-学生两阶段训练，关键点跟踪与速度控制解耦，Unitree G1/H1 验证 |
| 2025.01 | [BFM Survey](https://arxiv.org/abs/2412.07539) | 多机构 | 行为基础模型综述：梳理从运动数据预训练通用控制策略的技术路线 |
| 2025.02 | [**PhysHSI**](https://arxiv.org/abs/2502.07747) | 上海交大 | 真实世界可泛化的人形-场景交互系统，AMP 训练 + 场景感知 + Sim-to-Real |
| 2025.03 | [**HPC**](https://arxiv.org/abs/2503.01048) | PKU / 多机构 | 人形感知控制器，世界模型去噪 + 特权状态估计，7 种户外地形验证 |
| 2025.03 | [**NVIDIA GR00T N1**](https://arxiv.org/abs/2503.14734) ⭐ | NVIDIA | 开放基础模型：双系统架构（慢速 VLM 推理 + 快速扩散策略），人形机器人通用控制 |
| 2025.04 | [LangWBC](https://arxiv.org/abs/2504.01974) | 清华 / 多机构 | 语言指导的端到端全身控制策略 |
| 2025.06 | [**KungfuBot**](https://arxiv.org/abs/2506.00818) | 清华 | 物理人形全身控制学习高动态技能（功夫、舞蹈） |
| 2025.08 | [Fast Humanoid Locomotion](https://arxiv.org/abs/2512.03273) | 多机构 | 15 分钟训练人形行走策略，FastSAC/FastTD3 + 大规模并行仿真 |
| 2025.10 | [**DPL**](https://arxiv.org/abs/2510.13809) | 多机构 | 纯深度感知人形运动：合成深度 + 交叉注意力地形重建 |
| 2025.10 | [**SONIC**](https://sonic-humanoid.github.io/) | CMU | 超大规模运动跟踪：扩大模型+数据+计算，通用人形控制器 |
| 2025.12 | BFM Pretrain Survey v2 | 多机构 | 行为基础模型综述更新版，覆盖 2025 全年进展 |
| 2026.02 | [**MOSAIC**](https://arxiv.org/abs/2602.03344) | 多机构 | 通用人形运动跟踪与遥操作：快速残差适配弥合 Sim-to-Real 差距 |
| 2026.02 | [**ZEST**](https://arxiv.org/abs/2602.03827) | 多机构 | 零样本具身技能迁移：用于运动机器人控制 |
| 2026.02 | 研究爆发期 | — | 2026 年前两月，arXiv 上人形运动控制论文超百篇 |
