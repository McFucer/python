q1 = input('''Мне больше подходит (выберите один вариант):

1. Делать свою работу независимо от других людей.
2. Работать в команде, в сотрудничестве с другими людьми
3. Управлять людьми, организовывать их работу
__''')

q2 = input('''Во время учебы в школе у меня в большей 
степени проявлялись способности (выберите не более  вариантов):

1. К рисованию, прикладному творчеству   
2. К музыке, пению или диджеингу (создание 
музыкальных сетов)
3. К точным наукам (информатика, математика, 
физика, химия)
__''')

q3 = input('''В свободное время я предпочту (выберите не более  вариантов):

1. Играть в компьютерные игры   
2. Делать что-то красивое (рисовать, шить, мастерить поделки)
3. Общаться в соцсетях (писать посты, размещать фото)
4. Читать книги   
5. Заниматься спортом или смотреть спортивные соревнования
5. Общаться с друзьями, посещать вечеринки и мероприятия
6. Смотреть кино, сериалы, видео
__''')

q4 = input('''Я лучше воспринимаю и запоминаю информацию (выберите  вариант):

1. На слух   
2. С помощью картинок и образов   
3. Чтобы лучше запомнить, мне нужно понять логику, разобраться
__''')

q5 = input('''Мне больше нравится (выберите  вариант):

1. Решать задачи, где нужно поразмышлять, "поломать" голову
2. Исследовать, анализировать, "раскладывать по
полочкам"   
3. Придумывать что-то новое, экспериментировать
__''')

q6 = input('''Я в большей степени интересуюсь событиями в сфере(выберите не 
более  вариантов) :
1. Спорта   
2. Кино и телевидения   
3. Бизнеса   
4. Компьютерных технологий и игр   
5. Музыки   
6. Дизайна и моды
__''')

q7 = input('''Для меня проще и приятнее (выберите не более  вариантов):
1. Разобраться, как работает незнакомая компьютерная программа
   
2. Написать текст или документ организовать работу других людей   
составить бюджет или финансовый отчет сделать что-то своими руками
(нарисовать, сшить,смастерить)
__''')

q8 = input('''Какие соцсети вы предпочитаете и наболее активно ведете 
там свои аккаунты (выберите не более  вариантов):
     
1. Twitter
2. ВКонтакте
3. FaceBook
4. Instagram
5. Linkedin
6. Pinterest
7. Вообще не использую соцсети в своей жизни(вы далбaеб?)
__''')



import re


def remove_numbers_and_letters(text):
    # Удаление чисел
    text_without_numbers = re.sub(r'\d+', '', text)

    # Удаление английских букв
    text_without_letters = re.sub(r'[a-zA-Z]', '', text_without_numbers)

    return text_without_letters


text = '''ᑯɪʟઽⲏ૦ᑯ•🖤, [17.07.2023 22:18]
Мне больше подходит
(выберите 1 вариант):
1 A делать свою работу независимо от других людей 1 1 2
работать в команде, в сотрудничестве с другими 
людьми
B 3 2 2
C управлять людьми, организовывать их работу 2 1 2
Во время учебы в школе
у меня в большей
степени проявлялись
способности (выберите
не более 2 вариантов):
2 A к рисованию, прикладному творчеству 1 9 1
к музыке, пению или диджеингу (создание 
музыкальных сетов)
B 1 1 1
к точным наукам (информатика, математика, 
физика, химия)
C 7 1 2
В свободное время я
предпочту (выберите не
более 2 вариантов):
3 A играть в компьютерные игры 3 3 1
делать что-то красивое (рисовать, шить, мастерить 
поделки)
B 1 6 1
общаться в соцсетях (писать посты, размещать 
фото)
C 1 1 6
D читать книги 1 1 2
заниматься спортом или смотреть спортивные 
соревнования
E 1 1 1
общаться с друзьями, посещать вечеринки и 
мероприятия
F 1 1 2
G смотреть кино, сериалы, видео 1 2 1
Я лучше воспринимаю и
запоминаю информацию
(выберите 1 вариант):
4 A на слух 1 1 1
B с помощью картинок и образов 1 5 1
чтобы лучше запомнить, мне нужно понять логику, 
разобраться
C 4 1 2
Запишите промежуточные

баллы в этих окошках3
Запишите промежуточные

баллы в этих окошках
АйТи Дизайн Маркетинг
Мне больше нравится 
(выберите 1 вариант):
5 решать задачи, где нужно поразмышлять,
"поломать" голову
A 8 1 1
исследовать, анализировать, "раскладывать по
полочкам"
B 3 1 3
C придумывать что-то новое, экспериментировать 2 3 2
Я в большей степени 
интересуюсь событиями 
в сфере(выберите не 
более 2 вариантов) :
6 A спорта 1 1 1
B кино и телевидения 1 1 1
C бизнеса 2 1 6
D компьютерных технологий и игр 5 4 1
E музыки 1 1 1
F дизайна и моды 1 2 1
Для меня проще и 
приятнее (выберите не 
более 2 вариантов):
7 разобраться, как работает незнакомая
компьютерная программа
A 7 3 1
B написать текст или документ 1 1 5
C организовать работу других людей 2 1 2
D составить бюджет или финансовый отчет 1 1 1
сделать что-то своими руками (нарисовать, сшить,
смастерить)
E 1 5 1
Какие соцсети вы 
предпочитаете и 
наболее активно ведете 
там свои аккаунты 
(выберите не более 2 
вариантов):
8 A Twitter 1 1 1
B ВКонтакте 1 1 2
C Facebook 1 1 2
D Instagram 1 3 3
E LinkedIn 1 1 1
F Pinterest 1 3 1
G вообще не использую соцсети в своей жизни 1 1 14
АйТи Дизайн Маркетинг
Представьте, что вы
участвуете в съемках
фильма. Какая роль в
этом процессе вам
ближе (выберите не
более 2 вариантов):
9 A актер 1 1 1
B художник по костюмам 1 1 1
C разработчик компьютерной графики 1 6 1
D каскадер, постановщик трюков 1 1 1
E режиссер 1 1 2
F визажист 1 1 1
G оператор 1 1 1
H продюсер 1 1 1
I сценарист 1 1 2
J создатель спецэффектов 1 2 1
Мне больше подходит
(выберите 1 вариант):
10 постоянная работа на полную занятость в частной 
компании
A 3 1 1
внештатная работа на разные организации в 
качестве подрядчика
B 1 1 2
C работа в государственной организации 1 1 1
D развитие своего бизнеса, своего бренда 1 2 1
Для успеха в бизнесе
наиболее важно
(выберите 1 вариант):
11 создать уникальный, востребованный продукт или 
услугу
A 2 2 2
уметь продвигать и продавать свой товар или 
услугу
B 1 1 8
C грамотно управлять финансами и людьми 2 1 1
Я лучше справляюсь с
задачами, которые
требуют (выберите 1
вариант):
12 A концентрации, вдумчивости 3 1 2
B инициативы, самостоятельного принятия решений 1 1 1
гибкости, хорошего понимания потребностей 
заказчика
C 2 4 5
Запишите промежуточные

ᑯɪʟઽⲏ૦ᑯ•🖤, [17.07.2023 22:18]
баллы в этих окошках5
АйТи Дизайн Маркетинг
Мне проще работать
(выберите 1 вариант):
13 A с цифрами и таблицами 1 1 1
B с людьми 2 1 2
C с инструментами и материалами 1 3 1
D с компьютерными программами 6 3 2
Для меня важнее
(выберите 1 вариант):
14 быть известным в своей сфере, построить свой 
персональный бренд
A 1 1 1
иметь увлекательную работу, связанную с 
творчеством
B 1 5 1
иметь работу, которая, прежде всего, дает 
возможности карьерного роста
C 2 1 2
быть стабильно востребованным специалистом на 
рынке труда
D 3 1 3
Моя сильная сторона
(выберите 1 вариант):
15 A аналитический склад ума, развитая логика 4 1 2
творческие способности, художественный вкус, 
креативность
B 1 4 1
C гибкость, быстрая обучаемость и адаптация 2 2 3
D общительность, умение убеждать людей 1 1 2
Мне абсолютно не
подходит (выберите не
более 2 вариантов):
16 A работа с людьми 1 -1 -1
B монотонная работа, требующая усидчивости 1 1 1
C работа с цифрами 1 1 1
работа с техникой и сложными компьютерными 
программами
D -4 -1 1
публичная деятельность, где нужно выступать 
перед людьми, записывать видео и т.п.
E 1 1 1
Запишите промежуточные

баллы в этих окошках6
АйТи Дизайн Маркетинг
Какие красивые объекты
вам приятнее всего
рассматривать
(выберите не более 2
вариантов):
17 A цветы 1 2 1
B красивую одежду 1 2 1
C картины художников 1 2 1
D красивые лица людей 1 1 1
E красивые движения людей (в спорте, в танцах) 1 1 1
G драгоценности, украшения 1 4 1
1 1 1
F красивые интерьеры
H красивую анимацию 1 2 1
Мне комфортнее
работать (выберите 1
вариант):
18 когда мне дают конкретную задачу и адекватный 
план
A 2 1 2
когда я сам ставлю себе задачи и планирую свою 
работу
B 2 1 2
C когда я ставлю задачи другим людям 1 1 1
D на "драйве", увлеченности и вдохновении 1 2 1
Я скорее выберу
(выберите 1 вариант):
19 работать по свободному графику, с высоким, но 
нестабильным доходом
A 1 1 1
проектную работу с оплатой за выполненные 
проекты
B 1 2 2
стандартную 40 часовую рабочую неделю с 
гарантированной оплатой труда
C 3 1 2
У меня лучше получается
(выберите 1 вариант):
20 A анализировать факты, оценивать что-либо 2 1 3
понимать потребности людей и мотивы их 
поведения
B 1 1 2
C придумывать что-то новое, создавать с "нуля" 2 1 1
D делать из хаоса порядок 2 2 2
Запишите промежуточные

баллы в этих окошках7
АйТи Дизайн Маркетинг
Жизнь для меня была бы
гораздо скучнее без
(выберите 1 вариант):
21 A без фильмов, сериалов, видеороликов 1 2 1
B без музыки 1 1 1
C без соцсетей 1 1 5
D без компьютерных игр 1 2 1
E без спорта 1 1 1
В работе мне больше
всего не нравится
(выберите не более 2
вариантов):
22 подчиняться требованиям и решениям, которые я 
не считаю верными
A 1 1 1
B интриги, сплетни, разборки 1 1 1
когда мою работу не замечают и не оценивают по 
достоинству
C 1 1 1
D однообразие и скучные задачи 1 1 1
E когда меня критикуют 1 1 1
Когда мне нужно
объяснить что-то людям,
я чаще использую
(выберите 1 вариант):
23 A картинки, рисунки, образы 1 4 1
B схемы, чертежи 3 2 1
C цифры, таблицы, графики 2 1 2
D только слова 1 1 3
Я считаю, что для
успешной карьеры
нужно (выберите 1
вариант):
24 иметь широкий кругозор и знания во многих 
областях
A 1 1 2
не распыляться, а глубоко разбираться именно в 
своей специальности
B 2 2 2
C иметь амбиции и способности к управлению 1 1 1
На технической выставке
я больше обращаю
внимание (выберите 1
вариант):
25 A на внешний вид экспонатов, на то, как они выглядят 1 3 1
B на внутреннее устройство экспонатов 3 1 1
C на то, как их можно применить 1 1 1
Запишите промежуточные

ᑯɪʟઽⲏ૦ᑯ•🖤, [17.07.2023 22:18]
баллы в этих окошках8
АйТи Дизайн Маркетинг
Я предпочту (выберите 1
вариант):
26 в короткий срок изучить узкую область знаний и 
сразу начать работать, расширяя свой опыт на 
практике
A 2 2 3
получить основательные, широкие знания по 
профессии и лишь затем начать работать, чтобы не 
доучиваться на ходу
B 1 1 1
По натуре я (выберите не
более 2 вариантов):
27 A командир и организатор 1 1 1
B тот, кто помогает людям 1 1 1
C свободный художник 1 1 1
D внимательный исследователь 2 1 2
E предприимчивый и "бизнесовый" 1 1 2
F вдохновитель, мотиватор, "заводила" 1 1 2
Для меня более
комфортно:
28 A концентрироваться на одном деле, не отвлекаясь 2 2 2
переключаться на разные задачи, чтобы не 
заскучать
B 1 1 1
C делать несколько дел одновременно 1 1 1
Мне не нравится
(выберите 1 вариант):
29 A работа, в которой нет никакого творчества 1 1 1
B работа в условиях постоянного стресса 1 1 1
работа, связанная с материальной 
ответственностью
C 1 1 1
D работа в государственных организациях 1 1 1
У меня хуже всего
получается (выберите не
более 2 вариантов):
30 A долго концентрировать внимание на одном деле 1 1 1
B торговаться о цене на что-либо 1 1 1
C разбираться в цифрах -1 1 1
D делать что-то в стрессе, при дефиците времени 1 1 1
E писать тексты и документы 1 1 -3
F делать работу, в которой не очевиден результат 1 1 1
Запишите промежуточные

баллы в этих окошках9
АйТи Дизайн Маркетинг
На сегодняшний день
для меня важнее
(выберите 1 вариант):
31 строить карьеру, чтобы в будущем иметь достойную 
должность
A 2 1 2
обеспечить свою финансовую независимость и 
стабильность
B 2 2 2
C найти баланс между работой и жизнью 1 1 1
D найти себе дело "по душе", самореализоваться 1 2 1
Мне в большей степени
присущи такие деловые
качества, как (выберите
не более 2 вариантов):
32 A грамотная речь (устная и письменная) 1 1 3
B инициативность и новаторство 2 1 1
C клиентоориентированность 2 2 3
D пунктуальность, соблюдение сроков 2 1 1
E умение вести переговоры 1 1 1
F аккуратность в работе с документами 1 1 1
В какие компьютерные
игры вы чаще играете?
(выберите не более 2
вариантов)
33 A экшен (требующие хорошей моторики) 1 2 1
B симуляторы (спортивные, автогонки и т.п.) 1 1 1
C стратегии (управление ресурсами) 1 1 1
D ролевые (изменение персонажей) 1 1 1
E приключения (преодоление препятствий) 1 1 1
F головоломки 2 1 1
G вообще не играю в компьютерные игры 1 1 1
Запишите промежуточные

баллы в этих окошках10
АйТи Дизайн Маркетинг
Я совсем не люблю
(выберите не более 2
вариантов):
34 A танцевать 1 1 1
B разбираться с финансами 1 1 1
C сниматься на видео 1 1 1
D устанавливать компьютерные программы -2 -1 1
E шить 1 1 1
F спорт 1 1 1
G писать документы 1 1 -3
Меня, в большей
степени, мотивирует
(выберите не более 2
вариантов):
35 уважение и признание со стороны окружающих 
людей
A 1 1 1
B полезное, социально значимое дело 1 1 1
C дружный, веселый, драйвовый коллектив 1 1 1
D увлекательная, творческая работа 1 4 2
E работать "на острие" передовых технологий 3 1 2
F возможность быть лидером, вести людей за собой 1 1 1
У меня лучше развиты
(выберите 1 вариант):
36 A вкус, чувство стиля 1 2 1
B навыки общения 1 1 2
C аналитические  способности 4 1 2
D интуиция 1 1 2
У меня совершенно нет
способностей (выберите
не более 2 вариантов):
37 A к рисованию 1 -2 1
B к математике -2 1 1
C к музыке 1 1 1
D к педагогике 1 1 1
E к продажам 1 1 1
F к журналистике 1 1 -2
Запишите промежуточные

ᑯɪʟઽⲏ૦ᑯ•🖤, [17.07.2023 22:18]
баллы в этих окошках11
АйТи Дизайн Маркетинг
Я чаще (выберите 1
вариант):
38 A читаю книги 1 1 2
B фотографирую 1 2 1
C играю в компьютерные игры 2 2 1
D занимаюсь спортом 1 1 1
E не делаю ничего из перечисленного 1 1 1
Мои слабые стороны
(выберите не более 2
вариантов):
39 у меня недостаточно хорошо развита мелкая 
моторика (не люблю шить, мастерить из мелких 
деталей и т.п.)
A 1 1 1
у меня недостаточно уверенности в общении с 
другими людьми
B 1 1 1
у меня недостаточно развито пространственное 
мышление и воображение
C 1 -7 1
я недостаточно хорошо управляю своим временем 
(не могу точно рассчитать время, опаздываю)
D 1 1 1
я недостаточно хорошо управляю своими 
финансами (склонен к импульсивным покупкам, не 
отслеживаю свой бюджет)
E 1 1 1
я упрямый человек, недостаточно гибкий, не умею 
идти на компромисс
F 1 1 1
У меня есть довольно
успешный опыт
(выберите не более 2
пунктов из списка):
40 A в руководстве людьми 1 1 1
B в образовании и воспитании 1 1 1
C в киберспорте 2 1 1
D в маркетинге, PR, рекламе 1 2 4
E в создании видеороликов 1 2 1
F в прикладном творчестве, дизайне 1 4 1
G в финансовой сфере 1 1 1
H в музыке 1 1 1
пока нет никакого опыта ни в одной из этих 
областей
I 1 1 1
Запишите промежуточные

баллы в этих окошках12
АйТи Дизайн Маркетинг
Для меня проще
(выберите 1 вариант):
41 урегулировать конфликтную ситуацию, разрешить 
спор
A 1 1 1
B решить математическую задачу, головоломку 6 1 1
C придумать сценарий праздника 1 1 2
D записать видео для тик-ток 1 1 1
Представьте, что вы с
друзьями организуете
вечеринку. Какая роль в
этом процессе вам
больше по душе
(выберите не более 2
вариантов)?
42 я тот, кто ищет место для вечеринки и продумывает 
доставку всех и всего
A 1 1 1
я тот, кто придумывает идею для вечеринки и ее 
сценарий
B 1 1 2
я тот, кто подсчитывает расходы на вечеринку и 
планирует бюджет
C 1 1 1
я тот, кто распределяет между участниками 
обязанности по подготовке
D 1 1 1
E я тот, кто фотографирует всех на вечеринке 1 1 1
F я тот, кто выбирает и закупает еду и напитки 1 1 1
я тот, кто отвечает за музыку и делает плейлист 
вечеринки
G 1 1 1
я тот, кто всех развлекает на вечеринке и делает ее 
веселой
H 1 1 1
Я, как правило (выберите
1 вариант):
43 скрупулезно и внимательно проверяю документы и 
тексты, которые пишу
A 1 1 2
заполняю документы и пишу тексты быстро, но 
часто делаю ошибки
B 1 1 1
очень не люблю заполнять и проверять документы, 
стараюсь этого избегать
C 1 1 1
Запишите промежуточные

баллы в этих окошках13
АйТи Дизайн Маркетинг
Я предпочитаю одежду
(выберите 1 вариант):
44 A классический, деловой, "офисный" стиль 1 1 1
B спортивная, "кэжуал", практичная 1 2 1
C модная, стильная, неформальная 1 1 1
всегда подбираю одежду, подходящую для 
конкретной ситуации
D 1 1 1
Моя суперспособность
(выберите не более 2
вариантов):
45 я не боюсь выступать на публике и могу "зажечь" 
аудиторию
A 1 1 1
B я могу продать что угодно кому угодно 1 1 1
C я умею решать сложные задачи и никогда не сдаюсь 5 1 1
я могу понять любого человека и найти с ним общий 
язык
D 1 1 1
E я умею создавать красоту вокруг себя 1 4 1
F я могу все просчитать и оценить в цифрах 2 1 1
я умею спорить, доказывать и отстаивать свое 
мнение
G 1 1 1
я умею договариваться с чиновниками и знаю к ним 
подход
H 1 1 1
Финансовая мотивация,
которая мне больше
подходит:
46 A оклад + премии за выполнение показателей 1 1 2
нестабильный, но никем не ограниченный доход со 
своего бизнеса
B 1 1 1
C небольшой оклад + высокий процент с продаж 1 1 1
стабильный оклад с постепенным повышением за 
выслугу лет и опыт
D 3 1 2
Запишите промежуточные

ᑯɪʟઽⲏ૦ᑯ•🖤, [17.07.2023 22:18]
баллы в этих окошках14
АйТи Дизайн Маркетинг
Какие некомпьютерные
игры вам нравятся?
(выберите не более 2
вариантов)
47 A спортивные командные (типа футбола, волейбола) 1 1 1
B шахматы, го 2 1 1
C азартные игры (типа покера, преферанса) 1 1 1
D спортивные парные (теннис, сквош, бадминтон) 1 1 1
E настолки 1 1 1
F социальные (мафия, крокодил, квесты) 1 2 1
G вообще никогда не играю ни во что такое 1 1 1
Я не умею и не люблю
(выберите 1 вариант):
48 A хитрить, подстраиваться под людей, льстить 1 1 1
B убеждать, навязывать свое мнение, спорить 1 1 1
контролировать других людей, проверять их работу 
и указывать на ошибки
C 1 1 1
Я чаще читаю (выберите
не более 2 вариантов):
49 A научно-популярную литературу 1 1 1
B фантастику или фэнтези 1 2 1
C детективы 1 1 1
D психологическую литературу 1 1 1
E литературу по бизнесу и маркетингу 1 1 3
F историческую литературу 1 1 1
G справочники и техническую литературу 2 1 1
Мне ближе (выберите 1
вариант):
50 порядок, четкие задачи и инструкции, 
определенность
A 2 1 2
возможность выйти за рамки и стандарты, 
творческий беспорядок, непосредственность

Убери отсюда все числа и английские большие буквы'''
text_without_numbers_and_letters = remove_numbers_and_letters(text)
print(text_without_numbers_and_letters)