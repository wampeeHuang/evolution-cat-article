# evolution-cat-article · 10 维度逐项评分

> 审计日期: 2026-06-18
> 框架自检状态: ⚠️ skill-craftsmanship-framework 自检文件时间戳(2026-05-20)早于 SKILL.md(2026-05-21)，本次评估可靠性降低
> 复杂度: 完整模式（6 阶段 SOP + 16 个 reference 文件）

---

## 维度 1: 触发精准度 ★★☆

**证据**:
- description L6-8: 触发词列表具体（"写进化猫文章、写公众号文章、进化猫选题写作、把选题写成文章"）
- description L7: "也匹配含'进化猫'+'写'的任意表达" [逻辑推演] 过于宽泛——聊天中提到"进化猫写的XX"也会误触发
- description L11-12: 触发互斥声明完整，与 infographic 边界清晰
- description L13: "Do NOT trigger when" 具体可操作

**为什么不是 ★★★**: "含'进化猫'+'写'的任意表达"是 broad catch-all，缺少负面测试案例。用户闲聊中提到进化猫可能误触发。

**为什么不是 ★☆☆**: 触发互斥声明是同类 skill 中少见的完整——三个互斥分支 + "追问"降级路由。

---

## 维度 2: 信息架构 ★★☆

**证据**:
- SKILL.md 203 行，production-sop.md 322 行
- 三层分离明确: SKILL.md(概览) → production-sop.md(执行) → references/(细则)
- SKILL.md L67-76 与 production-sop.md L50-107 存在显著内容重复——6 阶段表格 + 每阶段加载说明在两处均完整出现
- SKILL.md L88-108 的阶段详情与 production-sop.md L50-175 的阶段详情重复度 > 50%

**为什么不是 ★★★**: SKILL.md 和 production-sop.md 之间的内容重复违反 DRY。任一文件修改时另一文件可能漂移。SKILL.md 可以再压缩 40-50 行。

**为什么不是 ★☆☆**: 三层架构方向正确，skeleton/flesh 分离清晰，按需加载机制在 production-sop 中明确标注。

---

## 维度 3: 验证体系 ★★☆

**证据**:
- kill-gate.md L9-14: 三道门禁 + 判定标准清晰
- writing-craft.md L175-211: L1-L4 四层质检，每层有 PASS 标准
- 缺少独立验证机制——写作、质检、门禁全由同一 agent 执行 [逻辑推演]
- SKILL.md 目录下无 `references/self-audit.md`（技能自身的独立审计记录）
- production-sop.md L273-285: 复盘机制提供人工反馈回路，但依赖用户主动参与

**为什么不是 ★★★**: 无独立于创作者的验证。同一 agent 写文章、质检、判门禁。复盘是唯一的外部验证但非结构化。

**为什么不是 ★☆☆**: 三道门禁 + 四层质检的 PASS/FAIL 标准具体可操作。L4 的两个一票否决项（Signal/Noise + 上帝之声）是可客观扫描的。

---

## 维度 4: 用户视角设计 ★★☆

**证据**:
- description L10-12: 入口反映用户意图（"写文章""公众号""长文"→ 触发），非内部结构暴露
- SKILL.md L80-84: --light/--deep 参数控制行为差异
- 用户无法直接控制深度——"写一篇公众号文章"可能产出 1000 或 5000 字，完全由 agent 在阶段一自行判定 [逻辑推演]
- SKILL.md L85: "Agent 自行评估深度潜力...告知用户后走对应参数"——用户被告知但未经同意
- evolution-cat-writer → evolution-cat-article --light 的路由增加了一层间接性

**为什么不是 ★★★**: 用户对深度无直接控制权。Agent 单方面决定 --deep 还是 --light，用户只能被告知。这与"用户意图驱动"的设计原则有差距。

**为什么不是 ★☆☆**: 入口是自然语言而非 CRUD 式指令。参数化行为差异存在。互斥声明保护用户不被错误路由。

---

## 维度 5: 诚实边界 ★★★

**证据**:
- SKILL.md L257-261: 5 条具体局限
- L257: "设计截止 2026-06-18"——明确时间锚点
- L258: "实战验证有限：v7.0 尚未跑过完整文章"——直接承认验证不足
- L260: "门禁判断质量取决于 agent 对规则的执行力度"——承认系统依赖性
- L261: "平台合规裁判常识盲区...边缘案例应标 🔴 安全侧，不赌"——给出决策原则
- description L13: "Do NOT trigger when" = 不适用场景
- production-sop.md L291-301: 全流程禁则（9 条）明确标注禁止行为

**为什么不是 ★★★**: 已达到。5 条具体局限 + 截止日期 + 不适用场景 + 安全侧决策原则。

---

## 维度 6: 产物自包含 ★★☆

**证据**:
- 所有 reference 文件均在 skill 目录内，组织清晰（skeleton/ flesh/ 子目录）
- production-sop.md L30: 输出路径 `D:/HHH/自媒体/进化猫/AI/{YYYYMMDD}_{标题}/`——硬编码绝对路径
- production-sop.md L239: Forma 路径 `D:\Claude code_workspace\2026-05-29-排版工匠\forma`——外部硬依赖
- image-generation.md L15-16: gpt-image-2 API + 即梦网页版——外部服务依赖
- image-generation.md L107-111: GitHub raw 文件引用——外部网络依赖
- 适用条件: 纯个人使用 → ★★☆ 可接受

**为什么不是 ★★★**: 三个硬外部依赖（Forma 项目、图片 API、GitHub 图库）。无法复制到另一台机器直接使用。

**为什么不是 ★☆☆**: 技能内部文件自包含，依赖均已文档化。换电脑时知道缺什么。

---

## 维度 7: 表达一致性 ★★★

**证据**:
- humanizer-zh.md L69-80: 24 种 AI 模式，每种有禁用词 + 改写前后对比（反例）
- humanizer-zh.md L466-481: 进化猫特定禁止词表，10 条，每条有原因 + 替代
- density-gate.md L56-68: 骨架禁止词库，🔴绝对禁止 8 条 + 🟡谨慎使用 3 条
- flesh/avoid-list.md: 7 条个人回避模式，每条有原因 + 反例
- opening-patterns.md: 4 种模式，每种有检验标准（可验证）
- closing-patterns.md: 5 种模式，每种有检验标准（可验证）
- voice-signals.md: 15 条信号，每条有具体 pattern + 检验标准

**为什么不是 ★★★**: 已达到。风格规则密集、可验证、每条有反例。禁止词有替代方案，开头/结尾有具体检验标准。

---

## 维度 8: 迭代纪律 ★★☆

**证据**:
- production-sop.md L273-285: 复盘机制——每篇写完问 ≥3 个问题
- voice-signals.md L19-25: 驱逐规则（容量满 20→淘汰最低置信度，连续 3 篇未触发→置信度-1，归零→淘汰）
- hard-preferences.md L15-18: 容量控制（≤5 条，新晋升挤最旧）
- avoid-list.md L20-24: 容量控制（≤10 条）
- production-sop.md L287: "复盘只能写入 flesh/，不能改 skeleton/"——边界清晰
- voice-signals.md L24: "单次 retro 最多写入 3 条、修改 2 条"——单次迭代上限

**为什么不是 ★★★**: 缺少整体迭代终止条件。技能什么时候"够好了"？信号池满 20 条后持续淘汰但没有"稳定"判定。复盘依赖用户参与，用户不回答 → 技能不生长。

**为什么不是 ★☆☆**: 生长规则具体（容量上限 + 驱逐算法 + 置信度评分 + 单次写入上限），flesh/skeleton 修改边界清晰。

---

## 维度 9: 交付物链 ★★★

**证据**:
- production-sop.md L115: 阶段三 "前置：article-source-pack.md + surprise-findings.md 存在"——下游验证上游
- production-sop.md L136: 阶段四 "前置：creative-brief.md 锁定 + 素材包 + 意外发现 存在"
- production-sop.md L169: 阶段五 "前置：draft-v1.md + title-candidates.md + 素材包 存在"
- production-sop.md L96: 阶段二输出 `_runtime/article-source-pack.md` + `_runtime/surprise-findings.md`
- production-sop.md L119: 阶段三输出 `_runtime/creative-brief.md`
- production-sop.md L156-157: 阶段四输出 `_runtime/draft-v1.md` + `_runtime/title-candidates.md`
- kill-gate.md L146-154: 杀稿后动作包含 `touch .abandoned` 写入原因

**为什么不是 ★★★**: 已达到。每阶段明确输入/输出文件，下游硬阻断检查上游产出。杀稿也产生文件痕迹。

---

## 维度 10: 层层外化门禁 ★★☆

**证据**:
- kill-gate.md: 三道门禁定义完整，判定标准清晰
- production-sop.md L116: 第二道门禁输出 `surprise-findings.md`（至少 1 条意外 = PASS，0 条 = FAIL / .abandoned）
- production-sop.md L73: 第一道门禁判定（0🔴/1🔴/2🔴/3+🔴）——**无文件化产出** [逻辑推演]
- production-sop.md L212-216: 第三道门禁判定（L4 PASS/FAIL）——**无文件化产出** [逻辑推演]
- 框架红线 9: "不设无文件化的门禁"

**为什么不是 ★★★**: 三道门禁中仅第二道有文件化产出（surprise-findings.md / .abandoned）。第一道和第三道的 PASS/FAIL 判词仅存在于对话上下文。Agent 跳过门禁无法事后检测。

**为什么不是 ★☆☆**: 门禁定义本身质量高（kill-gate.md 含判定表 + 真/假意外对抗 + 杀稿示例）。第二道门禁有完整的文件化链路。
