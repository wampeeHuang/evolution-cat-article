# 生产指令

> v7.0 — 6 阶段管线，单人设，三道门禁。血肉优先骨架兜底。

---

## 加载规则

```
加载顺序：血肉 → 骨架
冲突裁决：血肉覆盖骨架
空白填补：骨架填补血肉未覆盖的部分
```

写作者唯一：**进化猫**。所有风格决策先查 flesh/ 层，找不到再走 skeleton/ 层。

---

## 输入

飞书选题（状态=`已入选`）或用户直接抛（疑问/链接/一句话想法）。

无选题 → 终止，提示用户提供。

---

## 输出

所有产物落盘到 `D:\workspace\_output\evolution-cat\文章\{YYYYMMDD}_{标题}\`：

- md 文件 + 封面图 ≥1 + 配图 ≥2（--light 封面 1 张即可）
- 字数：--deep 2000-5000，--light 1000-2000
- **写文件前先查重**：扫描 `D:\workspace\_output\evolution-cat\文章\` 下当天日期+同主题已有目录（关键词模糊匹配），存在则复用，不新建。

---

## 读者恒定画像

| 维度 | 定义 |
|------|------|
| 身份 | 会使用 AI 产品的互联网人（非工程师） |
| 技术基线 | 知道 Token、API、开源大概是什么；不理解协议、框架 |
| 阅读场景 | 微信公众号 + 手机竖屏，碎片时间 |
| 弃读原因 | 连续两个自然段看不懂 → 划走 |

每句话落笔前自问：一个午休刷手机看到这句话的人，能一眼看懂吗？

---

## 阶段一：判 — 选题判断

```
>> 读取 flesh/topic-taxonomy.md
>> 读选题。判定内容基因：

    置信度 ≥ 0.8 → 直接路由
    置信度 0.5-0.8 → 报 Top 2 候选 → 问用户
    置信度 < 0.5 或完全陌生 → 报未知 + 建议新分类 → 用户确认 → 写入 taxonomy

分类 → 对应管线：
  🛠️ 推荐流 → --light
  📖 复盘流 → --light
  📡 快评流 → --light
  🎯 主张流 → --light（证据链深但结构轻）
  🏗️ 深度流 → --deep（三个条件缺一不可：Agent 判定深度潜力 + ≥2 个意外 + ≥3 个子论点）

>> 读取 skeleton/kill-gate.md §一
>> 运行第一道门禁（四问）：
   ① 认知税：≥3 🔴 | 2 🟡 | 0-1 🟢
   ② 洞察值："操原来可以这样"🟢 | "有点意思"🟡 | "嗯我知道"🔴
   ③ 分享货币：标榜🟢 | 有用🟡 | 讲不清🔴
   ④ 平台合规

判定：0🔴 → 过 | 1🔴 → 过，写作时补强 | 2🔴 → 退回 | 3+🔴 → 🔴 杀 | ④任一🔴 → 🔴 杀或重定角度

路由：默认 --light。Agent 自行评估深度潜力（跨领域连接/可展开理论框架/反直觉对比，≥2 条即判深度），告知用户后走对应参数。

>> 输出 _runtime/gate-1-result.md：
   - 四问逐项判定（🔴/🟡/🟢 + 一句话理由）
   - 总红灯数 + 最终判定（过/退回/杀）
   - 若 1🔴：标注补强方向
   - 若 🔴 杀：touch _runtime/.abandoned，写入杀稿原因，流程终止
```

---

## 阶段二：搜 — 深度搜索

```
>> 读取 skeleton/source-trace.md + fact-check.md

>> AI 透镜前置（搜索前必读）：
   这是进化猫账号 DNA——每篇文章透过 AI 透镜过滤。
   动手搜索前自问：
   ① 这个领域/方法论/事件，对 AI 用户意味着什么？
   ② AI 工具/行为在这里改变了什么？
   ③ 原领域专家如何看待 AI 对该领域的冲击？

>> 6 维度并行搜索（source-trace.md §一），每个维度追加 AI 变体搜索词
   - 第 6 维度（跨领域类比）输出必须含 ≥1 个 AI 用户行为类比
>> 每个数字从源头核实（fact-check.md §四）
>> 如文章涉及产品/价格对比，运行对比公平性校验（fact-check.md §三）：同档对齐、时效性、地域可用性、极值不单独引、口径一致
>> 输出素材包 → _runtime/article-source-pack.md

>> 读完整素材包，提炼意外发现：
   ① 有没有哪个事实让我停下来想了超过 3 秒？
   ② 有没有哪个数据跟我之前的假设对不上？
   ③ 有没有哪个类比让我觉得"操，原来可以这样想"？
>> 意外发现写入 _runtime/surprise-findings.md（3-5 条），每条引用素材包行号

>> 读取 skeleton/kill-gate.md §二
>> 🚪 第二道门禁：
   至少 1 个意外发现来自一手来源 → 🟢 过
   0 意外发现 → 🔴 杀。touch .abandoned，写入原因。
```

---

## 阶段三：构 — 结构构思

```
>> 前置：article-source-pack.md + surprise-findings.md 存在
>> 读取 skeleton/reader-contract.md
>> 读取 flesh/writing-patterns.md

>> 输出 _runtime/creative-brief.md，6 字段必填：

   ① 意外发现（≥3 条，每条引用素材）
   ② 读者契约（8 类型选 ≤2 种混合，选型理由引用 ≥2 条素材信息）
   ③ 递进链（section 流程图，每 section 标注回答契约哪一层问题）
   ④ 舍弃清单（≥3 项，每项说明为什么舍弃——这是收集→过滤模式切换的关键动作）
   ⑤ 翻牌点（在哪 section 揭示最大意外，标注翻牌 section + 误导预期 + 真相）
   ⑥ 一句话核心（≤30 字，不含"和""与""以及"）

🚪 门禁：6 项全 PASS → 阶段四。任一项 FAIL → 退回补全。
```

---

## 阶段四：写 — 执行写作

```
>> 前置：creative-brief.md 锁定 + 素材包 + 意外发现 存在
>> 读取 skeleton/writing-craft.md + density-gate.md
>> 读取 flesh/voice-signals.md + opening-patterns.md + closing-patterns.md

写作指令：
  - 严格按 creative-brief ③ 递进链组织 section
  - 在 creative-brief ⑤ 指定的翻牌点揭示最大意外
  - creative-brief ④ 舍弃清单的内容——不写进正文
  - 开头按 opening-patterns.md 选最合的模式
  - 结尾按 closing-patterns.md 选最合的模式
  - 写作技法按 writing-craft.md §二 执行
  - 禁止词库按 density-gate.md §五 + humanizer-zh.md 进化猫特定禁止词 避开
  - 术语降维：类比在前术语在后
  - 用"你"直接跟读者对话
  - 文末：参考来源 + 这里是进化猫，陪你一起看世界✨
  - 同时输出 3 个标题候选

🚪 标题门禁（输出 title-candidates.md 前自检，FAIL 不得进入阶段五）：

  ① 公式匹配：标题符合 writing-patterns.md 当前类型的标题公式吗？
     不符 → FAIL。不是"不够好"，是"类型不对"

  ② 主题标签检测：这个标题是文章的文件名还是文章的标题？
     如果标题只是主题标签（读者看不出读完能带走什么）→ FAIL
     例："中美AI角色互换" → FAIL（知道主题，不知道观点）
     例："中美AI差距只剩2.7%——但你猜错了追上来的方式" → PASS（知道结论方向+有信息缺口）

  ③ 三问诚实：
     a. 标题承诺正文能兑现吗？不能 → FAIL
     b. 标题中的数字/断言可追溯吗？不能 → FAIL
     c. 读完标题+开头能猜出全文结论吗？能 → FAIL（标题剧透=读者不用往下读了）

  ④ 3 个候选至少 1 个 ①②③ 全 PASS → 过，否则退回重写标题

写作时即遵守 formatting-convention.md，不事后补排版。

输出：
  - _runtime/draft-v1.md
  - _runtime/title-candidates.md

>> 事实核查（搜索驱动，非推理）：
   逐条搜索核查草稿中的数字/日期/研究结论/专有名词
   不确定的标注「单一来源，未交叉验证」
   不在素材包里但草稿中断言的 → 额外搜索验证
```

---

## 阶段五：审 — 质量检查

```
>> 前置：draft-v1.md + title-candidates.md + 素材包 存在
>> 读取 humanizer-zh.md（24 通用模式 + 通用中文口语词库）
>> 读取 flesh/avoid-list.md + flesh/colloquial-phrases.md
>> 读取 skeleton/fact-check.md

F0 事实复核（L1-L4 之前必须先过）：
  从 draft-v1.md 逐条提取事实断言（数字/日期/研究结论/专有名词/产品名称），写入核查表。
  每条断言用 WebFetch 抓取一手来源页面核验，不用 WebSearch 摘要替代。
  不能抓取的（付费墙/404）→ 至少 2 个独立二手来源交叉验证，否则标注"无法验证"。

  核查结果分三级标注：
    ✅ 一手验证 — WebFetch 直接命中官方页面，数字一致
    ⚠️ 二手佐证 — 一手源不可访问，≥2 个独立二手来源交叉一致
    ❌ 无法验证 / 事实错误 — 找不到来源 / 数字与来源不符

  判定标准：
    ❌ 事实错误 → 必须修正后重过 F0
    ❌ 无法验证 → 必须删除该断言或替换为可验证的
    ⚠️ 二手佐证 → 可保留，但必须在正文中标注来源局限性（如"据XX报道""XX自报，未经第三方审计"）
    全部 ✅ + ⚠️（已标注）→ F0 PASS

  核查过程中发现的数字修正，同步更新 draft-v1.md。
  输出 _runtime/fact-verification.md（每条的断言原文 + 核查方法 + 来源 URL + 分级 + 修正动作）。

  🚪 F0 门禁：
    ALL PASS（无 ❌）→ 进入 L1
    有 ❌ → 硬阻断。修正后重新过 F0，不过不进入 L1。

四层质检（详见 writing-craft.md §四）：

L1 硬性规则：
  - 禁止词扫描（骨架 density-gate.md §五 + flesh/avoid-list.md 合并扫描）
  - 禁止标点扫描（按 flesh/hard-preferences.md 个人标点规则）
  - 结构套话扫描
  - 空泛名称扫描
  标准：零命中。

L2 风格一致性：
  - 开头检查（是否具体事件/场景切入）
  - 长短句交替
  - 断裂效果（一句话独立成段，≥3 次）
  - 扣主线句
  - 知识输出是否聊天式

L3 内容质量：
  - 观点是否有具体支撑
  - 是否至少一处文化升维
  - 是否有对立面的理解和承认
  - 创意案例是否包装成微型故事

L4 活人感：
  核心问题：读起来像活人写的吗？
  两个一票否决项：
    Signal/Noise：0-signal 句 ≥3 处 → FAIL
    上帝之声："值得注意的是""毋庸置疑""众所周知" ≥2 处 → FAIL

>> 标题裁定（阶段四标题门禁已过滤，此处终审）：
   从 title-candidates.md 中 Pick 最优。
   确认被选标题已写入 draft-v2.md 的第一行（# 标题）。
   如果 draft-v2.md 仍用主题标签而非已选标题 → 硬阻断，不得进入 gate-3。

>> 写入 draft-v2.md

>> 🚪 前置：_runtime/fact-verification.md 存在且 ALL PASS
   缺失或 FAIL → 硬阻断。F0 事实复核未通过，不得进入 L1-L4。

>> 读取 skeleton/kill-gate.md §三
>> 🚪 第三道门禁：
   F0 事实复核 PASS + L4 全部 PASS → 🟢 过
   F0 FAIL → 🔴 硬阻断（不给退回，必须修正事实）
   L4 FAIL → 🔴 杀或退回重写（最多一次）
   Signal/Noise FAIL → 🔴 杀（不给退回）
   上帝之声 FAIL → 🔴 杀（不给退回）

>> 读取 skeleton/kill-gate.md §四
>> 平台合规复核（kill-gate.md §四·复核）：
   - 文中数字/断言是否有公开来源可追溯？
   - AI能力声明是否夸大？（对照素材包逐条核验）
   - 反向映射：文中每个事实声明 → 素材包来源
   - 任一 🔴 → 修复后重审

>> 平台合规终审（kill-gate.md §四·终审）：
   - 标题承诺是否兑现？（标题党终审）
   - 引用内容是否侵权？
   - 有无诱导分享措辞？
   - 任一 🔴 → 杀或重定角度

>> 字数检查

>> spawn 子 agent 独立 L1 扫描：
   子 agent 加载 humanizer-zh.md + flesh/avoid-list.md + skeleton/density-gate.md
   独立扫描 draft-v1.md，输出 _runtime/independent-l1-scan.md
   主 agent L1 结果与子 agent 对比 → 不一致项标注 "主/子判定冲突，人工裁定"

>> 输出 _runtime/gate-3-result.md：
   - F0 事实复核结果（核查条数 / ✅ 条数 / ⚠️ 条数 / ❌ 条数 / 修正动作）
   - L4 四个感知维度逐项判定（温度感/独特性/姿态/心流）
   - Signal/Noise 扫描结果（0-signal 句数 + 行号）
   - 上帝之声扫描结果（命中数 + 行号）
   - 标题裁定结果
   - 平台合规复核结果（数字可追溯 / AI声明核实 / 反向映射）
   - 平台合规终审结果（标题党 / 侵权 / 诱导分享）
   - 最终判定（PASS / FAIL+退回 / FAIL+杀）
   - 若 🔴 杀：touch _runtime/.abandoned，写入杀稿原因
```

---

## 阶段六：发 — 输出发布

```
>> 🚪 前置检查（硬阻断）：
   - _runtime/gate-1-result.md 存在且 PASS（含平台合规粗筛）
   - _runtime/gate-3-result.md 存在且 PASS（含平台合规复核 + 平台合规终审）
   - _runtime/draft-v2.md 存在
   任一缺失 → 硬阻断：门禁未执行，退回阶段一/五
   任一 FAIL（含平台合规 🔴）→ 硬阻断：门禁不通过，不得发布

>> 配图生成：
   读取 image-generation.md
   封面：900×383，不写标题文字
   配图 ≥2（--light 封面 1 张即可）

>> 终稿落盘：_runtime/draft-v2.md → ../{标题}.md

>> Forma 排版推送（不可跳过）：

   1. 检查 Forma 运行：curl http://localhost:3100/api/status → 200 则跳过
      未运行 → cd D:\workspace\forma-typesetting && npm run dev
      等待 /api/status 返回 200（轮询至多 15s）

   2. 推送文章：
      POST http://localhost:3100/api/save
      body: { markdown, slug, displayName, theme: "evolution-cat" }
      slug = 标题转拼音连字符
      → 保存响应到 _runtime/forma-deploy.json

   3. 拷贝图片：cp images/ → public/previews/{slug}/images/

   4. 验证就绪：
      curl http://localhost:3100/api/v1/articles?slug={slug} → 200
      curl http://localhost:3100/api/article-images?slug={slug}&path=images/cover.png → 200
      → 验证结果写入 _runtime/forma-deploy.json

   5. 写入 forma-deploy.json 最终内容：
      { slug, url, displayName, deployedAt, apiVerified, imageVerified }

   6. 打开预览：http://localhost:3100/view/{slug}

>> 🚪 后置检查（硬阻断）：
   _runtime/forma-deploy.json 存在且 apiVerified=true
   缺失 → Forma 推送未完成，阶段六未结束
```

---

## --light 模式

触发：阶段一路由到轻输出 OR 用户说"简单写""不用太深"。

| 阶段 | --deep | --light |
|------|--------|---------|
| 判 | 分类+第一道门禁 | **同** |
| 搜 | 6维搜索+第二道门禁 | **同**（搜索不缩水，0意外→杀） |
| 构 | creative-brief 6字段 | creative-brief 缩减（舍弃清单 ≥2 项即可） |
| 写 | 全文 2000-5000字 | 全文 1000-2000字，轻量化 |
| 审 | L1-L4 完整质检 + 第三道门禁 | L1 + L4 快扫 |
| 发 | 配图 ≥2 + Forma | 封面 1 张 + Forma |

---

## 复盘

发布完成后自动触发。

```
>> 通读终稿，诊断最弱的 3 个点
>> 向用户提 ≥3 个问题：
   一个关于声音（哪段最像/最不像自己）
   一个关于禁区边界（哪句踩线或差点踩线）
   一个关于结构偏好（开头/结尾/递进哪个最不舒服）
>> 提取的风格信号写入 flesh/voice-signals.md（单次最多 3 条新增、2 条修改）
>> 用户随时喊停
```

**复盘只能写入 `flesh/`，不能改 `skeleton/`。**

---

## 全流程禁则

- ❌ 文件写 home 目录或盘符根目录
- ❌ 数据不核实就进分析
- ❌ 伪造第一人称体验
- ❌ 门禁不通过强行推进
- ❌ retro 回流写入 skeleton/
- ❌ 深度流缺任一条件还强行走深度
- ❌ 第三道门禁 FAIL 不杀稿或不退回
- ❌ 平台合规 🔴 强行继续
- ❌ 跳过 Forma 推送（forma-deploy.json 缺失 = 阶段六未完成）
- ❌ 标题承诺正文无法兑现仍发布

---

## 迭代方式

| 要改什么 | 改哪里 |
|---------|-------|
| 杀稿三道门禁 | skeleton/kill-gate.md |
| 写作技法 + 质检体系 | skeleton/writing-craft.md |
| 事实校验规则 | skeleton/fact-check.md |
| 读者契约/文章类型 | skeleton/reader-contract.md |
| 搜索维度/素材包 | skeleton/source-trace.md |
| 禁止词库 | skeleton/density-gate.md |
| 去 AI 味 | humanizer-zh.md |
| 通用口语词组 | humanizer-zh.md §通用中文口语词库 |
| 进化猫口语词组 | flesh/colloquial-phrases.md |
| 内容分类库 | flesh/topic-taxonomy.md |
| 开头/结尾模式 | flesh/opening-patterns.md / closing-patterns.md |
| 风格信号/硬偏好/回避 | flesh/voice-signals.md / hard-preferences.md / avoid-list.md |
| 写作模式（6维定义） | flesh/writing-patterns.md |
| 配图 | image-generation.md |
| 排版格式 | formatting-convention.md |
