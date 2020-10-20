"""
    name            - jméno                                 discord_role_name
    id              - id                                    discord_role_id
    payday          - výplata                               integer coins
    payday_time     - čas než dostaneš peníze               integer secunds
    last_colect     - čas posledního převzetí peněz         time_stemp
"""
from time import time
class auto_role:
    def __init__(self, discord_role, **args):
        self.name = discord_role.name
        self.id   = discord_role.id
        try:
            self.payday = int(args['payday'])
        except:
            self.payday = 100
        try:
            self.payday_time = int(args['payday_time'])
        except:
            self.payday_time = 60*60
        self.last_collect = time()

    def get_income(self):
        if time() - self.last_collect >= self.payday_time:
            self.last_collect = time()
            return self.payday
        else:
            return 0