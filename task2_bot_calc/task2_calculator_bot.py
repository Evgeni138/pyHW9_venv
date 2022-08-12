from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

updater = Updater(token= 'TOKEN')

def log(update, context):
    file = open('logger.csv', 'a')
    file.write(f'{update.effective_user.username}, {update.effective_user.id}, {update.message.text}\n')
    file.close()

def start(update, context):
    log(update, context)
    update.message.reply_text('Вы включили калькулятор. '
                              'Введите два числа через пробел '
                              'или введите "stop", для выхода из калькулятора')
    return 1

def first_response(update, context):
    log(update, context)
    list_numbers = update.message.text
    if list_numbers == 'stop':
        return stop(update, context)
    else:
        list_numbers = list_numbers.split()

        if (list_numbers[0].isdigit() == True) and (list_numbers[1].isdigit() == True) and (len(list_numbers) == 2):
            global a
            a = int(list_numbers[0])
            global b
            b = int(list_numbers[1])
            update.message.reply_text('Введите "+" для сложения,\n '
                                      'введите "-" для вычитания,\n '
                                      'введите "*" для ужножения,\n '
                                      'введите "/" для деления')
            return 2
        else:
            return start(update, context)

def second_response(update, context):
    log(update, context)
    operation = update.message.text
    if (operation == '+'):
        update.message.reply_text(f'{a} + {b} = {a + b}')
    elif (operation == '-'):
        update.message.reply_text(f'{a} - {b} = {a - b}')
    elif (operation == '*'):
        update.message.reply_text(f'{a} * {b} = {a * b}')
    elif (operation == '/'):
        update.message.reply_text(f'{a} / {b} = {a / b}')

    return start(update, context)

def stop(update, context):
    log(update, context)
    update.message.reply_text('А жаль, хотелось бы пообщаться!')
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states = {
    1: [MessageHandler(Filters.text, first_response)],
    2: [MessageHandler(Filters.text, second_response)]
    },
    fallbacks=[CommandHandler('stop', stop)]
)

dp = updater.dispatcher
dp.add_handler(conv_handler)
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('stop', stop))

updater.start_polling()
updater.idle()