import discord
import random
import os
from discord.ext import commands
from fun import aia
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')
@bot.command()
async def buy(ctx):
    await ctx.send('Пока, мой господин')


@bot.command()
async def heh(ctx, count_heh: int):
    await ctx.send("he" * count_heh)

@bot.command()
async def equation(ctx, first: int, action: str, second: int):
      if action == "+":
            await ctx.send(first + second)
      elif action == "-":
            await ctx.send(first - second)
      elif action == "*":
            await ctx.send(first * second)
      elif action == "/":
            await ctx.send(first / second)
spis = []
@bot.command()
async def choose(ctx, fc: str, sc: str):
     spis.append(fc)
     spis.append(sc)
     random.choice(spis)
     if random.choice(spis) == fc:
          await ctx.send(fc)
     else:
           await ctx.send(sc)    
     spis.remove(fc)
     spis.remove(sc)

@bot.command()
async def repeat(ctx, content: str, times: int):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
@bot.command()
async def emojes(ctx):
      listik = ['😎👍','🤤🍕','🎶😊','😍','😎🍿','😉👌','🤔💬','😡👊','🔫🤠','🎤😃','☝️🤓','🎁😊','😎🚬','😃💡','😣💢','🤑💰','🔥🙂🔥'] 
      smile = random.choice(listik) 
      await ctx.send(smile)
@bot.command()
async def create_new_nikname(ctx, long: int):
      elementers = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
      nicname = ""
      for i in range(long):
            nicname += random.choice(elementers)
      await ctx.send(nicname)
@bot.command()
async def helps(ctx):
     await ctx.send('hello-buy= приветствие и прощание,'
                    ' heh - просто прикольная команда, напиши heh а затем напиши число, сколько раз оно повториться,'
                    ' equation- канкулятор(на два числа), испоьзуться + - * /(деление),'
                    ' choose - рандомный выбор между чем то,'
                    ' repeat - повторяет любое слово(напиши слово, пробел и цифру),'
                    ' emojes - вызывает любую эмоцию,'
                    ' create_new_nikname- создает любой никнейм с любой длиной рандомно'
                    ' mem - высылает рандомный мем,'
                    ' ran_card - игра с карточками, кому больше повезет тот и выйграл(игра будет разрабатываться все больше и больше)')


@bot.command()
async def mem(ctx):
    im = os.listdir('images')
    img_name = random.choice(im)
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)


@bot.command()
async def ran_card(ctx):
    ran = random.choice(os.listdir('ranimage'))
    
    with open(f'ranimage/{ran}', 'rb') as f:
        pictures = discord.File(f)
        if 'rin' in ran:
            await ctx.send('Редкость - обычная')
        if 'isagi' in ran:
            await ctx.send('Редкость - редкая')
        if 'Akashi' in ran:
            await ctx.send('Редкость - сверхредкая')
        if 'mahor' in ran:
            await ctx.send('Редкость - эпическая')
        if 'sukuna' in ran:
            await ctx.send('Редкость - мифическая ')
        if 'gojo' in ran:
            await ctx.send('Редкость - легендарная')
        if 'goku' in ran:
            await ctx.send('Редкость - супер-легендарная')
        await ctx.send(file=pictures)


@bot.command()
async def quest(ctx):
     q1 = ['Понедельник - выбросить мусор, Вторник - почистить улицу, Среда - убрать дом, Четверг - надоедать друзьям про природу, Пятница - ругай людей за мусор',
           'Понедельник - Проведи исследование о вреде пластика для окружающей среды, Вторник - Организуй экологическую акцию в своем районе, Среда - Проведи день без использования пластиковых продуктов, Четверг - Изучи возможности переработки отходов в твоем районе Пятница -  Создай план экологических действий на следующую неделю',
           'Понедельник - Проведи исследование о влиянии автомобильных выбросов в воздух, Вторник - Организуй кампанию по сбору старых батареек в школе, Среда -  Проведи экскурсию в местный парк или заповедник, Четверг - Орагнизуй конкурс, кто больше соберет мусора. Пятница - Создай информационный буклет о методах снижения загрязнения']
     pp = random.choice(q1)
     await ctx.send(pp)

@bot.event #модерация канала
async def on_message(message):
    if message.author == bot.user:  # Чтобы бот не реагировал на свои же сообщения
        return
    deel = ['ах тыж писька волосатая, че материшься?','сэр, прошу вас в следущий раз не матюканьтесь',
            'ты офигел вообще, я папе пожалаюсь','не стоит этого делать...','ага, ну давай, попробуй еще раз']
    pq = random.choice(deel)
    forbidden_words = ['Блять', 'блять', 'бля',"Бля","Пиздец", "пиздец", "Нахуй", "нахуй", "пздц", "Пздц","нах","Нах",
                       "Сука", "сука", "блядь", "Блять",'ебаный в рот','Ебаный в рот','Иди нахуй','иди нахуй','пидор','Пидор','пидорас',
                       'Сын шлюхи','сын шлюхи','шлюха','Шлюха','Пизда','пизда', 'ебал', 'мразь','мрази',
                       'уебан','еблан','долбоеб','сучка','Еблан','ебаный','ебанный','Ебаный','хуй','трахал','трахать',
                       'пид0р','пид0рас','о4ко']
    
    for word in forbidden_words:
        if word in message.content.lower():
            await message.delete()  # Удаляем сообщение, если оно содержит запрещенное слово
            await message.channel.send(f'{message.author.mention}, {pq}')
            break  # Прерываем цикл, если найдено запрещенное слово

    await bot.process_commands(message)
@bot.command()
async def ai(ctx):  
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
             file_name = attachment.filename
             file_url = attachment.url
             await attachment.save(f'images_ai/{file_name}')
             await ctx.send(f'save into the images_ai/{file_name}')
             zombie = aia(f'images_ai/{file_name}')
             await ctx.send(zombie)
             if zombie == 'air':
                await ctx.send('"Пять минут полет нормальный👍" Эти подвешеные чертята не представляют огромной опасности, если это чертик на шарике, его можно збить💥 с помощью кактуса или ветродуя или остановить Высоким орехом.')
                await ctx.send('Если это подвешеный зомби на локации "Крыша" то он почти безвредный, можете конечно использовать Зонтичный Лист по желанию(Всех можно подорвать)')   
             elif zombie == 'on the ice':
                await ctx.send('Появляються после того как "Зомбони" на своей машине проложит ледянной путь, повезет если пойдет один, с группой будет тяжело')
             elif zombie == 'zombie':
                await ctx.send('Просто убивайти их, самые простые🙄')
             elif zombie == 'car':
                await ctx.send('Это конечно интресные ребята, машины стыбзили - Если это зомби на леденой машине именыемый Зомбони, то вам не очень повезло, он имеет ОГРОМНУЮ прочность, давит растение, и после него идут сноубардисты')
                await ctx.send('Если это Зомби на машине с мячиками, он не такой грозный, просто кидает мячики🏀')
                await ctx.send('Их можно убить сломав их машину - горохострелами, шипами, и про себя читая молитву(не всегда помогает)')
             elif zombie == 'jupming':
                await ctx.send('Ироды еще какие, все они перепрыгивают одно растение(кроме Пого-зомби, он все перепрыгивают)- их можно контрить - Магнит грибом(у которых есть железные вещи),')
                await ctx.send('Выскоим орехом - он всегда брутал🗻 и через него не перепрыгнуть, Убить - самый простой способ')
             elif zombie == 'hiding':
                await ctx.send('Я промолчу кто они, если он в воде, то он подплывет только к первому растению на своем пути, советую ставить кувшинку в начале, а еще лучше и ореха вбахнуть туда же')
                await ctx.send('Если шахтер⚰, то он идет в самый конец карты и атакует растения на первой линии, против них хорошо работает сиамский горохострел, кабачок перец и мина')
             elif zombie == 'sosut':
                await ctx.send('Идут в комплетке с сильными челиками, обычные зомби')
             elif zombie == 'newspaper':
                await ctx.send('Челик пришел чисто газету почитать на поле битвы📃, если сломаете газету, то он просто ускориться, он не представляет опасности')
             elif zombie == 'super armor':
                await ctx.send('Да, бесячий челик, но что поделать, против них действует хорошая защита, либо растения которые ван шотают')
             elif zombie == 'dancer':
                await ctx.send('👇🤩🤘Гибдна денс - туц туц, Гибдна денс - туц туц - ОО гибна деееенс, ой запелся - трудный зомбарь, он имеет чуть выше прочность нежели обычный зомби - так и еще и танцоров призывает')
                await ctx.send('Так же моичте сильными ракстениями либо растения которые ван шотают')
             elif zombie == 'armor':
                await ctx.send('Прости усиленый зомби, не чего сказать')
             elif zombie == 'japan':
                await ctx.send('"ЗА ИМПЕРАТОРА"-единственое что он знает -  совет таков - убить как можно скорее, а то будет кабум💥💥💥')


    else:
         await ctx.send('Вы не загрузили картинку')        
       

bot.run('')