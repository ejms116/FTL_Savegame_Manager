import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os
import shutil
from datetime import datetime
from source import savegame as sg
from source import database_connector as db_con
from configparser import ConfigParser
from source import run as r
import copy
import numpy as np
from pprint import pprint


# compile with pyinstaller.exe --onefile --windowed  ftl_savegame_manager.py


class Gui:
    def __init__(self):
        #self.db_con = db_con.DatabaseConnector("")
        config = ConfigParser()
        config.read("config.ini")
        self.target_path = config["DEFAULT"]["target_path"]
        self.target_path_mv = config["DEFAULT"]["target_path_mv"]
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

        self.filename_suffix = ".sav"
        self.savegame = sg.Savegame(self.target_path, self.target_path_mv)

        self.root = tk.Tk()
        self.root.title("FTL Savegame Manager")

        self.root.after(0, self.track_file)

        self.c_width = 400
        self.c_height = 350

        # menu left
        self.menu_left = tk.Frame(self.root, width=150, height=1800, bg="#ababab")

        # right area
        self.title_frame_overview = tk.Frame(self.root, height=1800, bg="#dfdfdf", borderwidth=1, relief="ridge")
        self.title_frame_detail = tk.Frame(self.root, height=1800, bg="#dfdfdf", borderwidth=1, relief="ridge")

        self.title_overview = tk.Label(self.title_frame_overview, text="Run Overview", bg="#dfdfdf", anchor="w")
        #self.title_overview.pack()

        self.title_detail = tk.Label(self.title_frame_detail, text="Current Run", bg="#dfdfdf", anchor="w")
        self.title_detail.pack()

        self.canvas_area_overview = tk.Canvas(self.root, width=1000, height=1800, background="#ffffff")
        #self.canvas_area_overview.grid(row=1, column=1)

        self.canvas_area_upload = tk.Canvas(self.root, width=self.c_width, height=self.c_height, background="#ffffff")
        #self.canvas_area_upload.grid(row=2, column=1)

        self.ship_class_label = tk.Label(self.canvas_area_upload, text="Ship Class")
        self.ship_class_text = tk.StringVar()
        self.ship_class_value = tk.Label(self.canvas_area_upload, textvariable=self.ship_class_text)


        self.ship_class_label.grid(row=0, column=0)
        self.ship_class_value.grid(row=0, column=1)

        self.ship_variant_label = tk.Label(self.canvas_area_upload, text="Ship Variant")
        self.ship_variant_text = tk.StringVar()
        self.ship_variant_value = tk.Label(self.canvas_area_upload, textvariable=self.ship_variant_text)

        self.ship_variant_label.grid(row=1, column=0)
        self.ship_variant_value.grid(row=1, column=1)

        self.result_label = tk.Label(self.canvas_area_upload, text="Result")
        self.result_text = tk.StringVar()
        self.result_value = tk.Label(self.canvas_area_upload, textvariable=self.result_text)

        self.result_label.grid(row=2, column=0)
        self.result_value.grid(row=2, column=1)

        self.uploaded_label = tk.Label(self.canvas_area_upload, text="Uploaded")
        self.uploaded_text = tk.StringVar()
        self.uploaded_value = tk.Label(self.canvas_area_upload, textvariable=self.uploaded_text)

        self.uploaded_label.grid(row=2, column=0)
        self.uploaded_value.grid(row=2, column=1)

        self.result_label = tk.Label(self.canvas_area_upload, text="Result")
        self.result_entry = tk.Entry(self.canvas_area_upload)

        self.result_label.grid(row=3, column=0)
        self.result_entry.grid(row=3, column=1)


        self.title_frame_upload = tk.Frame(self.root, height=1800, bg="#dfdfdf", borderwidth=1, relief="ridge")

        self.title_upload = tk.Label(self.title_frame_upload, text="Selected Run", bg="#dfdfdf", anchor="w")
        self.title_upload.pack()

        self.canvas_area_detail = tk.Canvas(self.root, width=1000, height=1800, background="#ffffff")
        self.canvas_area_detail.grid(row=1, column=2)

        self.title_frame_inventory = tk.Frame(self.root, height=1800, bg="#dfdfdf", borderwidth=1, relief="ridge")
        self.title_frame_graph = tk.Frame(self.root, height=1800, bg="#dfdfdf", borderwidth=1, relief="ridge")

        self.title_inventory = tk.Label(self.title_frame_inventory, text="Inventory", bg="#dfdfdf", anchor="w")
        self.title_inventory.pack()

        self.title_graph = tk.Label(self.title_frame_graph, text="Scrap per Sector", bg="#dfdfdf", anchor="w")
        self.title_graph.pack()

        self.canvas_area_inventory = tk.Canvas(self.root, width=self.c_width, height=self.c_height, background="#ffffff", borderwidth=1, relief="sunken")
        self.canvas_area_inventory.grid(row=1, column=3)

        self.canvas_area_graph = tk.Canvas(self.root, width=self.c_width, height=self.c_height, background="#ffffff", borderwidth=1, relief="sunken")
        self.canvas_area_graph.grid(row=2, column=2)

        # inventory
        self.frame_inventory = tk.Frame(self.canvas_area_inventory)
        self.frame_inventory.pack(fill=None, expand=False)

        self.run_inventory = ttk.Treeview(self.frame_inventory, height=29)

        self.run_inventory['columns'] = ('item', 'sector', 'origin', 'status')


        self.run_inventory.column("#0", width=0, stretch="no")
        self.run_inventory.column("item", anchor="w", width=200)
        self.run_inventory.column("sector", anchor="w", width=40)
        self.run_inventory.column("origin", anchor="w", width=80)
        self.run_inventory.column("status", anchor="w", width=80)

        self.run_inventory.heading("#0", text="", anchor="center")
        self.run_inventory.heading("item", text="Item", anchor="w")
        self.run_inventory.heading("sector", text="Sec", anchor="w")
        self.run_inventory.heading("origin", text="Origin", anchor="w")
        self.run_inventory.heading("status", text="Status", anchor="w")


        self.run_inventory.pack()



        # Savegame overview
        self.frame_overview = tk.Frame(self.canvas_area_overview)
        self.frame_overview.pack(fill=None, expand=False)

        self.run_overview = ttk.Treeview(self.frame_overview, height=10)

        self.run_overview['columns'] = ('ship_name', 'current', 'uploaded')

        self.run_overview.column("#0", width=0, stretch="no")
        self.run_overview.column("ship_name", anchor="w", width=200)
        self.run_overview.column("current", anchor="w", width=100)
        self.run_overview.column("uploaded", anchor="w", width=100)

        self.run_overview.heading("#0", text="", anchor="center")
        self.run_overview.heading("ship_name", text="Ship Name", anchor="w")
        self.run_overview.heading("current", text="Current", anchor="w")
        self.run_overview.heading("uploaded", text="Uploaded", anchor="w")

        self.run_overview.bind("<Double-1>", self.OnDoubleClick)

        self.run_overview.pack()

        # Savegame details
        self.frame_detail = tk.Frame(self.canvas_area_detail)
        self.frame_detail.pack(fill=None, expand=False)

        self.run_detail = ttk.Treeview(self.frame_detail, height=10)

        self.run_detail['columns'] = ('property', 'value')

        self.run_detail.column("#0", width=0, stretch="no")
        self.run_detail.column("property", anchor="w", width=160)
        self.run_detail.column("value", anchor="w", width=240)

        self.run_detail.heading("#0", text="", anchor="center")
        self.run_detail.heading("property", text="Property", anchor="w")
        self.run_detail.heading("value", text="Value", anchor="w")

        self.run_detail_init()

        self.run_detail.pack()

        # status bar
        self.status_frame = tk.Frame(self.root)
        self.status_text = tk.StringVar()
        self.status_text.set("Program started")
        self.status = tk.Label(self.status_frame, textvariable=self.status_text, bd=1, relief="sunken", anchor="w")
        self.status.pack(fill="both", expand=True)

        self.menu_left.grid(row=0, column=0, rowspan=4, sticky="nsew")
        #self.title_frame_overview.grid(row=0, column=1, sticky="ew")
        self.title_frame_detail.grid(row=0, column=2, sticky="ew")
        self.title_frame_inventory.grid(row=0, column=3, sticky="ew")
        #self.canvas_area_overview.grid(row=1, column=1, sticky="nsew")
        self.canvas_area_detail.grid(row=1, column=2, sticky="nsew")
        self.title_frame_graph.grid(row=2, column=2, sticky="ew")
        #self.title_frame_upload.grid(row=2, column=1, sticky="ew")
        #self.canvas_area_upload.grid(row=3, column=1, rowspan= 1, sticky="nsew")
        self.canvas_area_inventory.grid(row=1, column=3, rowspan=3, sticky="nsew")
        self.canvas_area_graph.grid(row=3, column=2, sticky="nsew")
        self.status_frame.grid(row=4, column=0, columnspan=4, sticky="ew")

        #self.root.grid_rowconfigure(1, minsize=400)

        # self.root.grid_rowconfigure(1, weight=1)
        # self.root.grid_columnconfigure(1, weight=1)

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

        load_save_button = tk.Button(self.menu_left, text="Load Save", padx=10, pady=5, fg="white",
                                     bg=self.button_color, command=self.load_save)
        self.track_run_button = tk.Button(self.menu_left, text="Toggle Tracking", padx=10, pady=5, fg="white",
                                          bg=self.button_color,
                                          command=self.toggle_tracking)
        save_run_button = tk.Button(self.menu_left, text="Save Last File", padx=10, pady=5, fg="white",
                                    bg=self.button_color,
                                    command=self.save_file)

        self.version_text = tk.StringVar()
        self.switch_version_button = tk.Button(self.menu_left, textvariable=self.version_text, padx=10, pady=5, fg="white",
                                          bg=self.button_color,
                                          command=self.change_version)



        open_saves_button = tk.Button(self.menu_left, text="Open Saves Folder", padx=10, pady=5, fg="white",
                                      bg=self.button_color,
                                      command=self.open_saves_folder)

        open_current_button = tk.Button(self.menu_left, text="Open Current Folder", padx=10, pady=5, fg="white",
                                        bg=self.button_color,
                                        command=self.open_current_folder)

        load_save_button.pack(fill="x")
        save_run_button.pack(fill="x")
        open_saves_button.pack(fill="x")
        open_current_button.pack(fill="x")

        self.track_run_button.pack(fill="x", pady=10)
        self.switch_version_button.pack(fill="x")


        end_run_button = tk.Button(self.menu_left, text="End Run", padx=10, pady=5, fg="white",
                                     bg=self.button_color, command=self.end_run)

        upload_run_button = tk.Button(self.menu_left, text="Upload Run", padx=10, pady=5, fg="white",
                                     bg=self.button_color, command=self.load_save)

        #end_run_button.pack(fill="x")
        #upload_run_button.pack(fill="x")


        test_button = tk.Button(self.menu_left, text="Test", padx=10, pady=5, fg="white", bg=self.button_color,
                                command=self.test_read)
        #test_button.pack()

        self.change_color()
        self.change_version_button()


        # initialize
        self.runs = []
        self.beacons = 999
        self.last_run = None
        self.ship_name = None
        self.selected_run_index = 999


        self.latest_filepath = ""

    def change_version(self):
        self.savegame.mv = not self.savegame.mv
        self.change_version_button()

    def change_version_button(self):
        if self.savegame.mv:
            self.switch_version_button.configure(bg="blue")
            self.version_text.set("Multiverse")
        else:
            self.switch_version_button.configure(bg="gray")
            self.version_text.set("Vanilla")

    def run_detail_init(self):
        self.run_detail.delete(*self.run_detail.get_children())
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
                               values=('Free Stuff Scrap', ''))
        self.run_detail.insert(parent='', index='end', iid=7, text='',
                               values=('Ships defeated', ''))


    def update_all(self):
        self.update_run_detail()
        self.update_run_overview()
        self.update_inventory()

    def test_read(self):

        # item = {}
        # item["item"] = "Burst Laser"
        # item["origin"] = "starting"
        # item["status"] = "sold"
        # self.savegame.run.inventory.append(item)
        if os.path.exists(self.target_path):
            try:
                self.savegame.parse()
                pprint(self.savegame.run.inventory)
                pprint(self.savegame.run.current_beacon)
            except Exception:
                print("error trying to read file")

        #self.savegame.run.sector_scrap = [120, 140, 621, 144, 150, 202, 300, 250]
        #self.savegame.run.sector_scrap_stuff = [80, 110, 521, 134, 190, 80, 230, 100]
        self.update_all()




    def OnDoubleClick(self, event):
        self.selected_run_index = self.run_overview.identify('item',event.x,event.y)

        self.ship_class_text.set(self.runs[int(self.selected_run_index)].ship_class)
        self.ship_variant_text.set(self.runs[int(self.selected_run_index)].ship_variant)
        self.uploaded_text.set(self.runs[int(self.selected_run_index)].uploaded)

        item = self.run_overview.identify('item',event.x,event.y)
        test = self.run_overview.item(item,"text")
        test2 = self.run_overview.item(item)
        print("you clicked on", self.run_overview.item(item,"text"))



    def show_help(self):
        pass

    def open_saves_folder(self):
        os.startfile(self.saves_db_path)

    def open_current_folder(self):
        os.startfile(self.saves_new_path)

    def update_inventory(self):
        self.run_inventory.delete(*self.run_inventory.get_children())
        for i in self.savegame.run.inventory:
            self.run_inventory.insert(parent='', index=0, text='', values=(i["name"], i["sector"], i["origin"], i["status"]))


    def update_scrap_graph(self):
        # TEST ANFANG
        #data = [20, 15, 10, 7, 5, 4, 3, 2, 1, 1, 0]

        self.canvas_area_graph.delete("all")

        # the variables below size the bar graph
        # experiment with them to fit your needs
        # highest y = max_data_value * y_stretch
        max_scrap_normal = np.amax(self.savegame.run.sector_scrap)
        max_scrap_stuff = np.amax(self.savegame.run.sector_scrap_stuff)
        max_scrap = max(max_scrap_normal, max_scrap_stuff)
        if max_scrap == 0:
            y_stretch = 1
        else:
            y_stretch = min(320/max_scrap, 1)
        # gap between lower canvas edge and x axis
        y_gap = 10
        # stretch enough to get all data items in
        x_stretch = 10
        x_width = 19
        # gap between left canvas edge and y axis
        x_gap = 20

        print(self.savegame.run.sector_scrap)

        for x, y in enumerate(self.savegame.run.sector_scrap):
            # calculate rectangle coordinates (integers) for each bar
            x0 = x * x_stretch + x * x_width*2 + x_gap
            y0 = self.c_height - (y * y_stretch + y_gap)
            x1 = x * x_stretch + x * x_width*2 + x_width + x_gap
            y1 = self.c_height - y_gap
            # draw the bar
            self.canvas_area_graph.create_rectangle(x0, y0, x1, y1, fill="red")
            # put the y value above each bar
            self.canvas_area_graph.create_text(x0, y0, anchor=tk.SW, text=str(y))
            msg = "S" + str(x+1)
            self.canvas_area_graph.create_text(x0, y1, anchor=tk.NW, text=msg)

        for x, y in enumerate(self.savegame.run.sector_scrap_stuff):
            # calculate rectangle coordinates (integers) for each bar
            x0 = x * x_stretch + x * x_width*2 + x_gap + x_width
            y0 = self.c_height - (y * y_stretch + y_gap)
            x1 = x * x_stretch + x * x_width*2 + x_width + x_gap + x_width
            y1 = self.c_height - y_gap
            # draw the bar
            self.canvas_area_graph.create_rectangle(x0, y0, x1, y1, fill="blue")
            # put the y value above each bar
            self.canvas_area_graph.create_text(x0+2, y0, anchor=tk.SW, text=str(y))


    def update_run_overview(self):
        # self.run_overview.delete(*self.run_overview.get_children())
        # self.run_overview.insert(parent='', index='end', iid=i, text='',
        #                          values=(self.savegame.run.ship_name, 'Yes', 'No'))
        for num, run in enumerate(self.runs, start = 0):
            if not run.inserted:
                self.run_overview.insert(parent='', index=0, iid=num, text='', values=(run.ship_name, 'No', 'No'))
                run.inserted = True


    def update_run_detail(self):
        self.run_detail.delete(*self.run_detail.get_children())

        self.run_detail.insert(parent='', index='end', iid=0, text='',
                               values=('Ship', self.savegame.run.blueprint_name))
        self.run_detail.insert(parent='', index='end', iid=1, text='',
                               values=('Ship Name', self.savegame.run.ship_name))
        self.run_detail.insert(parent='', index='end', iid=2, text='',
                               values=('Difficulty', self.savegame.run.difficulty))
        self.run_detail.insert(parent='', index='end', iid=3, text='',
                               values=('Sector', self.savegame.run.sector))
        self.run_detail.insert(parent='', index='end', iid=4, text='',
                               values=('Beacons', self.savegame.run.total_beacons_explored))
        self.run_detail.insert(parent='', index='end', iid=5, text='',
                               values=('Scrap collected', self.savegame.run.total_scrap_collected))
        self.run_detail.insert(parent='', index='end', iid=6, text='',
                               values=('Free Stuff Scrap', self.savegame.run.sector_scrap_total))
        self.run_detail.insert(parent='', index='end', iid=7, text='',
                               values=('Ships defeated', self.savegame.run.total_ships_defeated))

        self.update_scrap_graph()
        self.update_inventory()

    def end_run(self):
        if self.beacons != 999:  # don't append if it's the first run since starting the program
            self.runs.append(self.last_run)
        self.beacons = 0
        self.savegame.clear()
        self.run_detail_init()
        self.update_run_overview()

    def update_statusbar(self, msg):
        self.status_text.set(msg)

    def change_color(self):
        if self.tracking:
            self.track_run_button.configure(bg="green")
        else:
            self.track_run_button.configure(bg="red")

    def track_file(self):
        self.update_statusbar("")  # clear status bar
        if self.tracking:
            if os.path.exists(self.target_path) and not self.savegame.mv or os.path.exists(self.target_path_mv) and self.savegame.mv:
                try:
                    self.savegame.parse()
                    date_time_obj = datetime.now()
                    timestamp_str = date_time_obj.strftime("%Y-%b-%d %H-%M-%S")
                    # check if new ship is played
                    if self.savegame.run.total_beacons_explored < self.beacons or self.savegame.run.ship_name != self.ship_name:
                        foldername = "%s-%s" % (timestamp_str, self.savegame.run.ship_name)
                        self.folder_path = os.path.join(self.saves_new_path, foldername)
                        if not os.path.exists(self.folder_path):
                            os.makedirs(self.folder_path)
                            self.update_statusbar("folder created")
                        if self.beacons != 999: # don't append if it's the first run since starting the program
                            self.runs.append(self.last_run)
                        self.beacons = 0
                    self.ship_name = self.savegame.run.ship_name
                    self.last_run = copy.deepcopy(self.savegame.run)

                    if self.savegame.run.total_beacons_explored > self.beacons:
                        self.beacons = self.savegame.run.total_beacons_explored
                        filename = "%s(%s)-%s-%s" % (
                        str(self.beacons), self.savegame.run.sector, self.savegame.run.ship_name, timestamp_str)
                        new_path = os.path.join(self.folder_path, filename + self.filename_suffix)
                        self.latest_filepath = new_path
                        if self.savegame.mv:
                            shutil.copy(self.target_path_mv, new_path)
                        else:
                            shutil.copy(self.target_path, new_path)
                        self.update_statusbar(filename + " copied")
                        self.update_run_detail()
                        self.update_run_overview()
                except Exception:
                    print("file is currently in use")
            self.update_all()
            print("running...")
        self.root.after(self.update_frequency, self.track_file)

    def save_file(self):
        if not len(self.latest_filepath) == 0:
            fname = os.path.basename(self.latest_filepath)
            filename = filedialog.asksaveasfilename(initialdir=self.latest_filepath, initialfile=fname,
                                                    title="Select Save Location", defaultextension=".sav",
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
                if self.savegame.mv:
                    shutil.copy(filename, self.target_path_mv)
                else:
                    shutil.copy(filename, self.target_path)
                self.update_statusbar("file loaded")
                # self.ship_name = self.savegame.run.ship_name
                # self.last_run = copy.deepcopy(self.savegame.run)
                # self.beacons = 0
                # self.update_all()
            except Exception:
                print(filename)
                self.update_statusbar("Unable to copy latest save")
                print("Unable to copy latest save")

    def toggle_tracking(self):
        self.tracking = not self.tracking
        self.change_color()
        print(self.tracking)

    def close(self):
        self.root.destroy()


    def loop(self):
        self.root.mainloop()
