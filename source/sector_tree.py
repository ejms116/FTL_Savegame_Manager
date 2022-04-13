class RandomSectorTreeGenerator:
    def __init__(self, rng):
        self.rng = rng

    def generate_sector_tree(self, seed):
        civilian_sectors = self.get_civilian_sectors()
        hostile_sectors = self.get_hostile_sectors()
        nebula_sectors = self.get_nebula_sectors()
        self.generate_sector_tree(seed, civilian_sectors, nebula_sectors, hostile_sectors)

    # internal function
    def generate_sector_tree(self, seed, civilian_sectors, nebula_sectors, hostile_sectors):
        random = self.rng(seed)
        

    def get_dat_sectors(self):
        pass

    def get_nebula_sectors(self):
        nebula_sectors = []
        nebula_sectors.append(Sector(False, 0, "NEBULA_SECTOR"))
        nebula_sectors.append(Sector(True, 3, "SLUG_HOME"))
        nebula_sectors.append(Sector(False, 3, "SLUG_SECTOR"))
        return nebula_sectors

    def get_hostile_sectors(self):
        hostile_sectors = []
        # TODO
        return hostile_sectors

    def get_civilian_sectors(self):
        civilian_sectors = []
        # TODO
        return civilian_sectors

    def get_random_sector_type(self):
        n = self.rng.rand()
        if n % 10 <= 1:
            result = "NEBULA"
        elif n % 10 > 5:
            result = "HOSTILE"
        else:
            result = "CIVILIAN"

        return result

    def get_random_sector_column_size(self, column, prev_size):
        while True:
            n = self.rng.rand()
            result = n % 3 + 2
            if result != prev_size:
                break

        if column == 1:
            result = 2

        return result




class Sector:
    def __init__(self, unique, min, id, title_list=[]):
        self.unique = unique
        self.min = min
        self.id = id
        self.title_list = title_list


class SectorDot:
    def __init__(self, sector_type, sector_id, sector_title):
        self.sector_type = sector_type
        self.sector_id = sector_id
        self.sector_title = sector_title
        self.visited = False

    def is_similar_to(self, sdot):
        if self.sector_type != sdot.sector_type:
            return False

        if self.sector_id != sdot.sector_id:
            return False

        if self.sector_title != sdot.sector_title:
            return False

        return True






