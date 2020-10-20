import discord
from discord.ext import commands

TOKEN = 'NzY2NjExODM4ODEyNjg0MzEw.X4l46Q.6P5ZfopwrrVRF5Al48NauAt8HyY'

bot = commands.Bot(command_prefix='-')
bot.remove_command('help')

print(bot.command_prefix*30)
print(f"Token: {TOKEN}")
def admin(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        return True
    else:
        return False


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{bot.command_prefix}help"))
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    print(f'Prefix: {bot.command_prefix}')
    print(bot.command_prefix*30)

@bot.command()
async def ping(ctx):
    await ctx.send(':ping_pong: pong')

# obchod, inventář, auto_peníze, válku, del msg, ban, kick, random num
@bot.command(name = "help")
async def help_(ctx, *, args = None):
    if args != None:
        await info(ctx, args = args)
        return
    embed = discord.Embed(title = ":question:***Help***:question:")
    embed.add_field(name = ':keyboard:__server__:keyboard:', value = '`info server`')
    embed.add_field(name = ':pencil:__syntax__:pencil:', value = '`syntax`')
    embed.add_field(name = ':game_die:__random__:game_die:', value = '`info random`')
    embed.add_field(name = ':baggage_claim:__inventroy__:baggage_claim:', value = '`info inventory`')
    embed.add_field(name = ':moneybag:__balance__:moneybag:', value = '`info balance`')
    embed.add_field(name = ':money_with_wings:__war__:money_with_wings:', value = '`info war`')
    embed.add_field(name = ':pencil:__income__:pencil:', value = '`info income`')
    embed.add_field(name = ':money_mouth:__auto money__:money_mouth:', value = '`info auto_money`')
    embed.add_field(name = ':shopping_cart:__shop__:shopping_cart:', value = '`info shop`')
    await ctx.channel.send(embed = embed)

@bot.command()
async def info(ctx, *, args):
    embed = discord.Embed(title = ":question:***Info***:question:")
    if args   in ["shop"]:
        if admin(ctx):
            embed.add_field(name = "Shop set up", value = """`add {item_name} {price} [{type}] [{info}] [{who_takes_money}/bot]` - add some item (if you want know about types, type to chat 'about types')
                                                             `remove {item_name}` - remove some item 
                                                             `edit {item_name} {edit_thing} {new_value}` - edit value of some item""", inline = False)
        embed.add_field(name = "For dumbs", value = """`buy {item_name} [{amount}]` - buy some item/items
                                                       `count_price {item_name} {amount}` - count how much something costs
                                                       `info {item_name}` - return info of item""", inline = False)
    elif args in ["inv", "inventory"]:
        if admin(ctx):
            embed.add_field(name = "Inventory editor", value = """`delete {user} {item_name} [{amount}]` - remove someone item/items
                                                                  `add {user} {item_name} [{amount}]` - add someone item/items
                                                                  `clear {user} [{item_name}/all]` - delete all of/all items in someone inventory""")
        embed.add_field(name = "For dumbs", value = """`remove {item_name} [{amount}]` - remove item
                                                       `info {item_name}` - info about item
                                                       `give {item_name} {user}` - give some items to other user""", inline = False)
    elif args in ["auto_money", "am"]:
        if admin(ctx):
            embed.add_field(name = "Auto Money Set up", value = """`set_auto_money_editor_role {role}` - set role that can edit auto_money
                                                                   `new_role {role} {amount} [0-7day] [0-24hour] [0-59min] [0-59s]` - new auto addin role
                                                                   `edit_role {role} {edit_thing} {new_value}` - edit role""")
        embed.add_field(name = "For dumbs", value = "`auto_roles` - returns full list and info about roles")
    elif args in ["balance", "bal"]:
        embed.add_field(name = "For dumbs", value = """`balance [{user}]` - get info about player
                                                       `give {user} [{amount}]` - give someone money
                                                       `discard [{amount}]` - remove money from your acconut""")
    elif args in ["war"]:
        embed.add_field(name = "For dumbs", value = """`war {user}...` - decline war
                                                       `attack {user}` - attack to user
                                                       `peace {user}` - peace with user need to other confirm
                                                       `contract {user} {years}` - contract(pact of non-attacking) with someone need to other confirm
                                                       `aliance {thing} [{aliance_name}] {user}...` - editing aliance need to other confirm""")
    elif args in ["server"]:
        if admin(ctx):
            embed.add_field(name = "Admin Only", value = """`ban {user}` - ban someone
                                                            `kick {user}` - kick someone
                                                            `warning {user} {text_of_warning}` - warn someone""")
        else:
            embed.add_field(name = "You are dumb", value = "If you are dumb you can't use server commands\nIf you want not be dumb write to server owner to get you administation permission")
    elif args in ["random"]:
        embed.add_field(name = "For dumbs", value = """`roll_die 2/3/4/6/8/12/16/20/30/100` - roll with die
                                                       `roll_dies {number_of_dies}d{dies_pages}+{add_number}...` - roll with more dies at same time
                                                       `random_year` - give random year in history or future""")
    elif args in ["syntax"]:
        embed.add_field(name = "Syntax for Beginners", value = """{} - input text
                                                                  [] - may or not may include
                                                                  x-y - number from x to y include x and y
                                                                  A-B - letters A to B
                                                                  some1/some2/some3 - input some1 or some2 or some3
                                                                  ... - and other that""")
    elif args in ["income"]:
        if admin(ctx):
            embed.add_field(name = "Income Set up", value = """`new_work {work_name} {payday_perwork} [1-100] [{vacancy}/infinite] [every [0-7day] [0-24hour] [0-59min] [0-59s]]/[never]` - create new work
                                                               `edit_work {work_name} {edit_thing} {new_value}` - edit exitstin work
                                                               `set_police_chance 0-100` - set chance to police arrest you if you rob or crime !! raise when too much crimes and robs per day !! 
                                                               `set_rob_time [[0-7day] [0-24hour] [0-59min] [0-59s]]/[never]` - set time between robs
                                                               `set_crime_time [[0-7day] [0-24hour] [0-59min] [0-59s]]/[never]` - set time between crimes""")
        embed.add_field(name = "For dumbs", value = """`get_work {work_name}` - get work !! you can have only one work !!
                                                       `work` - work and get money
                                                       `rob {user}` - rob someone !! you can be arrest !!
                                                       `crime shop/market/bank/police/gold_storage` - rob something""")
    else:
        await help_(ctx)
        return
    await ctx.channel.send(embed = embed)

@info.error
async def info_error(ctx, error):
    await help_(ctx)

@bot.command()
async def syntax(ctx):
    await info(ctx, args = "syntax")

bot.run(TOKEN)