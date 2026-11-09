# -*- coding: utf-8 -*-
"""生成网站「英语阅读」题库 reading.json。
素材来源：用户提供的 CET-4 / CET-6 真题 PDF（学习 Section A 选词填空、Section C 仔细阅读的
题型与难度）+《大学英语四六级常用词组》《英语六级-高频词汇》。全部题目为原创编写，
词组与释义取自资料，文章按「较短」要求控制在 100–180 词，难度分 CET-4 / CET-6 两档。
"""
import json, re, sys

PHRASE = []   # 词组填空（选词填空）
READING = []  # 短篇阅读选择

# ---------------------------------------------------------------- 词组填空
# 结构：一段短文用 {1}{2}... 标空；bank 为词组库（含中文释义，含干扰项）；
#       answers 为 {空号: 词组}；explain 为每空的解析（中文）。
def phrase(id, level, topic, title, passage, bank, answers, explain, glossary=None):
    PHRASE.append(dict(
        id=id, level=level, topic=topic, title=title,
        passage=passage.strip(), bank=bank, answers=answers,
        explain=explain, glossary=glossary or []
    ))

# ===== CET-4 =====
phrase(
    "pc4-1", "CET-4", "校园生活", "Starting University",
    """Many freshmen find it hard to {1} campus life in the first weeks. They must {2} a tighter budget, share a room, and plan their own time. The university has {3} a peer-mentoring programme to help. Students who {4} it say they quickly become {5} of campus resources such as the library writing centre. {6}, asking a senior for advice is often the fastest way to settle in.""",
    [
        {"key": "A", "en": "adapt to", "zh": "适应"},
        {"key": "B", "en": "cope with", "zh": "妥善处理，应对"},
        {"key": "C", "en": "set up", "zh": "建立，设立"},
        {"key": "D", "en": "take part in", "zh": "参加，参与"},
        {"key": "E", "en": "be aware of", "zh": "意识到，知道"},
        {"key": "F", "en": "above all", "zh": "首先，尤其是"},
        {"key": "G", "en": "run out of", "zh": "用完，耗尽"},
        {"key": "H", "en": "bring about", "zh": "带来，引起"},
    ],
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F"},
    {
        1: "adapt to 意为「适应」，后接名词 campus life；find it hard to 后须用动词原形。",
        2: "cope with 意为「应对、妥善处理」，宾语是 a tighter budget（更紧的预算）。",
        3: "set up 意为「建立、设立」，与 programme 搭配；has 后用过去分词 set（set 三态同形）。",
        4: "take part in 意为「参加」，指参与朋辈辅导项目。",
        5: "be / become aware of 意为「意识到、了解到」，后接 campus resources。",
        6: "above all 意为「尤其是、最重要的是」，位于句首作评注性状语，后用逗号隔开。",
    },
    [{"en": "freshman", "zh": "大一新生"}, {"en": "peer-mentoring", "zh": "朋辈辅导"}, {"en": "settle in", "zh": "适应新环境"}],
)

phrase(
    "pc4-2", "CET-4", "学习方法", "How to Review Effectively",
    """Good grades rarely {1} luck alone. Researchers suggest that students who {2} a study plan and {3} it every week do better {4}. Before an exam, it helps to {5} what you still cannot explain, and to {6} the mistakes in old quizzes instead of simply rereading notes. Small, regular effort usually {7} steady progress.""",
    [
        {"key": "A", "en": "result from", "zh": "由…产生（区别于 result in 导致）"},
        {"key": "B", "en": "come up with", "zh": "提出，想出"},
        {"key": "C", "en": "carry out", "zh": "执行，开展"},
        {"key": "D", "en": "in the long run", "zh": "从长远来看"},
        {"key": "E", "en": "be aware of", "zh": "意识到"},
        {"key": "F", "en": "pay attention to", "zh": "注意，重视"},
        {"key": "G", "en": "bring about", "zh": "带来，引起"},
        {"key": "H", "en": "give rise to", "zh": "引起，导致"},
    ],
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"},
    {
        1: "result from 意为「源于」，此处指好成绩很少「来自」运气；注意 result in 是「导致」，方向相反。",
        2: "come up with 意为「想出、提出」，与 a study plan（学习计划）搭配。",
        3: "carry out 意为「执行、落实」，指每周执行计划。",
        4: "in the long run 意为「从长远来看」，作时间状语。",
        5: "be aware of / become aware of 意为「意识到」，指弄清自己还讲不明白的内容。",
        6: "pay attention to 意为「注意、重视」，后接 the mistakes。",
        7: "bring about 意为「带来、引起（结果）」，主语是 effort；give rise to 多指引起问题，语气偏负面，为干扰项。",
    },
    [{"en": "steady", "zh": "稳定的，持续的"}, {"en": "reread", "zh": "重读"}],
)

phrase(
    "pc4-3", "CET-4", "健康生活", "Sleep and Study",
    """A short night of sleep can {1} poor concentration the next day. Students often {2} energy by noon and reach for coffee, which may {3} a second sleepless night. Doctors {4} that teens {5} at least eight hours of rest, and they {6} using phones in bed. {7}, a regular schedule matters more than an occasional early night.""",
    [
        {"key": "A", "en": "give rise to", "zh": "引起，导致"},
        {"key": "B", "en": "run out of", "zh": "用完，耗尽"},
        {"key": "C", "en": "bring about", "zh": "带来，引起"},
        {"key": "D", "en": "be aware of", "zh": "意识到"},
        {"key": "E", "en": "be in need of", "zh": "需要"},
        {"key": "F", "en": "object to", "zh": "反对"},
        {"key": "G", "en": "above all", "zh": "首先，尤其是"},
        {"key": "H", "en": "in addition", "zh": "另外"},
    ],
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"},
    {
        1: "give rise to 意为「引起、导致」，接抽象结果 poor concentration。",
        2: "run out of 意为「用完、耗尽」，run out of energy 即「精力耗尽」。",
        3: "bring about 意为「带来（某种结果）」，指咖啡又带来一个不眠之夜。",
        4: "be aware of 在此用 doctors are aware that… 的语义：医生「意识到/指出」；注意后接从句时用 be aware that。",
        5: "be in need of 意为「需要」，teens are in need of at least eight hours of rest。",
        6: "object to 意为「反对」，to 是介词，后接动名词 using。",
        7: "above all 意为「最重要的是」，用于强调规律作息。in addition（另外）为干扰项。",
    },
    [{"en": "concentration", "zh": "注意力"}, {"en": "occasional", "zh": "偶尔的"}],
)

phrase(
    "pc4-4", "CET-4", "环境保护", "A Cleaner Campus",
    """Our university has decided to {1} a recycling scheme this term. Volunteers will {2} a survey to find out how much waste each building produces, and the data will {3} about 60% of the total. Plastic bottles {4} the largest single category. The team hopes the project will {5} real changes in daily habits, and {6} a cleaner campus for everyone.""",
    [
        {"key": "A", "en": "set up", "zh": "建立，设立"},
        {"key": "B", "en": "carry out", "zh": "开展，执行"},
        {"key": "C", "en": "account for", "zh": "（比例上）占；解释"},
        {"key": "D", "en": "make up", "zh": "构成，占"},
        {"key": "E", "en": "bring about", "zh": "带来，引起"},
        {"key": "F", "en": "result in", "zh": "导致，结果是"},
        {"key": "G", "en": "deal with", "zh": "处理"},
        {"key": "H", "en": "turn out", "zh": "结果是；生产"},
    ],
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F"},
    {
        1: "set up 意为「建立、设立」，与 scheme（方案/机制）搭配。",
        2: "carry out 意为「开展、执行」，carry out a survey 即「做一项调查」。",
        3: "account for 意为「（在比例上）占」，后接 about 60% of the total。",
        4: "make up 意为「构成、占（比例）」，主语是复数 Plastic bottles。",
        5: "bring about 意为「带来（变化）」，bring about real changes 是固定搭配。",
        6: "result in 意为「导致、结果是」，指最终带来更干净的校园；与 bring about 近义，此处按「项目 → 结果」使用。",
    },
    [{"en": "recycling scheme", "zh": "回收方案"}, {"en": "category", "zh": "类别"}],
)

phrase(
    "pc4-5", "CET-4", "科技与生活", "Living with Smartphones",
    """Smartphones help us {1} friends and information instantly, but they can also {2} problems in class. A teacher may find it hard to {3} students who check messages every few minutes. Some schools now ask learners to {4} their devices during lessons. {5}, phones are useful tools; the key is to {6} them wisely rather than let them take over.""",
    [
        {"key": "A", "en": "keep in touch with", "zh": "与…保持联系"},
        {"key": "B", "en": "give rise to", "zh": "引起，导致"},
        {"key": "C", "en": "deal with", "zh": "处理，应对"},
        {"key": "D", "en": "put away", "zh": "收起，放好"},
        {"key": "E", "en": "after all", "zh": "毕竟"},
        {"key": "F", "en": "make use of", "zh": "利用"},
        {"key": "G", "en": "be subject to", "zh": "易受…的"},
        {"key": "H", "en": "ahead of schedule", "zh": "提前"},
    ],
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F"},
    {
        1: "keep in touch with 意为「与…保持联系」，此处指与朋友和信息保持连接。",
        2: "give rise to 意为「引起、导致（问题）」。",
        3: "deal with 意为「处理、应对」，此处指老师难以对付频繁看手机的学生。",
        4: "put away 意为「收起、放好」，指课堂上把设备收起来。",
        5: "after all 意为「毕竟」，用于让步后回到主论点。",
        6: "make use of 意为「利用」，make use of them wisely 即「明智地使用」。",
    },
    [{"en": "instantly", "zh": "即时地"}, {"en": "take over", "zh": "占据主导"}],
)

phrase(
    "pc4-6", "CET-4", "计划与效率", "Finishing on Time",
    """Our group was asked to {1} a class presentation. We first {2} a rough plan and {3} the tasks among four members. Two of us {4} the slides while the others {5} the data. Because we started early, everything was ready {6}. Good teamwork, {7}, was the real reason we succeeded.""",
    [
        {"key": "A", "en": "carry out", "zh": "开展，执行"},
        {"key": "B", "en": "come up with", "zh": "想出，提出"},
        {"key": "C", "en": "divide up", "zh": "分配"},
        {"key": "D", "en": "be responsible for", "zh": "负责"},
        {"key": "E", "en": "deal with", "zh": "处理"},
        {"key": "F", "en": "ahead of schedule", "zh": "提前"},
        {"key": "G", "en": "above all", "zh": "首先，尤其是"},
        {"key": "H", "en": "in addition", "zh": "另外"},
    ],
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"},
    {
        1: "carry out 意为「开展、完成（一项任务）」，与 presentation 搭配。",
        2: "come up with 意为「想出、提出」，与 a rough plan 搭配。",
        3: "divide up 意为「分配」，divide the tasks among four members。",
        4: "be responsible for 意为「负责」，Two of us were responsible for the slides。",
        5: "deal with 意为「处理」，指另一组人处理数据。",
        6: "ahead of schedule 意为「提前」，与 started early 呼应。",
        7: "above all 意为「最重要的是」，句首强调团队合作才是关键。",
    },
    [{"en": "rough", "zh": "粗略的"}, {"en": "slide", "zh": "幻灯片"}],
)

# ===== CET-6 =====
phrase(
    "pc6-1", "CET-6", "经济与政策", "Weighing a New Policy",
    """Before the council approved the plan, it had to {1} several objections raised by local residents. Critics argued that the project would expand the car park {2} the public garden, and that spending was already {3} the original budget. Officials replied that, {4} its scale, the scheme was modest, and that all contractors must {5} the safety rules. Any firm that failed to {6} the deadlines would {7} the delay.""",
    [
        {"key": "A", "en": "take into account", "zh": "把…考虑进去"},
        {"key": "B", "en": "at the expense of", "zh": "以…为代价"},
        {"key": "C", "en": "in excess of", "zh": "超过"},
        {"key": "D", "en": "in terms of", "zh": "就…而言，根据"},
        {"key": "E", "en": "abide by", "zh": "遵守（法律、规则）"},
        {"key": "F", "en": "adhere to", "zh": "坚持，遵守"},
        {"key": "G", "en": "answer for", "zh": "对…负责"},
        {"key": "H", "en": "allow for", "zh": "考虑到，预留"},
    ],
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"},
    {
        1: "take into account 意为「把…考虑进去」，宾语是 several objections。",
        2: "at the expense of 意为「以…为代价」，指扩建停车场牺牲公共花园。",
        3: "in excess of 意为「超过」，用于数量/金额，in excess of the original budget。",
        4: "in terms of 意为「就…而言」，in terms of its scale 即「就规模而言」。",
        5: "abide by 意为「遵守（法律、规则）」，与 the safety rules 搭配。",
        6: "adhere to 意为「坚持、遵守」，此处指遵守截止期限；与 abide by 近义，按搭配区分。",
        7: "answer for 意为「对…负责」，would answer for the delay 即「须为延误负责」。",
    },
    [{"en": "objection", "zh": "反对意见"}, {"en": "contractor", "zh": "承包方"}, {"en": "modest", "zh": "不大的，适度的"}],
)

phrase(
    "pc6-2", "CET-6", "科研与发现", "What the Data Show",
    """The authors {1} the unexpected result {2} a small change in the sampling method. They note that such differences often {3} confusion among readers, and that a single striking number can {4} a misleading headline. {5} the storm of criticism, the team chose to {6} its original conclusion, while {7} that the finding {8} be replicated before it is applied.""",
    [
        {"key": "A", "en": "attribute ... to", "zh": "把…归因于"},
        {"key": "B", "en": "give rise to", "zh": "引起，导致"},
        {"key": "C", "en": "in the wake of", "zh": "紧随…之后，作为…的后果"},
        {"key": "D", "en": "adhere to", "zh": "坚持"},
        {"key": "E", "en": "be aware that", "zh": "意识到"},
        {"key": "F", "en": "be bound to", "zh": "一定会，必然"},
        {"key": "G", "en": "stem from", "zh": "源于"},
        {"key": "H", "en": "act on", "zh": "按照…行事"},
    ],
    {1: "A", 2: "A", 3: "B", 4: "B", 5: "C", 6: "D", 7: "E", 8: "F"},
    {},  # 下面单独补
)
# attribute ... to 是「分离式」词组，占两个空，重写为单空形式以免歧义
PHRASE.pop()
phrase(
    "pc6-2", "CET-6", "科研与发现", "What the Data Show",
    """The authors {1} the unexpected result to a small change in the sampling method. They note that such differences often {2} confusion among readers, and that a single striking number can {3} a misleading headline. {4} the storm of criticism, the team chose to {5} its original conclusion, while {6} that the finding {7} be replicated before it is applied.""",
    [
        {"key": "A", "en": "attribute", "zh": "把…归因于（attribute A to B）"},
        {"key": "B", "en": "give rise to", "zh": "引起，导致"},
        {"key": "C", "en": "in the wake of", "zh": "紧随…之后"},
        {"key": "D", "en": "adhere to", "zh": "坚持"},
        {"key": "E", "en": "be aware", "zh": "意识到（be aware that…）"},
        {"key": "F", "en": "be bound to", "zh": "一定会，必然"},
        {"key": "G", "en": "stem from", "zh": "源于"},
        {"key": "H", "en": "act on", "zh": "按照…行事"},
    ],
    {1: "A", 2: "B", 3: "B", 4: "C", 5: "D", 6: "E", 7: "F"},
    {
        1: "attribute A to B 意为「把 A 归因于 B」；句中已有 to，故填 attribute。",
        2: "give rise to 意为「引起、导致」，接抽象名词 confusion。",
        3: "同样用 give rise to；一个显眼的数字也「催生」误导性标题（词组可重复使用，符合真题规则）。",
        4: "in the wake of 意为「紧随…之后 / 作为…的后果」，后接 the storm of criticism。",
        5: "adhere to 意为「坚持」，adhere to its original conclusion 即「坚持原有结论」。",
        6: "be aware 后接 that 从句，be aware that… 意为「意识到…」。",
        7: "be bound to 意为「一定会、必然」，后接动词原形 be replicated。",
    },
    [{"en": "sampling", "zh": "抽样"}, {"en": "replicate", "zh": "复现（实验）"}, {"en": "misleading", "zh": "误导性的"}],
)

phrase(
    "pc6-3", "CET-6", "气候与环境", "After the Flood",
    """{1} the floods, engineers found that the old drains were {2} to blockage and that rainfall had been far {3} the design limit. Repair crews had to {4} further damage while the council agreed to {5} stricter building codes. Residents, {6} to noisy streets, were surprisingly patient; {7}, most accepted that the work was necessary.""",
    [
        {"key": "A", "en": "in the wake of", "zh": "紧随…之后"},
        {"key": "B", "en": "be susceptible", "zh": "易受…影响的（be susceptible to）"},
        {"key": "C", "en": "in excess of", "zh": "超过"},
        {"key": "D", "en": "ward off", "zh": "避开，防止"},
        {"key": "E", "en": "abide by", "zh": "遵守"},
        {"key": "F", "en": "be accustomed", "zh": "习惯于（be accustomed to）"},
        {"key": "G", "en": "by virtue of", "zh": "凭借，由于"},
        {"key": "H", "en": "above all", "zh": "尤其是"},
    ],
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "H"},
    {
        1: "in the wake of 意为「紧随…之后」，指洪水过后。",
        2: "be susceptible to 意为「易受…影响」，句中已有 to，故填 susceptible。",
        3: "in excess of 意为「超过」，far in excess of the design limit 即「远超设计上限」。",
        4: "ward off 意为「防止、挡开」，ward off further damage。",
        5: "abide by 意为「遵守（法规）」，与 stricter building codes 搭配。",
        6: "be accustomed to 意为「习惯于」，句中已有 to，填 accustomed。",
        7: "above all 意为「最重要的是」；此处亦可理解为评注状语，强调整体态度。by virtue of 为干扰项。",
    },
    [{"en": "drain", "zh": "排水管"}, {"en": "blockage", "zh": "堵塞"}, {"en": "code", "zh": "规范，法规"}],
)

phrase(
    "pc6-4", "CET-6", "教育与公平", "Who Gets a Place",
    """{1} a new rule, children from low-income families are {2} paying tuition at the city college. The policy does not {3} every hardship, but it does {4} the most obvious barrier. Critics {5} the change, arguing that merit should {6} over background. {7} its defenders, however, equal access is a goal worth protecting.""",
    [
        {"key": "A", "en": "by virtue of", "zh": "凭借，由于"},
        {"key": "B", "en": "be exempt from", "zh": "被免除"},
        {"key": "C", "en": "allow for", "zh": "考虑到，顾及"},
        {"key": "D", "en": "do away with", "zh": "消除，废除"},
        {"key": "E", "en": "object to", "zh": "反对"},
        {"key": "F", "en": "take precedence", "zh": "优先（take precedence over）"},
        {"key": "G", "en": "in terms of", "zh": "就…而言"},
        {"key": "H", "en": "in the long run", "zh": "从长远来看"},
    ],
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"},
    {
        1: "by virtue of 意为「凭借、由于」，引出政策依据。",
        2: "be exempt from 意为「被免除」，句中已有 from…（paying），填 exempt。",
        3: "allow for 意为「顾及、考虑到」，指政策无法顾及所有困难。",
        4: "do away with 意为「消除、废除」，与 the most obvious barrier 搭配。",
        5: "object to 意为「反对」，to 为介词。",
        6: "take precedence over 意为「优先于」，句中已有 over，填 take precedence。",
        7: "in terms of 意为「就…而言」，in terms of its defenders 指「在其支持者看来」。",
    },
    [{"en": "tuition", "zh": "学费"}, {"en": "merit", "zh": "才学，功绩"}, {"en": "equal access", "zh": "平等入学机会"}],
)

phrase(
    "pc6-5", "CET-6", "心理与行为", "Why We Procrastinate",
    """People who {1} to distraction often {2} short tasks that feel urgent. Researchers {3} this habit {4} a preference for immediate reward, and warn that it can {5} real losses over a term. The advice is not to {6} all pleasure, but to {7} the working day into short blocks and {8} one clear goal for each.""",
    [
        {"key": "A", "en": "be prone", "zh": "易于…的（be prone to）"},
        {"key": "B", "en": "crave", "zh": "渴望"},
        {"key": "C", "en": "attribute", "zh": "把…归因于（attribute A to B）"},
        {"key": "D", "en": "entail", "zh": "带来，使必要"},
        {"key": "E", "en": "abstain from", "zh": "戒除，避开"},
        {"key": "F", "en": "break down", "zh": "分解"},
        {"key": "G", "en": "act on", "zh": "按照…行事"},
        {"key": "H", "en": "be capable of", "zh": "能够"},
    ],
    {1: "A", 2: "B", 3: "C", 4: "C", 5: "D", 6: "E", 7: "F", 8: "G"},
    {},
)
PHRASE.pop()
phrase(
    "pc6-5", "CET-6", "心理与行为", "Why We Procrastinate",
    """People who {1} to distraction often {2} short tasks that feel urgent. Researchers {3} this habit to a preference for immediate reward, and warn that it can {4} real losses over a term. The advice is not to {5} all pleasure, but to {6} the working day into short blocks and {7} one clear goal for each.""",
    [
        {"key": "A", "en": "be prone", "zh": "易于…的（be prone to）"},
        {"key": "B", "en": "crave", "zh": "渴望"},
        {"key": "C", "en": "attribute", "zh": "把…归因于（attribute A to B）"},
        {"key": "D", "en": "entail", "zh": "带来，使必要"},
        {"key": "E", "en": "abstain from", "zh": "戒除，避开"},
        {"key": "F", "en": "break down", "zh": "分解"},
        {"key": "G", "en": "set", "zh": "设定（set a goal）"},
        {"key": "H", "en": "be capable of", "zh": "能够"},
    ],
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"},
    {
        1: "be prone to 意为「易于、倾向于」，句中已有 to，填 prone。",
        2: "crave 意为「渴望」，指偏爱看起来紧急的短任务。",
        3: "attribute A to B 意为「把 A 归因于 B」；句中已有 to，填 attribute。",
        4: "entail 意为「带来、使必然产生（后果）」，entail real losses。",
        5: "abstain from 意为「戒除、避开」，指不必戒掉全部娱乐。",
        6: "break down 意为「分解」，break the day into short blocks。",
        7: "set a goal 意为「设定目标」；此处 set 为实义动词，与 set up（建立）区分。",
    },
    [{"en": "procrastinate", "zh": "拖延"}, {"en": "distraction", "zh": "分心事物"}, {"en": "immediate reward", "zh": "即时回报"}],
)

phrase(
    "pc6-6", "CET-6", "城市与人口", "A Changing City",
    """The report shows that {1} have shifted {2} over the past decade: the city is older, and its households smaller. Planners must {3} these trends when they design housing, or new flats will be {4} rigid in layout to suit smaller families {5} young couples. Spending on services has risen {6} inflation, {7} an ageing population that needs more care.""",
    [
        {"key": "A", "en": "demographics", "zh": "人口结构（数据）"},
        {"key": "B", "en": "substantially", "zh": "大幅地"},
        {"key": "C", "en": "take into account", "zh": "把…考虑进去"},
        {"key": "D", "en": "too", "zh": "太…（too … to）"},
        {"key": "E", "en": "such as", "zh": "例如"},
        {"key": "F", "en": "in excess of", "zh": "超过"},
        {"key": "G", "en": "by virtue of", "zh": "凭借，由于"},
        {"key": "H", "en": "be correlated", "zh": "相关（be correlated with）"},
    ],
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"},
    {
        1: "demographics 意为「人口结构/人口统计数据」，作主语。",
        2: "substantially 意为「大幅地」，修饰 have shifted。",
        3: "take into account 意为「把…考虑进去」，宾语是 these trends。",
        4: "too … to 结构，意为「太…以致不能」，填 too。",
        5: "such as 意为「例如」，引出 young couples 作为小家庭例子。",
        6: "in excess of 意为「超过」，指服务支出涨幅超过通胀。",
        7: "by virtue of 意为「由于、凭借」，引出原因：老龄化人口需要更多照护。",
    },
    [{"en": "household", "zh": "家庭户"}, {"en": "layout", "zh": "布局"}, {"en": "inflation", "zh": "通货膨胀"}],
)
# 单独补 pc6-2 的解释（前面第一个版本被 pop，第二个已带解释）
# 修正 pc6-1 提示：explain 完整

# ---------------------------------------------------------------- 短篇阅读
def reading(id, level, topic, title, passage, questions, glossary=None):
    READING.append(dict(
        id=id, level=level, topic=topic, title=title,
        passage=passage.strip(), questions=questions, glossary=glossary or []
    ))

def q(text, options, answer, explain, qtype="detail"):
    return {"q": text, "options": options, "answer": answer, "explain": explain, "type": qtype}

# ===== CET-4（100–140 词，句子较短，重细节与词义）=====
reading("rd4-1", "CET-4", "校园生活", "The Library at Night",
    """The university library used to close at nine in the evening. Last term, after a survey showed that most students studied late, the school extended the closing time to midnight. The change was small but popular. Quiet reading rooms on the third floor now stay open, and a free shuttle bus runs every half hour to take students back to their dorms. Librarians say the number of evening visitors has doubled. Some staff members were worried about the extra cost, yet the school found that most of it went to lighting, which was already on for the security system. The library has also started a late-night help desk, where two senior students answer questions about finding books and using the databases.""",
    [
        q("Why did the school change the library's closing time?",
          ["A new security system was installed.", "A survey showed students studied late.", "The shuttle bus was not busy at night.", "Librarians asked for shorter hours."],
          1, "第一段明确说 after a survey showed that most students studied late（调查显示多数学生学习到很晚），因此延长开放时间。", "detail"),
        q("What does the word \"shuttle\" most probably mean in the passage?",
          ["A kind of ticket", "A bus that runs regularly between two places", "A quiet study room", "A database for books"],
          1, "a free shuttle bus runs every half hour to take students back to their dorms 指「每半小时一班的接驳班车」，故选定期往返的车辆。", "vocab"),
        q("What can we learn about the extra cost?",
          ["It was much higher than expected.", "It was paid by the students.", "Most of it was for lighting that was already on.", "It forced the library to close earlier again."],
          2, "第二段说 most of it went to lighting, which was already on for the security system——照明本就因安保系统开着，因此新增成本有限。", "inference"),
    ],
    [{"en": "extend", "zh": "延长"}, {"en": "database", "zh": "数据库"}])

reading("rd4-2", "CET-4", "健康", "A Short Walk After Lunch",
    """A team of researchers followed 200 office workers for six weeks. Half of them were asked to walk for fifteen minutes after lunch; the others sat or returned to their desks as usual. At the end of the study, the walking group reported better concentration in the afternoon and fewer feelings of sleepiness. Their work output did not change much, but they said the break made the rest of the day feel easier. The researchers were careful not to claim too much. The sample was small, and people who chose to join may already have been more active. Still, the result agrees with earlier studies suggesting that light movement after a meal helps the body handle sugar more steadily. A short walk, the authors conclude, is a low-cost habit worth trying.""",
    [
        q("What were half of the workers asked to do?",
          ["Work longer in the afternoon", "Walk for fifteen minutes after lunch", "Skip lunch twice a week", "Record their sleep every night"],
          1, "第一段：Half of them were asked to walk for fifteen minutes after lunch.", "detail"),
        q("Which of the following did NOT change much according to the study?",
          ["Afternoon concentration", "Feelings of sleepiness", "The amount of work produced", "How the rest of the day felt"],
          2, "Their work output did not change much（工作产出变化不大），而注意力和困倦感都有改善。", "detail"),
        q("What is the researchers' attitude towards the result?",
          ["They are cautious about it.", "They are certain it applies to everyone.", "They think the study was wasted.", "They refuse to publish it."],
          0, "第二段 were careful not to claim too much、sample was small 表明作者态度谨慎（cautious）。", "attitude"),
    ],
    [{"en": "concentration", "zh": "注意力"}, {"en": "sample", "zh": "样本"}, {"en": "steadily", "zh": "平稳地"}])

reading("rd4-3", "CET-4", "科技", "Why Old Phones Slow Down",
    """Many people notice that a phone feels slower after two or three years. The reason is not always the hardware. New apps are written for newer devices, so they ask for more memory and faster processors than an old phone can offer. At the same time, a battery that has been charged hundreds of times holds less power, and the system may lower its speed to protect it. Storage matters too: when a phone is nearly full, it has trouble moving files around, which makes everything take longer. The good news is that simple steps help. Removing unused apps, clearing large videos and restarting the phone once a week can bring back much of its old speed. Replacing the battery is often cheaper than buying a new phone.""",
    [
        q("According to the passage, why do new apps slow an old phone?",
          ["They are written to need more memory and faster processors.", "They always contain large videos.", "They stop the battery from charging.", "They delete files from the storage."],
          0, "第一段：new apps … ask for more memory and faster processors than an old phone can offer.", "detail"),
        q("What does the passage suggest about the battery?",
          ["It works better after hundreds of charges.", "It is the only reason a phone slows down.", "The system may reduce speed to protect a weak battery.", "It should never be replaced."],
          2, "the system may lower its speed to protect it（系统可能降速以保护老化电池）。", "detail"),
        q("What is the main idea of the last paragraph?",
          ["Old phones should be thrown away.", "Simple actions can make an old phone faster.", "New apps are badly designed.", "Batteries are more expensive than phones."],
          1, "末段列举删除不用应用、清理大视频、每周重启、换电池等低成本做法，主旨是「简单操作能让旧手机变快」。", "main"),
    ],
    [{"en": "hardware", "zh": "硬件"}, {"en": "processor", "zh": "处理器"}, {"en": "storage", "zh": "存储空间"}])

reading("rd4-4", "CET-4", "环境", "A Town That Bans Plastic Bags",
    """A small coastal town stopped giving out free plastic bags last spring. Shopkeepers were nervous at first, but the town handed out cheap cloth bags to every household before the rule began. Six months later, volunteers collected rubbish along the beach and found far fewer plastic bags than in the same month of the previous year. Fishermen said the change also helped their nets, which used to get caught on floating plastic. Not everyone is happy. A few shop owners say that paper bags cost more and that some customers still forget to bring their own bag. The town council has now started a scheme that lets people borrow a bag from one shop and return it to another. Early figures suggest that most borrowed bags do come back.""",
    [
        q("What did the town do before the rule started?",
          ["It closed several shops.", "It gave cheap cloth bags to households.", "It cleaned the beach once.", "It paid the fishermen."],
          1, "the town handed out cheap cloth bags to every household before the rule began.", "detail"),
        q("Why were fishermen pleased with the change?",
          ["They could sell more fish.", "Fewer plastic bags got caught in their nets.", "They received free cloth bags.", "The council repaired their boats."],
          1, "Fishermen said the change also helped their nets, which used to get caught on floating plastic.", "detail"),
        q("What problem do some shop owners still mention?",
          ["Customers borrow too many bags.", "Paper bags cost more than plastic ones.", "The beach is dirtier than before.", "Nobody returns borrowed bags."],
          1, "A few shop owners say that paper bags cost more and that some customers still forget…", "detail"),
    ],
    [{"en": "coastal", "zh": "沿海的"}, {"en": "household", "zh": "家庭"}, {"en": "scheme", "zh": "方案"}])

reading("rd4-5", "CET-4", "文化", "Learning to Cook from Grandmother",
    """When Li Mei went to university, she could not cook even an egg. In her first winter holiday, her grandmother taught her five simple dishes, writing each step down in a small notebook. Li Mei took the notebook back to campus and began cooking for her roommates on Sundays. What started as a way to save money became the thing her friends looked forward to most. She now posts short videos of the same five dishes, and thousands of students watch them. She says the videos are not about showing skill: many viewers live far from home and miss familiar food. The notebook, now stained with oil, stays on her desk. Her grandmother's handwriting is hard to read, but Li Mei says she would not replace it with a printed recipe for anything.""",
    [
        q("What did Li Mei's grandmother do?",
          ["She posted cooking videos online.", "She wrote down the steps of five dishes.", "She cooked for the roommates.", "She bought Li Mei a printed recipe."],
          1, "her grandmother taught her five simple dishes, writing each step down in a small notebook.", "detail"),
        q("Why does Li Mei make the videos?",
          ["To become a professional chef", "To sell her notebook", "To help students who miss food from home", "To prove that she cooks better now"],
          2, "many viewers live far from home and miss familiar food——她强调视频不是炫技，而是抚慰想家的学生。", "inference"),
        q("What does the stained notebook suggest?",
          ["It has been used many times.", "It should be thrown away.", "It was printed recently.", "It belongs to her roommates."],
          0, "now stained with oil（沾满油渍）说明被反复使用；且她说不愿换成打印菜谱，可见其珍贵。", "inference"),
    ],
    [{"en": "stained", "zh": "沾污的"}, {"en": "recipe", "zh": "食谱"}, {"en": "familiar", "zh": "熟悉的"}])

reading("rd4-6", "CET-4", "职场", "The First Day at Work",
    """On her first day at a design company, Chen Yu was given no big task. Her manager simply asked her to sit with three different teams and write down anything she did not understand. By Friday she had filled two pages with questions. Some were small, such as where files were kept; others were about why a client had rejected a draft. At the end of the week, the manager read the list with her and said it was the most useful thing a new employee had produced in months. Teams often forget what is confusing to an outsider, she explained. Chen Yu later learned that several of her questions led to a clearer internal guide. Looking back, she is glad her first job was to notice, not to pretend she already knew.""",
    [
        q("What was Chen Yu asked to do in her first week?",
          ["Finish a design draft", "Write down things she did not understand", "Train three new teams", "Meet an important client"],
          1, "asked her to sit with three different teams and write down anything she did not understand.", "detail"),
        q("Why did the manager value the list of questions?",
          ["It was longer than expected.", "It showed what was confusing to an outsider.", "It contained a new design idea.", "It proved Chen Yu worked fast."],
          1, "Teams often forget what is confusing to an outsider——老员工习以为常之处恰是新人的价值所在。", "inference"),
        q("What did several of her questions lead to?",
          ["A clearer internal guide", "A pay rise", "A new client", "A shorter working week"],
          0, "several of her questions led to a clearer internal guide.", "detail"),
    ],
    [{"en": "draft", "zh": "草稿"}, {"en": "internal", "zh": "内部的"}, {"en": "outsider", "zh": "局外人，新人"}])

# ===== CET-6（150–180 词，长句、抽象话题，重推断/态度/主旨）=====
reading("rd6-1", "CET-6", "社会政策", "When a City Removes Its Fences",
    """For decades the riverfront of the city was separated from the neighbourhoods behind it by a high fence and a busy road. Last year the council removed both, replacing the road with a wide path lined with trees. The stated aim was modest: give residents a place to walk. What followed was less modest. Within a year, small cafés and bookshops opened along the path, and property values in the adjacent streets rose sharply. Critics had warned that such improvements merely push poorer residents out, and the early figures partly bear them out: rents near the path have climbed faster than anywhere else in the city. Supporters reply that the answer is not to abandon public space but to build affordable housing at the same time. The dispute is unlikely to be settled soon, yet both sides now agree on one point — that a river which people can actually reach changes how a city thinks about itself.""",
    [
        q("What was the council's original purpose in removing the fence and road?",
          ["To raise property values", "To attract cafés and bookshops", "To give residents a place to walk", "To reduce traffic in the whole city"],
          2, "The stated aim was modest: give residents a place to walk.（公开宣称的目标很朴素：给居民一处散步之地）其余为后续结果。", "detail"),
        q("What does \"the early figures partly bear them out\" most probably mean?",
          ["The figures completely disprove the critics.", "The figures partly support the critics' warning.", "The critics refused to look at the figures.", "The figures were collected by the critics."],
          1, "bear out 意为「证实、支持」；紧接着 rents near the path have climbed faster 说明租金上涨，部分印证了批评者关于挤走低收入居民的警告。", "vocab"),
        q("What do both sides in the dispute agree on?",
          ["Affordable housing should be the only priority.", "The project should never have been started.", "Reaching the river changes how the city sees itself.", "Rents will stop rising next year."],
          2, "末句 both sides now agree on one point — that a river which people can actually reach changes how a city thinks about itself.", "detail"),
        q("What is the author's tone in describing the outcome?",
          ["Strongly disapproving", "Detached but observant", "Openly celebratory", "Bitter and personal"],
          1, "作者并列陈述支持与批评双方、用 modest / less modest / unlikely to be settled 等克制措辞，属客观观察而非赞扬或反对。", "attitude"),
    ],
    [{"en": "riverfront", "zh": "滨河地带"}, {"en": "adjacent", "zh": "毗邻的"}, {"en": "affordable housing", "zh": "保障性住房"}])

reading("rd6-2", "CET-6", "教育与科技", "Grades, Rewritten",
    """Universities have long treated the exam as a clean measure of what a student knows. That confidence is quietly eroding. When a large online course compared the marks of students who sat the same paper in a quiet hall with those who took it at home with a screen open, the difference was not large enough to settle the argument — but it was large enough to unsettle it. More troubling was what happened afterwards: students who had been told their results were provisional went on to outperform their peers in the following term, while those given a fixed grade did not. The researchers are careful to say that a label is not a destiny. Still, if a number handed out in December can alter how much effort someone makes in March, then the exam is measuring something more than knowledge. It is also, inadvertently, helping to produce it.""",
    [
        q("What did the comparison of exam marks show?",
          ["Home-sit students cheated systematically.", "The difference was too small to be measured.", "The difference was not decisive but was disturbing.", "Quiet halls produced clearly better marks."],
          2, "not large enough to settle the argument — but it was large enough to unsettle it：不足以定论，却足以让人不安。", "detail"),
        q("What happened to students told their results were provisional?",
          ["They performed better in the following term.", "They stopped attending classes.", "They asked to retake the exam.", "They received lower final grades."],
          0, "students who had been told their results were provisional went on to outperform their peers in the following term.", "detail"),
        q("What does the last sentence imply about exams?",
          ["Exams should be abolished immediately.", "Exams measure nothing at all.", "Exam results can influence the very ability they claim to measure.", "Only December exams are unreliable."],
          2, "末句 helping to produce it：分数不仅「测量」知识，还反过来「制造/影响」了被测量的东西（后续努力）。", "inference"),
        q("Which word best describes the researchers' position?",
          ["Dogmatic", "Cautious", "Dismissive", "Alarmist"],
          1, "The researchers are careful to say that a label is not a destiny：措辞审慎，拒绝过度推论。", "attitude"),
    ],
    [{"en": "erode", "zh": "逐渐削弱"}, {"en": "provisional", "zh": "临时的，暂定的"}, {"en": "destiny", "zh": "宿命"}, {"en": "inadvertently", "zh": "无意中"}])

reading("rd6-3", "CET-6", "环境与经济", "The Price of Cleaner Air",
    """Few policies are as easy to praise and as hard to price as air quality regulation. A factory ordered to fit cleaner equipment faces a bill it can count; the benefit — fewer hospital visits across a region — is spread thinly over thousands of households and years, and therefore rarely appears in anyone's accounts. Economists have tried to close this gap by putting a number on avoided illness, but such figures are routinely attacked as speculative. The objection is not unreasonable, yet it is applied asymmetrically: the cost of compliance is treated as hard fact, while the cost of doing nothing is treated as guesswork. Several long-term studies now suggest that the latter has been consistently underestimated. If so, the familiar complaint that regulation is too expensive may rest less on arithmetic than on which column of the ledger we are willing to look at.""",
    [
        q("Why is the benefit of cleaner air hard to account for?",
          ["It is small and short-lived.", "It is spread over many households and years.", "Factories refuse to report it.", "No hospital keeps records."],
          1, "the benefit … is spread thinly over thousands of households and years, and therefore rarely appears in anyone's accounts.", "detail"),
        q("What does \"applied asymmetrically\" refer to?",
          ["Costs and benefits are judged by different standards.", "Both sides use the same data.", "Only factories are regulated.", "Studies are repeated every year."],
          0, "合规成本被当作 hard fact，而不作为的代价被当作 guesswork——同一把尺子没有用在两边，即标准不对称。", "inference"),
        q("What do several long-term studies suggest?",
          ["The cost of compliance has been exaggerated.", "The cost of inaction has been underestimated.", "Air quality has no effect on health.", "Regulation always reduces employment."],
          1, "Several long-term studies now suggest that the latter has been consistently underestimated（后者＝不作为的代价，被低估）。", "detail"),
        q("What is the main point of the passage?",
          ["Factories should never be regulated.", "Claims that regulation is too costly may reflect accounting bias.", "Economists cannot measure anything.", "Hospital visits are rising everywhere."],
          1, "末句点题：所谓「监管太贵」，更多取决于我们愿意看账本的哪一栏，即核算口径的偏差。", "main"),
    ],
    [{"en": "compliance", "zh": "合规（成本）"}, {"en": "speculative", "zh": "推测性的"}, {"en": "asymmetrically", "zh": "不对称地"}, {"en": "ledger", "zh": "账本"}])

reading("rd6-4", "CET-6", "心理", "The Myth of the Empty Mind",
    """We tend to assume that doing nothing is the absence of thought. Brain-imaging studies have made that assumption increasingly difficult to hold. When participants are left alone in a quiet room with no task, a network associated with memory, planning and self-reference becomes more, not less, active. Far from idling, the mind rehearses recent conversations, simulates tomorrow's difficulties and quietly rearranges what it knows. This may explain why solutions so often arrive in the shower rather than at the desk. It also complicates a familiar complaint about modern work: that constant interruption is merely a loss of time. If uninterrupted stretches are when the brain consolidates and recombines, then a calendar packed with short meetings is not only inefficient; it removes the very condition under which understanding forms. Rest, on this account, is not the reward for thinking but part of the machinery of it.""",
    [
        q("What have brain-imaging studies shown about a person left with no task?",
          ["The brain becomes almost inactive.", "A network linked to memory and planning becomes more active.", "Only visual areas of the brain respond.", "The brain cannot be measured reliably."],
          1, "a network associated with memory, planning and self-reference becomes more, not less, active.", "detail"),
        q("Why does the author mention solutions arriving in the shower?",
          ["To show that people think better when relaxed", "To argue that showers save time", "To criticise poor working conditions", "To introduce a new imaging technique"],
          0, "「远非空转」的大脑会排演、模拟、重组已知，故答案常在淋浴时冒出——用以说明放松时思维仍在运作。", "inference"),
        q("What does the author suggest about a calendar full of short meetings?",
          ["It is the most efficient way to work.", "It mainly wastes travelling time.", "It removes the condition needed for understanding to form.", "It has no effect on how people think."],
          2, "it removes the very condition under which understanding forms（恰恰剥夺了理解得以形成的条件）。", "detail"),
        q("What does the last sentence mean?",
          ["Rest should be earned by hard work.", "Rest is a component of thinking itself.", "Machines need regular rest too.", "Thinking is impossible without a desk."],
          1, "Rest … is not the reward for thinking but part of the machinery of it：休息不是思考之后的奖赏，而是思考机制本身的一环。", "inference"),
    ],
    [{"en": "idle", "zh": "空转，闲着"}, {"en": "simulate", "zh": "模拟"}, {"en": "consolidate", "zh": "巩固"}, {"en": "recombine", "zh": "重新组合"}])

reading("rd6-5", "CET-6", "文化与社会", "What a Dictionary Leaves Out",
    """A dictionary tells us what a word may mean; it is remarkably silent on what a word has been allowed to mean. Consider the vocabulary of work. For much of the last century, terms such as \"career\" and \"profession\" were reserved for occupations that required formal qualifications, while the activities that filled most people's days were described with humbler verbs. The distinction was presented as neutral, a matter of precision. Yet it quietly sorted lives into those that progressed and those that merely passed. Linguists point out that such boundaries rarely survive contact with evidence: the skills required in so-called unskilled work often take years to acquire. What is interesting is not that the labels were unfair — that is easily said — but that they were so durable. A category, once printed, acquires the quiet authority of something that was always there; challenging it requires not a better definition but a willingness to notice that a definition was made at all.""",
    [
        q("According to the passage, how were \"career\" and \"profession\" once used?",
          ["For any paid activity", "Only for work needing formal qualifications", "Mainly for manual labour", "Only in spoken English"],
          1, "terms such as career and profession were reserved for occupations that required formal qualifications.", "detail"),
        q("What does the author find most interesting about such labels?",
          ["That they were obviously unfair", "That they lasted so long", "That they came from Latin", "That linguists invented them"],
          1, "What is interesting is not that the labels were unfair — that is easily said — but that they were so durable（耐人寻味的是其持久性）。", "detail"),
        q("What does \"a category, once printed, acquires the quiet authority of something that was always there\" suggest?",
          ["Printed categories are always accurate.", "Written labels come to seem natural and unquestionable.", "Dictionaries should not be printed.", "Old words are more precise than new ones."],
          1, "一旦被印成条目，分类就获得了「仿佛向来如此」的隐蔽权威——即被自然化、不再被质疑。", "inference"),
        q("Which statement would the author most likely agree with?",
          ["Definitions are discovered rather than made.", "Better dictionaries will solve the problem.", "We should notice that definitions are human constructions.", "Unskilled work requires no training."],
          2, "末句：challenging it requires … a willingness to notice that a definition was made at all（意识到定义是被造出来的）。", "inference"),
    ],
    [{"en": "reserved for", "zh": "专用于"}, {"en": "neutral", "zh": "中立的"}, {"en": "durable", "zh": "持久的"}, {"en": "authority", "zh": "权威"}])

reading("rd6-6", "CET-6", "科技与就业", "The Tool That Changed the Task",
    """When a new automation tool was introduced into a hospital's records department, managers expected it to reduce headcount. Eighteen months later, staff numbers were unchanged, but the work was unrecognisable. Clerks who had spent their days transcribing forms now spent them checking the tool's output, handling the cases it flagged as uncertain, and explaining decisions to patients. The tool had not removed the job; it had relocated its difficulty to the edges, where judgement was still required. Researchers who studied the change call this the \"residual problem\": automation reliably handles the routine middle and leaves behind precisely those cases that are hardest to codify. The consequence is counter-intuitive. Because the remaining work is less repetitive, it demands more experience, not less — and the people doing it need support and training that the original plan had not budgeted for. Efficiency, it turns out, is not the same as simplification.""",
    [
        q("What did managers expect the automation tool to do?",
          ["Improve patient communication", "Reduce the number of staff", "Make records easier to codify", "Remove all uncertain cases"],
          1, "managers expected it to reduce headcount（缩减人员编制）。", "detail"),
        q("What happened to the clerks' work after eighteen months?",
          ["It disappeared entirely.", "It became purely routine.", "It shifted to checking, judging and explaining.", "It was moved to another department."],
          2, "checking the tool's output, handling the cases it flagged as uncertain, and explaining decisions to patients.", "detail"),
        q("What does the \"residual problem\" refer to?",
          ["The high cost of the software", "The difficult cases automation leaves behind", "Staff refusing to use new tools", "Errors in the original budget"],
          1, "automation reliably handles the routine middle and leaves behind precisely those cases that are hardest to codify.", "vocab"),
        q("What is the main idea of the passage?",
          ["Automation always destroys jobs.", "Hospitals should avoid new technology.", "Automation can make the remaining work more demanding.", "Clerks need fewer skills than before."],
          2, "末两句点题：剩余工作更不重复、更需要经验，Efficiency … is not the same as simplification（效率≠简化）。", "main"),
    ],
    [{"en": "headcount", "zh": "人员编制"}, {"en": "transcribe", "zh": "誊录，转录"}, {"en": "codify", "zh": "编码，条理化"}, {"en": "counter-intuitive", "zh": "反直觉的"}])

# ---------------------------------------------------------------- 严格校验
errs = []
ids = set()
for p in PHRASE + READING:
    if p["id"] in ids: errs.append(f"重复 id: {p['id']}")
    ids.add(p["id"])
    if p["level"] not in ("CET-4", "CET-6"): errs.append(f"{p['id']} level 非法")

bank_keys = {}
for p in PHRASE:
    keys = [b["key"] for b in p["bank"]]
    if len(keys) != len(set(keys)): errs.append(f"{p['id']} bank 字母重复")
    bank_keys = {b["key"]: b for b in p["bank"]}
    found = [int(x) for x in re.findall(r"\{(\d+)\}", p["passage"])]
    if sorted(found) != sorted(p["answers"].keys()):
        errs.append(f"{p['id']} 空格与 answers 不一致: passage={sorted(found)} answers={sorted(p['answers'].keys())}")
    for n, k in p["answers"].items():
        if k not in bank_keys: errs.append(f"{p['id']} 第{n}空答案 {k} 不在 bank")
        if n not in p["explain"]: errs.append(f"{p['id']} 第{n}空缺解析")
    if not p["passage"] or not p["title"]: errs.append(f"{p['id']} 缺标题/正文")

for r in READING:
    wc = len(r["passage"].split())
    if not (90 <= wc <= 200): errs.append(f"{r['id']} 词数 {wc} 不在 90–200")
    if not r["questions"]: errs.append(f"{r['id']} 无题目")
    for j, qq in enumerate(r["questions"]):
        if len(qq["options"]) != 4: errs.append(f"{r['id']} 第{j+1}题选项数≠4")
        if not (0 <= qq["answer"] < 4): errs.append(f"{r['id']} 第{j+1}题答案越界")
        if not qq.get("explain"): errs.append(f"{r['id']} 第{j+1}题缺解析")

if errs:
    print("校验失败:"); [print("  -", e) for e in errs]; sys.exit(1)

data = {"phrase": PHRASE, "reading": READING}
import os
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs/public/data/reading.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("校验通过 ✓")
print(f"词组填空: {len(PHRASE)} 段（CET-4 {sum(1 for p in PHRASE if p['level']=='CET-4')} / CET-6 {sum(1 for p in PHRASE if p['level']=='CET-6')}），共 {sum(len(p['answers']) for p in PHRASE)} 空")
print(f"短篇阅读: {len(READING)} 篇（CET-4 {sum(1 for r in READING if r['level']=='CET-4')} / CET-6 {sum(1 for r in READING if r['level']=='CET-6')}），共 {sum(len(r['questions']) for r in READING)} 题")
for r in READING:
    print(f"  {r['id']} {r['level']} {len(r['passage'].split())}词 {len(r['questions'])}题")
print("输出:", out)
