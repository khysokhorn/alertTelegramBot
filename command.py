from datetime import date, datetime


def sample_res(input_text):
    user_message = str(input_text).lower().replace("/", "")
    print('user command ' + user_message)
    if user_message in ("hello", "hi", "sub"):
        return "hey yo what's up !"

    if user_message in ("whoareyou", "whoareyou ?"):
        return "Here is sokhorn bot, u can ask any thing form Google "

    if user_message in 'menu':
        menus = (
                "/menu for display all available menu" + "\n"
                                                         "/help if u need help" + "\n"
                                                                                  "/start to start bot" + "\n"
                                                                                                          "/web to see my Portfolio"
        )
        return menus

    if user_message in ("honey", "bi", "oun", "bibi", "np jit"):
        return "This command is not available unless you find our " + user_message

    if user_message in ("web", "Find me in website"):
        return "Google.com"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y : %H/%M%S")
        return date_time

    if user_message in ("morning", "Good morning", ""):
        return "Good morning bibi, cute salop"

    if user_message in ("khom mes", "ខំមេស bro"):
        return user_message + " tv chir na ke merl, pg single pg hik "

    return "Command not Found!!!!"
