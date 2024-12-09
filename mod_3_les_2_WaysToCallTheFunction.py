# Домашняя работа по уроку "Способы вызова функции". Задача "Рассылка писем".

def check_email(mail:str)->bool:
    check_list = ('.com', '.ru', '.net')
    check = '@'
    return mail.find(check) and mail.endswith(check_list)

def send_email(message, recipient,
               sender='university.help@gmail.com')->None:
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif check_email(recipient) and check_email(sender):
        if sender != 'university.help@gmail.com':
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! '
                  f'Письмо успешно отправлено с адреса {sender} '
                  f'на адрес {recipient}.')
        else:
            print(f'"{message}" успешно отправлено '
                  f'с адреса {sender} '
                  f'на адрес {recipient}.')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} '
              f'на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
