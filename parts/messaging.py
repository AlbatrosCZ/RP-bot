import discord
async def send(channel, text):
    await channel.send(text)
async def send_embed(channel, embed):
    await channel.send(embed = embed)
async def add_reaction(message, reaction):
    message.add_reaction(reaction)

async def send_bad(message_text, channel):
    await channel.send(f":disappointed_relieved:{message_text}")

async def send_help(message_text: list, channel):
    embed = discord.Embed(title = ":question:***Help***:question:")
    if type(message_text[0]) == str:
        embed.add_field(name = message_text[0], value = message_text[1])
    else:
        for i in message_text:
            try:
                in_line = i[2]
            except:
                in_line = True
            embed.add_field(name = i[0], value = i[1], inline = in_line)
    await channel.send(embed = embed)

async def dont_have_permmission(ctx, permmission):
    await ctx.message.add_reaction("⚠️")
    await ctx.channel.send(f"```You don have Permmission ({permmission})```")

async def send_error(ctx, error):
    await ctx.message.add_reaction("⚠️")
    await ctx.channel.send(f"```Error:\n{error}```")