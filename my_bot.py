
import telebot
from telebot import types

token = "5479631641:AAHz_sY7SlufNNRHLONGl8T_o7KjgSYbx94"
bot = telebot.TeleBot(token)
 

service_button = types.KeyboardButton("Юридические услуги⚖")
stat_button = types.KeyboardButton("Статьи✒")
tel_button = types.KeyboardButton("Обратная связь☎")
doc_button = types.KeyboardButton("Услуги по составлению документов🖊")
reg_button = types.KeyboardButton("Регистрационные услуги💼")
exp_button = types.KeyboardButton("Экспертиза документов🔎")
sud_button = types.KeyboardButton("Судебное представительство🛡")
inostr_button = types.KeyboardButton("Услуги для иностранных граждан💂")
btn_contract = types.InlineKeyboardButton("Составление договоров📜")
btn_isk = types.InlineKeyboardButton("Составление заявлений📎")
btn_ust = types.InlineKeyboardButton("Составление учредительных документов🔨")
btn_reg = types.InlineKeyboardButton("Регистрация ТОО🧱")
btn_perereg = types.InlineKeyboardButton("Перерегистрация ТОО🔗")
btn_izm = types.InlineKeyboardButton("Регистрация внесения изменений🧹")
back_button = types.KeyboardButton("Назад🔙")
btn_expdog = types.InlineKeyboardButton("Экспертиза договоров и соглашений🔎📜")
btn_expuch = types.InlineKeyboardButton("Анализ учредительных документов компаний🔎📚")
btn_iin = types.InlineKeyboardButton("Получение ИИН📂")
btn_bin = types.InlineKeyboardButton("Получение БИН💼")
btn_ecp = types.InlineKeyboardButton("Получение ЭЦП🔑")
btn_fil = types.InlineKeyboardButton("Открытие филиалов🏰")
back_button1 = types.KeyboardButton("Назад⬅")
btn_comm = types.InlineKeyboardButton("Коммерческие споры🏛")
btn_stroy = types.InlineKeyboardButton("Строительные споры🏗")
btn_zem = types.InlineKeyboardButton("Земельные споры⛰")
btn_debt = types.InlineKeyboardButton("Возврат долгов💰")
btn_inostrcom = types.InlineKeyboardButton("Как иностранцу открыть компанию в РК?🌍💼")
btn_zakldog = types.InlineKeyboardButton("На что следует обращать внимание при заключении договоров?🤝📄")
btn_debtvozv = types.InlineKeyboardButton("Как возвратить долг?🤏💸")
btn_pereregstat = types.InlineKeyboardButton("В каких случаях компания подлежит государственной перерегистрации?🛠🏢")


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup().add(service_button).add(stat_button).add(tel_button)
    bot.send_message(message.chat.id, "Здравствуйте, вы попали в чат бот LawyerInAlmaty ✋\n\nС помощью бота Вы можете ознакомиться с перечнем юридических услуг и стоимостью на данные услуги. Также Вы можете прочесть юридические статьи, которые со временем будут добавляться.\n\nВыберите интересующую категорию⬇", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def primer(message):
    markup = types.ReplyKeyboardMarkup()
    if message.text == 'Юридические услуги⚖':
        markup = types.ReplyKeyboardMarkup().add(doc_button).add(reg_button).add(exp_button).add(sud_button).add(inostr_button).add(back_button1)
        bot.send_message(message.chat.id, "Выберите", reply_markup=markup)

    if message.text == "Услуги по составлению документов🖊":
        markup = types.ReplyKeyboardMarkup().add(btn_contract).add(btn_isk).add(btn_ust).add(back_button)
        bot.send_message(message.chat.id, "Выберите", reply_markup=markup)     

    if message.text == "Составление договоров📜":   
        bot.send_message(message.chat.id, "Стоимость услуги от 20 000 тенге в зависимости от сложности🛒")

    if message.text == "Составление заявлений📎":   
        bot.send_message(message.chat.id, "Составление исков - от 15 000 тенге\nСоставление жалоб и обращений - от 20 000 тенге\nСоставление претензий - от 10 000 тенге🛒")

    if message.text == "Составление учредительных документов🔨":   
        bot.send_message(message.chat.id, "Разработка уставов - от 20 000 тенге\nСоставление решений-протоколов общего собрания участников - от 10 000 тенге\nСоставление учредительного договора - 10 000 тенге🛒")

    if message.text == "Назад🔙":   
        markup = types.ReplyKeyboardMarkup().add(doc_button).add(reg_button).add().add(exp_button).add(sud_button).add(inostr_button).add(back_button1)
        bot.send_message(message.chat.id, "Выберите", reply_markup=markup)

    if message.text == "Назад⬅":   
        markup = types.ReplyKeyboardMarkup().add(service_button).add(stat_button).add(tel_button)
        bot.send_message(message.chat.id, "Выберите", reply_markup=markup)

    if message.text == "Регистрационные услуги💼":
        markup = types.ReplyKeyboardMarkup().add(btn_reg).add(btn_perereg).add(btn_izm).add(back_button)
        bot.send_message(message.chat.id, "Выберите", reply_markup=markup) 

    if message.text == "Регистрация ТОО🧱":   
        bot.send_message(message.chat.id, "Стоимость услуги от 35 000 тенге в зависимости от количества участников и объема документов🛒\nВ услугу входит:\n-Процедура регистрации ТОО на портале электронного правительства\n-Разработка устава\n-Составление решения о создании ТОО\n-Составление приказа о вступлении в должность директора\n-Разработка учредительного договора(в случае если участников более одного)\n-Изготовление печати")

    if message.text == "Перерегистрация ТОО🔗":   
        bot.send_message(message.chat.id, "Стоимость услуги 55 000 тенге🛒\nВ услугу входит:\n-Проведение процедуры перерегистрации в регистрирующем органе\n-Разработка учредительных документов в новой редакции/приложений к учредительным документам\n-Замена печати(при необходимости)\n-Оплата регистрационного сбора")

    if message.text == "Регистрация внесения изменений🧹":   
        bot.send_message(message.chat.id, "Стоимость услуги от 25 000 тенге в зависимости от категории вносимых изменений🛒") 

    if message.text == "Экспертиза документов🔎":
        markup = types.ReplyKeyboardMarkup().add(btn_expdog).add(btn_expuch).add(back_button)
        bot.send_message(message.chat.id, "Выберите", reply_markup=markup) 

    if message.text == "Экспертиза договоров и соглашений🔎📜":   
        bot.send_message(message.chat.id, "Стоимость услуги от 25 000 тенге за экспертизу одного документа🛒")

    if message.text == "Анализ учредительных документов компаний🔎📚":   
        bot.send_message(message.chat.id, "Стоимость услуги от 30 000 тенге за экспертизу одного документа🛒")

    if message.text == "Судебное представительство🛡":
        markup = types.ReplyKeyboardMarkup().add(btn_comm).add(btn_stroy).add(btn_zem).add(btn_debt).add(back_button)
        bot.send_message(message.chat.id, "Выберите", reply_markup=markup) 

    if message.text == "Коммерческие споры🏛":   
        bot.send_message(message.chat.id, "Споры между юридическими лицами и государственными органами, стоимость услуги от 400 000 тенге в зависимости от сложности дела, в услугу входит представление интересов в суде первой инстанции🛒")

    if message.text == "Строительные споры🏗":   
        bot.send_message(message.chat.id, "Споры вытекающие из договоров строительного подряда, стоимость услуги от 350 000 тенге в зависимости от сложности дела, в услугу входит представление интересов в суде первой инстанции🛒")

    if message.text == "Земельные споры⛰":   
        bot.send_message(message.chat.id, "Стоимость услуги от 500 000 тенге, в зависимости от сложности дела, в услугу входит представление интересов в суде первой инстанции🛒")

    if message.text == "Возврат долгов💰":   
        bot.send_message(message.chat.id, "Стоимость услуги от 150 000 тенге в зависимости от суммы иска, в услугу входит представление интересов в суде первой инстанции🛒")

    if message.text == "Услуги для иностранных граждан💂":
        markup = types.ReplyKeyboardMarkup().add(btn_iin).add(btn_bin).add(btn_ecp).add(btn_fil).add(back_button)
        bot.send_message(message.chat.id, "Выберите", reply_markup=markup) 

    if message.text == "Получение ИИН📂":   
        bot.send_message(message.chat.id, "Стоимость услуги по получению индивидуального идентификационного номера и регистрации иностранца в качестве налогоплательщика от 20 000 тенге🛒")

    if message.text == "Получение БИН💼":   
        bot.send_message(message.chat.id, "Стоимость услуги по получению бизнес идентификационного номера от 35 000 тенге🛒")
    
    if message.text == "Получение ЭЦП🔑":   
        bot.send_message(message.chat.id, "Стоимость услуги по получению электронной цифровой подписи для нерезидентов физических лиц от 30 000 тенге\nСтоимость услуги по получению электронной цифровой подписи для нерезидентов юридических лиц 50 000 тенге🛒") 
    
    if message.text == "Открытие филиалов🏰":   
        bot.send_message(message.chat.id, "Стоимость услуги учетной регистрации филиалов от 140 000 тенге🛒")

    if message.text == "Статьи✒":
        markup = types.ReplyKeyboardMarkup().add(btn_inostrcom).add(btn_zakldog).add(btn_debtvozv).add(btn_pereregstat).add(back_button1)
        bot.send_message(message.chat.id, "Выберите", reply_markup=markup) 

    if message.text == "Как иностранцу открыть компанию в РК?🌍💼":   
        bot.send_message(message.chat.id, "Для начала иностранцу необходимо зарегистрироваться в качестве налогоплательщика Республики Казахстан и получить индивидуальный идентификационный номер либо бизнес идентификационный номер.\nДалее иностранцу необходимо получить электронную цифровую подпись на свое имя и зарегистрироваться в мобильной базе данных Республики Казахстан.\nПосле чего необходимо принять решение о создании компании, разработать учредительные документы и пройти процедуру государственной регистрации юридического лица на портале электронного правительства egov.kz.\nВ случае успешного прохождения процедуры государственной регистрации, компания будет считаться зарегистрированной на территории Республики Казахстан, а иностранное лицо будет являться учредителем данной компании.\nПосле государственной регистрации компании, необходимо изготовить фирменную печать компании и открыть счет в банке второго уровня РК.\nБолее подробно Вы можете узнать по номеру +7 707 225 26 20📞")

    if message.text == "На что следует обращать внимание при заключении договоров?🤝📄":   
        bot.send_message(message.chat.id, "Перед тем как заключать договор с тем или иным лицом рекомендуется проверить информацию о данном юридическом лице из открытых государственных источников Республики Казахстан,\nтаких как судебный кабинет, реестр должников по исполнительным производствам и портал комитета государственных доходов. если по результатам проверки, за компанией не числится каких-либо нарушений можно заключать договор.\nДоговор может содержать множество условий как предусмотренных законодательством, так и нет.\nОднако основные условия, на которые следует обратить внимание в договоре являются: условие о порядке взаиморасчетов, права и обязанности сторон договора, ответственность сторон, порядок разрешение споров и применимое право, условие об изменении и расторжении договора.\nИсходя из юридической практики, чаще всего предприниматели сталкиваются с рисками вытекающие из данных условий договора.\nВместе с тем данные условия не являются исчерпывающими, это лишь основные условия, которые должны содержаться в договоре, при этом содержание договора в основном зависит от характера и природы предмета договорных отношений.\nБолее подробно Вы можете узнать по номеру +7 707 225 26 20📞")

    if message.text == "Как возвратить долг?🤏💸":   
        bot.send_message(message.chat.id, "В случае если с должником заключен договор, то зачастую условиями договора предусматривается претензионный порядок, то есть перед тем как обратиться в суд, необходимо направить письмо претензионного характера в адрес должника с требованием о возврате долга и установлением сроков возврата.\nВ случае если должник проигнорировал данное письмо либо ответил неудовлетворительно, то следует обратиться с иском о взыскании долга в суд.\nВ случае если с должником договор не заключался, то в любом случае перед тем как обратиться в суд необходимо направить претензионное письмо по известному адресу должника.\nДоказательством передачи денежных средств в долг могут служить: переписки с должником как письменные, так и электронные в частности в мессенджерах за которыми зарегистрирован мобильный номер должника, аудио и видео фиксации разговоров факта передачи денежных средств, а также другие обстоятельства, подтверждающие факт передачи денежных средств.\nДля того чтобы имелись шансы возвратить долг рекомендуется заключать договор либо составлять расписку о передаче денег в долг, в случае если по каким-либо причинам вы не заключили договор и не составили расписку, все переговоры с должником необходимо вести письменно либо путем личной переписки через мессенджер whatsapp.\nБолее подробно Вы можете узнать по номеру +7 707 225 26 20📞")

    if message.text == "В каких случаях компания подлежит государственной перерегистрации?🛠🏢":   
        bot.send_message(message.chat.id, "В процессе осуществления своей предпринимательской деятельности компания может столкнуться с множествами внутрикорпоративными изменениями.\nОднако основания, влекущие перерегистрацию компании, будут являться:\n- изменения состава участников;\n- смена наименования;\n- уменьшения уставного капитала.\nВ каждом из видов оснований для перерегистрации компаний имеются отличительные особенности.\nИзменение состава участников возможно после заключения договора купли-продажи доли уставного капитала, который заключается у нотариуса.\nПри смене наименования, замене также подлежит фирменная печать компании.\nПроцедура уменьшения уставного капитала компании занимает длительное время более 2 месяцев и требует от компании официального опубликования объявления в печатном источнике об уменьшении уставного капитала.\nОстальные изменения, возникающие в хозяйственной деятельности компании, например, такие как смена юридического адреса, смена директора, изменения в учредительные документы, увеличение уставного капитала и другие не влекут перерегистрацию, компании достаточно лишь уведомить территориальный регистрирующий орган о данных изменениях.\nБолее подробно Вы можете узнать по номеру +7 707 225 26 20📞")
 
    if message.text == "Обратная связь☎":
        bot.send_message(message.chat.id, "Контактный номер (Whatsapp)📱✆:\n+7 707 225 26 20\nПодписывайтесь на наш инстаграм♞@: jurist_almaty_")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('Отправить свой контакт ☎️', request_contact=True)).add(back_button1)
        bot.send_message(message.chat.id, "Отправьте свой контакт, мы свяжемся с Вами в ближайшее время📠", reply_markup=markup) 

bot.polling(non_stop=True)
   





        

   
  
    










   

 


   
    

    

    
    


  















        

   
  
    










   

 


   
    

    

    
    


  












