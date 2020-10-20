"""
    name            - jméno                                 string
    health          - životy                                integer
    attack          - útok                                  integer
    def_poz         - prvni se ničí jednotky s nižší pozicí 1-100
    beaters         - slovník zlepšení jednotky             (string:string)         - vždy co a o kolik
    can_train       - čísla pro trening jednotky            (integer)               - pokud je v budově alespoň jedno z těchto čísel může budova trénovat tuto jednotku (čím víc společných čísel tím kratší doba tréningu)                     
    train_time      - doba než se jednotka vycvičí          integer sec
"""
class unit:
    def __init__(self, name, health, attack, def_poz, beaters, can_train, train_time):
        self.name = name
        self.health = health
        self.attack = attack
        self.def_poz = def_poz
        self.beaters = beaters
        self.can_train = can_train
        self.train_time = train_time

    def attack_beater(self, enemy_def_poz):
        if enemy_def_poz == 0:
            if "buildings" in self.beaters:
                return self.beaters["buildings"]
            else:
                return 1
        if enemy_def_poz <= 50:
            if "units" in self.beaters:
                return self.beaters["units"]
            else:
                return 1
        else:
            if "warmachines" in self.beaters:
                return self.beaters["warmachines"]
            else:
                return 1