

class Parser:
    def __init__(self):
        x  = 0

    # this method returns the total amount of ints that have to be read/removed from input
    # every room has 3 ints (O2, station direction and station flag) and 2 or 4 times 3 ints depending on the tiles
    def get_room_detail(self, input):
        if input == "PLAYER_SHIP_HARD":
            return (48+17)*3
        if input == "PLAYER_SHIP_HARD_2":
            return (42+15)*3
        if input == "PLAYER_SHIP_HARD_3":
            return (46+18)*3
        if input == "PLAYER_SHIP_CIRCLE":
            return (42+16)*3
        if input == "PLAYER_SHIP_CIRCLE_2":
            return (32+14)*3
        if input == "PLAYER_SHIP_CIRCLE_3":
            return (40+17)*3
        if input == "PLAYER_SHIP_FED":
            return (46+18)*3
        if input == "PLAYER_SHIP_FED_2":
            return (44+18)*3
        if input == "PLAYER_SHIP_FED_3":
            return (46+19)*3
        if input == "PLAYER_SHIP_ENERGY":
            return (46+18)*3
        if input == "PLAYER_SHIP_ENERGY_2":
            return (40+15)*3
        if input == "PLAYER_SHIP_ENERGY_3":
            return (46+18)*3
        if input == "PLAYER_SHIP_MANTIS":
            return (54+18)*3
        if input == "PLAYER_SHIP_MANTIS_2":
            return (46+17)*3
        if input == "PLAYER_SHIP_MANTIS_3":
            return (56+18)*3
        if input == "PLAYER_SHIP_JELLY":
            return (40+15)*3
        if input == "PLAYER_SHIP_JELLY_2":
            return (54+20)*3
        if input == "PLAYER_SHIP_JELLY_3":
            return (42+16)*3
        if input == "PLAYER_SHIP_ROCK":
            return (48+18)*3
        if input == "PLAYER_SHIP_ROCK_2":
            return (44+16)*3
        if input == "PLAYER_SHIP_ROCK_3":
            return (40+17)*3
        if input == "PLAYER_SHIP_STEALTH":
            return (40+15)*3
        if input == "PLAYER_SHIP_STEALTH_2":
            return (38+15)*3
        if input == "PLAYER_SHIP_STEALTH_3":
            return (40+14)*3
        if input == "PLAYER_SHIP_ANAEROBIC":
            return (42+16)*3
        if input == "PLAYER_SHIP_ANAEROBIC_2":
            return (50+18)*3
        if input == "PLAYER_SHIP_CRYSTAL":
            return (54+19)*3
        if input == "PLAYER_SHIP_CRYSTAL_2":
            return (46+16)*3

    def get_door_count(self, input):
        if input == "PLAYER_SHIP_HARD":
            return 26
        if input == "PLAYER_SHIP_HARD_2":
            return 31
        if input == "PLAYER_SHIP_HARD_3":
            return 32
        if input == "PLAYER_SHIP_CIRCLE":
            return 22
        if input == "PLAYER_SHIP_CIRCLE_2":
            return 21
        if input == "PLAYER_SHIP_CIRCLE_3":
            return 23
        if input == "PLAYER_SHIP_FED":
            return 26
        if input == "PLAYER_SHIP_FED_2":
            return 26
        if input == "PLAYER_SHIP_FED_3":
            return 33
        if input == "PLAYER_SHIP_ENERGY":
            return 27
        if input == "PLAYER_SHIP_ENERGY_2":
            return 23
        if input == "PLAYER_SHIP_ENERGY_3":
            return 28
        if input == "PLAYER_SHIP_MANTIS":
            return 25
        if input == "PLAYER_SHIP_MANTIS_2":
            return 29
        if input == "PLAYER_SHIP_MANTIS_3":
            return 34
        if input == "PLAYER_SHIP_JELLY":
            return 20
        if input == "PLAYER_SHIP_JELLY_2":
            return 32
        if input == "PLAYER_SHIP_JELLY_3":
            return 28
        if input == "PLAYER_SHIP_ROCK":
            return 30
        if input == "PLAYER_SHIP_ROCK_2":
            return 21
        if input == "PLAYER_SHIP_ROCK_3":
            return 31
        if input == "PLAYER_SHIP_STEALTH":
            return 21
        if input == "PLAYER_SHIP_STEALTH_2":
            return 20
        if input == "PLAYER_SHIP_STEALTH_3":
            return 23
        if input == "PLAYER_SHIP_ANAEROBIC":
            return 26
        if input == "PLAYER_SHIP_ANAEROBIC_2":
            return 34
        if input == "PLAYER_SHIP_CRYSTAL":
            return 31
        if input == "PLAYER_SHIP_CRYSTAL_2":
            return 20

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

    # IMPORTANT: TODO read_ship is not correct for the flagship, because the artillery are in multiple rooms!
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

        ship["power"] = self.read_int(fin)

        # Read systems
        # 0 Shields
        # 1 Engines
        # 2 Oxygen
        # 3 Weapons
        # 4 Drone Control
        # 5 Medbay
        # 6 Piloting
        # 7 Sensors
        # 8 Doors
        # 9 Teleporter
        # 10 Cloaking
        # 11 Artillery
        # 12 Battery
        # 13 Clonebay
        # 14 Mind Control
        # 15 Hacking

        ship["systems"] = []
        for i in range(16):
            ship["systems"].append(self.read_system(fin))

        if ship["systems"][13]["capacity"] > 0:
            ship["clonebay_info"] = self.read_clonebay_info(fin)

        if ship["systems"][12]["capacity"] > 0:
            ship["battery_info"] = self.read_battery_info(fin)

        ship["shields_info"] = self.read_shields_info(fin)

        if ship["systems"][10]["capacity"] > 0:
            ship["cloaking_info"] = self.read_cloaking_info(fin)

        ship["room_detail"] = self.get_room_detail(ship["blueprint_name"])

        for i in range(ship["room_detail"]):
            self.read_int(fin)

        ship["breach_count"] = self.read_int(fin)

        ship["breaches"] = []

        for i in range(ship["breach_count"]):
            ship["breaches"].append(self.read_breach(fin))

        ship["door_count"] = self.get_door_count(ship["blueprint_name"])

        ship["doors"] = []

        for i in range(ship["door_count"]):
            ship["doors"].append(self.read_door(fin))

        ship["cloak_anim_ticks"] = self.read_int(fin)

        ship["crystal_count"] = self.read_int(fin)

        ship["crystal_lockdowns"] = []

        for i in range(ship["crystal_count"]):
            ship["crystal_lockdowns"].append(self.read_crystal(fin))

        ship["weapon_count"] = self.read_int(fin)

        ship["weapons"] = []

        for i in range(ship["weapon_count"]):
            ship["weapons"].append(self.read_string(fin))
            self.read_bool(fin) # flag for armed

        ship["drone_count"] = self.read_int(fin)

        ship["drones"] = []

        for i in range(ship["drone_count"]):
            ship["drones"].append(self.read_drone(fin))

        ship["augment_count"] = self.read_int(fin)

        ship["augments"] = []

        for i in range(ship["augment_count"]):
            ship["augments"].append(self.read_string(fin))

        return ship

    def read_drone(self, fin):
        drone = {}
        drone["name"] = self.read_string(fin)
        drone["armed"] = self.read_bool(fin)
        drone["player_controlled"] = self.read_bool(fin)
        drone["body_x"] = self.read_int(fin)
        drone["body_y"] = self.read_int(fin)
        drone["body_room_id"] = self.read_int(fin)
        drone["body_room_square"] = self.read_int(fin)
        drone["health"] = self.read_int(fin)

        return drone


    def read_crytal(self, fin):
        crystal_lockdown = {}
        crystal_lockdown["current_x_pos"] = self.read_int(fin)
        crystal_lockdown["current_y_pos"] = self.read_int(fin)
        crystal_lockdown["speed"] = self.read_int(fin)
        crystal_lockdown["goal_x_pos"] = self.read_int(fin)
        crystal_lockdown["goal_y_pos"] = self.read_int(fin)
        crystal_lockdown["arrived"] = self.read_bool(fin)
        crystal_lockdown["done"] = self.read_bool(fin)
        crystal_lockdown["lifetime"] = self.read_int(fin)
        crystal_lockdown["super_freeze"] = self.read_bool(fin)
        crystal_lockdown["locking_room"] = self.read_int(fin)
        crystal_lockdown["anim_direction"] = self.read_int(fin)
        crystal_lockdown["shard_progress"] = self.read_int(fin)

        return  crystal_lockdown



    def read_breach(self, fin):
        breach = {}
        breach["x"] = self.read_int(fin)
        breach["y"] = self.read_int(fin)
        breach["health"] = self.read_int(fin)
        return breach

    def read_door(self, fin):
        door = {}
        door["current_max_health"] = self.read_int(fin)
        door["health"] = self.read_int(fin)
        door["nominal_health"] = self.read_int(fin)

        door["open"] = self.read_bool(fin)
        door["walking_through"] = self.read_bool(fin)
        door["unknown_delta"] = self.read_int(fin)
        door["unknown_epsilon"] = self.read_int(fin)
        return door

    def read_system(self, fin):
        system = {}
        system["capacity"] = self.read_int(fin)
        if system["capacity"] > 0:
            system["power"] = self.read_int(fin)
            system["damaged_bars"] = self.read_int(fin)
            system["ionized_bars"] = self.read_int(fin)
            system["deionization_ticks"] = self.read_int(fin)
            system["repair_progress"] = self.read_int(fin)
            system["damage_progress"] = self.read_int(fin)
            system["battery_power"] = self.read_int(fin)
            system["hack_level"] = self.read_int(fin)
            system["hacked"] = self.read_bool(fin)
            system["tempcapacity_cap"] = self.read_int(fin)
            system["tempcapacity_loss"] = self.read_int(fin)
            system["tempcapacity_divisor"] = self.read_int(fin)
        return system

    def read_clonebay_info(self, fin):
        clonebay_info = {}
        clonebay_info["build_ticks"] = self.read_int(fin)
        clonebay_info["build_ticks_goal"] = self.read_int(fin)
        clonebay_info["doom_ticks"] = self.read_int(fin)
        return clonebay_info

    def read_battery_info(self, fin):
        battery_info = {}
        battery_info["active"] = self.read_bool(fin)
        battery_info["used_battery"] = self.read_int(fin)
        battery_info["discharge_ticks"] = self.read_int(fin)
        return battery_info

    def read_shields_info(self, fin):
        shields_info = {}
        shields_info["shield_layers"] = self.read_int(fin)
        shields_info["energy_shield_layers"] = self.read_int(fin)
        shields_info["energy_shield_max"] = self.read_int(fin)
        shields_info["shield_recharge_ticks"] = self.read_int(fin)

        shields_info["shield_drop_anim"] = self.read_bool(fin)
        shields_info["shield_drop_anim_ticks"] = self.read_int(fin)

        shields_info["shield_raised_anim"] = self.read_bool(fin)
        shields_info["shield_raised_anim_ticks"] = self.read_int(fin)

        shields_info["energy_shield_anim"] = self.read_bool(fin)
        shields_info["energy_shield_anim_ticks"] = self.read_int(fin)

        shields_info["unkonwn_lambda"] = self.read_int(fin)
        shields_info["unkonwn_mu"] = self.read_int(fin)

        return shields_info

    def read_cloaking_info(self, fin):
        cloaking_info = {}
        cloaking_info["unkonwn_alpha"] = self.read_int(fin)
        cloaking_info["unkonwn_beta"] = self.read_int(fin)
        cloaking_info["cloak_ticks_goal"] = self.read_int(fin)
        cloaking_info["cloak_ticks"] = self.read_int(fin)
        return cloaking_info



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

        cargo_count = self.read_int(fin)
        save["cargo"] = []
        for i in range(cargo_count):
            save["cargo"].append(self.read_string(fin))

        save["sector_tree_seed"] = self.read_int(fin)
        save["sector_layout_seed"] = self.read_int(fin)
        save["rebel_fleet_offset"] = self.read_int(fin)
        save["rebel_fleet_fudge"] = self.read_int(fin)
        save["rebel_pursuit_mod"] = self.read_int(fin)

        save["current_beacon_id"] = self.read_int(fin)
        save["waiting"] = self.read_bool(fin)
        save["wait_event_seed"] = self.read_int(fin)
        save["unknown_epsilon"] = self.read_string(fin)
        save["sector_hazard_visible"] = self.read_bool(fin)
        save["rebel_flagship_visible"] = self.read_bool(fin)
        save["rebel_flagship_hop"] = self.read_int(fin)
        save["rebel_flagship_moving"] = self.read_bool(fin)
        save["rebel_flagship_retreating"] = self.read_bool(fin)
        save["rebel_flagship_base_turns"] = self.read_int(fin)

        save["sector_visitation_count"] = self.read_int(fin)

        save["route"] = []

        for i in range(save["sector_visitation_count"]):
            save["route"].append(self.read_bool(fin))

        save["sector_number"] = self.read_int(fin)
        save["hidden_crystal_world"] = self.read_bool(fin)
        save["beacon_count"] = self.read_int(fin)
        save["beacons"] = []

        for i in range(save["beacon_count"]):
            save["beacons"].append(self.read_beacon(fin))

        save["quest_event_count"] = self.read_int(fin)
        save["quest_events"] = []

        for i in range(save["quest_event_count"]):
            save["quest_events"].append(self.read_quest_event(fin))

        save["distant_quest_event_count"] = self.read_int(fin)
        save["distant_quest_events"] = []

        for i in range(save["distant_quest_event_count"]):
            save["distant_quest_events"].append(self.read_string(fin))

        save["unknown_mu"] = self.read_int(fin)

        # TODO read ship continue in Line 229

        return save

    def read_quest_event(self, fin):
        quest_event = {}
        quest_event["quest_event_id"] = self.read_string(fin)
        quest_event["quest_beacon_id"] = self.read_int(fin)
        return quest_event

    def read_beacon(self, fin):
        beacon = {}
        beacon["visit_count"] = self.read_int(fin)
        if beacon["visit_count"] > 0:
            beacon["bg_starscape_image_inner_path"] = self.read_string(fin)
            beacon["bg_sprite_image_inner_path"] = self.read_string(fin)
            beacon["bg_sprite_pos_x"] = self.read_int(fin)
            beacon["bg_sprite_pos_y"] = self.read_int(fin)
            beacon["bg_sprite_rotation"] = self.read_int(fin)

        beacon["seen"] = self.read_bool(fin)
        beacon["enemy_present"] = self.read_bool(fin)
        if beacon["enemy_present"]:
            beacon["ship_event_id"] = self.read_string(fin)
            beacon["auto_blueprint_id"] = self.read_string(fin)
            beacon["ship_event_seed"] = self.read_int(fin)

        beacon["fleet_presence"] = self.read_int(fin)
        beacon["under_attack"] = self.read_bool(fin)

        beacon["store_present"] = self.read_bool(fin)

        if beacon["store_present"]:
            beacon["store"] = self.read_store(fin)

        return beacon

    def read_store(self, fin):
        store = {}
        shelf_count = self.read_int(fin)

        store["shelves"] = []

        for i in range(shelf_count):
            store["shelves"].append(self.read_shelf(fin))

        store["fuel"] = self.read_int(fin)
        store["missiles"] = self.read_int(fin)
        store["drone_parts"] = self.read_int(fin)
        return store

    def read_shelf(self, fin):
        shelf = {}
        item_type = self.read_int(fin)
        if item_type == 0:
            shelf["item_type"] = "WEAPON"
        elif item_type == 1:
            shelf["item_type"] = "DRONE"
        elif item_type == 2:
            shelf["item_type"] = "AUGMENT"
        elif item_type == 3:
            shelf["item_type"] = "CREW"
        elif item_type == 4:
            shelf["item_type"] = "SYSTEM"

        shelf["items"] = []

        for i in range(3):
            available = self.read_int(fin)
            if available == 1 or available == 0:
                shelf["items"].append(self.read_item(fin, available))

        return shelf

    def read_item(self, fin, available):
        item = {}
        item["name"] = self.read_string(fin)
        if available > 0:
            item["available"] = True
        else:
            item["available"] = False

        item["extra_data"] = self.read_int(fin)
        return item

    def parse_mv(self, filename):

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

        return save
8