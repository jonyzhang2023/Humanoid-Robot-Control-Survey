import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ router }) {
    if (typeof window !== 'undefined') {
      // 页面切换后初始化可排序表格
      const initSortableTables = () => {
        document.querySelectorAll('.vp-doc table').forEach((table) => {
          const thead = table.querySelector('thead')
          if (!thead || table.classList.contains('sortable-init')) return
          table.classList.add('sortable-init')
          const ths = thead.querySelectorAll('th')
          ths.forEach((th, colIdx) => {
            th.style.cursor = 'pointer'
            th.style.userSelect = 'none'
            th.title = '点击排序'
            // 添加排序指示器
            const indicator = document.createElement('span')
            indicator.className = 'sort-indicator'
            indicator.textContent = ' ⇅'
            indicator.style.opacity = '0.4'
            indicator.style.fontSize = '0.8em'
            th.appendChild(indicator)

            let asc = true
            th.addEventListener('click', () => {
              const tbody = table.querySelector('tbody')
              if (!tbody) return
              const rows = Array.from(tbody.querySelectorAll('tr'))
              rows.sort((a, b) => {
                const aText = a.children[colIdx]?.textContent?.trim() ?? ''
                const bText = b.children[colIdx]?.textContent?.trim() ?? ''
                // 尝试数字排序
                const aNum = parseFloat(aText.replace(/[^\d.\-]/g, ''))
                const bNum = parseFloat(bText.replace(/[^\d.\-]/g, ''))
                if (!isNaN(aNum) && !isNaN(bNum)) {
                  return asc ? aNum - bNum : bNum - aNum
                }
                return asc ? aText.localeCompare(bText, 'zh') : bText.localeCompare(aText, 'zh')
              })
              rows.forEach((row) => tbody.appendChild(row))
              // 重置所有指示器
              ths.forEach((h) => {
                const ind = h.querySelector('.sort-indicator')
                if (ind) { ind.textContent = ' ⇅'; ind.style.opacity = '0.4' }
              })
              indicator.textContent = asc ? ' ↑' : ' ↓'
              indicator.style.opacity = '1'
              asc = !asc
            })
          })
        })
      }

      router.onAfterRouteChanged = () => {
        setTimeout(initSortableTables, 100)
      }
      // 初始页面加载
      if (document.readyState === 'complete') {
        setTimeout(initSortableTables, 100)
      } else {
        window.addEventListener('load', () => setTimeout(initSortableTables, 100))
      }
    }
  },
} satisfies Theme
