---
outline: deep
---

# 一、执行摘要

> **版本**：v2.0 · **更新日期**：2026 年 2 月 25 日
> **覆盖范围**：2000–2026 年 2 月 · **收录论文**：~150 篇
> **更新频率**：每月一次 · **下次计划更新**：2026 年 3 月
> **数据来源**：arXiv、顶会论文（RSS / CoRL / ICRA / Humanoids / SIGGRAPH / ICLR / CVPR）、GitHub、企业技术博客

**人形机器人运动控制（Humanoid Robot Motion Control）** 是实现通用人形机器人的核心技术挑战——让双足类人平台在复杂真实环境中安全、灵活、自然地执行多样化运动任务。这一领域融合了控制理论、强化学习、计算机视觉和生物力学，其终极目标是赋予机器人**类人级别的运动智能**。

**截至 2026 年 2 月，人形机器人运动控制已经历三次范式跃迁：**

| 阶段 | 时间 | 代表工作 | 核心特征 |
|------|------|---------|---------| 
| **传统控制** | 2000–2018 | ASIMO、Atlas（液压）、WBC/ZMP | 基于模型的轨迹优化与逆运动学 |
| **Sim-to-Real 突破** | 2019–2023 | [DeepMimic](https://arxiv.org/abs/1804.02717)、[AMP](https://arxiv.org/abs/2104.02180)、[DWL](https://arxiv.org/abs/2408.14472) | 大规模仿真 + 深度 RL + 域随机化 |
| **基础模型时代** | 2024– | [ExBody2](https://arxiv.org/abs/2412.13196)、[SONIC](https://sonic-humanoid.github.io/)、[GR00T N1](https://arxiv.org/abs/2503.14734)、[FAST](https://arxiv.org/abs/2602.01186) | BFM 预训练、多模态控制、跨平台泛化 |

**八大标志性事件定义了当前格局：**

1. **Boston Dynamics Atlas 全电动化 + CES 2026 商业版**：液压→全电驱转型，CES 2026 发布商业产品版，2026 全部预定，Hyundai 年产 30K 工厂 $26B 开建
2. **Sim-to-Real 全面突破**：[ExBody2](https://arxiv.org/abs/2412.13196)（G1/H1 表达性控制）、[HumanPlus](https://arxiv.org/abs/2406.10454)（单 RGB 全身模仿）、[OmniH2O](https://arxiv.org/abs/2406.08858)（多模态遥操作）
3. **感知移动大规模验证**：[HPC](https://arxiv.org/abs/2503.01048)（7 种户外地形）、[DPL](https://arxiv.org/abs/2510.13809)（纯深度感知）、[RPL](https://arxiv.org/abs/2602.00000)（多方向深度蒸馏 2026）
4. **BFM 范式确立**：[SONIC](https://sonic-humanoid.github.io/)（42M 参数 / 700h 数据）、[BFM Survey v2](https://arxiv.org/abs/2506.20487)、[FAST](https://arxiv.org/abs/2602.01186)（快速适配）、[XHugWBC](https://arxiv.org/abs/2602.04485)（跨平台泛化）
5. **移动操作爆发**：[VIRAL](https://arxiv.org/abs/2411.09838)（视觉 sim-to-real 70%+）、[ResMimic](https://arxiv.org/abs/2502.20030)（残差学习）
6. **VLA/LLM 渗透运动控制**：[GR00T N1](https://arxiv.org/abs/2503.14734)（双系统 VLA）、[LangWBC](https://arxiv.org/abs/2504.01974)（语言→全身控制）、[NaVILA](https://arxiv.org/abs/2503.16404)（VLA 导航）
7. **中国硬件全球称冠**：2025 年全球出货前六全部中国企业，智元 5100+ 全球第一，2026 中国产量预计 10–20 万台
8. **1000+ Tesla Optimus 工厂部署**：Optimus Gen3 在 Tesla 工厂运行 1000+ 台，目标年产百万台
9. **零样本迁移与扩散模型控制**：[BeyondMimic](https://arxiv.org/abs/2508.08241) 和 [ZEST](https://arxiv.org/abs/2602.00401) 证明基于纯数据生成的策略可以直接零样本部署到多种真实人形双足上。

**当前最活跃的六个交叉前沿：**
1. **全身控制 × BFM** → 一个策略控制所有运动（SONIC, FAST, XHugWBC）← **2026 最活跃**
2. **感知移动 × 复杂地形** → 自适应地形感知与鲁棒行走（HPC, DPL, RPL）
3. **HOI × VLA 基础模型** → 语义驱动的灵巧移动操作（GR00T N1, VIRAL）
4. **HSI × 真实部署** → 从动画到机器人场景交互（PhysHSI, HSI-GPT）
5. **导航 × VLA** → 语义理解驱动的长程自主导航（NaVILA, Humanoid-VLA）
6. **全身控制 × Zero-Shot 迁移** → 彻底抛弃复杂奖励工程，扩散模型端到端直接迁移真机（BeyondMimic, ZEST）

<!-- 更新标记：执行摘要 最后更新 2026.02 -->
