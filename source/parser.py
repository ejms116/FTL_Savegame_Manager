

class Parser:
    def __init__(self):
        x  = 0

    def read_int(self, fin):
        return int.from_bytes(fin.read(4), byteorder="little")

    def read_string(self, fin):
        length = int.from_bytes(fin.read(4), byteorder="little")
        string = fin.read(length)
        return string.decode("utf-8")

    def read_bool(self, fin):
        boolean = int.from_bytes(fin.read(4), byteorder="little")
        return boolean != 0

    def read_animation(self, fin):
        self.read_bool(fin)
        self.read_bool(fin)
        self.read_int(fin)
        self.read_int(fin)
        self.read_int(fin)
        self.read_int(fin)
        self.read_int(fin)

    def read_crew(self, fin):
        crew = {}
        crew["name"] = self.read_string(fin)
        crew["race"] = self.read_string(fin)
        crew["boarding_drone"] = self.read_bool(fin)
        crew["health"] = self.read_int(fin)
        # Sprite locations
        self.read_int(fin)
        self.read_int(fin)
        crew["room_id"] = self.read_int(fin)
        crew["room_square"] = self.read_int(fin)
        crew["player"] = self.read_bool(fin)

        crew["clone_ready"] = self.read_int(fin)
        crew["death_order"] = self.read_int(fin)

        tint_count = self.read_int(fin)
        for i in range(tint_count):
            self.read_int(fin)

        crew["mind_controlled"] = self.read_bool(fin)
        crew["saved_room_square"] = self.read_int(fin)
        crew["saved_room_id"] = self.read_int(fin)

        crew["skill_pilot"] = self.read_int(fin)
        crew["skill_engine"] = self.read_int(fin)
        crew["skill_shield"] = self.read_int(fin)
        crew["skill_weapon"] = self.read_int(fin)
        crew["skill_repair"] = self.read_int(fin)
        crew["skill_combat"] = self.read_int(fin)

        crew["male"] = self.read_bool(fin)

        crew["repairs"] = self.read_int(fin)
        crew["combat_kills"] = self.read_int(fin)
        crew["pilot_evasions"] = self.read_int(fin)
        crew["jumps_survived"] = self.read_int(fin)
        crew["masteries_earned"] = self.read_int(fin)

        crew["stun_ticks"] = self.read_int(fin)
        crew["health_boost"] = self.read_int(fin)
        crew["clonebay_priority"] = self.read_int(fin)
        crew["damage_boost"] = self.read_int(fin)
        crew["unknown_lambda"] = self.read_int(fin)
        crew["universal_death_count"] = self.read_int(fin)

        # masteries skip
        self.read_bool(fin)
        self.read_bool(fin)
        self.read_bool(fin)
        self.read_bool(fin)
        self.read_bool(fin)
        self.read_bool(fin)
        self.read_bool(fin)
        self.read_bool(fin)
        self.read_bool(fin)
        self.read_bool(fin)
        self.read_bool(fin)
        self.read_bool(fin)

        # unknown
        self.read_int(fin)

        self.read_animation(fin)

        # unknown
        self.read_int(fin)

        if crew["race"] == "crystal":
            crew["lockdown_recharge_ticks"] = self.read_int(fin)
            crew["lockdown_recharge_ticks_goal"] = self.read_int(fin)
            # unkown
            self.read_int(fin)

        return crew

    def read_ship(self, fin):
        ship = {}
        ship["blueprint_name"] = self.read_string(fin)
        ship["ship_name"] = self.read_string(fin)
        ship["gfx_name"] = self.read_string(fin)

        ship["starting_crew"] = []
        starting_crew = self.read_int(fin)
        for i in range(starting_crew):
            crew = {}
            crew["race"] = self.read_string(fin)
            crew["name"] = self.read_string(fin)
            ship["starting_crew"].append(crew)

        ship["hostile"] = self.read_bool(fin)
        ship["jump_charge_ticks"] = self.read_int(fin)
        ship["jumping"] = self.read_bool(fin)
        ship["jump_animation_ticks"] = self.read_int(fin)

        ship["hull"] = self.read_int(fin)
        ship["fuel"] = self.read_int(fin)
        ship["drone_parts"] = self.read_int(fin)
        ship["missiles"] = self.read_int(fin)
        ship["scrap"] = self.read_int(fin)

        crew = self.read_int(fin)
        ship["crew"] = []
        for i in range(crew):
            ship["crew"].append(self.read_crew(fin))

        return ship

    def parse_ftl(self, filename):

        fin = open(filename, "rb")

        save = {}

        save["file_format"] = self.read_int(fin)
        if save["file_format"] == 11:
            save["random_native"] = self.read_bool(fin)
        else:
            save["random_native"] = True

        if save["file_format"] == 2:
            save["advanced"] = False
        else:
            save["advanced"] = self.read_bool(fin)

        difficulty = self.read_int(fin)
        if difficulty == 0:
            save["difficulty"] = "easy"
        elif difficulty == 1:
            save["difficulty"] = "normal"
        else:
            save["difficulty"] = "hard"

        save["total_ships_defeated"] = self.read_int(fin)
        save["total_beacons_explored"] = self.read_int(fin)
        save["total_scrap_collected"] = self.read_int(fin)
        save["total_crew_hired"] = self.read_int(fin)

        save["ship_name"] = self.read_string(fin)
        save["blueprint_name"] = self.read_string(fin)

        # one based sector number
        save["sector"] = self.read_int(fin)

        # unknown value
        fin.read(4)

        statevars = self.read_int(fin)

        save["state_vars"] = {}
        for i in range(statevars):
            var_name = self.read_string(fin)
            var_value = self.read_int(fin)
            save["state_vars"][var_name] = var_value

        save["player_ship"] = self.read_ship(fin)

        return save
8