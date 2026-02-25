import { defineConfig } from 'vitepress'

export default defineConfig({
  title: '人形机器人运动控制研究报告',
  description: '人形机器人运动控制完整研究报告 — 覆盖 2000–2026 年，~150 篇论文，5 大研究方向',
  lang: 'zh-CN',
  base: '/Humanoid-Robot-Control-Survey/',
  lastUpdated: false,
  cleanUrls: true,

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/Humanoid-Robot-Control-Survey/favicon.svg' }],
  ],

  markdown: {
    math: true,
  },

  themeConfig: {
    logo: '/favicon.svg',
    siteTitle: '人形机器人运动控制',

    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: '搜索', buttonAriaLabel: '搜索' },
          modal: {
            noResultsText: '未找到结果',
            resetButtonTitle: '清除搜索',
            footer: { selectText: '选择', navigateText: '导航', closeText: '关闭' },
          },
        },
      },
    },

    nav: [
      { text: '首页', link: '/' },
      {
        text: '研究方向',
        items: [
          { text: '① 通用全身控制', link: '/directions/01-whole-body-control' },
          { text: '② 人-场景交互 (HSI)', link: '/directions/02-hsi' },
          { text: '③ 人-物交互 (HOI)', link: '/directions/03-hoi' },
          { text: '④ 感知移动', link: '/directions/04-perceptive-locomotion' },
          { text: '⑤ 感知导航', link: '/directions/05-perceptive-navigation' },
        ],
      },
      { text: '生态', link: '/ecosystem/enterprises' },
      { text: '分析', link: '/analysis/tech-comparison' },
      { text: '附录', link: '/appendix' },
    ],

    sidebar: [
      {
        text: '第一部分：认知建立',
        collapsed: false,
        items: [
          { text: '执行摘要', link: '/overview/executive-summary' },
          { text: '什么是人形机器人运动控制？', link: '/overview/definition' },
          { text: '发展历程与时间线', link: '/overview/timeline' },
        ],
      },
      {
        text: '第二部分：五大研究方向',
        collapsed: false,
        items: [
          { text: '① 通用全身控制', link: '/directions/01-whole-body-control' },
          { text: '② 人-场景交互 (HSI)', link: '/directions/02-hsi' },
          { text: '③ 人-物交互 (HOI)', link: '/directions/03-hoi' },
          { text: '④ 感知移动', link: '/directions/04-perceptive-locomotion' },
          { text: '⑤ 感知导航', link: '/directions/05-perceptive-navigation' },
        ],
      },
      {
        text: '第三部分：生态与产业',
        collapsed: false,
        items: [
          { text: '全球企业与机构布局', link: '/ecosystem/enterprises' },
          { text: '开源生态全景', link: '/ecosystem/opensource' },
        ],
      },
      {
        text: '第四部分：分析与展望',
        collapsed: false,
        items: [
          { text: '技术路线对比', link: '/analysis/tech-comparison' },
          { text: '评估基准景观', link: '/analysis/benchmarks' },
          { text: '关键趋势与展望', link: '/analysis/trends' },
          { text: '结论', link: '/analysis/conclusion' },
        ],
      },
      {
        text: '附录',
        items: [
          { text: '论文与参考文献索引', link: '/appendix' },
        ],
      },
    ],

    outline: {
      level: [2, 3],
      label: '本页目录',
    },

    lastUpdated: {
      text: '最后更新',
    },

    docFooter: {
      prev: '上一篇',
      next: '下一篇',
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/jonyzhang2023/Humanoid-Robot-Control-Survey' },
    ],

    footer: {
      message: '基于 VitePress 构建',
      copyright: 'MIT License © 2026',
    },
  },
})
