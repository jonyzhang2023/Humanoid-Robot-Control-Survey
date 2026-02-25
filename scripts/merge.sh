#!/bin/bash
# 将多个 VitePress 内容页面合并为单文件完整版报告
# 用法: npm run merge

set -e
cd "$(dirname "$0")/.."

OUTPUT="人形机器人运动控制完整研究报告.md"

# 写入报告头
cat > "$OUTPUT" << 'HEADER'
# 人形机器人运动控制完整研究报告

> **版本**：v2.0 · **更新日期**：2026 年 2 月 25 日
> **覆盖范围**：2000–2026 年 2 月 · **收录论文**：~150 篇
> **更新频率**：每月一次 · **下次计划更新**：2026 年 3 月
> **数据来源**：arXiv、顶会论文（RSS / CoRL / ICRA / Humanoids / SIGGRAPH / ICLR / CVPR）、GitHub、企业技术博客

---

HEADER

# 定义页面列表（按报告顺序）
PAGES=(
  "docs/overview/executive-summary.md"
  "docs/overview/definition.md"
  "docs/overview/timeline.md"
  "docs/directions/01-whole-body-control.md"
  "docs/directions/02-hsi.md"
  "docs/directions/03-hoi.md"
  "docs/directions/04-perceptive-locomotion.md"
  "docs/directions/05-perceptive-navigation.md"
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
