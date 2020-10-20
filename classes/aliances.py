"""
    name            - jméno aliace                          string
    user_list       - seznam členů aliace (odkaz na ně)     (user)
    user_prefs      - síla hlasů členů                      (user:1-10)
    bank            - peníze                                integer coins
    army            - seznam jednotek                       (unit)
"""
from classes.users import user
from classes.units import unit

class aliace:
    def __init__(self, name, owner:user):
        self.name = name
        self.user_list = [owner]
        self.user_prefs = {owner:10}
        self.bank = 0
        self.army = []

    def pay(self, money):
        if money > self.bank:
            return False
        self.bank -= money
        return True