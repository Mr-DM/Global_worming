import discord
from discord.ext import commands
import random
import os 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

reason_list = ["Выбросы паровых газов","Вырубка лесов","промышленные процессы","Увелечение городов","Истощение озонового слоя"]

soloves_list = ["Переход на возобноляемые источники энергии","Энергоэффективные техгорогии","Защита и восстановление лесов","Снижение выбросов в промышленности","сокрощение потребления и отходов",""]




@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command(name="привет")
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}! моя задача обяснять про Глобалное потепления')

@bot.command(name="помошь")
async def help(ctx):
    await ctx.send("Что я Могу:")
    await ctx.send("Команда 'Что-это' - обясняет про что это глобалное потепления")
    await ctx.send("Команда 'причины' - несколько причины появления Глобальное потепление")
    await ctx.send("Команда 'решения' - несколько решения для решеней Глобальное потепление")
    await ctx.send("Команда 'мем' - несколько мемемов про Глобальное потепление")


@bot.command(name="что-это")
async def what_is_global_warming(ctx):
    await ctx.send(f"Глобальное потепление — это долгосрочное повышение средней температуры атмосферы и океанов Земли.")

    
@bot.command(name="причины")
async def how_is_heppend(ctx):
    random_reason = random.choice(reason_list)
    await ctx.send(f"Основной причиной появления Глобальное потепление это - {random_reason}"  )

@bot.command(name="решения")
async def how_to_solve(ctx):
    random_soloves = random.choice(soloves_list)
    await ctx.send(f"Решения Глобальное потепление - {random_soloves}"  )

@bot.command(name="мем")
async def Mem(ctx):
    global_warming_mem_random = random.choice(os.listdir('mem_global_warming'))
    with open(f'mem_global_warming/{global_warming_mem_random}', 'rb') as f:
            picture = discord.File(f)
 
    await ctx.send(file=picture)  


bot.run("Token")