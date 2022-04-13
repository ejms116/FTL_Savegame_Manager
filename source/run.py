from collections import Counter
import math

class Run:
    def __init__(self):
        # TODO this is ugly, do this in a different way!
        self.item_ids = [{'id': 'ARTILLERY_BOSS_1', 'name': '', 'cost': '55'}, {'id': 'ARTILLERY_BOSS_2', 'name': '', 'cost': '80'}, {'id': 'ARTILLERY_BOSS_3', 'name': '', 'cost': '70'}, {'id': 'ARTILLERY_BOSS_4', 'name': '', 'cost': '40'}, {'id': 'ARTILLERY_FED', 'name': 'Artillery Beam', 'cost': '0'}, {'id': 'LASER_BURST_1', 'name': 'Defense Laser Mark I', 'cost': '20'}, {'id': 'LASER_BURST_2', 'name': 'Dual Shot Laser', 'cost': '25'}, {'id': 'LASER_BURST_2_A', 'name': 'Burst Laser Mark I', 'cost': '50'}, {'id': 'LASER_BURST_3', 'name': 'Burst Laser Mark II', 'cost': '80'}, {'id': 'LASER_BURST_5', 'name': 'Burst Laser Mark III', 'cost': '95'}, {'id': 'LASER_HEAVY_1', 'name': 'Heavy Laser Mark I', 'cost': '50'}, {'id': 'LASER_HEAVY_2', 'name': 'Heavy Laser Mark II', 'cost': '65'}, {'id': 'LASER_HEAVY_1_SP', 'name': 'Heavy Pierce Laser Mark I', 'cost': '55'}, {'id': 'CRYSTAL_1', 'name': '', 'cost': '20'}, {'id': 'MISSILES_1', 'name': 'Leto Missiles', 'cost': '20'}, {'id': 'MISSILES_2_PLAYER', 'name': 'Artemis Missiles', 'cost': '38'}, {'id': 'MISSILES_2', 'name': 'Artemis Missiles', 'cost': '38'}, {'id': 'MISSILES_3', 'name': 'Hermes Missile', 'cost': '45'}, {'id': 'MISSILES_BURST', 'name': 'Pegasus Missile', 'cost': '60'}, {'id': 'MISSILES_BREACH', 'name': 'Breach Missiles', 'cost': '65'}, {'id': 'BEAM_1', 'name': 'Mini Beam', 'cost': '20'}, {'id': 'BEAM_LONG', 'name': 'Pike Beam', 'cost': '55'}, {'id': 'BEAM_2', 'name': 'Halberd Beam', 'cost': '65'}, {'id': 'BEAM_3', 'name': 'Glaive Beam', 'cost': '95'}, {'id': 'BEAM_FIRE', 'name': 'Fire Beam', 'cost': '50'}, {'id': 'BEAM_BIO', 'name': 'Anti-Bio Beam', 'cost': '50'}, {'id': 'LASER_HULL_1', 'name': 'Hull Smasher Laser', 'cost': '55'}, {'id': 'LASER_HULL_2', 'name': 'Hull Smasher Laser Mark II', 'cost': '75'}, {'id': 'BEAM_HULL', 'name': 'Hull Beam', 'cost': '70'}, {'id': 'MISSILES_HULL', 'name': 'Hull Missile', 'cost': '65'}, {'id': 'ION_1', 'name': 'Ion Blast', 'cost': '30'}, {'id': 'ION_2', 'name': 'Heavy Ion', 'cost': '45'}, {'id': 'ION_4', 'name': 'Ion Blast Mark II', 'cost': '70'}, {'id': 'BOMB_1', 'name': 'Small Bomb', 'cost': '45'}, {'id': 'BOMB_BREACH_1', 'name': 'Breach Bomb Mark I', 'cost': '50'}, {'id': 'BOMB_BREACH_2', 'name': 'Breach Bomb Mark II', 'cost': '60'}, {'id': 'BOMB_FIRE', 'name': 'Fire Bomb', 'cost': '50'}, {'id': 'BOMB_ION', 'name': 'Ion Bomb', 'cost': '55'}, {'id': 'BOMB_HEAL', 'name': 'Healing Burst', 'cost': '40'}, {'id': 'BOMB_LOCK', 'name': 'Crystal Lockdown Bomb', 'cost': '45'}, {'id': 'CRYSTAL_BURST_1', 'name': 'Crystal Burst Mark I', 'cost': '20'}, {'id': 'CRYSTAL_BURST_2', 'name': 'Crystal Burst Mark II', 'cost': '20'}, {'id': 'CRYSTAL_HEAVY_1', 'name': 'Heavy Crystal Mark I', 'cost': '20'}, {'id': 'CRYSTAL_HEAVY_2', 'name': 'Heavy Crystal Mark II', 'cost': '20'}, {'id': 'DRONE_LASER', 'name': '', 'cost': 0}, {'id': 'DRONE_LASER_2', 'name': '', 'cost': 0}, {'id': 'DRONE_BEAM', 'name': '', 'cost': 0}, {'id': 'DRONE_ION', 'name': '', 'cost': 0}, {'id': 'DRONE_MISSILE', 'name': '', 'cost': 0}, {'id': 'ANTI_DRONE_ION', 'name': '', 'cost': 0}, {'id': 'DRONE_BEAM2', 'name': '', 'cost': 0}, {'id': 'DRONE_FIREBEAM', 'name': '', 'cost': 0}, {'id': 'BOMB_HEAL_SYSTEM', 'name': 'Repair Burst', 'cost': '40'}, {'id': 'SHOTGUN_PLAYER', 'name': 'Adv. Flak Gun', 'cost': '60'}, {'id': 'SHOTGUN', 'name': 'Flak Gun Mark I', 'cost': '65'}, {'id': 'ARTILLERY_FED_C', 'name': 'Flak Artillery', 'cost': '75'}, {'id': 'SHOTGUN_2', 'name': 'Flak Gun Mark II', 'cost': '80'}, {'id': 'MISSILE_CHARGEGUN', 'name': 'Swarm Missiles', 'cost': '65'}, {'id': 'LASER_CHAINGUN', 'name': 'Chain Burst Laser', 'cost': '65'}, {'id': 'LASER_CHAINGUN_2', 'name': 'Chain Vulcan', 'cost': '95'}, {'id': 'ION_CHAINGUN', 'name': 'Chain Ion', 'cost': '55'}, {'id': 'LASER_CHARGEGUN_PLAYER', 'name': 'Laser Charger', 'cost': '30'}, {'id': 'LASER_CHARGEGUN', 'name': 'Laser Charger', 'cost': '55'}, {'id': 'LASER_CHARGEGUN_2', 'name': 'Laser Charger Mark II', 'cost': '70'}, {'id': 'ION_CHARGEGUN', 'name': 'Ion Charger', 'cost': '50'}, {'id': 'ION_STUN', 'name': 'Ion Stunner', 'cost': '35'}, {'id': 'BOMB_STUN', 'name': 'Stun Bomb', 'cost': '45'}, {'id': 'PDS_SHOT', 'name': '', 'cost': '55'}, {'id': 'COMBAT_ION', 'name': '', 'cost': '50'}, {'id': 'COMBAT_MISSILE', 'name': '', 'cost': '50'}, {'id': 'COMBAT_1', 'name': 'Combat Drone Mark I', 'cost': '50'}, {'id': 'COMBAT_BEAM', 'name': 'Anti-Ship Beam Drone I', 'cost': '50'}, {'id': 'COMBAT_2', 'name': 'Combat Drone Mark II', 'cost': '75'}, {'id': 'SHIP_REPAIR', 'name': 'Hull Repair', 'cost': '85'}, {'id': 'DEFENSE_1', 'name': 'Defense Drone Mark I', 'cost': '50'}, {'id': 'DEFENSE_2', 'name': 'Defense Drone Mark II', 'cost': '70'}, {'id': 'DEFENSE_2_ENEMY', 'name': '', 'cost': '70'}, {'id': 'BOSS_DEFENSE_2', 'name': '', 'cost': '75'}, {'id': 'REPAIR', 'name': 'System Repair Drone', 'cost': '30'}, {'id': 'BATTLE', 'name': 'Anti-Personnel Drone', 'cost': '35'}, {'id': 'BOARDER', 'name': 'Boarding Drone', 'cost': '70'}, {'id': 'BOARDER_BOSS', 'name': '', 'cost': '70'}, {'id': 'BOARDER_ION', 'name': 'Ion Intruder Drone', 'cost': '65'}, {'id': 'DRONE_HACKING', 'name': '', 'cost': '70'}, {'id': 'ANTI_DRONE', 'name': 'Anti-Combat Drone', 'cost': '35'}, {'id': 'COMBAT_BEAM_2', 'name': 'Anti-Ship Beam Drone II', 'cost': '60'}, {'id': 'COMBAT_FIRE', 'name': 'Anti-Ship Fire Drone', 'cost': '50'}, {'id': 'DRONE_SHIELD', 'name': 'Shield Overcharger', 'cost': '60'}, {'id': 'DRONE_SHIELD_PLAYER', 'name': 'Shield Overcharger', 'cost': '60'}, {'id': 'ROCK_ARMOR', 'name': 'Rock Plating', 'cost': '80'}, {'id': 'CRYSTAL_SHARDS', 'name': 'Crystal Vengeance', 'cost': '80'}, {'id': 'ENERGY_SHIELD', 'name': 'Zoltan Shield', 'cost': '80'}, {'id': 'NANO_MEDBAY', 'name': 'Engi Med-bot Dispersal', 'cost': '60'}, {'id': 'SLUG_GEL', 'name': 'Slug Repair Gel', 'cost': '60'}, {'id': 'CREW_STIMS', 'name': 'Mantis Pheromones', 'cost': '50'}, {'id': 'DRONE_SPEED', 'name': 'Drone Reactor Booster', 'cost': '50'}, {'id': 'SYSTEM_CASING', 'name': 'Titanium System Casing', 'cost': '80'}, {'id': 'ION_ARMOR', 'name': 'Reverse Ion Field', 'cost': '45'}, {'id': 'CLOAK_FIRE', 'name': 'Stealth Weapons', 'cost': '50'}, {'id': 'REPAIR_ARM', 'name': 'Repair Arm', 'cost': '50'}, {'id': 'SCRAP_COLLECTOR', 'name': 'Scrap Recovery Arm', 'cost': '50'}, {'id': 'ADV_SCANNERS', 'name': 'Long-Ranged Scanners', 'cost': '30'}, {'id': 'AUTO_COOLDOWN', 'name': 'Automated Re-loader', 'cost': '40'}, {'id': 'SHIELD_RECHARGE', 'name': 'Shield Charge Booster', 'cost': '45'}, {'id': 'WEAPON_PREIGNITE', 'name': 'Weapon Pre-igniter', 'cost': '120'}, {'id': 'FTL_BOOSTER', 'name': 'FTL Recharge Booster', 'cost': '50'}, {'id': 'FTL_JUMPER', 'name': 'Adv. FTL Navigation', 'cost': '50'}, {'id': 'DRONE_RECOVERY', 'name': 'Drone Recovery Arm', 'cost': '50'}, {'id': 'FTL_JAMMER', 'name': 'FTL Jammer', 'cost': '30'}, {'id': 'STASIS_POD', 'name': 'Damaged Stasis Pod', 'cost': '30'}, {'id': 'FTL_BOOSTER', 'name': 'FTL Recharge Booster', 'cost': '50'}, {'id': 'AUTO_COOLDOWN', 'name': 'Automated Re-loader', 'cost': '40'}, {'id': 'O2_MASKS', 'name': 'Emergency Respirators', 'cost': '50'}, {'id': 'EXPLOSIVE_REPLICATOR', 'name': 'Explosive Replicator', 'cost': '60'}, {'id': 'FIRE_EXTINGUISHERS', 'name': 'Fire Suppression', 'cost': '65'}, {'id': 'FLEET_DISTRACTION', 'name': 'Distraction Buoys', 'cost': '55'}, {'id': 'TELEPORT_HEAL', 'name': 'Reconstructive Teleport', 'cost': '70'}, {'id': 'BATTERY_BOOSTER', 'name': 'Battery Charger', 'cost': '40'}, {'id': 'DEFENSE_SCRAMBLER', 'name': 'Defense Scrambler', 'cost': '80'}, {'id': 'BACKUP_DNA', 'name': 'Backup DNA Bank', 'cost': '40'}, {'id': 'HACKING_STUN', 'name': 'Hacking Stun', 'cost': '60'}, {'id': 'LIFE_SCANNER', 'name': 'Lifeform Scanner', 'cost': '40'}, {'id': 'ZOLTAN_BYPASS', 'name': 'Zoltan Shield Bypass', 'cost': '55'}]
        self.raw = None
        self.state_vars = {}
        self.total_beacons_explored = 999
        self.ship_name = None
        self.blueprint_name = None
        self.sector = 1
        self.total_scrap_collected = 0
        self.total_ships_defeated = 0
        self.difficulty = None

        # Data required for
        self.ship_class = None
        self.ship_variant = None
        self.result = None
        self.sector = None
        self.category = None


        self.last_ship_name = None
        self.last_beacons = 1000  # to make sure initialize_extra gets called when first run

        self.inserted = False  # boolean to display on GUI
        self.uploaded = False

        self.initialize_extra()

    def initialize_extra(self):
        self.sector_scrap_total = 0
        self.sector_scrap = [0, 0, 0, 0, 0, 0, 0, 0]
        self.sector_scrap_stuff = [0, 0, 0, 0, 0, 0, 0, 0]
        self.scrap_diff = 0  # used to calculate scrap per sector
        self.sector_diff = 1  # used to calculate scrap per sector
        self.inventory = []
        self.inventory_raw = []
        self.last_inventory_raw = []
        self.bought_items = []
        self.last_bought_items = []
        self.bought_diff = []
        self.current_beacon = None
        self.last_beacon = None


    
    def update(self, save):
        self.total_beacons_explored = save["total_beacons_explored"]
        self.current_beacon = save["beacons"][save["current_beacon_id"]]
        self.state_vars = save["state_vars"]
        self.ship_name = save["ship_name"]
        self.blueprint_name = save["blueprint_name"]
        self.sector = save["sector"]
        self.total_scrap_collected = save["total_scrap_collected"]
        self.total_ships_defeated = save["total_ships_defeated"]
        self.difficulty = save["difficulty"]

        if self.last_ship_name != self.ship_name or self.last_beacons > self.total_beacons_explored:
            self.initialize_extra()

        self.last_beacons = self.total_beacons_explored
        self.last_ship_name = self.ship_name

        if self.sector != self.sector_diff:
            self.sector_diff = self.sector
            self.scrap_diff = self.total_scrap_collected
            # new sector so reset bought items
            self.bought_items = []
            self.last_bought_items = []

        if 0 <= self.sector <= 8:
            self.sector_scrap[self.sector - 1] = self.total_scrap_collected - self.scrap_diff

        ship = self.convert_ship_name(self.blueprint_name)
        self.ship_class = ship["ship_class"]
        self.ship_variant = ship["ship_variant"]

        self.raw = save

        self.inventory_raw = []
        self.inventory_raw += save["player_ship"]["weapons"]
        temp_drones = [o["name"] for o in save["player_ship"]["drones"]]
        self.inventory_raw += temp_drones
        self.inventory_raw += save["player_ship"]["augments"]
        self.inventory_raw += save["cargo"]

        # Initialize Inventory
        origin = "free"
        if len(self.inventory) == 0:
            if self.total_beacons_explored == 1:
                origin = "starting"

        item = {}
        # check for missing items => sold/discarded
        c1 = Counter(self.last_inventory_raw)
        c2 = Counter(self.inventory_raw)

        inv_diff = (c1-c2).elements()
        for d in inv_diff:
            for i in self.inventory:
                if i["item"] == d and i["status"] == "inventory":
                    if self.current_beacon["store_present"] or self.last_beacon["store_present"]:
                        i["status"] = "sold"
                    else:
                        i["status"] = "discarded"
                    break
        # INFO this doesn't work 100%
        # If you sell something and close the store the save file is not updated
        # Therefore we check if the current beacon or the last beacon was a store to set the status to "sold"
        # When jumping to a next beacon the games always writes a new save file, so this works good
        # The only problem is when really discarding an item right after a store,
        # because that will always be considered as a "sold" item
        # TODO Try to find a way to solve this inaccuracy (low prio)

        # check for new items
        # new items are added to the real inventory with the status "free"
        # bought items are updated
        inv_diff = (c2-c1).elements()

        for i in inv_diff:
            print(inv_diff)
            item["name"] = self.get_name(i)
            item["item"] = i
            item["sector"] = self.sector
            item["origin"] = origin
            item["status"] = "inventory"
            self.inventory.append(item.copy())

        # get sold items this sector
        self.bought_items = []
        for b in save["beacons"]:
            if b["store_present"]:
                for s in b["store"]["shelves"]:
                    for i in s["items"]:
                        if not i["available"]:
                            self.bought_items.append(i["name"])
                            if i["name"] == "drones":
                                if i["extra_data"] == 0:
                                    self.bought_items.append("DEFENSE_1")
                                elif i["extra_data"] == 1:
                                    self.bought_items.append("REPAIR")
                                elif i["extra_data"] == 2:
                                    self.bought_items.append("COMBAT_1")


        d1 = Counter(self.last_bought_items)
        d2 = Counter(self.bought_items)

        # new bought items
        bought_diff = (d2-d1).elements()

        self.bought_diff += bought_diff

        temp_bought_diff = []

        for b in self.bought_diff:
            removed = False
            for i in self.inventory:
                if i["item"] == b and i["origin"] == "free" and i["sector"] == self.sector:
                    i["origin"] = "bought"
                    removed = True
                    break
            if not removed:
                temp_bought_diff.append(b)

        self.bought_diff = temp_bought_diff

        # copy a few current variables for comparison
        self.last_inventory_raw = self.inventory_raw
        self.last_beacon = self.current_beacon
        self.last_bought_items = self.bought_items

        # update sector_scrap
        self.sector_scrap_stuff = [0, 0, 0, 0, 0, 0, 0, 0]
        self.sector_scrap_total = 0
        for s in self.inventory:
            if s["origin"] == "free":
                self.sector_scrap_total += self.get_value(s["item"])
                self.sector_scrap_stuff[s["sector"]-1] += self.get_value(s["item"])

    def convert_ship_name(self, input):
        ship = {
            "ship_class": "",
            "ship_variant": ""
        }

        if input == "PLAYER_SHIP_HARD":
            ship["ship_class"] = "Kestrel"
            ship["ship_variant"] = "A"
        if input == "PLAYER_SHIP_HARD_2":
            ship["ship_class"] = "Kestrel"
            ship["ship_variant"] = "B"
        if input == "PLAYER_SHIP_HARD_3":
            ship["ship_class"] = "Kestrel"
            ship["ship_variant"] = "C"

        if input == "PLAYER_SHIP_CIRCLE":
            ship["ship_class"] = "Engi"
            ship["ship_variant"] = "A"
        if input == "PLAYER_SHIP_CIRCLE_2":
            ship["ship_class"] = "Engi"
            ship["ship_variant"] = "B"
        if input == "PLAYER_SHIP_CIRCLE_3":
            ship["ship_class"] = "Engi"
            ship["ship_variant"] = "C"

        if input == "PLAYER_SHIP_FED":
            ship["ship_class"] = "Federation"
            ship["ship_variant"] = "A"
        if input == "PLAYER_SHIP_FED_2":
            ship["ship_class"] = "Federation"
            ship["ship_variant"] = "B"
        if input == "PLAYER_SHIP_FED_3":
            ship["ship_class"] = "Federation"
            ship["ship_variant"] = "C"

        if input == "PLAYER_SHIP_ENERGY":
            ship["ship_class"] = "Zoltan"
            ship["ship_variant"] = "A"
        if input == "PLAYER_SHIP_ENERGY_2":
            ship["ship_class"] = "Zoltan"
            ship["ship_variant"] = "B"
        if input == "PLAYER_SHIP_ENERGY_3":
            ship["ship_class"] = "Zoltan"
            ship["ship_variant"] = "C"

        if input == "PLAYER_SHIP_MANTIS":
            ship["ship_class"] = "Mantis"
            ship["ship_variant"] = "A"
        if input == "PLAYER_SHIP_MANTIS_2":
            ship["ship_class"] = "Mantis"
            ship["ship_variant"] = "B"
        if input == "PLAYER_SHIP_MANTIS_3":
            ship["ship_class"] = "Mantis"
            ship["ship_variant"] = "C"

        if input == "PLAYER_SHIP_JELLY":
            ship["ship_class"] = "Slug"
            ship["ship_variant"] = "A"
        if input == "PLAYER_SHIP_JELLY_2":
            ship["ship_class"] = "Slug"
            ship["ship_variant"] = "B"
        if input == "PLAYER_SHIP_JELLY_3":
            ship["ship_class"] = "Slug"
            ship["ship_variant"] = "C"

        if input == "PLAYER_SHIP_ROCK":
            ship["ship_class"] = "Rock"
            ship["ship_variant"] = "A"
        if input == "PLAYER_SHIP_ROCK_2":
            ship["ship_class"] = "Rock"
            ship["ship_variant"] = "B"
        if input == "PLAYER_SHIP_ROCK_3":
            ship["ship_class"] = "Rock"
            ship["ship_variant"] = "C"

        if input == "PLAYER_SHIP_STEALTH":
            ship["ship_class"] = "Stealth"
            ship["ship_variant"] = "A"
        if input == "PLAYER_SHIP_STEALTH_2":
            ship["ship_class"] = "Stealth"
            ship["ship_variant"] = "B"
        if input == "PLAYER_SHIP_STEALTH_3":
            ship["ship_class"] = "Stealth"
            ship["ship_variant"] = "C"

        if input == "PLAYER_SHIP_ANAEROBIC":
            ship["ship_class"] = "Lanius"
            ship["ship_variant"] = "A"
        if input == "PLAYER_SHIP_ANAEROBIC_2":
            ship["ship_class"] = "Lanius"
            ship["ship_variant"] = "B"

        if input == "PLAYER_SHIP_CRYSTAL":
            ship["ship_class"] = "Crystal"
            ship["ship_variant"] = "A"
        if input == "PLAYER_SHIP_CRYSTAL_2":
            ship["ship_class"] = "Crystal"
            ship["ship_variant"] = "B"
        return ship


    def get_value(self, item_id):
        res = 0
        try:
            res = math.floor(int(next((i for i in self.item_ids if i['id'] == item_id), None)["cost"]) / 2)
        except Exception:
            print("error in method get_value")
        return res

    def get_name(self, item_id):
        res = ''
        try:
            res = next((i for i in self.item_ids if i['id'] == item_id), None)["name"]
        except Exception:
            print("error in method get_name")
        return res


        
    