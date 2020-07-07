import vk
import config
import del_name

session = vk.Session(config.tokenVK)
api = vk.API(session, v='5.85')
id_name = "0"

def mama(s):
    result = s.replace("маме ", "")
    return result

def papa(s):
    result = s.replace("папе ", "")
    return result

def inna(s):
    result = s.replace("инне ", "")
    return result

def roma(s):
    result = s.replace("роме ", "")
    return result

def seva(s):
    result = s.replace("севе ", "")
    return result

def mne(s):
    result = s.replace("мне ", "")
    return result

def mama2(s):
    result = s.replace("Маме ", "")
    return result

def papa2(s):
    result = s.replace("Папе ", "")
    return result

def inna2(s):
    result = s.replace("Инне ", "")
    return result

def roma2(s):
    result = s.replace("Роме ", "")
    return result

def seva2(s):
    result = s.replace("Севе ", "")
    return result

def mne2(s):
    result = s.replace("Мне ", "")
    return result

def remove_char(s):
    result = s.replace("Новый пост ", "")
    return result

def remove_char1(s):
    result = s.replace("новый пост ", "")
    return result

def del_name(s):
    a = mama(s)
    b = papa(a)
    c = inna(b)
    d = roma(c)
    e = seva(d)
    f = mne(e)
    g = mama2(f)
    h = papa2(g)
    i = inna2(h)
    j = roma2(i)
    k = seva2(j)
    result = mne2(k)
    return result

def name_to_id(s):
    global id_name
    if s == "Маме" or s == "маме":
        id_name = "516717987"
    elif s == "Папе" or s == "папе":
        id_name = "3883837"
    elif s == "Инне" or s == "инне":
        id_name = "25070022"
    elif s == "Роме" or s == "роме":
        id_name = "397205762"
    elif s == "Севе" or s == "севе":
        id_name = "507564168"
    elif s == "Мне" or s == "мне":
        id_name = "267303926"
    return id_name

def remove_charmess(s):
    result = s.replace("Отправь сообщение ", "")
    return result

def remove_charmess1(s):
    result = s.replace("отправь сообщение ", "")
    return result

def message_send(event, context):
    intents = event.get('request', {}).get('nlu', {}).get('intents', {})
    command = event.get('request', {}).get('command')
    chto = event.get('request', {}).get('nlu', {}).get('intents', {}).get('vkmessage', {}).get('slots', {}).get('Chto', {}).get('value')
    chtostatus = event.get('request', {}).get('nlu', {}).get('intents', {}).get('statusset', {}).get('slots', {}).get('Chto', {}).get('value')
    komu = event.get('request', {}).get('nlu', {}).get('intents', {}).get('vkmessage', {}).get('slots', {}).get('Komu', {}).get('value')
    
    if intents.get('yes'):
        text = str(config.MESS_TEXT1) + str(chto) + str(config.MESS_TEXT2) + str(komu)
        komu_id = name_to_id(komu)
        api.messages.send(user_id = komu_id, message = chto)
        end_session = 'true'
    else:
        text = "Хорошо, отменил отправку."
        end_session = 'true'

def handler(event, context):
    intents = event.get('request', {}).get('nlu', {}).get('intents', {})
    command = event.get('request', {}).get('command')
    chto = event.get('request', {}).get('nlu', {}).get('intents', {}).get('vkmessage', {}).get('slots', {}).get('Chto', {}).get('value')
    chtostatus = event.get('request', {}).get('nlu', {}).get('intents', {}).get('statusset', {}).get('slots', {}).get('Chto', {}).get('value')
    komu = event.get('request', {}).get('nlu', {}).get('intents', {}).get('vkmessage', {}).get('slots', {}).get('Komu', {}).get('value')
    ev = event
    cont = context


    text = config.INTRO_TEXT
    end_session = 'false'

    if intents.get('exit'):
        text = 'Ну пока) Жду снова!'
        end_session = 'true'
    elif intents.get('help'):
        text = config.INTRO_TEXT
        end_session = 'true'
    elif intents.get('vkpost'):
        messagepost1 = remove_char(command)
        messagepost = remove_char1(messagepost1)
        textold = config.POST_TEXT1 + messagepost + config.POST_TEXT2
        text = textold
        api.wall.post(message = messagepost)
        end_session = 'true'
    elif intents.get('vkmessage'):
        text_mess1 = del_name(command)
        text_mess2 = remove_charmess(text_mess1)
        text_mess = remove_charmess1(text_mess2)
        if text_mess == None:
            text = "Вы не сказали что отправить..."
            end_session = 'true'
        else:
            text = "Вы подтверждаете отправку? Скажите 'Да' или 'Нет'."
            end_session = 'false'
            message_send(ev, cont)

    elif intents.get('statusset'):
        api.status.set(text = chtostatus)
        text = str(config.STAT_TEXT1) + str(chtostatus) + str(config.STAT_TEXT2)
        end_session = 'true'
    elif command:
        text = 'Не поняла тебя. Для выхода, скажи "Хватит".'
        end_session = 'true'

    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text': text,
            'end_session': end_session
        },
    }
