"""
    name            - jméno                                 string
    payday          - výplata                               integer coins
    payday_time     - čas mezi pracemi                      integer secunds
    request         - seznam prací s minimalní časem        (work:integer sec)      - pez requestů si nemůžeš práci vybrat
"""
class work:
    def __init__(self, name, payday, payday_time, request = {}):
        self.name = name
        self.payday = payday
        self.payday_time = payday_time
        self.request = request

    def can_have(self, user):
        money = 0
        for i in self.request:
            if type(i) == list:
                can = False
                for j in i:
                    if j in user.old_works or j == user.work:
                        can = True
            elif type(i) == str:
                can = False
                if i == "money":
                    if self.request[i] <= user.walet+user.bank:
                        money = self.request[i]
                        can = True
            else:
                can = False
                if i in user.old_works or j == user.work:
                    can = True
            if not can:
                return False
        return user.pay(money)
