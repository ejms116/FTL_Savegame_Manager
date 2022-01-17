from source import parser as p

class Savegame:
    def __init__(self, filepath):
        self.filepath = filepath
        self.parser = p.Parser()
        self.data = None
        self.total_beacons_explored = None
        self.ship_name = None
        self.blueprint_name = None
        self.sector = None
        self.scrap = None
        self.total_scrap_collected = None
        self.total_ships_defeated = None
        self.difficulty = None

        self.fp_test = "C:\\Users\\Erik\\Desktop\\FTL Savegame Manager\\saves\\continue.sav"

    def parse(self):
        self.data = self.parser.parse_ftl(self.filepath)
        self.total_beacons_explored = self.data["total_beacons_explored"]
        self.ship_name = self.data["ship_name"]
        self.blueprint_name = self.data["blueprint_name"]
        self.sector = self.data["sector"]
        self.total_scrap_collected = self.data["total_scrap_collected"]
        self.total_ships_defeated = self.data["total_ships_defeated"]
        self.difficulty = self.data["difficulty"]

    def parse_all(self):
        #fin = open(self.filepath, "rb")
        #fin2 = open(self.filepath, "rb")
        #full_save = fin.read(-1)
        #full_save_conv = int.from_bytes(fin2.read(-1), byteorder="little")
        save = self.parser.parse_ftl(self.fp_test)
        return save
