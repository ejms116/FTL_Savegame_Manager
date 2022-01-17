import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os
import shutil
from datetime import datetime
from source import savegame as sg
from configparser import ConfigParser


class Gui:
    def __init__(self):
        config = ConfigParser()
        config.read("config.ini")
        self.target_path = config["DEFAULT"]["target_path"]
        self.saves_db_path = config["DEFAULT"]["saves_db_path"]
        self.saves_new_path = config["DEFAULT"]["saves_new_path"]
        self.update_frequency = config["DEFAULT"]["update_frequency"]
        self.button_color = "#857E7D"

        if not os.path.exists(self.saves_db_path):
            os.makedirs(self.saves_db_path)
        if not os.path.exists(self.saves_new_path):
            os.makedirs(self.saves_new_path)

        if self.update_frequency is None:
            self.update_frequency = 2000

        self.tracking = False
        self.run = True

        self.filename_suffix = ".sav"
        self.savegame = sg.Savegame(self.target_path)

        self.root = tk.Tk()
        self.root.title("FTL Savegame Manager")

        self.root.after(0, self.track_file)

        # menu left
        self.menu_left = tk.Frame(self.root, width=150, bg="#ababab")

        # right area
        self.some_title_frame = tk.Frame(self.root, bg="#dfdfdf")

        self.some_title = tk.Label(self.some_title_frame, text="Run Details", bg="#dfdfdf", anchor="w")
        self.some_title.pack()

        self.canvas_area = tk.Canvas(self.root, width=500, height=400, background="#ffffff")
        self.canvas_area.grid(row=1, column=1)

        # Savegame details
        self.game_frame = tk.Frame(self.canvas_area)
        self.game_frame.pack()

        self.run_detail = ttk.Treeview(self.game_frame)

        self.run_detail['columns'] = ('property', 'value')

        self.run_detail.column("#0", width=0, stretch="no")
        self.run_detail.column("property", anchor="w", width=100)
        self.run_detail.column("value", anchor="w", width=160)

        self.run_detail.heading("#0", text="", anchor="center")
        self.run_detail.heading("property", text="Property", anchor="w")
        self.run_detail.heading("value", text="Value", anchor="w")

        self.run_detail.insert(parent='', index='end', iid=0, text='',
                       values=('Ship'))
        self.run_detail.insert(parent='', index='end', iid=1, text='',
                       values=('Ship Name', ''))
        self.run_detail.insert(parent='', index='end', iid=2, text='',
                       values=('Difficulty', ''))
        self.run_detail.insert(parent='', index='end', iid=3, text='',
                       values=('Sector', ''))
        self.run_detail.insert(parent='', index='end', iid=4, text='',
                       values=('Beacons', ''))
        self.run_detail.insert(parent='', index='end', iid=5, text='',
                       values=('Total Scrap', ''))
        self.run_detail.insert(parent='', index='end', iid=6, text='',
                       values=('Ships defeated', ''))
        self.run_detail.pack()

        # status bar
        self.status_frame = tk.Frame(self.root)
        self.status_text = tk.StringVar()
        self.status_text.set("Program started")
        self.status = tk.Label(self.status_frame, textvariable=self.status_text, bd=1, relief="sunken", anchor="w")
        self.status.pack(fill="both", expand=True)

        self.menu_left.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.some_title_frame.grid(row=0, column=1, sticky="ew")
        self.canvas_area.grid(row=1, column=1, sticky="nsew")
        self.status_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Load", command=self.load_save)
        filemenu.add_command(label="Save Last File", command=self.save_file)
        filemenu.add_command(label="Toggle Tracking", command=self.toggle_tracking)
        filemenu.add_separator()
        filemenu.add_command(label="Open Saves Folder", command=self.open_saves_folder)
        filemenu.add_command(label="Open Current Folder", command=self.open_current_folder)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.close)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.show_help)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=menubar)

        load_save_button = tk.Button(self.menu_left, text="Load Save", padx=10, pady=5, fg="white", bg=self.button_color, command=self.load_save)
        self.track_run_button = tk.Button(self.menu_left, text="Toggle Tracking", padx=10, pady=5, fg="white", bg=self.button_color,
                                     command=self.toggle_tracking)
        save_run_button = tk.Button(self.menu_left, text="Save Last File", padx=10, pady=5, fg="white", bg=self.button_color,
                                     command=self.save_file)

        test_button = tk.Button(self.menu_left, text="Test", padx=10, pady=5, fg="white", bg=self.button_color,
                                     command=self.test_read)

        open_saves_button = tk.Button(self.menu_left, text="Open Saves Folder", padx=10, pady=5, fg="white", bg=self.button_color,
                                     command=self.open_saves_folder)

        open_current_button = tk.Button(self.menu_left, text="Open Current Folder", padx=10, pady=5, fg="white", bg=self.button_color,
                                     command=self.open_current_folder)

        load_save_button.pack(fill="x")
        save_run_button.pack(fill="x")
        open_saves_button.pack(fill="x")
        open_current_button.pack(fill="x")

        self.track_run_button.pack(fill="x", pady=10)

        test_button.pack()

        self.change_color()

        self.beacons = 999 # initialize
        self.latest_filepath = ""

    def test_read(self):
        if os.path.exists(self.target_path):
            full_save = self.savegame.parse_all()
            self.update_statusbar("full_save read")


    def show_help(self):
        pass

    def open_saves_folder(self):
        os.startfile(self.saves_db_path)

    def open_current_folder(self):
        os.startfile(self.saves_new_path)

    def update_run_detail(self):
        self.run_detail.delete(*self.run_detail.get_children())
        self.run_detail.insert(parent='', index='end', iid=0, text='',
                       values=('Ship', self.savegame.blueprint_name))
        self.run_detail.insert(parent='', index='end', iid=1, text='',
                       values=('Ship Name', self.savegame.ship_name))
        self.run_detail.insert(parent='', index='end', iid=2, text='',
                       values=('Difficulty', self.savegame.difficulty))
        self.run_detail.insert(parent='', index='end', iid=3, text='',
                       values=('Sector', self.savegame.sector))
        self.run_detail.insert(parent='', index='end', iid=4, text='',
                       values=('Beacons', self.savegame.total_beacons_explored))
        self.run_detail.insert(parent='', index='end', iid=5, text='',
                       values=('Scrap collected', self.savegame.total_scrap_collected))
        self.run_detail.insert(parent='', index='end', iid=6, text='',
                       values=('Ships defeated', self.savegame.total_ships_defeated))

    def update_statusbar(self, str):
        self.status_text.set(str)

    def change_color(self):

        if self.tracking:
            self.track_run_button.configure(bg="green")
        else:
            self.track_run_button.configure(bg="red")

    def track_file(self):
        self.update_statusbar("") # clear status bar
        if self.tracking:
            if os.path.exists(self.target_path):
                try:
                    self.savegame.parse()
                    date_time_obj = datetime.now()
                    timestamp_str = date_time_obj.strftime("%Y-%b-%d %H-%M-%S")
                    if self.savegame.total_beacons_explored < self.beacons:
                        foldername = "%s-%s" % (timestamp_str, self.savegame.ship_name)
                        self.folder_path = os.path.join(self.saves_new_path, foldername)
                        if not os.path.exists(self.folder_path):
                            os.makedirs(self.folder_path)
                            self.update_statusbar("folder created")
                        self.beacons = 0
                    if self.savegame.total_beacons_explored > self.beacons:
                        self.beacons = self.savegame.total_beacons_explored
                        filename = "%s(%s)-%s-%s" % (str(self.beacons), self.savegame.sector, self.savegame.ship_name, timestamp_str)
                        new_path = os.path.join(self.folder_path, filename + self.filename_suffix)
                        self.latest_filepath = new_path
                        shutil.copy(self.target_path, new_path)
                        print(self.target_path)
                        self.update_statusbar(filename + " copied")
                        self.update_run_detail()
                        print(new_path)
                        print(self.savegame)
                except Exception:
                    print("file is currently in use")
            print("running...")
        self.root.after(self.update_frequency, self.track_file)


    def save_file(self):
        if not len(self.latest_filepath) == 0:
            fname = os.path.basename(self.latest_filepath)
            filename = filedialog.asksaveasfilename(initialdir=self.latest_filepath, initialfile=fname, title="Select Save Location", defaultextension=".sav",
                                                    filetypes=(("Save-Files", "*.sav"), ("all files", "*.*")))
            if len(filename) == 0:
                self.update_statusbar("no file selected")
                print("no file selected")
            else:
                try:
                    shutil.copy(self.latest_filepath, filename)
                    self.update_statusbar(filename + " saved successfully")
                except Exception:
                    self.update_statusbar("Unable to copy latest save")
                    print("Unable to copy latest save")
        else:
            self.update_statusbar("no file to save")
            print("no file to save")


    def load_save(self):
        filename = filedialog.askopenfilename(initialdir=self.saves_db_path, title="Select File",
                                              filetypes=(("Save-Files", "*.sav"), ("all files", "*.*")))

        if len(filename) == 0:
            self.update_statusbar("no file selected")
            print("no file selected")
        else:
            try:
                print(filename)
                self.beacons = 999
                shutil.copy(filename, self.target_path)
                self.update_statusbar("file loaded")
            except Exception:
                print(filename)
                self.update_statusbar("Unable to copy latest save")
                print("Unable to copy latest save")

    def toggle_tracking(self):
        self.tracking = not self.tracking
        self.beacons = 999
        self.change_color()
        print(self.tracking)

    def close(self):
        self.root.destroy()

    def loop(self):
        self.root.mainloop()