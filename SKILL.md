---
name: evolution-cat-article
description: |
  进化猫公众号文章写作全流程编排。v7.0 核心变更：6 阶段管线（判→搜→构→写→审→发）、单人设（进化猫）、血肉优先骨架兜底、三道杀稿门禁统一收归 skeleton/kill-gate.md。

  触发：写进化猫文章、写公众号文章、进化猫选题写作、把选题写成文章。
  也匹配含"进化猫"+"写"的任意表达。

  **触发互斥：**
  - 用户说"进化猫"+"写"→ 触发本 Skill
  - 用户说"文章""长文""公众号""写一篇""2000字"（未指定人设）→ 默认触发本 Skill
  - 用户说"多人设""多角色""换个风格""用XX人设写"→ 触发 persona-article（多人设）
  - 用户说"图文""小绿书""信息图""卡片""1080×1440"→ 触发 evolution-cat-infographic
  - 用户说"写作方向""研究写作"→ 追问：进化猫单人设/多人设/图文？

  Do NOT trigger when: 指定其他人设名（走 persona-article）、小绿书/图文（走 infographic）、通用写作建议、非进化猫品牌。
---

# 进化猫文章写作 · 6 阶段管线

> v7.0 — 单人设，6 阶段，三道门禁。血肉优先，骨架兜底。

## 加载优先级

```
血肉 → 骨架
冲突：血肉覆盖骨架
空白：骨架填补血肉未覆盖的部分
```

写作者唯一：**进化猫**。所有风格决策先查 flesh/ 层，找不到再走 skeleton/ 层。

---

## 架构

```
references/
├── skeleton/            ← 骨架层：通用写作工程规则，不可通过 retro 修改
│   ├── kill-gate.md        ← 三道杀稿门禁（统一收归）
│   ├── writing-craft.md    ← 22 个通用写作技法 + AI 角色边界 + 四层质检体系
│   ├── reader-contract.md  ← 读者契约：8 类型 + 选型决策
│   ├── fact-check.md       ← 事实校验铁律
│   ├── density-gate.md     ← 禁止词库 + 信息密度 + 开头硬门禁
│   └── source-trace.md     ← 6 维度搜索 + 素材包
├── flesh/               ← 血肉层：进化猫个人风格，仅通过 retro 写入
│   ├── voice-signals.md    ← 15 维风格指纹（≤20 条信号）
│   ├── hard-preferences.md ← 硬偏好（≤5 条）
│   ├── avoid-list.md          ← 个人回避模式（≤15 条）
│   ├── colloquial-phrases.md   ← 进化猫个人口语词组库
│   ├── opening-patterns.md     ← 四种开头模式 + 禁止开头
│   ├── closing-patterns.md     ← 五种结尾模式 + 禁止结尾
│   ├── topic-taxonomy.md       ← 内容基因分类库（5 类型）
│   ├── time-consistency.md     ← 相对时间校验
│   └── writing-patterns.md     ← 写作模式库（每类怎么写的 6 维定义）
├── humanizer-zh.md      ← 去 AI 味（24 通用模式 + 进化猫特定禁止词 + 口语词组库）
├── formatting-convention.md ← 排版工匠 markdown 格式规范
├── image-generation.md  ← 配图生成
└── production-sop.md    ← 6 阶段生产指令
```

---

## 6 阶段管线

```
判 → 搜 → 构 → 写 → 审 → 发
 │      │                │
杀稿   杀稿             杀稿
```

| 阶段 | 做什么 | 加载骨架 | 加载血肉 | 门禁 |
|------|--------|---------|---------|------|
| **判** | 选题判断 + 内容分类 | kill-gate.md | topic-taxonomy.md | 第一道：3🔴→杀 |
| **搜** | 深度搜索 + 素材包 | source-trace.md + fact-check.md | — | 第二道：0意外→杀 |
| **构** | 结构构思 + 创意简报 | reader-contract.md | writing-patterns.md | — |
| **写** | 执行写作 | writing-craft.md + density-gate.md | voice-signals.md + opening/closing-patterns.md | — |
| **审** | F0 事实复核 + 质检（L1-L4）+ 平台合规复核 + 平台合规终审 | humanizer-zh.md + fact-check.md + kill-gate.md §三/§五 | avoid-list.md + colloquial-phrases.md + voice-signals.md(L4) | F0：❌→硬阻断；第三道：L4 FAIL→杀；平台合规终审 🔴→杀 |
| **发** | 输出：配图 + 排版 + Forma 预览 | formatting-convention.md | image-generation.md | — |

### 轻/重分流

同一条管线，参数控制：

- **--light**：判同、搜同、构缩减为选结构模板、写轻量化（1000-2000字）、审缩减为 L1+L4 快扫、发同
- **--deep**：全阶段展开（2000-5000 字）

路由：Step 判 时 Agent 自行评估深度潜力（跨领域连接/可展开理论框架/反直觉对比，≥2 条即判深度），告知用户后走对应参数。

---

## 阶段一：判 — 选题判断

```
>> 读取 flesh/topic-taxonomy.md
>> 读选题。判定内容基因 → 路由（--light / --deep）

>> 读取 skeleton/kill-gate.md §一
>> 运行第一道门禁（四问）：
   ① 认知税：≥3 🔴 | 2 🟡 | 0-1 🟢
   ② 洞察值："操原来可以这样"🟢 | "有点意思"🟡 | "嗯我知道"🔴
   ③ 分享货币：标榜🟢 | 有用🟡 | 讲不清🔴
   ④ 平台合规：任一🔴 → 杀或重定角度

判定：
  0🔴 → 过
  1🔴 → 过，写作时针对性补强
  2🔴 → 退回，重新找角度
  3+🔴 → 🔴 杀
  ④任一🔴 → 🔴 杀或重定角度
```

---

## 阶段二：搜 — 深度搜索

```
>> 读取 skeleton/source-trace.md
>> 6 维度搜索 + AI 透镜 + 素材包落盘

>> 读取 skeleton/kill-gate.md §二
>> 运行第二道门禁（意外发现）：
   至少 1 个意外发现来自一手来源 → 🟢 过
   0 意外发现 → 🔴 杀（或退回换方向重搜）
```

---

## 阶段三：构 — 结构构思

```
>> 读取 skeleton/reader-contract.md
>> 基于意外发现声明读者契约（8 类型选 1-2）

>> 读取 flesh/writing-patterns.md
>> 按文章类型加载对应的 6 维写作模式

>> 输出 creative-brief：
   - 核心契约 + 意外发现
   - 递进链（3-5 段）
   - 舍弃清单（≥2 项明确不写的内容）
   - 翻牌点（核心意外揭露位置）
   - 贯穿反派（全文共享的力）
```

---

## 阶段四：写 — 执行写作

```
>> 读取 skeleton/writing-craft.md + density-gate.md
>> 读取 flesh/voice-signals.md + opening-patterns.md + closing-patterns.md

写作时即遵守 formatting-convention.md 排版规范，不事后补。

输出：
  - 全文 markdown
  - 3 个标题候选
  - 事实核查（搜索驱动，非推理）
```

---

## 阶段五：审 — 质量检查

```
>> 读取 humanizer-zh.md（24 通用模式 + 进化猫特定禁止词 + 口语词组库）
>> 读取 flesh/avoid-list.md
>> 读取 skeleton/fact-check.md

F0 事实复核（L1 之前必须先过）：
  从 draft-v1.md 逐条提取事实断言 → WebFetch 一手来源核验
  → ✅一手验证 / ⚠️二手佐证 / ❌无法验证/事实错误
  → ❌ → 硬阻断，修正后重过 F0

L1 硬性规则扫描 → L2 风格一致性检查 → L3 内容质量审查 → L4 活人感终审

>> 读取 skeleton/kill-gate.md §三/§四
>> 运行 F0 事实门禁 + 第三道门禁（编辑判断）：
   F0 ALL PASS → 进入 L1
   F0 ❌ → 🔴 硬阻断（不给退回，必须修正事实）
   L4 全部 PASS → 🟢 过
   L4 FAIL → 🔴 杀或退回重写（最多一次）
   Signal/Noise FAIL → 🔴 杀（不给退回）
   上帝之声 FAIL → 🔴 杀（不给退回）
```

---

## 阶段六：发 — 输出发布

```
>> 配图生成（封面 + ≥2 张配图，--light 封面 1 张即可）
>> Forma 排版推送 + 预览打开
>> 终稿落盘
```

---

## 输出路径

所有产物落盘到 `D:\workspace\_output\evolution-cat\文章\{YYYYMMDD}_{标题}\`。

写文件前先查重：扫描 `D:\workspace\_output\evolution-cat\文章\` 下是否存在当天日期 + 同主题目录。

---

## Forma 排版预览

> 阶段六自动执行。

- 端口：`3100`
- 项目路径：`D:\workspace\forma-typesetting`
- 主题：`evolution-cat`
- 预览 URL：`http://localhost:3100/view/{slug}`

流程：检查端口 → 未启动则启动 → POST markdown 到 `/api/save` → 拷贝图片 → 打开浏览器预览。

---

## 血肉生长机制

```
写完一篇文章
  ↓
向用户提问（≥3 个：一个关于声音、一个关于禁区边界、一个关于结构偏好）
  ↓
用户回答 → 写入对应 flesh/ 文件
  ↓
下一篇自动生效
```

---

## 约束红线

| # | 红线 |
|---|------|
| 1 | 禁止虚假链接和死链 |
| 2 | 禁止标注"待确认"后发布 |
| 3 | 禁止编造第一人称体验 |
| 4 | AI 高频词命中 = 0 |
| 5 | 术语首次出现：类比在前术语在后 |
| 6 | 第一道门禁 3+ 🔴 → 必须杀稿 |
| 7 | 第二道门禁 0 意外 → 必须杀稿 |
| 8 | 第三道门禁 L4 FAIL → 必须杀稿 |
| 9 | 平台合规 ④ 任一 🔴 → 必须杀或重定角度 |
| 10 | 标题门禁：标题必须是标题（不是主题标签），必须符合 writing-patterns.md 公式，3 候选至少 1 个全 PASS |
| 11 | retro 回流只能写入 flesh/，不能改 skeleton/ |
| 12 | 用户指任一问题 → 全文扫同类 |
| 13 | 选题无法分类 → 必须问用户，不猜测 |
| 14 | 门禁结果必须文件化：gate-1-result.md / gate-3-result.md 缺失 → 阶段六硬阻断 |
| 15 | forma-deploy.json 缺失 → 阶段六未完成，不得宣布发文结束 |
| 16 | F0 事实复核 ❌ → 硬阻断，不得进入 L1-L4。事实错误必须修正，无法验证必须删除 |

---

## 完成标志

- [ ] md 文件已保存
- [ ] 封面图 ≥1（--deep 配图 ≥2）
- [ ] AI 高频词 0 命中
- [ ] 三道门禁 + F0 事实门禁 + 标题门禁全部 PASS（gate-1-result.md + fact-verification.md + gate-3-result.md 落盘）
- [ ] 平台合规三道检查全部 PASS（粗筛 gate-1 + 复核 gate-3 + 终审 gate-3）
- [ ] 最终标题不是主题标签，符合 writing-patterns.md 公式
- [ ] forma-deploy.json 落盘（apiVerified=true）
- [ ] `这里是进化猫，陪你一起看世界✨` 结尾
- [ ] Forma 预览已推送 + 浏览器已打开

---

## 诚实边界

- **设计截止 2026-06-18**。v7.0 核心变更：6 阶段管线、单人设（进化猫）、血肉优先骨架兜底、三道门禁统一收归、22 技法骨架化。
- **实战验证有限**：v7.0 尚未跑过完整文章
- 骨架层开源后别人直接用；血肉层从已有文章提取 + 每篇写完生长
- 门禁判断质量取决于 agent 对规则的执行力度
- **平台合规裁判常识盲区**：agent 领域知识限于训练数据。边缘案例应标 🔴 安全侧，不赌。
- **自评盲区**：同一模型创作+质检存在模式自噬风险——AI 倾向给 AI 文本打高分。当前缓解：L1 硬性扫描由 spawn 子 agent 独立执行（阶段五），L1 不受此盲区影响；L4 主观判断仍可能偏松。
