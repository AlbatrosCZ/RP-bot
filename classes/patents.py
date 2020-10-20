"""
    name            - jméno                                 string
    need            - patenty potřebné pro výzkum           (patent)
    research_time   - doba výzkumu                          integer secunds
    research_price  - cena výzkumu                          integer coins
    unit_list       - seznam jednotek které lze trenovat    (unit)                  - s tímto patentem
    buildings       - seznam budov které lze postavit       (building)              - s tímto patentem
"""
class patent:
    def __init__(self, name, need, unit_list, buildings, **args):
        self.name = name
        self.need = need
        self.unit_list = unit_list
        self.buildings = buildings
        try:
            self.research_time = args["research_time"]
        except:
            self.research_time = 60*60
        try:
            self.research_price = args["research_price"]
        except:
            self.research_price = 0

    def can_do(self, user):
        for i in self.need:
            if i not in user.patents:
                return False
        return True