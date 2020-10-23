from parts.messaging import send_help
from parts.if_is import *
async def default_help(ctx):
    await send_help([[":crossed_swords: RP Commands :crossed_swords:", "help RP"], 
                     [":keyboard: Server Commands :keyboard:", "help server"], 
                     [":sunglasses: User Commands :sunglasses:", "help user"], 
                     [":baggage_claim: Items Commands :baggage_claim:", "help item"], 
                     [":warning: Warning Commands :warning:", " help warning"],
                     [":pencil: All Commands list :pencil:", "help list"],
                     [":regional_indicator_v::regional_indicator_e::regional_indicator_r::regional_indicator_s::regional_indicator_i::regional_indicator_o::regional_indicator_n:", ":zero::record_button::one: (uncomplite)"],
                     [":incoming_envelope: News in this version:incoming_envelope:", "news"],
                     [":regional_indicator_v::regional_indicator_e::regional_indicator_r::regional_indicator_s::regional_indicator_i::regional_indicator_o::regional_indicator_n:", ":zero::record_button::one: (uncomplite)"]], ctx.channel)
async def help_me(ctx):
    args = ctx.content.lower().split(" ")[1:]
    if len(args) == 0:
        await default_help(ctx)
    elif args[0] in ["rp", "rpg", "role_play", "roleplay"]:
        try:
            if args[1] == "start":
                await send_help(["RP start", "This command start RP (delete all stats)\n\nAdministrator use only\n\nNo arguments\n\nexample: `RP start`"], ctx.channel)
            elif args[1] == "stop":
                await send_help(["RP stop", "This command stop RP \nstoped RP can't be resume, can be only start again\n\nAdministrator use only\n\nNo arguments\n\nexample: `RP stop`"], ctx.channel)
            elif args[1] == "pause":
                await send_help(["RP pause", "This command pause RP \n\nAdministrator use only\n\navailable arguments:\n:white_small_square: time (days hours minutes seconds) - specifies how long the RP will be paused. If not specified, the RP will be paused until the resume.\n\nexample: `RP pause 1d 2h 3m 4s` (this pause the RP for 1 day, 2 hours, 3 minutes and 4 secunds)"], ctx.channel)
            elif args[1] == "resume":
                await send_help(["RP resume", "This command resume RP \n\nAdministrator use only\n\navailable arguments:\n:white_small_square: time (days hours minutes seconds) - specifies how long the RP will be paused before it is resumed. If not entered, the resume is immediate.\n\nexample: `RP resume 1d 2h 3m 4s` (this resume the RP in 1 day, 2 hours, 3 minutes and 4 secunds)"], ctx.channel)
            else:
                await default_help(ctx)
        except:
            await send_help([["List of helps", "```help RP\nhelp RP start\nhelp RP stop\nhelp RP pause\nhelp RPresume```"], ["Aliases", "rpg, role_play, roleplay"]], ctx.channel)
    elif args[0] in ["auto_role", "ar", "autorole"]:
        try:
            if args[1] == "add":
                await send_help(["auto_role add", "add new automaticaly income role\n\nAdministrator use only\n\navailable arguments:\n:black_small_square: name (@ROLE or ROLE) - specifies role if role dosn't exist create one\n:black_small_square: payday (money) - how much someone who have roll get\n:black_small_square: payday_time (days hours minutes seconds) - time between incomes\n\nexample: `auto_role add @role 2000 1d 2h 3m 4s` (This create new auto income role named role that get 2000 coins every 1 day, 2 hours, 3 minutes and 4 secunds)"], ctx.channel)
            elif args[1] in ["rem", "remove", "del", "delete"]:
                await send_help(["auto_role remove", "remove existing automaticaly income role\n\nAdministrator use only\n\navailable arguments:\n:black_small_square: name (@ROLE or ROLE) - specifies role name\n\nexample: `auto_role remove role` (This remove auto_role named role)\n\naliases: rem, remove, del, delete"], ctx.channel)
            elif args[1] == "edit":
                await send_help(["auto_role edit", "edit old automaticaly income role\n\nAdministrator use only\n\navailable arguments:\n:black_small_square: name (@ROLE or ROLE) - specifies role name\n:black_small_square: value_name (payday/pd or payday_time/pdt)- specifies what woud be changed\n:black_small_square: new_value (value) - it is specific for every value\n\nexamples: `auto_role edit role payday 5000` (set payday of role to 5000)\n`auto_role edit role payday_time 1d 2h 3m 4s` (set payday_time of role to 1 day, 2 hours, 3 minutes and 4 secunds"], ctx.channel)
            elif args[1] == "get":
                await send_help(["auto_role get", "get every auto_role\n\neveryone can use\n\nNo arguments\n\nexample: `auto_role get`"], ctx.channel)
            else:
                await default_help(ctx)
        except:
            await send_help([["Commands list", "```help auto_role add\nhelp auto_role remove\nhelp auto_role edit```"], ["Aliases", "ar, autorole"]], ctx.channel)
    elif args[0] in ["server", "sr", "serv"]:
        try:
            if args[1] == "clear":
                await send_help(["server clear", "Clear text form channel where was command writed\n\nCan use everyone who can edit messages\n\nNo argumets\n\nexample: `server clear`"], ctx.channel)
            elif args[1] == "delete":
                await send_help(["server delete", "Delete amount of messages\n\nCan use everyone who can edit messages\n\navailable arguments:\n:black_small_square: amount (1 or more) - amount of messages that must be deleted\n\nexample: `server delete 123` (This delete 123 message in channel where used"], ctx.channel)
            else:
                await default_help(ctx)
        except:
            await send_help([["Commands List", "```help server clear\nhelp server delete```"], ["Aliases", "sr, serv"]], ctx.channel)
    elif args[0] in ["aconut", "balance", "bal", "user", "mem", "member"]:
        await send_help(["aconut", "Show someone aconut\n\nEveryone can use\n\navailable arguments:\n:white_small_square: user (@user or user name) - if you dont specify set to you"], ctx.channel)
    elif args[0] in ["list", "all"]:
        await send_help([["Commands' list",
                        """
                        RP - `rp`, `rpg`, `role_play`, `roleplay`
                        - start: `start`
                        - stop: `stop`
                        - pause: `pause`
                        - resume: `resume`
                        
                        auto_role - `auto_role`, `ar`, `autorole`
                        - add: `auto_role add`
                        - remove: `auto_role remove`/`auto_role rem`/`auto_role del`/``
                        - edit: `auto_role edit`
                        - get: `auto_role get`
                        
                        server
                        - clear: `server clear`
                        - delete: `server delete`

                        nuke_channel: `nuke_channel`
                        ping: `ping`
                        aconut: `aconut`
                        help `help`
                        """], ["Syntax here", 
                        """
                        command - `how to write it`
                         - sub command: `this must be afer command tu func sub command`
                        !!! If a sub command exists it must be used. Without it the command does not work. !!!
                        """, False]], ctx.channel)







