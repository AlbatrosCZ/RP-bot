"""
    name            - jméno                                 discord_server_name
    id              - id                                    discord_server_id
    user_list       - seznam uživatelů                      (user)
    alis_list       - seznam aliancí                        (aliace)                - aliace
    unit_list       - seznam najatelných jednotek           (unit)                  - inventory
    buildings       - seznam postavytelných budov           (building)              - inventory
    research        - seznam vyzkoumatelných patentů        (patent)                - research
    work_list       - seznam prací                          (work)                  - income
    auto_role_list  - seznam automatických rolý             (auto_role)             - income
    police          - šance na to že tě chytne policie      -1-100
    rob_time        - čas než budeš moct znovu krást        integer secunds
    crime_time      - čas než budeš moct znovu loupit       integer secunds
    mapa            - mapa                                  ((field))
"""
from classes.users import user
from classes.aliances import aliace
from classes.units import unit
from classes.buildings import building
from classes.patents import patent
from classes.works import work
from classes.auto_roles import auto_role
from classes.fields import field

from time import time


class server:
    def __init__(self, discord_server):
        self.name = discord_server.name
        self.id   = discord_server.id

        self.user_list = []
        for mem in discord_server.users:
            self.user_list.append(user(mem))
        
        self.alis_list = []
        self.unit_list = []
        self.buildings = []
        self.research  = []

        self.work_list      = []
        self.auto_role_list = []

        self.rob_time   = 0
        self.crime_time = 0
        self.police     = 0
        
        self.mapa = []

    def add_user(self, discord_user):
        self.user_list.append(user(discord_user))

    def add_aliance(self, name, creator):
        self.alis_list.append(aliace(name, creator))

    def add_unit(self, name, health, attack, def_poz, beaters, can_train, train_time):
        self.unit_list.append(unit(name, [health, health], attack, def_poz, beaters, can_train, train_time))

    def add_building(self, name, can_train, defend_power, lifes, income, pay_time):
        self.buildings.append(building(name, can_train, defend_power, [lifes, lifes], [income, pay_time, time()]))

    def add_research(self, name, need, unit_list, buildings, research_time, research_price):
        self.research.append(patent(name, need, unit_list, buildings, research_time=research_time, research_price=research_price))

    def add_work(self, name, payday, payday_time, request):
        self.work_list.append(work(name, payday, payday_time, request))

    def add_auto_role(self, discord_role, payday, payday_time):
        self.auto_role_list.append(auto_role(discord_role, payday = payday, payday_time))

        