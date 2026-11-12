# -*- coding: utf-8 -*-
"""「英语阅读」题库第二批：新增 16 套（CET-4 × 8 + CET-6 × 8）。

每套 = 1 段词组填空（选词填空，6 空 / 8 候选）+ 1 篇短篇阅读（四级 3 题 / 六级 4 题）。
素材仍取自用户提供的真题 PDF 与《大学英语四六级常用词组》等资料；词组释义优先用资料
中的权威释义，少量资料未收的常见搭配由编者据标准词典释义补注。

运行：python3 scripts/gen_reading_part2.py
  - 读取现有 docs/public/data/reading.json
  - 严格校验新增题目（id 不冲突 / 空格与答案一致 / 答案索引 / 选项数 / 词数 / 解析完整）
  - 合并写回、随机化词组填空的答案位置（避免按顺序猜答案），并打印统计
"""
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "docs", "public", "data", "reading.json")
OUT = os.path.normpath(OUT)

NEW_PHRASE = []
NEW_READING = []


def phrase(id, level, topic, title, passage, bank, answers, explain, glossary=None):
    NEW_PHRASE.append(dict(
        id=id, level=level, topic=topic, title=title,
        passage=passage.strip(), bank=bank, answers=answers,
        explain=explain, glossary=glossary or []
    ))


def reading(id, level, topic, title, passage, questions, glossary=None):
    NEW_READING.append(dict(
        id=id, level=level, topic=topic, title=title,
        passage=passage.strip(), questions=questions, glossary=glossary or []
    ))


def q(text, options, answer, explain, qtype="detail"):
    return {"q": text, "options": options, "answer": answer, "explain": explain, "type": qtype}


def b(items):
    """[('A','adapt to','适应'), ...] -> [{'key','en','zh'}, ...]"""
    return [{"key": k, "en": en, "zh": zh} for k, en, zh in items]


# ============================================================ CET-4（8 套）
# ---- 套 7：社区志愿 ----
phrase(
    "pc4-7", "CET-4", "社区与志愿", "A Saturday Reading Club",
    """Our community runs a Saturday reading club for children. Any student who wants to {1} the club must first fill in a form. Two volunteers are {2} each group of six children; they {3} the children during the two-hour session and answer their questions. Most children {4} one another quickly, so the room is noisy but happy. Every volunteer has to {5} a short report at the end of term. The work is unpaid, yet few volunteers {6} it.""",
    b([
        ("A", "take part in", "参加，参与"),
        ("B", "look after", "照顾，照料"),
        ("C", "get along with", "与…友好相处"),
        ("D", "hand in", "交上，递交"),
        ("E", "in charge of", "负责，总管"),
        ("F", "give up", "放弃"),
        ("G", "on purpose", "故意地"),
        ("H", "in the end", "最后，终于"),
    ]),
    {1: "A", 2: "E", 3: "B", 4: "C", 5: "D", 6: "F"},
    {
        1: "want to 后接动词原形；take part in 意为「参加」，与 the club 搭配。",
        2: "be in charge of 意为「负责」，Two volunteers are in charge of each group。",
        3: "look after 意为「照顾、照看」，宾语是 the children。",
        4: "get along with one another 意为「彼此相处融洽」，与后半句 noisy but happy 呼应。",
        5: "hand in 意为「上交」，hand in a report 即「交一份报告」。",
        6: "give up 意为「放弃」；few volunteers give it up 指几乎没人放弃这份工作。",
    },
    [{"en": "volunteer", "zh": "志愿者"}, {"en": "session", "zh": "（一次）活动时段"}],
)
reading("rd4-7", "CET-4", "社区与志愿", "The Empty Lot",
    """There was a piece of empty land behind our apartment block. For years people used it as a car park, and nobody thought much about it. Last spring a few neighbours asked the owners if they could turn part of it into a garden. To everyone's surprise, the owners agreed. Within two months there were twelve wooden boxes of soil, a water tap and a small tool shed. Families each took one box. Children planted beans and tomatoes; older residents grew flowers. Nobody was paid, and the tools were bought with money collected door to door. By autumn the corner had become the busiest place in the block. People who had lived there for ten years and never spoken now met every Saturday morning. The owners have since said the garden can stay.""",
    [
        q("What was the empty land used for before last spring?",
          ["A children's playground", "A car park", "A flower market", "A tool shed"],
          1, "第一句之后：For years people used it as a car park（多年来被当作停车场）。", "detail"),
        q("How was the garden paid for?",
          ["By the owners", "By the local government", "By money collected from neighbours", "By selling vegetables"],
          2, "the tools were bought with money collected door to door（挨家挨户凑钱买的）。", "detail"),
        q("What is the main change the garden brought?",
          ["The land became more valuable.", "Neighbours began to know one another.", "Children stopped playing outside.", "The owners sold the block."],
          1, "倒数第二句：住了十年都没说过话的邻居现在每周六早上见面——花园带来的是邻里关系的改变。", "main"),
    ],
    [{"en": "lot", "zh": "一块地"}, {"en": "shed", "zh": "小棚屋"}, {"en": "resident", "zh": "居民"}])

# ---- 套 8：通勤 ----
phrase(
    "pc4-8", "CET-4", "交通与出行", "The Morning Bus",
    """Every weekday I {1} for the office at seven, because the bus is often late. A minibus {2} passengers at the corner, so I never wait more than five minutes. I am always {3} in the morning, yet I still {4} an old classmate on the bus now and then. Last week we {5} that we had taken the same route for two years without knowing it. If you leave {6} ten minutes earlier, the whole trip feels easier.""",
    b([
        ("A", "set off", "动身，出发"),
        ("B", "pick up", "（车辆）中途搭载"),
        ("C", "in a hurry", "匆忙，急于"),
        ("D", "run into", "偶然遇到"),
        ("E", "work out", "算出；弄明白"),
        ("F", "at least", "至少"),
        ("G", "on purpose", "故意地"),
        ("H", "turn down", "关小；拒绝"),
    ]),
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F"},
    {
        1: "set off for… 意为「动身去…」，与 at seven 呼应。",
        2: "pick up passengers 指车辆「中途接乘客」。",
        3: "in a hurry 意为「匆忙」，be always in a hurry 是常用表达。",
        4: "run into 意为「偶然遇见」，与 now and then（时不时）呼应。",
        5: "work out 意为「弄明白、算出」；此处用过去式 worked out，填字母即可。",
        6: "at least 意为「至少」，at least ten minutes earlier。",
    },
    [{"en": "minibus", "zh": "小巴"}, {"en": "route", "zh": "路线"}],
)
reading("rd4-8", "CET-4", "交通与出行", "Bikes on Campus",
    """Our university started a bike-sharing scheme last September. Five hundred bicycles were placed near the gates, the library and the dining halls. Students unlock them with a phone app and pay by the minute. At first the scheme was so popular that there were never enough bikes at eight in the morning. The office then moved one hundred bicycles from the quieter west gate to the teaching area. It also added painted parking lines, because bikes left across the path had become a problem. Six months later, the number of short bus trips inside the campus had fallen by a third. Some students still complain that the app fails in the rain, and a few older teachers say they would rather walk. But most agree that getting from the dormitory to a lecture now takes half the time.""",
    [
        q("What problem did the office face at first?",
          ["Bikes were too expensive.", "There were not enough bikes in the morning.", "Students did not have phones.", "The buses stopped running."],
          1, "there were never enough bikes at eight in the morning（早上八点车总是不够）。", "detail"),
        q("Why were painted parking lines added?",
          ["To make the campus look nicer", "To mark the bus stops", "Because bikes blocked the path", "Because the app could not find bikes"],
          2, "because bikes left across the path had become a problem（自行车横放在路上成了问题）。", "detail"),
        q("What can be inferred from the last paragraph?",
          ["The scheme has been given up.", "Most users think the scheme saves time.", "Older teachers use the app most.", "Bus trips have increased."],
          1, "most agree that getting from the dormitory to a lecture now takes half the time（多数人认为路程时间减半）。", "inference"),
    ],
    [{"en": "scheme", "zh": "方案"}, {"en": "painted line", "zh": "划定的停车线"}, {"en": "dormitory", "zh": "宿舍"}])

# ---- 套 9：食堂 ----
phrase(
    "pc4-9", "CET-4", "饮食与健康", "The Dining Hall Menu",
    """New students are not always {1} the food in the dining hall; most miss home cooking at first. Within a month, however, they {2} that habit and begin to {3} the cheap set meals, adding fruit from the market. Each term the manager {4} the whole menu and removes dishes that few people order. If the kitchen {5} a popular dish by mistake, students notice at once. The survey is never {6}; it opens on the first Monday of each term.""",
    b([
        ("A", "be fond of", "爱好，喜欢"),
        ("B", "get rid of", "摆脱，除去"),
        ("C", "take advantage of", "利用"),
        ("D", "go over", "检查；从头至尾温习"),
        ("E", "leave out", "遗漏，省略"),
        ("F", "in the end", "最后，终于"),
        ("G", "put off", "推迟，拖延"),
        ("H", "at least", "至少"),
    ]),
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "G"},
    {
        1: "be fond of 意为「喜欢」；are not always fond of 指起初并不总喜欢。",
        2: "get rid of 意为「摆脱、改掉」，宾语是 that habit（想家的习惯）。",
        3: "take advantage of 意为「利用」，指开始利用便宜的套餐。",
        4: "go over 意为「仔细检查、逐一过一遍」，与 the whole menu 搭配。",
        5: "leave out 意为「遗漏、省去」，指厨房漏掉了某道受欢迎的菜。",
        6: "put off 意为「推迟」；调查从不推迟，每学期第一个周一就开放。",
    },
    [{"en": "set meal", "zh": "套餐"}, {"en": "survey", "zh": "问卷调查"}],
)
reading("rd4-9", "CET-4", "饮食与健康", "Breakfast Before Class",
    """A primary school in the north of the city began offering a free breakfast at half past seven. The idea came from a teacher who noticed that several children arrived tired and could not concentrate until mid-morning. The meal is simple: porridge, an egg, milk and a piece of fruit. No one is asked to sign up, and no child is marked out as poor, because everyone eats together in the same hall. After one term, teachers reported fewer visits to the school nurse in the morning and better attention in the first lesson. Parents were more surprised than anyone. Many said their children now left home earlier without being asked. The head teacher admits the scheme costs money, but she points out that it is far cheaper than repeating a year of teaching.""",
    [
        q("Why did the school start the breakfast scheme?",
          ["Some children were too tired to concentrate in the morning.", "The government ordered it.", "Parents asked for a longer school day.", "The old hall was empty."],
          0, "a teacher who noticed that several children arrived tired and could not concentrate until mid-morning.", "detail"),
        q("Why is no child marked out as poor?",
          ["Because the food is free for teachers too", "Because everyone eats together in the same hall", "Because the school does not keep records", "Because only a few children come"],
          1, "because everyone eats together in the same hall（所有人同厅就餐，不区分谁需要帮助）。", "detail"),
        q("What does the head teacher suggest about the cost?",
          ["It is too high to continue.", "Parents should pay for it.", "It is small compared with the cost of children falling behind.", "It will be covered by the nurse."],
          2, "far cheaper than repeating a year of teaching（比留级重读一年便宜得多）。", "inference"),
    ],
    [{"en": "porridge", "zh": "粥"}, {"en": "concentrate", "zh": "集中注意力"}, {"en": "repeat a year", "zh": "留级"}])

# ---- 套 10：借书 ----
phrase(
    "pc4-10", "CET-4", "阅读与图书馆", "A Book Nobody Borrowed",
    """While looking for a novel, you may {1} an old book that nobody has borrowed for years — usually {2}, not because anyone planned it. Our librarian will {3} where it came from and {4} its publication year on the record card. The handwriting is so faint that it is hard to {5} the date. A small exhibition of such books {6} in the reading room every spring.""",
    b([
        ("A", "come across", "偶然发现，偶然遇见"),
        ("B", "look into", "调查，观察"),
        ("C", "point out", "指出，指明"),
        ("D", "make out", "辨认出，看清楚"),
        ("E", "hold on", "握住不放；坚持下去"),
        ("F", "take place", "发生；举行"),
        ("G", "be good at", "善于，擅长于"),
        ("H", "by accident", "偶然"),
    ]),
    {1: "A", 2: "H", 3: "B", 4: "C", 5: "D", 6: "F"},
    {
        1: "come across 意为「偶然发现」，与 While looking for… 的语境一致。",
        2: "by accident 意为「偶然」，与后半句 not because anyone planned it 呼应。",
        3: "look into 意为「调查、查一查」，指追查这本书的来源。",
        4: "point out 意为「指出、标明」，指在登记卡上标出出版年份。",
        5: "make out 意为「辨认出（模糊的字迹）」，与 The handwriting is so faint 呼应。",
        6: "take place 意为「举行」，展览每年春天举办。",
    },
    [{"en": "faint", "zh": "（字迹）模糊的"}, {"en": "exhibition", "zh": "展览"}],
)
reading("rd4-10", "CET-4", "阅读与图书馆", "The Box by the Gate",
    """At the end of our street there is a wooden box on a post, with a glass door and a painted sign: take a book, leave a book. A retired teacher built it three years ago from an old cupboard. It has no lock, no membership and no opening hours. Anyone can walk up, open the door and choose whatever is inside. At first there were only a dozen books, mostly dictionaries. Now the box holds novels, cookbooks, children's picture books and even a few textbooks. Neighbours say the rule works better than they expected: people rarely take without leaving something, and the box has never been damaged. The teacher's only complaint is that she has to straighten the books every few days. Last winter the council put a small roof over the box to keep the rain out. It is, she says, the cheapest library in town.""",
    [
        q("What is the rule of the wooden box?",
          ["Borrow and return within two weeks", "Take a book, leave a book", "Pay a small fee", "Show a library card"],
          1, "牌子上写着 take a book, leave a book（拿一本，留一本）。", "detail"),
        q("What surprised the neighbours?",
          ["The box was never damaged and people follow the rule.", "The teacher closed it in winter.", "Only dictionaries were left.", "The council removed it."],
          0, "people rarely take without leaving something, and the box has never been damaged.", "detail"),
        q("What does \"the cheapest library in town\" suggest?",
          ["The books are of low quality.", "It costs almost nothing to run.", "The council charges for it.", "It is smaller than other libraries."],
          1, "无锁、无会员、无开放时间、由旧柜子改造、只加了个小屋顶——运行成本几乎为零，故称最便宜的图书馆。", "inference"),
    ],
    [{"en": "retired", "zh": "退休的"}, {"en": "membership", "zh": "会员资格"}, {"en": "straighten", "zh": "整理整齐"}])

# ---- 套 11：储蓄 ----
phrase(
    "pc4-11", "CET-4", "兼职与理财", "A Part-time Job",
    """Many students take a part-time job, but few {1} how much they can actually save. A simple rule helps: {2} one evening a week is kept for rest, or you will {3} in your coursework. It is wise to {4} a shift that pays well but leaves no time for sleep. If you {5} for a whole term, the money adds up; {6}, most students say the habit matters more than the amount.""",
    b([
        ("A", "at least", "至少"),
        ("B", "in the end", "最后，终于"),
        ("C", "work out", "算出；想出"),
        ("D", "give up", "放弃"),
        ("E", "fall behind", "落在…后面，跟不上"),
        ("F", "carry on", "继续开展，坚持下去"),
        ("G", "turn down", "关小；拒绝"),
        ("H", "on purpose", "故意地"),
    ]),
    {1: "C", 2: "A", 3: "E", 4: "G", 5: "F", 6: "B"},
    {
        1: "work out 意为「算出」，work out how much they can save。",
        2: "at least 意为「至少」，每周至少留一个晚上休息。",
        3: "fall behind 意为「落后、跟不上」，fall behind in your coursework。",
        4: "turn down 意为「拒绝」，指婉拒报酬高但挤占睡眠的班次。",
        5: "carry on 意为「坚持下去」，坚持一整个学期钱就攒起来了。",
        6: "in the end 意为「最后、说到底」，用于引出结论。",
    },
    [{"en": "shift", "zh": "（轮）班次"}, {"en": "add up", "zh": "累积起来"}],
)
reading("rd4-11", "CET-4", "兼职与理财", "Writing It Down",
    """Lin kept no record of what she spent during her first term. By December she had borrowed money from a roommate twice and could not explain where it had gone. In January she began writing every purchase in a small notebook: bus fares, snacks, a concert ticket, even a bottle of water. She did not try to spend less at first. She only wanted to see the numbers. After three weeks she noticed that small buys between classes came to more than her monthly phone bill. She started carrying a bottle from home and buying fruit at the market instead of at the campus shop. Nothing felt like a sacrifice, she says, because she had not given anything up. By the end of the term she had saved enough to buy a second-hand bicycle. Her roommate now keeps the same notebook.""",
    [
        q("What did Lin do at first to change her spending?",
          ["She borrowed less money.", "She simply wrote down every purchase.", "She stopped going to concerts.", "She got a part-time job."],
          1, "She did not try to spend less at first. She only wanted to see the numbers.（先只记录，不刻意省）", "detail"),
        q("What did she discover after three weeks?",
          ["Her phone bill was too high.", "Small purchases added up to a large amount.", "The campus shop was cheaper.", "Her roommate spent more."],
          1, "small buys between classes came to more than her monthly phone bill.", "detail"),
        q("Why did the changes not feel like a sacrifice?",
          ["She had more money than before.", "She did not feel she had given anything up.", "Her parents paid for the bicycle.", "She stopped keeping the notebook."],
          1, "because she had not given anything up（因为她并不觉得自己放弃了什么）。", "detail"),
    ],
    [{"en": "purchase", "zh": "购买的东西"}, {"en": "sacrifice", "zh": "牺牲"}, {"en": "second-hand", "zh": "二手的"}])

# ---- 套 12：运动会 ----
phrase(
    "pc4-12", "CET-4", "运动与团队", "Sports Day",
    """The college sports day {1} on the last Friday of October. About two hundred students {2} the races, though not all of them {3} running. A teacher is {4} each event and checks that everyone follows the rules. In the relay, the team that {5} early usually {6} cheering until the last runner crosses the line.""",
    b([
        ("A", "take part in", "参加，参与"),
        ("B", "be good at", "善于，擅长于"),
        ("C", "fall behind", "落在…后面，跟不上"),
        ("D", "carry on", "继续开展，坚持下去"),
        ("E", "take place", "发生；举行"),
        ("F", "get along with", "与…友好相处"),
        ("G", "in charge of", "负责，总管"),
        ("H", "on purpose", "故意地"),
    ]),
    {1: "E", 2: "A", 3: "B", 4: "G", 5: "C", 6: "D"},
    {
        1: "take place 意为「举行」，指运动会在十月最后一个周五举办。",
        2: "take part in 意为「参加」，take part in the races。",
        3: "be good at 意为「擅长」，not all of them are good at running。",
        4: "be in charge of 意为「负责」，一位老师负责每个项目。",
        5: "fall behind 意为「落后」，接力中早早落后的队伍。",
        6: "carry on doing 意为「继续做」，carry on cheering 一直加油到最后。",
    },
    [{"en": "relay", "zh": "接力赛"}, {"en": "event", "zh": "比赛项目"}],
)
reading("rd4-12", "CET-4", "运动与团队", "Walking Football",
    """Walking football looks like ordinary football with one important difference: players are not allowed to run. If you run, the other team gets a free kick. The game was designed for people over fifty who want to keep moving without hurting their knees. Our town club started with six members two years ago; it now has more than forty, including several who had not played any sport since school. Matches are short, and everyone plays the same amount of time. Because speed no longer decides the result, passing and positioning matter more. Members say the best part is not the score but the half hour of talk afterwards. One of them, a retired bus driver, puts it simply: at our age, you win by turning up.""",
    [
        q("What is the main rule of walking football?",
          ["Players must not run.", "Only five players are allowed.", "There is no goalkeeper.", "Matches last two hours."],
          0, "players are not allowed to run（不许跑）。", "detail"),
        q("For whom was the game designed?",
          ["Professional footballers", "Children under twelve", "People over fifty", "University teams"],
          2, "designed for people over fifty who want to keep moving without hurting their knees.", "detail"),
        q("What does the retired bus driver mean by \"you win by turning up\"?",
          ["Arriving early guarantees a win.", "Taking part matters more than the result.", "The club needs more players.", "Older players never lose."],
          1, "与前文 the best part is not the score 呼应：在这个年纪，能来参与本身就是胜利。", "inference"),
    ],
    [{"en": "free kick", "zh": "任意球"}, {"en": "positioning", "zh": "跑位，位置感"}, {"en": "turn up", "zh": "到场，露面"}])

# ---- 套 13：网购 ----
phrase(
    "pc4-13", "CET-4", "购物与服务", "Online Orders",
    """Online shopping is convenient, but the parcel does not always {1} on the promised day. Most students {2} their orders at the campus post office instead of waiting at home. If something is damaged, you should {3} the problem with the seller first; {4} one shop in our survey replied on the same day. Sellers rarely send a wrong item {5} — it is usually a mistake made {6} in a busy warehouse.""",
    b([
        ("A", "turn up", "出现，到达"),
        ("B", "pick up", "取（件）；中途搭载"),
        ("C", "get rid of", "摆脱，除去"),
        ("D", "on purpose", "故意地"),
        ("E", "by accident", "偶然"),
        ("F", "at least", "至少"),
        ("G", "work out", "解决；算出"),
        ("H", "put off", "推迟，拖延"),
    ]),
    {1: "A", 2: "B", 3: "G", 4: "F", 5: "D", 6: "E"},
    {
        1: "turn up 意为「出现、到达」，指包裹不一定按承诺日期送到。",
        2: "pick up 意为「取件」，在校邮局取包裹。",
        3: "work out 意为「解决（问题）」，work out the problem with the seller。",
        4: "at least 意为「至少」，调查中至少有一家当天回复。",
        5: "on purpose 意为「故意地」，商家很少故意发错货。",
        6: "by accident 意为「偶然、无意」，与 on purpose 形成对照。",
    },
    [{"en": "parcel", "zh": "包裹"}, {"en": "warehouse", "zh": "仓库"}],
)
reading("rd4-13", "CET-4", "购物与服务", "A Easier Return",
    """Returning goods bought online used to be a slow business at our local shop. Customers had to print a form, find a box and take the parcel to a different counter. Last year the shop changed the whole process. Now a customer shows the order code on a phone, an assistant scans it, and the refund is sent within two days. No printing is needed, and the shop supplies the box. Staff were trained to handle returns at the same desk where they sell goods, so nobody is sent to another queue. The manager expected complaints about the extra work. Instead, returns rose by a fifth, but so did sales. Her explanation is short: people buy more readily when they know that changing their mind is easy. Other shops in the street have since copied the idea.""",
    [
        q("What did customers have to do before last year?",
          ["Pay a return fee", "Print a form and go to a different counter", "Send an email first", "Bring the seller to the shop"],
          1, "had to print a form, find a box and take the parcel to a different counter.", "detail"),
        q("What happened after the process changed?",
          ["Both returns and sales increased.", "Sales fell sharply.", "Staff refused to handle returns.", "The shop closed the return service."],
          0, "returns rose by a fifth, but so did sales（退货量和销售额都涨了）。", "detail"),
        q("What is the manager's explanation?",
          ["Customers dislike printing.", "Easy returns make people more willing to buy.", "The refund is too slow.", "Other shops forced the change."],
          1, "people buy more readily when they know that changing their mind is easy.", "inference"),
    ],
    [{"en": "refund", "zh": "退款"}, {"en": "counter", "zh": "柜台"}, {"en": "readily", "zh": "乐意地"}])

# ---- 套 14：天气 ----
phrase(
    "pc4-14", "CET-4", "天气与出行", "Waiting for the Ferry",
    """When a storm {1} suddenly, the ferry company will {2} the crossing until the wind drops. Passengers who have already {3} for the port are told to {4} and wait in the hall. The annual sailing race cannot {5} that day; {6} it is held a week later.""",
    b([
        ("A", "set off", "动身，出发"),
        ("B", "put off", "推迟，拖延"),
        ("C", "break out", "（暴雨、火灾等）突然发生"),
        ("D", "hold on", "握住不放；等一下，坚持"),
        ("E", "in a hurry", "匆忙，急于"),
        ("F", "take place", "发生；举行"),
        ("G", "in the end", "最后，终于"),
        ("H", "look after", "照顾，照料"),
    ]),
    {1: "C", 2: "B", 3: "A", 4: "D", 5: "F", 6: "G"},
    {
        1: "break out 意为「（暴风雨等）突然发生」，主语是 a storm。",
        2: "put off 意为「推迟」，推迟航班/渡轮直到风小。",
        3: "set off for 意为「动身前往」，已经出发去港口的旅客。",
        4: "hold on 意为「稍等、坚持一下」，让大家在大厅等候。",
        5: "take place 意为「举行」，比赛当天无法举办。",
        6: "in the end 意为「最后」，最终改到一周后举行。",
    },
    [{"en": "ferry", "zh": "渡轮"}, {"en": "crossing", "zh": "（渡海）航程"}],
)
reading("rd4-14", "CET-4", "天气与出行", "A Message Before the Rain",
    """The city's weather service began sending short text messages to farmers two years ago. Before that, most growers relied on the radio or simply looked at the sky. Now, if heavy rain is expected within six hours, a message reaches every registered phone in the district. It says when the rain will start, how long it may last and what to do about young plants. The service is free, and signing up takes one minute at the village office. In the first year, fewer than half the farmers joined. Many did not trust a message more than their own experience. That changed after one storm in July, when those who received the warning covered their seedlings and lost almost nothing. This spring, nine out of ten growers in the district are on the list. The service now plans to add wind and frost warnings as well.""",
    [
        q("How did most growers get weather information before?",
          ["From a phone app", "From the radio or by looking at the sky", "From the village office", "From other farmers' messages"],
          1, "most growers relied on the radio or simply looked at the sky.", "detail"),
        q("Why did many farmers not join at first?",
          ["The service was too expensive.", "They did not have phones.", "They trusted their own experience more.", "The messages arrived too late."],
          2, "Many did not trust a message more than their own experience.", "detail"),
        q("What made most farmers change their minds?",
          ["A free phone offer", "A July storm in which warned farmers lost almost nothing", "A new law", "Frost warnings"],
          1, "that changed after one storm in July, when those who received the warning covered their seedlings and lost almost nothing.", "inference"),
    ],
    [{"en": "grower", "zh": "种植者"}, {"en": "seedling", "zh": "幼苗"}, {"en": "frost", "zh": "霜冻"}])


# ============================================================ CET-6（8 套）
# ---- 套 7：远程办公政策 ----
phrase(
    "pc6-7", "CET-6", "工作与政策", "Rules for Remote Work",
    """{1} recent surveys, firms that allow remote work tend to {2} strict reporting rules rather than loosen them. Managers must {3} the fact that home environments differ, and schedule meetings {4} local time zones. Policies written {5} cutting costs often overlook junior staff. At the annual review, one manager speaks {6} the whole team, and the rules are revised.""",
    b([
        ("A", "in the light of", "根据，鉴于"),
        ("B", "conform to", "符合，遵守"),
        ("C", "make allowance for", "考虑到，顾及"),
        ("D", "in conjunction with", "与…结合／协同"),
        ("E", "with a view to", "为了，着眼于"),
        ("F", "be liable to", "易于，往往会"),
        ("G", "on behalf of", "代表"),
        ("H", "in retrospect", "回想起来"),
    ]),
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "G"},
    {
        1: "in the light of 意为「根据、鉴于」，句首引出依据（近期调查）。",
        2: "conform to 意为「遵守、符合」，tend to 后接原形。",
        3: "make allowance for 意为「顾及、把…考虑在内」，must 后接原形。",
        4: "in conjunction with 意为「与…结合」，指结合当地时区安排会议。",
        5: "with a view to 意为「着眼于、为了」，to 是介词，后接动名词 cutting。",
        6: "on behalf of 意为「代表」，speak on behalf of the whole team。",
    },
    [{"en": "reporting rule", "zh": "汇报制度"}, {"en": "revise", "zh": "修订"}],
)
reading("rd6-7", "CET-6", "信息与媒体", "The Feed That Knows You",
    """Recommendation systems are usually defended on the grounds of convenience: they spare us the labour of choosing. What is less often discussed is how quietly they narrow the choosing itself. A platform that learns which articles you finish will, quite rationally, offer more of the same, because a satisfied reader is a returning one. Over months, the range of what appears on the screen can contract without the reader ever being told that anything was removed. Researchers call this a filter bubble, though the metaphor is mildly misleading — nothing has been sealed, and a determined reader can still search elsewhere. The more accurate complaint is about defaults. Most people do not search elsewhere; they take what is placed in front of them. Regulators have accordingly begun to ask not whether platforms censor, but whether the option to see a different ordering is visible at all. That question is harder to answer, and considerably more useful.""",
    [
        q("How are recommendation systems usually defended?",
          ["They protect users from harmful content.", "They save users the effort of choosing.", "They increase the number of articles written.", "They are required by regulators."],
          1, "on the grounds of convenience: they spare us the labour of choosing（以便利为由：省去选择的力气）。", "detail"),
        q("What does the author say about the term \"filter bubble\"?",
          ["It is completely accurate.", "It slightly misleads, because nothing is actually sealed.", "It was invented by regulators.", "It applies only to search engines."],
          1, "the metaphor is mildly misleading — nothing has been sealed（这个比喻有点误导，因为并没有被封起来）。", "detail"),
        q("What is the author's main point about the real problem?",
          ["Platforms deliberately remove content.", "Readers are too lazy to read long articles.", "The issue is the default ordering that most people accept.", "Regulators have already solved the problem."],
          2, "The more accurate complaint is about defaults… they take what is placed in front of them（问题在于多数人接受的默认排序）。", "main"),
        q("What is the author's attitude towards the regulators' new question?",
          ["Approving", "Sceptical", "Amused", "Indifferent"],
          0, "末句 That question is harder to answer, and considerably more useful（更难、也更有用）——明显是肯定的。", "attitude"),
    ],
    [{"en": "rationally", "zh": "合乎理性地"}, {"en": "contract", "zh": "收缩"}, {"en": "default", "zh": "默认设置"}, {"en": "censor", "zh": "审查，删改"}])

# ---- 套 8：算法争议 ----
phrase(
    "pc6-8", "CET-6", "信息与媒体", "What the Data Said",
    """{1} the launch of the new feed, editors assumed readers wanted variety. The data, {2}, told a different story: most clicks went to a handful of familiar topics. Such a result is {3} the platform's public promise to broaden horizons. Regulators have objected {4} user privacy, while researchers argue that the real problem may {5} how the ranking system rewards repetition. Users themselves must {6} the fact that convenience has a cost.""",
    b([
        ("A", "at odds with", "与…不一致，与…相抵触"),
        ("B", "in retrospect", "回想起来"),
        ("C", "on the grounds of", "根据，以…为由"),
        ("D", "come to terms with", "接受，与…妥协"),
        ("E", "boil down to", "归结为"),
        ("F", "in pursuit of", "追求"),
        ("G", "prior to", "在…之前"),
        ("H", "be apt to", "易于，倾向于"),
    ]),
    {1: "G", 2: "B", 3: "A", 4: "C", 5: "E", 6: "D"},
    {
        1: "prior to 意为「在…之前」，Prior to the launch 作时间状语。",
        2: "in retrospect 意为「回想起来」，作插入语，前后用逗号隔开。",
        3: "be at odds with 意为「与…相抵触」；句中已有 is，填 at odds with。",
        4: "on the grounds of 意为「以…为理由」，object on the grounds of user privacy。",
        5: "boil down to 意为「归结为」，may 后接原形。",
        6: "come to terms with 意为「接受（不如意的事实）」，must 后接原形。",
    },
    [{"en": "feed", "zh": "信息流"}, {"en": "ranking", "zh": "排序"}, {"en": "repetition", "zh": "重复"}],
)
reading("rd6-8", "CET-6", "工作与政策", "The Office After the Office",
    """When a large technology firm moved most of its staff to remote work, managers expected the main difficulty to be technical. It was not. Within a year the complaint that surfaced most often was subtler: junior employees no longer knew how the work was actually decided. In a shared room, a newcomer learns by overhearing — who asks which question, when a silence means disagreement, how a compromise is reached. Video calls transmit the conclusion of such exchanges but rarely the exchange itself. Senior staff, meanwhile, reported fewer interruptions and higher satisfaction, which made the discrepancy easy to miss. The firm's response was not to call everyone back. It created short, documented decision reviews in which the reasoning behind a choice is written down and opened to questions. Whether this substitutes for presence remains uncertain. What the episode suggests is that the value of an office lay less in its desks than in the accidental education it provided.""",
    [
        q("What problem did junior employees report?",
          ["Poor internet connections", "They could not see how decisions were actually made.", "Too many video calls", "Senior staff ignored their emails"],
          1, "junior employees no longer knew how the work was actually decided.", "detail"),
        q("Why was the problem easy to overlook?",
          ["Junior staff did not complain.", "Senior staff were more satisfied and less interrupted.", "The firm changed its software.", "Decisions were already documented."],
          1, "Senior staff… reported fewer interruptions and higher satisfaction, which made the discrepancy easy to miss.", "detail"),
        q("What does \"accidental education\" refer to?",
          ["Formal training courses", "Learning by overhearing how experienced colleagues work", "Online tutorials", "Written decision reviews"],
          1, "a newcomer learns by overhearing（新人靠旁听学到东西）——即无意中获得的经验。", "vocab"),
        q("What is the author's tone towards the firm's solution?",
          ["Fully convinced", "Cautiously non-committal", "Openly critical", "Amused"],
          1, "Whether this substitutes for presence remains uncertain（是否替代得了在场，仍不确定）——措辞审慎。", "attitude"),
    ],
    [{"en": "overhear", "zh": "无意中听到"}, {"en": "discrepancy", "zh": "差异，不一致"}, {"en": "substitute for", "zh": "替代"}])

# ---- 套 9：语言档案 ----
phrase(
    "pc6-9", "CET-6", "语言与文化", "Saving a Language",
    """Linguists note that the loss of a language can rarely {1} a single event; more often it {2} decades of pressure on the community that speaks it. {3} a detailed survey, several schools have begun teaching local vocabulary again. {4} the 1990s, such efforts were almost unknown. Some archives still {5} recordings that no one has catalogued, while a few are {6} any documentation at all.""",
    b([
        ("A", "stem from", "源于，来自"),
        ("B", "be attributed to", "把…归因于"),
        ("C", "in accordance with", "与…一致，按照"),
        ("D", "dispose of", "处理掉，清除"),
        ("E", "on behalf of", "代表"),
        ("F", "be devoid of", "缺乏，毫无"),
        ("G", "prior to", "在…之前"),
        ("H", "owing to", "由于，因为"),
    ]),
    {1: "B", 2: "A", 3: "C", 4: "G", 5: "D", 6: "F"},
    {
        1: "be attributed to 意为「归因于」；can rarely be attributed to a single event。",
        2: "stem from 意为「源于」，more often it stems from decades of pressure。",
        3: "in accordance with 意为「依照、按照」，句首引出依据。",
        4: "prior to 意为「在…之前」，Prior to the 1990s 指上世纪九十年代以前。",
        5: "dispose of 意为「处理掉、清除」，指档案仍在处理无人编目的录音。",
        6: "be devoid of 意为「完全没有」；句中已有 are，填 devoid of。",
    },
    [{"en": "linguist", "zh": "语言学家"}, {"en": "catalogue", "zh": "编目"}, {"en": "documentation", "zh": "文献记录"}],
)
reading("rd6-9", "CET-6", "语言与文化", "The Last Speakers",
    """A language is often declared dead on the strength of a number: the count of people who still speak it at home. That measure is convenient, and it is misleading. In several communities studied recently, fluent speakers in their seventies use the language mainly with one another, while their grandchildren understand it but answer in the dominant tongue. Whether the language survives depends less on this generation's vocabulary than on whether anyone has a reason to use it tomorrow. Recording the elders is therefore necessary but not sufficient; an archive preserves a voice, not a conversation. The projects that appear to work are modest and unromantic. They pay for a weekly market stall where the language is the normal way to bargain, or for a radio hour of local news. Such efforts rarely produce a dictionary. They produce something harder to count and more decisive: a setting in which speaking the language is simply what one does.""",
    [
        q("Why does the author call the speaker count misleading?",
          ["The numbers are usually wrong.", "It ignores whether the language has a context in which it is used.", "Grandchildren often speak it fluently.", "Archives already record every speaker."],
          1, "depends less on this generation's vocabulary than on whether anyone has a reason to use it tomorrow（关键是有没有使用场合）。", "detail"),
        q("What does \"an archive preserves a voice, not a conversation\" mean?",
          ["Recordings cannot capture pronunciation.", "Recording alone does not keep a language in use.", "Archives rarely include elders.", "Conversations are too long to record."],
          1, "录音保存的是声音，而不是活生生的交谈——单靠存档无法让语言继续被使用。", "vocab"),
        q("What do the successful projects have in common?",
          ["They publish dictionaries.", "They create everyday situations where the language is used naturally.", "They focus on teaching grandchildren.", "They are funded by universities."],
          1, "a setting in which speaking the language is simply what one does（营造自然语言使用场景）。", "inference"),
        q("Which word best describes the author's view of the projects?",
          ["Dismissive", "Pragmatic", "Nostalgic", "Sceptical"],
          1, "modest and unromantic、rarely produce a dictionary 但 more decisive——务实地肯定其效果。", "attitude"),
    ],
    [{"en": "on the strength of", "zh": "依据"}, {"en": "dominant tongue", "zh": "占主导地位的语言"}, {"en": "decisive", "zh": "决定性的"}])

# ---- 套 10：城市绿地 ----
phrase(
    "pc6-10", "CET-6", "城市与规划", "Rules for New Squares",
    """{1} the city's new plan, any square {2} a main road must include trees. {3} the extra cost, the council requires soil depth {4} one metre. {5} frequent summer heat, shade is now treated as infrastructure rather than decoration. Older districts, {6} stricter limits on building height, have been slower to change.""",
    b([
        ("A", "adjacent to", "与…毗连的"),
        ("B", "in excess of", "超过"),
        ("C", "by virtue of", "凭借，由于"),
        ("D", "be subject to", "受…支配；易受…的"),
        ("E", "with regard to", "关于，至于"),
        ("F", "in view of", "鉴于，考虑到"),
        ("G", "for the sake of", "为了，为了…的利益"),
        ("H", "in addition to", "除…之外（还）"),
    ]),
    {1: "E", 2: "A", 3: "H", 4: "B", 5: "F", 6: "D"},
    {
        1: "with regard to 意为「关于、就…而言」，句首引出规划的范围。",
        2: "adjacent to 意为「毗邻」，any square adjacent to a main road。",
        3: "in addition to 意为「除…之外还」，指除增加成本外还有要求。",
        4: "in excess of 意为「超过」，soil depth in excess of one metre。",
        5: "in view of 意为「鉴于」，引出原因（夏季频繁高温）。",
        6: "be subject to 意为「受…约束」；此处用过去分词作后置定语，填 subject to。",
    },
    [{"en": "square", "zh": "广场"}, {"en": "soil depth", "zh": "土层深度"}, {"en": "infrastructure", "zh": "基础设施"}],
)
reading("rd6-10", "CET-6", "城市与规划", "Cooler Streets",
    """Cities are routinely several degrees warmer than the countryside around them, a difference produced by dark surfaces, sparse vegetation and the heat released by buildings. The effect is not evenly distributed. Mapping studies in several large cities show that the hottest districts are frequently those with the fewest trees, and that these are often the same districts with the oldest housing and the lowest incomes. This correlation has turned a technical question about materials into a question about fairness. Planting trees sounds like a simple remedy, yet it is slow: a sapling provides little shade for a decade, and in dry regions it needs water that may itself be scarce. Some planners therefore favour lighter pavements and reflective roofs, which cool a street immediately. Others warn that such measures, precisely because they are quick, can be used to postpone the slower investment. The sensible reading is not that one approach wins, but that the timing of benefit matters as much as its size.""",
    [
        q("What produces the temperature difference between city and countryside?",
          ["Higher rainfall in cities", "Dark surfaces, little vegetation and heat from buildings", "Colder winds from nearby hills", "Fewer people living in rural areas"],
          1, "produced by dark surfaces, sparse vegetation and the heat released by buildings.", "detail"),
        q("Why has the issue become a question about fairness?",
          ["Trees are expensive to import.", "The hottest districts often have older housing and lower incomes.", "Reflective roofs are only available to the rich.", "Rural areas receive more funding."],
          1, "the hottest districts… are often the same districts with the oldest housing and the lowest incomes.", "detail"),
        q("What disadvantage of planting trees is mentioned?",
          ["Trees increase the need for air conditioning.", "A young tree gives little shade for years and needs water.", "Trees cannot grow in cities.", "They are disliked by residents."],
          1, "a sapling provides little shade for a decade, and in dry regions it needs water.", "detail"),
        q("What does the last sentence imply?",
          ["Quick fixes should always be preferred.", "Only large benefits are worth pursuing.", "When a benefit arrives is as important as how large it is.", "Planners should stop planting trees."],
          2, "the timing of benefit matters as much as its size（见效时间与效果大小同样重要）。", "inference"),
    ],
    [{"en": "sparse", "zh": "稀少的"}, {"en": "sapling", "zh": "树苗"}, {"en": "reflective", "zh": "反光的"}])

# ---- 套 11：政策委员会 ----
phrase(
    "pc6-11", "CET-6", "教育与健康", "The Start-time Committee",
    """The committee is {1} seven members, only two of whom {2} the proposal to delay start times. The report is {3} sleep duration rather than test scores alone, and it {4} its claims with three years of attendance data. Officials who {5} evidence rather than habit have begun to change the timetable. Parents are advised to be {6} screens late at night.""",
    b([
        ("A", "be composed of", "由…组成"),
        ("B", "be concerned with", "关心，涉及"),
        ("C", "be cautious of", "留心…，谨防…"),
        ("D", "act on", "按照…而行动"),
        ("E", "appeal to", "呼吁；对…有吸引力"),
        ("F", "approve of", "赞成，满意"),
        ("G", "back up", "支持，援助"),
        ("H", "be addicted to", "沉溺于"),
    ]),
    {1: "A", 2: "F", 3: "B", 4: "G", 5: "D", 6: "C"},
    {
        1: "be composed of 意为「由…组成」；is composed of seven members。",
        2: "approve of 意为「赞成」，只有两位成员赞成该提议。",
        3: "be concerned with 意为「关注的是」，is concerned with sleep duration。",
        4: "back up 意为「支持、为…提供佐证」，back up its claims with data。",
        5: "act on 意为「按…行事」，act on evidence 即依据证据行动。",
        6: "be cautious of 意为「对…留心、谨防」，提醒留意夜间屏幕。",
    },
    [{"en": "committee", "zh": "委员会"}, {"en": "attendance", "zh": "出勤"}, {"en": "duration", "zh": "时长"}],
)
reading("rd6-11", "CET-6", "文化与伦理", "Who Should Hold the Objects",
    """Debates about returning cultural objects are usually conducted as arguments about ownership, and that framing makes them hard to settle. Legal title, where it exists, is often clear; what is contested is whether a clear title is the same as a just one. Museums point to conservation: they have the climate control, the staff and the records that many objects would lack elsewhere. Institutions in countries of origin reply that preservation is not the only value at stake, and that an object kept behind glass far from the community that made it preserves material while severing meaning. Both claims are serious. What has changed is not the law but the willingness of museums to admit that their founding collections were assembled under conditions no longer defended. Several have begun long-term loans, shared catalogues and joint research rather than outright transfer. Critics call this a half-measure. It may also be the only arrangement durable enough to survive a change of government.""",
    [
        q("Why are these debates hard to settle according to the author?",
          ["The law is unclear in every case.", "They are framed as ownership, while the real dispute is about justice.", "Museums refuse to discuss conservation.", "No records of the objects survive."],
          1, "framed as arguments about ownership… whether a clear title is the same as a just one（争的是正当性而非名义所有权）。", "detail"),
        q("What is the museums' main argument?",
          ["They bought everything legally.", "They can preserve the objects better.", "Origin countries have no museums.", "The objects have no meaning now."],
          1, "Museums point to conservation: they have the climate control, the staff and the records.", "detail"),
        q("What does \"severing meaning\" mean?",
          ["Damaging the object physically", "Separating an object from the culture that gives it significance", "Losing the catalogue record", "Ending a loan agreement"],
          1, "preserves material while severing meaning：保住了实物，却切断了它与原社群的意义联系。", "vocab"),
        q("What is the author's view of long-term loans and joint research?",
          ["They fully resolve the dispute.", "They are a practical compromise that may last.", "They are worse than doing nothing.", "They are legally required."],
          1, "末句：可能是唯一「足够持久、能熬过政府更迭」的安排——视其为务实且耐久的折中。", "attitude"),
    ],
    [{"en": "legal title", "zh": "合法所有权"}, {"en": "conservation", "zh": "文物保护"}, {"en": "outright transfer", "zh": "彻底归还"}])

phrase(
    "pc6-12", "CET-6", "资源与环境", "Pricing Water",
    """Charges for household water are {1} seasonal review, and any increase {2} one percent must be published a month in advance. The authority must {3} households using very little water when it designs the tariff. {4} a dry winter, the region {5} stricter limits on irrigation. {6} these pressures, officials still refuse to describe the situation as a crisis.""",
    b([
        ("A", "be subject to", "受…支配；须经…"),
        ("B", "in excess of", "超过"),
        ("C", "make allowance for", "考虑到，体谅"),
        ("D", "in the wake of", "紧随…之后"),
        ("E", "be attributed to", "把…归因于"),
        ("F", "in view of", "鉴于，考虑到"),
        ("G", "conform to", "符合，遵守"),
        ("H", "in accordance with", "与…一致，按照"),
    ]),
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "A", 6: "F"},
    {
        1: "be subject to 意为「须经、受…约束」；are subject to seasonal review（须按季复核）。",
        2: "in excess of 意为「超过」，any increase in excess of one percent（任何超过 1% 的涨幅）。",
        3: "make allowance for 意为「顾及、体谅」，must 后接原形。",
        4: "in the wake of 意为「紧随…之后」，指干旱冬季之后。",
        5: "同样用 be subject to：the region is subject to stricter limits（须遵守更严格的灌溉限额）；词组可重复使用，符合真题规则。",
        6: "in view of 意为「鉴于」，句首引出让步背景：尽管有这些压力，官方仍不称其为危机。",
    },
    [{"en": "tariff", "zh": "（水、电）价目表"}, {"en": "irrigation", "zh": "灌溉"}, {"en": "crisis", "zh": "危机"}],
)
reading("rd6-12", "CET-6", "资源与环境", "The Price of a Tap",
    """Water is almost everywhere treated differently from other goods, and for good reason: a household cannot reasonably choose to do without it. Yet the way it is priced often assumes that demand behaves as it would for anything else. In many cities the first units consumed are charged at a low rate intended to cover basic needs, while heavy use is charged more steeply. The design is defensible, but its effects are uneven. A large family on a modest income may reach the expensive band simply by having more children, whereas a single person in a spacious flat never does. Metering, meanwhile, is frequently least reliable in the oldest districts, exactly where consumption is hardest to estimate. Economists tend to discuss such problems as matters of efficiency. Residents describe them in a different vocabulary — as fairness. Neither account is wrong; they simply measure different things, and a tariff has to answer to both.""",
    [
        q("Why is water treated differently from other goods?",
          ["It is difficult to transport.", "Households cannot reasonably go without it.", "It is owned by the state everywhere.", "Its price never changes."],
          1, "a household cannot reasonably choose to do without it.", "detail"),
        q("What problem does the pricing design create?",
          ["It discourages all use of water.", "A large low-income family may reach the expensive band just by having more children.", "Single people pay the highest rate.", "Meters are too accurate."],
          1, "A large family on a modest income may reach the expensive band simply by having more children.", "detail"),
        q("What does the last sentence suggest about a tariff?",
          ["Efficiency is the only valid measure.", "Fairness should replace efficiency entirely.", "It must satisfy both efficiency and fairness.", "Residents misunderstand the economics."],
          2, "Neither account is wrong… a tariff has to answer to both（两种标准都要顾及）。", "inference"),
        q("What is the author's tone?",
          ["Critical but balanced", "Strongly opposed to metering", "Light-hearted", "Openly partisan"],
          0, "既指出设计 defensible（可辩护）又指出 effects are uneven（效果不均），末句承认两种视角都不错——克制且平衡。", "attitude"),
    ],
    [{"en": "steeply", "zh": "（价格）大幅地"}, {"en": "band", "zh": "档，区间"}, {"en": "metering", "zh": "水表计量"}])

# ---- 套 13：默认选项 ----
phrase(
    "pc6-13", "CET-6", "行为与决策", "How Defaults Work",
    """The effect is usually {1} a preference for the familiar rather than to any deliberate choice. {2} the experiment, participants were told they could change any setting, and most did not. {3} strict rules on disclosure, the form still {4} the old option first. Reviewers have warned that such designs {5} be challenged in court, {6} their claim that consent was freely given.""",
    b([
        ("A", "be attributed to", "把…归因于"),
        ("B", "in the course of", "在…过程中"),
        ("C", "in accordance with", "与…一致，按照"),
        ("D", "be apt to", "易于，倾向于"),
        ("E", "on the grounds of", "根据，以…为由"),
        ("F", "be capable of", "有能力…"),
        ("G", "in view of", "鉴于，考虑到"),
        ("H", "set out", "陈列，列明"),
    ]),
    {1: "A", 2: "B", 3: "C", 4: "H", 5: "D", 6: "E"},
    {
        1: "be attributed to 意为「归因于」；is usually attributed to a preference…。",
        2: "in the course of 意为「在…过程中」，句首时间状语。",
        3: "in accordance with 意为「依照」，指依照严格的信息披露规定。",
        4: "set out 意为「列出、陈明」，the form still set out the old option first（表格仍把旧选项列在前面）。",
        5: "be apt to 意为「易于、往往会」；such designs are apt to be challenged。",
        6: "on the grounds of 意为「以…为理由」，指以「同意系自愿给出」为由（受到质疑）。",
    },
    [{"en": "default", "zh": "默认选项"}, {"en": "disclosure", "zh": "信息披露"}, {"en": "consent", "zh": "同意"}],
)
reading("rd6-13", "CET-6", "行为与决策", "The Line Already Filled In",
    """Few policy tools are as quiet as a pre-ticked box. When a form arrives with a choice already made, most people leave it alone — not because they have weighed the matter and agreed, but because changing a default requires an extra step and a moment's attention. Studies of organ-donation registers and retirement savings show the same pattern across countries: where enrolment is automatic, participation is high; where a box must be ticked, it falls sharply, even though the underlying decision is identical. Defenders call this helpful nudging, since most people say they intend to enrol anyway. Critics reply that an intention never acted upon is not obviously the same as consent, and that the ease of opting out matters less than whether anyone noticed the option existed. The empirical finding is not really in dispute. What remains contested is whether a result that people would have chosen counts as a choice they made.""",
    [
        q("Why do most people leave a pre-ticked box unchanged?",
          ["They have carefully considered and agreed.", "Changing it takes an extra step and attention.", "The law forbids changing it.", "They do not understand the form."],
          1, "changing a default requires an extra step and a moment's attention.", "detail"),
        q("What do the studies show across countries?",
          ["Automatic enrolment leads to much higher participation.", "People dislike retirement savings.", "Opting out is always difficult.", "Ticking a box increases participation."],
          0, "where enrolment is automatic, participation is high; where a box must be ticked, it falls sharply.", "detail"),
        q("What do critics question?",
          ["Whether the data are accurate", "Whether an unacted-upon intention counts as consent", "Whether defaults save money", "Whether people intend to enrol"],
          1, "an intention never acted upon is not obviously the same as consent.", "detail"),
        q("What is the central issue according to the last sentence?",
          ["How to design a clearer form", "Whether an outcome people would have chosen is a choice they actually made", "Whether nudging is legal", "How many people opt out"],
          1, "whether a result that people would have chosen counts as a choice they made（「本会选的结果」是否等于「做出的选择」）。", "main"),
    ],
    [{"en": "pre-ticked", "zh": "预先勾选的"}, {"en": "enrolment", "zh": "登记加入"}, {"en": "nudging", "zh": "助推"}])

phrase(
    "pc6-14", "CET-6", "工作与政策", "A Shorter Week",
    """{1} the trial, every department had to record how meetings were scheduled. {2} the first six months, output stayed level and staff reported less fatigue. {3} these results, the council voted to continue, though two members did not {4} the change. A full report is expected {5} the end of the year; {6} its findings, the council will decide whether the scheme becomes permanent.""",
    b([
        ("A", "prior to", "在…之前"),
        ("B", "in the course of", "在…过程中"),
        ("C", "in view of", "鉴于，考虑到"),
        ("D", "approve of", "赞成，满意"),
        ("E", "subsequent to", "在…之后"),
        ("F", "in the light of", "根据，鉴于"),
        ("G", "on the verge of", "濒于，即将"),
        ("H", "appeal to", "呼吁；对…有吸引力"),
    ]),
    {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F"},
    {
        1: "prior to 意为「在…之前」，Prior to the trial（试点开始前）。",
        2: "in the course of 意为「在…期间」，in the course of the first six months。",
        3: "in view of 意为「鉴于」，句首引出依据（这些结果）。",
        4: "approve of 意为「赞成」，did not approve of the change。",
        5: "subsequent to 意为「在…之后」，完整报告预计在年底之后发布。",
        6: "in the light of 意为「根据、参照」，in the light of its findings（参照报告结论再决定）。与 in view of 近义，按位置区分。",
    },
    [{"en": "trial", "zh": "试点"}, {"en": "fatigue", "zh": "疲劳"}, {"en": "permanent", "zh": "永久的"}],
)
reading("rd6-14", "CET-6", "工作与政策", "The Fifth Day",
    """Trials of a four-day week tend to be reported in one of two ways: either as proof that shorter hours cost nothing, or as evidence that they cannot last. Both readings simplify what the trials actually measure. Most involve firms that volunteered, which is to say firms already confident that their work could be reorganised; the least suitable cases never entered the sample. Output is usually held constant by removing meetings rather than by speeding people up, a gain that may be available only once. Employees, unsurprisingly, report better sleep and less intention to leave — outcomes that matter, but that are not the same as productivity. None of this makes the trials worthless. It does mean that the honest conclusion is narrower than the headlines: for some kinds of work, under some conditions, a shorter week can be introduced without an immediate loss. Whether it generalises is a question about organisations, not about the calendar.""",
    [
        q("Why does the author say both common readings are too simple?",
          ["The trials measured neither productivity nor attendance.", "Participating firms were volunteers likely suited to shorter hours.", "No employees reported any benefit.", "The trials lasted only one week."],
          1, "Most involve firms that volunteered… the least suitable cases never entered the sample（样本本身有选择性）。", "detail"),
        q("How is output usually kept constant in the trials?",
          ["By hiring more staff", "By cutting meetings", "By extending each working day", "By reducing pay"],
          1, "by removing meetings rather than by speeding people up.", "detail"),
        q("What does the author say about better sleep and lower turnover?",
          ["They are unimportant.", "They are valuable but not the same as productivity.", "They prove the four-day week always works.", "They were not measured."],
          1, "outcomes that matter, but that are not the same as productivity.", "detail"),
        q("What is the main conclusion of the passage?",
          ["A four-day week should be adopted everywhere.", "The trials were badly designed and prove nothing.", "The results are real but limited to certain kinds of work and conditions.", "Governments should legislate a shorter week."],
          2, "for some kinds of work, under some conditions… without an immediate loss（结论有条件、范围更窄）。", "main"),
    ],
    [{"en": "volunteer", "zh": "自愿参加"}, {"en": "turnover", "zh": "人员流失"}, {"en": "generalise", "zh": "推广，泛化"}])


# ============================================================ 校验 + 合并
def validate(existing):
    errs = []
    old_ids = {p["id"] for p in existing["phrase"]} | {r["id"] for r in existing["reading"]}
    seen = set()
    for p in NEW_PHRASE + NEW_READING:
        if p["id"] in old_ids: errs.append(f"id 与现有题库冲突: {p['id']}")
        if p["id"] in seen: errs.append(f"新题 id 重复: {p['id']}")
        seen.add(p["id"])
        if p["level"] not in ("CET-4", "CET-6"): errs.append(f"{p['id']} level 非法")

    for p in NEW_PHRASE:
        keys = [x["key"] for x in p["bank"]]
        if len(keys) != len(set(keys)): errs.append(f"{p['id']} bank 字母重复")
        kset = set(keys)
        found = [int(x) for x in re.findall(r"\{(\d+)\}", p["passage"])]
        if sorted(found) != sorted(p["answers"].keys()):
            errs.append(f"{p['id']} 空格与 answers 不一致: {sorted(found)} vs {sorted(p['answers'].keys())}")
        for n, k in p["answers"].items():
            if k not in kset: errs.append(f"{p['id']} 第{n}空答案 {k} 不在 bank")
            if n not in p["explain"] or not str(p["explain"][n]).strip():
                errs.append(f"{p['id']} 第{n}空缺解析")
        if not p["title"] or not p["passage"]: errs.append(f"{p['id']} 缺标题/正文")
        if len(p["bank"]) < len(p["answers"]) + 1:
            errs.append(f"{p['id']} 干扰项不足（bank 应多于空数）")

    for r in NEW_READING:
        wc = len(r["passage"].split())
        if not (90 <= wc <= 200): errs.append(f"{r['id']} 词数 {wc} 不在 90–200")
        if not r["questions"]: errs.append(f"{r['id']} 无题目")
        for j, qq in enumerate(r["questions"]):
            if len(qq["options"]) != 4: errs.append(f"{r['id']} 第{j+1}题选项数≠4")
            if not (0 <= qq["answer"] < 4): errs.append(f"{r['id']} 第{j+1}题答案越界")
            if not qq.get("explain"): errs.append(f"{r['id']} 第{j+1}题缺解析")
    return errs


def balance_options(data):
    """把全题库阅读选择题的正确答案位置均衡到 A/B/C/D。

    只交换「正确选项」与「目标位置选项」两项，其余选项顺序不动，解析文字不受影响
    （解析描述的是内容而非字母）。目标位置序列按固定种子打乱，因此：
      - A/B/C/D 分布均匀，且相邻题无固定规律，避免被猜答案；
      - 完全确定性、可重复运行（幂等：重复运行不会继续打乱）。
    """
    # 按难度分组各自均衡，保证 CET-4 与 CET-6 内部也各占约 1/4
    for level in ("CET-4", "CET-6"):
        questions = [
            qq for r in data["reading"] if r["level"] == level
            for qq in r["questions"]
        ]
        targets = [i % 4 for i in range(len(questions))]
        random.Random(20261109 + (0 if level == "CET-4" else 1)).shuffle(targets)
        for qq, target in zip(questions, targets):
            cur = qq["answer"]
            if cur == target:
                continue
            opts = qq["options"]
            opts[cur], opts[target] = opts[target], opts[cur]
            qq["answer"] = target



def shuffle_phrase_banks(data):
    """打乱每段词组填空的 Word Bank，使答案不再是「第1空 A、第2空 B…」的顺序。

    先用答案对应的英文词组**内容**记住每个空格的正确项，再把 bank 按 en 排序还原成
    规范态（与当前字母无关），用固定种子洗牌后重新赋 A/B/C/… 字母，最后按内容把
    答案映射到新字母。解析按空号索引且描述词组内容，不引用字母，故不受影响；
    前端按 bank 数组顺序渲染，界面字母仍然整齐。

    幂等：每次都从「按 en 排序」的规范态出发，固定种子决定排列，重跑结果一致。
    """
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for idx, item in enumerate(data["phrase"]):
        by_key = {b["key"]: b for b in item["bank"]}
        correct_en = {n: by_key[k]["en"] for n, k in item["answers"].items()}
        canonical = sorted(item["bank"], key=lambda b: b["en"])
        random.Random(20261112 + idx).shuffle(canonical)
        en_to_key = {}
        for i, b in enumerate(canonical):
            b["key"] = letters[i]
            en_to_key[b["en"]] = b["key"]
        assert set(correct_en.values()) <= set(en_to_key), item["id"] + " 正确词丢失"
        item["bank"] = canonical
        item["answers"] = {n: en_to_key[en] for n, en in correct_en.items()}

def main():
    with open(OUT, encoding="utf-8") as f:
        existing = json.load(f)
    # 幂等：先移除本批 id 的旧条目，重复运行不会累积重复题
    new_ids = {p["id"] for p in NEW_PHRASE} | {r["id"] for r in NEW_READING}
    existing["phrase"] = [p for p in existing["phrase"] if p["id"] not in new_ids]
    existing["reading"] = [r for r in existing["reading"] if r["id"] not in new_ids]
    errs = validate(existing)
    if errs:
        print("校验失败:")
        for e in errs: print("  -", e)
        sys.exit(1)
    existing["phrase"].extend(NEW_PHRASE)
    existing["reading"].extend(NEW_READING)
    # 均衡选项位置（对全题库，含第一批），使答案分布均匀且不可猜。
    # 幂等：目标位置由固定种子+题目顺序决定，重跑时正确选项已在目标位，故不再交换。
    balance_options(existing)
    shuffle_phrase_banks(existing)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    print("校验通过 ✓")
    c4p = sum(1 for p in NEW_PHRASE if p["level"] == "CET-4")
    c6p = sum(1 for p in NEW_PHRASE if p["level"] == "CET-6")
    c4r = sum(1 for r in NEW_READING if r["level"] == "CET-4")
    c6r = sum(1 for r in NEW_READING if r["level"] == "CET-6")
    print(f"本次新增: 词组填空 {len(NEW_PHRASE)} 段（CET-4 {c4p} / CET-6 {c6p}），"
          f"共 {sum(len(p['answers']) for p in NEW_PHRASE)} 空")
    print(f"           短篇阅读 {len(NEW_READING)} 篇（CET-4 {c4r} / CET-6 {c6r}），"
          f"共 {sum(len(r['questions']) for r in NEW_READING)} 题")
    print(f"题库合计: 词组 {len(existing['phrase'])} 段 / 阅读 {len(existing['reading'])} 篇")
    for r in NEW_READING:
        print(f"  {r['id']} {r['level']} {len(r['passage'].split())}词 {len(r['questions'])}题")
    print("输出:", OUT)


if __name__ == "__main__":
    main()
