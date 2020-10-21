def admin(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        return True
    else:
        return False

def edit_messages(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).edit_messages:
        return True
    else:
        return False