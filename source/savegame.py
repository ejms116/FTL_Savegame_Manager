from source import parser as p
from source import run as r

class Savegame:
    def __init__(self, filepath, filepath_mv):
        self.filepath = filepath
        self.filepath_mv = filepath_mv
        self.parser = p.Parser()
        self.run = r.Run()
        self.mv = False

    def clear(self):
        self.run.__init__()

    def parse(self):
        if self.mv:
            self.run.update(self.parser.parse_mv(self.filepath_mv))
        else:
            self.run.update(self.parser.parse_ftl(self.filepath))

    def parse_all(self):
        #fin = open(self.filepath, "rb")
        #fin2 = open(self.filepath, "rb")
        #full_save = fin.read(-1)
        #full_save_conv = int.from_bytes(fin2.read(-1), byteorder="little")
        #save = self.parser.parse_ftl(self.fp_test)

        #save = self.parser.parse_ftl(self.filepath)

        with open(self.filepath, mode='rb') as file:
            save = file.read()
        return save
