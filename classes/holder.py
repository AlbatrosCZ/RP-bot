from pickle import dump, load

from classes.servers import server

class holder:
    def __init__(self, save_path = "save/"):
        try:
            self.servers = load(open(save_path+"servers", 'rb'))
        except:
            self.servers = []
            open(save_path+"servers", 'wb').close()
        self.path = save_path

    def add_server(self, discord_server):
        for serve in self.servers:
            if serve.id == discord_server.id:
                return "Exists"
        self.servers.append(server(discord_server))
        return "Added"

    def get_server(self, id_):
        for server in self.servers:
            if server.id == id_:
                return server
        return None

    def get_servers(self, **args):
        try:
            name = args["name"]
        except:
            name = ""
        try:
            users = int(args['users'])
        except:
            users = 0

        ret = []
        for server in self.servers:
            if name in server.name:
                if users < len(server.user_list):
                    ret.append(server)
        return ret


    def save(self):
        dump(self.servers, open(self.path + "servers", 'wb'))