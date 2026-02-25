---
outline: deep
---

# 开源生态全景

人形机器人运动控制领域拥有活跃的开源生态。以下梳理截至 2026 年 2 月的核心开源项目和资源。

### 14.1 仿真平台

| 项目 | 机构 | 许可证 | 特色 | 链接 |
|------|------|--------|------|------|
| **Isaac Lab** | NVIDIA | Apache-2.0 | GPU 加速大规模并行仿真，支持 RL 训练 | [GitHub](https://github.com/isaac-sim/IsaacLab) |
| **MuJoCo** | DeepMind | Apache-2.0 | 高精度接触动力学，学术界标准 | [GitHub](https://github.com/google-deepmind/mujoco) |
| **Genesis** | 多机构 | Apache-2.0 | 通用物理仿真平台，支持多种机器人 | [GitHub](https://github.com/Genesis-Embodied-AI/Genesis) |
| **SAPIEN** | 上海 AI Lab | MIT | 操作仿真平台，丰富的物体资产 | [GitHub](https://github.com/haosulab/SAPIEN) |

### 14.2 运动控制代码库

| 项目 | 功能 | Stars | 链接 |
|------|------|-------|------|
| **legged_gym** | Unitree 腿式机器人 RL 训练基准 | 1.5k+ | [GitHub](https://github.com/leggedrobotics/legged_gym) |
| **humanoid-gym** | 人形机器人特化的 RL 训练框架 | 1k+ | [GitHub](https://github.com/roboterax/humanoid-gym) |
| **OmniH2O** | 全身遥操作+数据集 | 500+ | [GitHub](https://github.com/LeCAR-Lab/OmniH2O) |
| **HumanPlus** | 全栈人形模仿系统 | 1k+ | [GitHub](https://github.com/MarkFzp/humanplus) |
| **ExBody** | 表达性全身控制 | 400+ | [GitHub](https://github.com/chengxuxin/expressive-humanoid) |
| **PHC** | 永续人形控制器 | 800+ | [GitHub](https://github.com/ZhengyiLuo/PHC) |
| **AMP** | 对抗运动先验 | 700+ | [GitHub](https://github.com/nv-tlabs/ASE) |

### 14.3 人体运动数据集

| 数据集 | 规模 | 特色 | 链接 |
|--------|------|------|------|
| **AMASS** | 40+ 小时 | 统一格式的大规模 MoCap 数据集，覆盖 300+ 受试者 | [Project](https://amass.is.tue.mpg.de/) |
| **Motion-X** | 13M+ 帧 | 大规模多模态运动数据（文本+语音+MoCap） | [GitHub](https://github.com/IDEA-Research/Motion-X) |
| **OmniH2O-6** | 6 种场景 | 人形全身控制数据集 | [Project](https://human2humanoid.com/) |
| **CMU MoCap** | 2605 trials | 经典运动捕捉数据库 | [Project](http://mocap.cs.cmu.edu/) |

### 14.4 学术论文列表

| 项目 | 维护者 | 特色 | 链接 |
|------|--------|------|------|
| **awesome-humanoid-robot-learning** | 社区 | 最全面的人形机器人学习论文列表 | [GitHub](https://github.com/jonyzhang2023/awesome-humanoid-robot-learning) |
| **Awesome-Humanoid-Manipulation** | 社区 | 人形操控专题论文列表 | [GitHub](https://github.com/OpenRobotLab/Awesome-Humanoid-Manipulation) |

### 14.5 模型与权重

| 模型 | 机构 | 许可证 | 特色 |
|------|------|--------|------|
| **GR00T N1** | NVIDIA | 开放权重 | 人形机器人通用基础模型 |
| **π₀** | Physical Intelligence | 研究许可 | Flow Matching VLA 基础模型 |
