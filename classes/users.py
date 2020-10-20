"""
colors:
 1(0, 90, 0),       Green
 2(0, 190, 0),      Lime
 3(0, 140, 140),    Cyen
 4(0, 0, 190),      Blue
 5(0, 0, 90),       Dark Blue
 6(190, 0, 130),    Pink
 7(190, 0, 0),      Red
 8(0, 0, 0),        Black
 9(100, 30, 0),     Brown
10(100, 30, 120),   Purple
11(190, 190, 190),  White
12(190, 90, 0),     Orange
13(190, 190, 0),    Yellow  

    name            - jméno                                 discord_user_name
    id              - id                                    discord_user_id

    name_state      - jméno státu                           string
    color           - barva jeho území                      RGB
    aliace          - aliance (odkaz na ni)                 aliace

    research_now    - aktuálně zkoumaný patent              (patent, time_stemp)    - time_stemp je začátek vyzkumu
    work            - práce                                 work
    walet           - peníze v penežence                    integer coins
    bank            - peníze v bance                        integer coins
    old_works       - práce které měl                       (work:integer secunds)     
    last_do         - čas podlení work/rob/...              (work/rob/...:time_stemp)
"""
from classes.units import unit
from classes.buildings import building
from classes.patents import patent
from classes.works import work
from time import time
class user:
    def __init__(self, discord_user):
        self.name = discord_user.name
        self.id   = discord_user.id
        
        self.name_state = ""
        self.color = None
        self.aliance = None

        self.unit_list = []
        self.patents   = []
        self.buildings = []

        self.reserch = [None, 0]

        self.walet = 0
        self.bank  = 0

        self.work = None
        self.last_do = {"work":time(), "rob":time(), "crime":time()}
        self.old_works = []

    def pay(self, money):
        if money > self.walet + self.bank:
            return False
        if money > self.walet:
            money -= self.walet
            self.walet = 0
            self.bank -= money
        else:
            self.walet -= money
        return True