import vk
import config

# токен прилоги - d0e78ffb7185866fbe6ccdc608d25b71b74aaf32e10c545e64e750c71318153ee759303586b2c25427468
session = vk.Session(config.tokenVK)
api = vk.API(session, v='5.85')

def remove_char(s):
    result = s.replace("Новый пост ", "")
    return result

def remove_char1(s):
    result = s.replace("новый пост ", "")
    return result

def handler(event, context):
    intents = event.get('request', {}).get('nlu', {}).get('intents', {})
    command = event.get('request', {}).get('command')

    text = INTRO_TEXT
    end_session = 'false'

    if intents.get('exit'):
        text = 'Ну пока) Жду снова!'
        end_session = 'true'
    elif intents.get('help'):
        text = INTRO_TEXT
    elif intents.get('vkpost'):
        messagepost1 = remove_char(command)
        messagepost = remove_char1(messagepost1)
        textold = config.POST_TEXT1 + messagepost + config.POST_TEXT2
        text = textold
        api.wall.post(message = messagepost)
    elif command:
        text = 'Не поняла тебя. Для выхода, скажи "Хватит".'

    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text': text,
            'end_session': end_session
        },
    }
