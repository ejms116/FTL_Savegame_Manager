import tkinter as tk
from tkinter import filedialog
import os
import shutil
from datetime import datetime

from source import parser as p

import json
from collections import namedtuple


# TODO
# - only copy file if it was changed
# - read data like sector, beacon, ship type/name from .sav-file
# - configure paths
# - standalone version


class Gui():
    def __init__(self):

        self.parser = p.Parser()

        self.target_path = "C:\\Users\\Erik\Documents\\My Games\\FasterThanLight\\continue.sav"
        self.saves_db_path = "C:\\Users\\Erik\\PycharmProjects\\FTL_Savegame_Manager\\saves"
        self.saves_new_path = "C:\\Users\\Erik\\PycharmProjects\\FTL_Savegame_Manager\\current"

        self.tracking = False
        self.run = True

        self.filename_suffix = ".sav"
        self.root = tk.Tk()
        self.root.title("FTL Savegame Manager")
        self.root.resizable(0, 0)
        self.root.geometry("200x100")

        self.root.after(0, self.track_file)

        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Load", command=self.load_save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.close)
        menubar.add_cascade(label="File", menu=filemenu)

        self.root.config(menu=menubar)

        load_save_button = tk.Button(self.root, text="Load Save", padx=10, pady=5, fg="white", bg="#263D42", command=self.load_save)
        track_run_button = tk.Button(self.root, text="Start Tracking", padx=10, pady=5, fg="white", bg="#263D42",
                                     command=self.toggle_tracking)
        self.canvas = tk.Canvas(self.root, height=25, width=25, bg="#D1C4C1")

        self.change_color()

        load_save_button.grid(row=0, column=1, pady=2, columnspan=2)
        track_run_button.grid(row=1, column=1, pady=2)
        self.canvas.grid(row=1, column=2, padx=0, pady=0)
        self.canvas.move(self.tracking_status, 0, 0)

        self.beacons = 0

    def change_color(self):
        if self.tracking:
            self.tracking_status = self.canvas.create_rectangle(0, 0, 26, 26, fill="green")
        else:
            self.tracking_status = self.canvas.create_rectangle(0, 0, 26, 26, fill="red")

    def track_file(self):
        if self.tracking:
            if os.path.exists(self.target_path):
                save = self.parser.parse_ftl(self.target_path)
                if save["total_beacons_explored"] > self.beacons:
                    self.beacons = save["total_beacons_explored"]
                    date_time_obj = datetime.now()
                    timestamp_str = date_time_obj.strftime("%d-%b-%Y (%H-%M-%S-%f)")
                    filename = str(self.beacons) + "-" + save["ship_name"] + "-" + timestamp_str
                    new_path = os.path.join(self.saves_new_path, filename + self.filename_suffix)
                    shutil.copy(self.target_path, new_path)
                    print(self.target_path)
                    print(new_path)
                    print(save)
            print("running...")
        self.root.after(2000, self.track_file)

    def load_save(self):
        filename = filedialog.askopenfilename(initialdir=self.saves_db_path, title="Select File",
                                              filetypes=(("executables", "*.sav"), ("all files", "*.*")))

        if len(filename) == 0:
            print("no file selected")
        else:
            print(filename)
            shutil.copy(filename, self.target_path)

    def toggle_tracking(self):
        self.tracking = not self.tracking
        self.change_color()
        print(self.tracking)

    def close(self):
        self.root.destroy()

    def loop(self):
        self.root.mainloop()