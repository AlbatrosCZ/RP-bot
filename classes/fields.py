from random import random, randint
"""
    x               - xová pozice
    y               - yová pozice
    owner           - vlastník pole
    income          - příjem z pole
    secret_income   - příjem z pole pro uzpešném prohledání
    height          - výška
"""
class field:
    def __init__(self, x, y, height, **args):
        """
        args:
        *owner - vlastník
        *income - income pokud má vlastníka
        *gen_secrets - True/False
        *secrets - list of secrets
        
        if secrets and gen_secrets make"""
        self.x = x
        self.y = y
        self.height = height

        self.owner = False # false or user
        if "owner" in args:
            if args["owner"]:
                self.owner = args["owner"]

        self.income = [] # [payday, wear away in x hours]
        if "income" in args:
            if args["income"] != 0:
                self.income = args["income"]
        
        secrets = False
        self.secret_income = [] # [material, wear away in x hours]
        if "gen_secrets" in args:
            if args["gen_secrets"] == True:
                self.__generate_secrets()
                secrets = True
        elif "secrets" in args:
            if args["secrets"] != []:
                self.secret_income = args["secrets"]
                secrets = True
        if self.secret_income == [] and not secrets:
            self.__generate_secrets()

    def __generate_secrets(self):
        """
        Gold 10%
        Silver 27%
        Bronz 31,7%
        Iron 21,85%
        Dimond 9,45%
        """
        while (random() > 0.1 and self.height == 2) or (random() > 0.3 and self.height == 1) or (random() > 0.9 and self.height == 0):
            if random() > 0.9:
                self.secret_income.append(["Gold", randint(2, 10)]) # 500 000 per hour (2-10 hour) 
            elif random() > 0.7:
                self.secret_income.append(["Silver", randint(3, 11)]) # 300 000 per hour (3-11 hour)
            elif random() > 0.5:
                self.secret_income.append(["Bronz", randint(5, 13)]) # 100 000 per hour (4-12 hour)
            elif random() > 0.3:
                self.secret_income.append(["Iron", randint(4, 12)]) # 200 000 per hour (5-13 hour)
            else:
                self.secret_income.append(["Dimond", randint(1, 6)]) # 1 000 000 per hour (1-6 hour) 

    def finding(self, level):
        chance = {0:[0.3, 1], 1:[0.5, 5], 2:[0.8, 10]}[level]
        do = True
        while do and chance[1]:
            if random() <= chance[0]:
                self.income.append([{"Dimond":1000000,"Gold":500000,"Silver":300000,"Iron":200000,"Bronz":100000}[self.secret_income[0][0]], self.secret_income[0][1]])
                del self.secret_income[0]

    def get_income(self):
        money = 0
        for i in self.income:
            if i[1] > 0:
                i[1] -= 1
                money += i[0]
        for i in range(len(self.income), 0, -1):
            if self.income[i][1] == 0:
                del self.income[i]

    def get_color(self):
        color = [0, 0, 0]
        if self.owner:
            color = self.owner.color
        if self.height == 1:
            for i in range(3):
                color[i] += 40
        if self.height == 2:
            for i in range(3):
                color[i] += 60
        

