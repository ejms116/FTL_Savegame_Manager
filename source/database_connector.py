import pymongo
from pymongo import MongoClient
import pandas as pd
import json
import datetime
import ssl


class DatabaseConnector:
    def __init__(self, uri):
        db_name = "stats"
        collection_name = "runs"
        uri = uri
        self.client = pymongo.MongoClient(uri, tls=True, tlsAllowInvalidCertificates=True)
        self.DB = self.client[db_name]
        self.collection = self.DB[collection_name]
        #db = self.client.test


    def upload_raw(self, raw_xml):
        data = [
            {
                'ship_name':"Test",
                'raw': raw_xml
            }
        ]
        self.collection.insert_many(data)

    def upload_test(self):
        save = {
            "fetched": False,
            "timestamp": "2022-Dec-29 21-13-01",
            "category": "Normal",
            "ship_class": "Rock",
            "ship_variant": "C",
            "result": "Win",
            "misplay_count": "1",
            "sector": "",
            "time": "0:44:12",
            "difficulty_early": 4,
            "difficulty_mid": 3,
            "difficulty_end": 2,
            "difficulty_fs": 2,
            "flagship_start_hull": 30,
            "flagship_damage": 4,
            "flagship_repair_available": False,
            "ships_defeated": 41,
            "beacons_explored": 94,
            "scrap_collected": 1682,
            "score": 5163,
            "reactor": 24,
            "weapons": [102, 101],
            "drones": [201, 203],
            "crew": [0, 2, 1, 1, 2, 0, 0, 0],
            "systems": [8, 7, 2, 0, 2, 2, 3, 3, 0, 7, 0, 0],
            "subsystems": [2, 0, 2, 2],
            "augments": [103],
            "notes": "MongoDB Test upload 3"
        }
        self.collection.insert_one(save)

    def test(self):
        data = [
            {
                'name':"Suhas",
                'Date': datetime.datetime.now()
            },
            {
                'name': "Rocky",
                'Date': datetime.datetime.now()
            }
        ]
        self.collection.insert_many(data)
