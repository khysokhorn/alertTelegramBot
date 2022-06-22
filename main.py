from telegram import *
from telegram.ext import *
import command as cmd

token = "5476532482:AAFBrQgyMQXDN6bc27nuKYBfoYyAoz636bI" 

bot = Bot(token)
print(bot.get_me())

print("bot have start....")


def hey_yo_function(update: Update, context: CallbackContext):
    print(f"user chat id {update.effective_chat.id}")
    bot.send_message(chat_id= update.effective_chat.id, text="Welcome to sokhorn bot")



def sandVoice(update, context):
    bot.send_audio(chat_id=update.effective_chat.id, audio="/home/sokhorn/Desktop")


def start_command(update, context):
    
    update.message.reply_text(f"Here your Last Update id : {update.update_id}")


def help_command(update, context):
    update.message.reply_text('if need help as Google tv bong, Thanks')


def handle_message(update, context):
    text = str(update.message.text)
    res = cmd.sample_res(text)
    update.message.reply_text(res)


def error(update, context):
    return "something went wrong bong"


def main():
    updater = Updater(token, use_context=True)
    dispatch = updater.dispatcher
    dispatch.add_handler(CommandHandler("welcome", hey_yo_function))
    dispatch.add_handler(CommandHandler("start", start_command))
    dispatch.add_handler(CommandHandler("help", help_command))
    dispatch.add_handler(CommandHandler("voice", sandVoice))
    dispatch.add_handler(MessageHandler(Filters.text, handle_message))

    dispatch.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
