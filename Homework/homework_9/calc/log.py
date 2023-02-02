import datetime


def log(message):
    file = open('log_file.csv', 'a')
    file.write(f'{datetime.datetime.now().time()}, {message.chat.username}, {message.chat.id}, {message.text}\n')
    file.close()