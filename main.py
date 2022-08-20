import os
import random
import telebot
from webserver import keep_alive

keep_alive()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


class Song:
    def __init__(self, name, singer, url):
        self.__name = name
        self.__singer = singer
        self.__url = url

    def __str__(self):
        return f"""
    {self.__name} מאת {self.__singer}
    {self.__url}
    """


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, """
  /start - Start Conversation
/greet - Get a Greeting
/get_song - Get a Song
/get_compliment - Get a Compliment
/commands - Get a list of commands 
  """)


@bot.message_handler(commands=['greet'])
def greet(message):
    GREETINGS = ("Hey there", "How are you?", "\U0001F49A")
    bot.send_message(message.chat.id, random.choice(GREETINGS))


@bot.message_handler(commands=['commands'])
def commands(message):
    bot.send_message(
        message.chat.id, """
  /start - Start Conversation
/greet - Get a Greeting
/get_song - Get a Song
/get_compliment - Get a Compliment
/commands - Get a list of commands 
  """)


@bot.message_handler(commands=['get_song'])
def get_a_song(message):
    SONGS = (Song('בדיוק כמו שהיא', "אדיר גץ",
                  'https://www.youtube.com/watch?v=bnGk0Nqbq30'),
             Song('עשר אפס לך', "אדיר גץ",
                  'https://www.youtube.com/watch?v=BSarOZo9Ps0'),
             Song('איזה שבוע', "אדיר גץ",
                  'https://www.youtube.com/watch?v=0YUOPj8g_6k'),
             Song('ילד בשדות', "אדיר גץ",
                  'https://www.youtube.com/watch?v=doEwoSNmT6Q'),
             Song('שמישהו יעצור אותי', "עדן חסון",
                  'https://www.youtube.com/watch?v=pse5JzwHVtM'),
             Song('עושה לי צרות', "עדן חסון",
                  'https://www.youtube.com/watch?v=y6YpayxgNpY'),
             Song('איתך', "עדן חסון",
                  'https://www.youtube.com/watch?v=Ii8t-XIw6aM'),
             Song('גדל לי קצת זקן', "עדן חסון",
                  'https://www.youtube.com/watch?v=sLPt028Iao8'),
             Song('שיכורים', "עדן חסון",
                  'https://www.youtube.com/watch?v=pgAPwe4Ze3I'),
             Song('אין יותר מועדונים', "עדן חסון",
                  'https://www.youtube.com/watch?v=hySvIlHhCgA'),
             Song('עיניים', "עדן חסון",
                  'https://www.youtube.com/watch?v=1b_bhq0fFX0'),
             Song('זה בא אליי בלילה', "עדן חסון",
                  'https://www.youtube.com/watch?v=LYknC_3_n6c'),
             Song('מתגעגעת', "נתן גושן",
                  'https://www.youtube.com/watch?v=jQctQKwMyl8'),
             Song('יש בלאגן גדול', "נתן גושן",
                  'https://www.youtube.com/watch?v=jlBTpu2jvBc'),
             Song('באתי לחלום', "נתן גושן",
                  'https://www.youtube.com/watch?v=JjKsHEWiu_4'),
             Song('דברי איתי יותר', "נתן גושן",
                  'https://www.youtube.com/watch?v=XUtrAfFhAfo'),
             Song('איפה את', "נתן גושן",
                  'https://www.youtube.com/watch?v=MoOlwfEfbG0'),
             Song('ואם תבואי אליי', "עידן רייכל",
                  'https://www.youtube.com/watch?v=nI8n20UpaBY'),
             Song('אבן על אבן', "עידן רייכל",
                  'https://www.youtube.com/watch?v=NIi29Qeqlis'),
             Song('גלגל מסתובב', "עידן רייכל",
                  'https://www.youtube.com/watch?v=VwJiGK1uNYk'),
             Song('חלומות של אחרים', "עידן רייכל",
                  'https://www.youtube.com/watch?v=WDpUlvF0-Dg'),
             Song('תסתכלי לי בעיניים', "עידן עמדי",
                  'https://www.youtube.com/watch?v=nl1tsYXJHdM'),
             Song('מפה לשם', "עידן עמדי",
                  'https://www.youtube.com/watch?v=M79b596-1vY'),
             Song('בזמן האחרון', "עידן עמדי",
                  'https://www.youtube.com/watch?v=f5fTCR7TOEU'),
             Song('בקרוב יפתחו השמיים', "עידן עמדי",
                  'https://www.youtube.com/watch?v=cGbDHwrC_1E'),
             Song('מסע', "נתנאל יהודה",
                  'https://www.youtube.com/watch?v=oAe6WnziTUs'),
             Song('Yello', "Coldplay",
                  'https://www.youtube.com/watch?v=yKNxeF4KMsY'),
             Song('אינטלקטוערס', 'אודיה', 'https://youtu.be/27KJdsez9Aw'),
             Song('אם הייתי צריכה', 'אודיה', 'https://youtu.be/cSkTzkGoot0'),
             Song('אוהבת אותך בטעות', 'אודיה',
                  'https://www.youtube.com/watch?v=2FNJNnV9DxM'),
             Song('Do I Wanna Know?', 'Arctic Monkeys',
                  'https://www.youtube.com/watch?v=bpOSxM0rNPM'),
             Song('Here', 'Alessia Cara',
                  'https://www.youtube.com/watch?v=DArzZ3RvejU'),
             Song('Mi Gente', 'J Balvin, Willy William',
                  'https://www.youtube.com/watch?v=wnJ6LuUFpMo'),
             Song('Shape Of You', 'Ed Sheeran',
                  'https://www.youtube.com/watch?v=JGwWNGJdvx8'),
             Song('No Lie', 'Sean Pual, Dua Lipa',
                  'https://www.youtube.com/watch?v=GzU8KqOY8YA'),
             Song("Can't Holds Us", 'Macklemore & Ryan Lewis',
                  'https://www.youtube.com/watch?v=dbevJM-2lcY'),
             Song('Stay', 'The Kid LAROI, Justin Bieber',
                  'https://youtu.be/kTJczUoc26U?t=19'),
             Song('Counting Stars', 'OneRepublic',
                  'https://www.youtube.com/watch?v=hT_nvWreIhg'))
    bot.reply_to(
        message, SONGS[random.randint(0,
                                      len(SONGS) * 100000000000) % len(SONGS)])


@bot.message_handler(commands=['get_compliment'])
def get_a_compliment(message):
    COMPLIMENTS = ('adorable', 'beautiful', 'cute', 'handsome', 'pretty', 'funny', 'smart', 'interesting')
    bot.send_message(message.chat.id, 'You are ' + random.choice(COMPLIMENTS) + '.')


bot.polling()
