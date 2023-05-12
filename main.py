import telebot
from telebot import types

bot = telebot.TeleBot(token='"seu token"', parse_mode='HTML')


# $ Markups:
@bot.message_handler(commands=['start'])
def handler_start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton('📚livros', callback_data='/py-bot livros'),
        types.InlineKeyboardButton('Acesse: https://www.goodreads.com', url='https://www.goodreads.com'),
        row_width=2
    )
    bot.send_message(chat_id=message.from_user.id,
                     text=f'<b>Sr(a) {message.from_user.first_name}</b> bem vindo! escolha umas das opções abaixo',
                     reply_to_message_id=message.message_id, reply_markup=markup)


# $ callback Data:
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == '/py-bot livros':
        # Action: typing
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('📚Introducao_a_programacao_com_Python',
                                       callback_data='/py-bot"Introducao_a_programacao_com_Python"'),

            types.InlineKeyboardButton('📚Matematica-1400-Questoes-Resolvidas-e-Gabaritadas',
                                       callback_data='/py-bot "Matematica-1400-Questoes-Resolvidas"'),

            row_width=1

        )

        bot.send_message(chat_id=call.from_user.id,
                         text=f'<b>Sr(a) {call.from_user.first_name}</b> bem vindo! escolha um dos livros abaixo',
                         reply_markup=markup)

    elif call.data == '/py-bot"Introducao_a_programacao_com_Python"':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('⬅️ Voltar', callback_data='/chatbot voltar')
        )

        bot.send_document(chat_id=call.from_user.id,
                          document=open('livros/exemplo.pdf ', 'rb'),
                          caption='📚<b>livro escolhido</b> Introducao_a_programacao_com_Python.pdf',
                          reply_markup=markup)
    elif call.data == '/py-bot "Matematica-1400-Questoes-Resolvidas"':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('⬅️ Voltar', callback_data='/chatbot voltar')
        )

        bot.send_document(chat_id=call.from_user.id,
                          document=open('livros/exemplo.pdf', 'rb'),
                          caption='📚<b>livro escolhido</b> Matematica-1400-Questoes-Resolvidas-e-Gabaritadas.pdf',
                          reply_markup=markup)
    elif call.data == '/chatbot voltar':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('📚livros', callback_data='/py-bot livros'),
            types.InlineKeyboardButton('Acesse: https://www.goodreads.com', url='https://www.goodreads.com'),
            row_width=1
        )
        bot.send_message(chat_id=call.from_user.id,
                         text=f'<b>Sr(a) {call.from_user.first_name}</b> bem vindo! escolha umas das opções abaixo',
                         reply_markup=markup)


bot.polling()
