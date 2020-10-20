from pickle import dump, load

from classes.server import *
from classes.item_type import *

class holder:
    def __init__(self, save_path = "save/"):
        try:
            self.servers = load(open(save_path+"servers", 'rb'))
            self.itme_types = load(open(save_path+"it_types", 'rb'))
        except:
            self.servers = []
            self.itme_types = []
            open(save_path+"it_types", 'wb').close()
            open(save_path+"servers", 'wb').close()
        self.path = save_path

    def add_server(self, discord_server):
        pass
        
    def get_server(self, id):
        pass

    def get_servers(self, **args):
        pass

    def save(self):
        dump(self.servers, open(self.path + "servers", 'wb'))
        dump(self.itme_types, open(self.path + "it_types", 'wb'))