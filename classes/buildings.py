"""
    name            - jméno
    pozition        - pozice                                (x, y)
    can_train       - čísla pro trening jednotky            (integer)               - pokud je má jednotka alespoň jedno z těchto čísel může budova trénovat tuto jednotku (čím víc společných čísel tím kratší doba tréningu)
    defend_power    - sílá obrany                           integer                 - 0 neučastní se obrany
    lifes           - počet životů                          (integer, integer)      - aktuálně, maximalně | 0 v maximalně zničení při zničení města, -1 v maximalně zničení při útoku na město, ostantí kladná čísla v maximalně zničení při dosažení 0
    income          - vydělá za čas                         (integer, integer, integer) - vydělá, za, posledně
"""
from time import time
class building:
    def __init__(self, name, can_train, defend_power = 0, lifes = [0, 0], income = [0, 0, time()], pozition = "Tamplate"):
        self.name = name
        self.can_train = can_train
        self.defend_power = defend_power
        self.lifes = lifes
        self.income = income

    def get_income(self):
        if not self.income[0]:
            return 0
        if time() - self.income[2] >= self.income[1]:
            self.income[2] = time()
            return self.income[0]
        return 0

    def defend(self):
        if self.lifes == [-1, -1]:
            return "destroy"
        elif self.lifes == [0, 0]:
            if not self.defend_power:
                return "no_defend"
            else:
                return [self.defend_power, self.lifes]
        else:
            if not self.defend_power:
                return [0, self.lifes]
            else:
                return [self.defend_power, self.lifes]