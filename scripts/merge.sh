#!/bin/bash
# 将多个 VitePress 内容页面合并为单文件完整版报告
# 用法: npm run merge

set -e
cd "$(dirname "$0")/.."

OUTPUT="世界模型完整研究报告.md"

# 写入报告头
cat > "$OUTPUT" << 'HEADER'
# 世界模型（World Model）完整研究报告

> **版本**：v1.0 · **更新日期**：2026 年 2 月 24 日
> **覆盖范围**：1943–2026 年 2 月 · **收录论文**：~200 篇
> **更新频率**：每月一次 · **下次计划更新**：2026 年 3 月
> **数据来源**：arXiv、顶会论文（NeurIPS / ICLR / ICML / CVPR / ICCV / ECCV / RSS / CoRL）、Nature、GitHub、企业技术博客

---

HEADER

# 定义页面列表（按报告顺序）
PAGES=(
  "docs/overview/executive-summary.md"
  "docs/overview/definition.md"
  "docs/overview/timeline.md"
  "docs/directions/01-reinforcement-learning.md"
  "docs/directions/02-video-generation.md"
  "docs/directions/03-autonomous-driving.md"
  "docs/directions/04-embodied-ai.md"
  "docs/directions/05-llm.md"
  "docs/directions/06-jepa.md"
  "docs/directions/07-interactive-games.md"
  "docs/directions/08-3d-4d.md"
  "docs/directions/09-domain-specific.md"
  "docs/ecosystem/enterprises.md"
  "docs/ecosystem/opensource.md"
  "docs/analysis/tech-comparison.md"
  "docs/analysis/benchmarks.md"
  "docs/analysis/trends.md"
  "docs/analysis/conclusion.md"
  "docs/appendix.md"
)

for page in "${PAGES[@]}"; do
  if [[ -f "$page" ]]; then
    # 去掉 frontmatter (--- ... ---) 然后追加
    sed '/^---$/,/^---$/d' "$page" >> "$OUTPUT"
    echo -e "\n---\n" >> "$OUTPUT"
  else
    echo "WARNING: $page not found, skipping"
  fi
done

LINES=$(wc -l < "$OUTPUT")
echo "✅ 合并完成: $OUTPUT ($LINES 行)"
