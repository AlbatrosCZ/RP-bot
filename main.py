import discord
from discord.ext import commands, tasks
from classes.holder import holder
from parts.if_is import *
from parts.messaging import *
from parts.helps import help_me
from parts.to_time import *
TOKEN = open("token.txt").read()

bot = commands.Bot(command_prefix='-')
bot.remove_command('help')

DATA = holder()

print(bot.command_prefix*30)
print(f"Token: {TOKEN}")

@bot.event
async def on_ready():
    global DATA
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{bot.command_prefix}help"))
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    print(f'Prefix: {bot.command_prefix}')
    print(bot.command_prefix*30)
    print("Init server database")
    for server in bot.guilds:
        print(f"{server.name} is {DATA.add_server(server)}")
    print(bot.command_prefix*30)
    every_sec.start()


@bot.command(aliases = ["rpg", "role_play", "roleplay"])
async def RP(ctx, *args):
    if len(args) < 1:
        send_error(ctx, "This function need more arguments. For more info write help rp")
        return
    elif args[0] == "start":
        await startRP(ctx)
    elif args[0] == "stop":
        await stopRP(ctx)
    elif args[0] == "pause":
        await pauseRP(ctx, args)
    elif args[0] == "resume":
        await resumeRP(ctx, args)
    else:
        await send_error(ctx, "Bad argumenting")
        return
async def startRP(ctx):
    if not admin(ctx):
        await dont_have_permmission(ctx, "Administration")
        return
    try:
        if not DATA.get_server(ctx.guild.id).reset():
            await send_error(ctx, "write `report error on start`\nError will be eliminated as soon as posible")
            return
        DATA.get_server(ctx.guild.id).rp_paused = 0
        DATA.get_server(ctx.guild.id).rp_started = True
        await ctx.message.add_reaction("✅")
    except:
        await send_error(ctx, "You aren't in guild\nif you are in guild write `report error on start`\nError will be eliminated as soon as posible")
        return
async def stopRP(ctx):
    if not admin(ctx):
        await dont_have_permmission(ctx, "Administration")
        return
    try:
        DATA.get_server(ctx.guild.id).rp_started = False
        await ctx.message.add_reaction("✅")
    except:
        await send_error(ctx, "You aren't in guild")
        return
async def pauseRP(ctx, args):
    if not admin(ctx):
        await dont_have_permmission(ctx, "Administration")
        return
    try:
        if DATA.get_server(ctx.guild.id).rp_started:
            try:
                pause_time = args[1:]
                pausing_time = 0
                for pause in pause_time:
                    if pause[-1:] == "d":
                        pausing_time += 60*60*24*int(pause[:-1])
                    elif pause[-1:] == "h":
                        pausing_time += 60*60*int(pause[:-1])
                    elif pause[-1:] == "m":
                        pausing_time += 60*int(pause[:-1])
                    elif pause[-1:] == "s":
                        pausing_time += int(pause[:-1])
            except:
                await send(ctx.channel, "RP is paused to be resume or start again")
                pausing_time = -1 
            DATA.get_server(ctx.guild.id).rp_paused = pausing_time
            await ctx.message.add_reaction("✅")
        else:
            await send_error(ctx, "RP isn't started")
            return
    except:
        await send_error(ctx, "You aren't in guild")
        return
async def resumeRP(ctx, args):
    if not admin(ctx):
        await dont_have_permmission(ctx, "Administration")
        return
    try:
        if DATA.get_server(ctx.guild.id).rp_started:
            DATA.get_server(ctx.guild.id).rp_paused = False
            await ctx.message.add_reaction("✅")
        else:
            await send_error(ctx, "RP isn't started")
            return
    except:
        await send_error(ctx, "You aren't in guild")
        return


@bot.command(aliases = ["ar", "autorole"])
async def auto_role(ctx, *args):
    if len(args) < 1:
        send_error(ctx, "This function need more arguments. For more info write help auto_role")
        return 
    if args[0] == "add":
        await add_auto_role(ctx, args[1:])
    elif args[0] == "get":
        await get_auto_role(ctx, args)
    elif args[0] in ["rem", "remove", "del", "delete"]:
        await remove_auto_role(ctx, args[1:])
    elif args[0] in ["edit"]:
        await edit_auto_role(ctx, args[1:])
    else:
        await send_error(ctx, "Bad argumenting")
        return
async def add_auto_role(ctx, args):
    if not admin:
        await dont_have_permmission(ctx, "Administration")
        return
    if len(args) < 1:
        await send_error(ctx, "This function need more arguments. For more info write help auto_role add")
        return
    if "<@&" not in args[0]:
        role = discord.utils.get(ctx.guild.roles, name = args[0])
    else:
        role = discord.utils.get(ctx.guild.roles, id = int(args[0][3:-1]))

    if len(args) > 1:
        try:
            money = int(args[1])
        except:
            money = 100
    else:
        money = 100

    full_time = 0
    if len(args) > 2:
        for i in range(2, len(args)):
            try:
                time_type = args[i][-1:]
                time = int(args[i][:-1])
                full_time += {"d":60*60*24, "h":60*60, "m":60, "s":1}[time_type] * time
            except:
                return
    else:
        full_time = 60
    for role in DATA.get_server(ctx.guild.id).auto_role_list:
        if role.name == args[0]:
            await send_error(ctx, "This auto_role is exists. You can't duplicate it only edit. For more info write help auto_role")
            return
    if role != None:
        DATA.get_server(ctx.guild.id).add_auto_role(role, 2000, 60)
        await ctx.channel.delete_messages([ctx.message])
    else:
        role = await ctx.guild.create_role(name = args[0])
        DATA.get_server(ctx.guild.id).add_auto_role(role, 2000, 60)
        await ctx.channel.delete_messages([ctx.message])
    await ctx.send(f"New Auto Role {role.name}\npayday: {money}\npay every: {full_time}s")
async def get_auto_role(ctx, args):
    ret = "```Auto Income Roles:\n"
    roles = DATA.get_server(ctx.guild.id).auto_role_list
    for role in roles:
        ret += "\n"
        ret += f"  {role.name} - {role.payday}/{time_to_text(role.payday_time)}"
    await ctx.channel.send(ret + "```")
async def remove_auto_role(ctx, args):
    if not admin(ctx):
        await dont_have_permmission(ctx, "administrator")
        return
    if len(args) < 1:
        send_error(ctx, "This function need more arguments. For more info write help auto_role")
        return
    roles = DATA.get_server(ctx.server.id).auto_role_list
    for i in range(len(roles)):
        if roles[i].name == args[0]:
            del roles[i]
            await ctx.message.add_reaction("✅")
            await send(ctx.channel, "Succesfully deleted")
            return
    await send_error(ctx, f"Role named {args[0]} dosn't exists")
async def edit_auto_role(ctx, args):
    if not admin(ctx):
        await dont_have_permmission(ctx, "administrator")
        return
    if len(args) < 3:
        await send_error(ctx, "This function need more arguments. For more info write help auto_role add")
        return
    if "<@&" not in args[0]:
        role = discord.utils.get(ctx.guild.roles, name = args[0])
    else:
        role = discord.utils.get(ctx.guild.roles, id = int(args[0][3:-1]))
    value_name = args[1]
    if role == None:
        await send_error(ctx, "Bad role")
        return
    elif value_name == "name":
        await send_error(ctx, "Value name change automaticaly on role name changed and if you want change auto_role delete this and next create new")
        return
    roles = DATA.get_server(ctx.guild.id).auto_role_list
    for rol in roles:
        if role.name != rol.name:
            pass
        elif value_name in ["payday", "pd"]:
            try:
                rol.payday = int(args[2])
            except:
                await send_error(ctx, "You must input integer when chanege how much money role get (payday)")
                return
        elif value_name in ["payday_time", "pdt"]:
            tim = 0
            try:
                for i in args[2:]:
                    if i[-1:] == "d":
                        tim += int(i[:-1])*60*60*24
                    elif i[-1:] == "h":
                        tim += int(i[:-1])*60*60
                    elif i[-1:] == "m":
                        tim += int(i[:-1])*60
                    elif i[-1:] == "s":
                        tim += int(i[:-1])
                    else:
                        await send_error(ctx, "Bad time input")
            except:
                await send_error(ctx, "Bad input on payday_time")
                return

            rol.payday_time = tim
        else:
            await send_error(ctx, "Bad inputed value name")
            return 


@bot.command(aliases = ["sr", "serv"])
async def server(ctx, *args):
    if len(args) < 1:
        await send_error(ctx, "This function need more arguments. For more info write help server")
        return
    if args[0] == "clear":
        await clear(ctx)
    if args[0] == "delete":
        await clear_msgs(ctx, args)
    else:
        await send_error(ctx, "Bad argumenting")
        return
async def clear(ctx):
    if not edit_messages:
        return
    run = True
    while run:
        messages = []
        async for message in ctx.channel.history(limit = 30):
            messages.append(message)
        if len(messages) == 0:
            run = False
        await ctx.channel.delete_messages(messages)
    await ctx.send(":sponge:  -----  Succesfully deleted  -----  :sponge:")
async def clear_msgs(ctx, args):
    if not edit_messages:
        await dont_have_permmission(ctx, "Editing messages")
        return 
    if len(args) < 2:
        await send_error(ctx, "This function need more arguments. For more info write help server")
        return
    try:
        count = int(args[1])
    except:
        await send_error(ctx, "Bad argumenting")
        return
    msgs = []
    skiped_first = False
    async for msg in ctx.channel.history(limit = count+1):
        if skiped_first:
            msgs.append(msg)
        else:
            skiped_first = True
        if len(msgs) == 50:
            await ctx.channel.delete_messages(msgs)
            msgs = []
    await ctx.channel.delete_messages(msgs)
    await ctx.send(":sponge:  -----  Succesfully deleted  -----  :sponge:")
    await ctx.message.add_reaction("✅")


@bot.command(aliases = ["nuke", "nk", "nuke_ch", "nu_ch", "n_ch"])
async def nuke_channel(ctx, *args):
    if not admin(ctx):
        await dont_have_permmission(ctx, "administrator")
        await send_error(ctx, "nuke is most powerfull command you can't use it")
        return
    try:
        nuke_times = int(args[0])
        try:
            who = " : " + " ".join(args[1:])
        except:
            who = ""
    except:
        nuke_times = 100
        try:
            who = " : " + " ".join(args[0:])
        except:
            who = ""

    for i in range(nuke_times):
        await send(ctx.channel, f":bomb: `nuking {i+1}/{nuke_times}`{who}")

    await send(ctx.channel, ":bomb: `Succesfully nuked` :bomb:")
@bot.command()
async def ping(ctx):
    await ctx.send(':ping_pong: pong :ping_pong:')
@bot.command(aliases = ["balance", "bal", "user", "mem", "member"])
async def aconut(ctx):
    server = DATA.get_server(ctx.guild.id)
    for user in server.user_list:
        if user.id == ctx.author.id:
            mem = user
    embed = discord.Embed(title = f"{mem.name}")
    embed.add_field(name = "Money", value = f"bank: {mem.bank}\nwalet: {mem.walet}")
    await ctx.send(embed = embed)
    await ctx.channel.delete_messages([ctx.message])
@bot.command()
async def news(ctx):
    await ctx.channel.send("""BOTS NEWS
    ```Version: 0.2 (unfinished)
        
    New in this version:
        1 New in program
        1.1 Automaticaly rename auto_role

    Bug fix:
        Nothing bug fix (nothing find)

    Edit olds:
        1 Commands
        1.1 auto_role (add get, remove and edit)
        1.2 help (update) ```""")

@bot.event
async def on_member_remove(member):
    users = DATA.get_server(member.guild.id).user_list
    for i in range(len(users)):
        if users[i].id == member.id:
            del users[i]
@bot.event
async def on_member_join(member):
    if member.id == 284204934818430996:
        member.guild.system_channel.send("<@!284204934818430996> (bot's author) just connect to your server. You can task him for bot")
    DATA.get_server(member.guild.id).add_user(member)
@bot.event
async def on_guild_role_update(before, after):
    roles = DATA.get_server(before.guild.id).auto_role_list
    for i in range(len(roles)):
        if roles[i].name == before.name:
            roles[i].name = after.name
@bot.event
async def on_message(ctx):
    if ctx.content[0:5] == bot.command_prefix + "help" or ctx.content[0:4] == "help":
        await help_me(ctx)
        return
    if ctx.content[0:6] == "report" or ctx.content[0:7] == bot.command_prefix + "report":
        for guild in bot.guilds:
            for member in guild.members:
                if member.id == 284204934818430996:
                    member.create_dm()
                    link = await ctx.channel.create_invite(max_age = 300)
                    member.send(f"REPORT on {ctx.guild.name} in {ctx.channel.name}:\ncontent:{ctx.content}\n{link}") 
    else:
        await bot.process_commands(ctx)
@tasks.loop(seconds = 1, reconnect = True)
async def every_sec():
    DATA.save()
    for server in DATA.get_servers():
        server.update(bot)

bot.run(TOKEN)