from tkinter import *
import tkintermapview
import customtkinter
import BreadthFirstSearch
import DepthFirstSearch
import A_Star_Algorithm
import Uniform_Cost_Algorithm
import coordinates
from threading import Thread
from time import sleep


class App(Tk):
    # --------------------------------  [Intro]  --------------------
    def __init__(self):
        Tk.__init__(self)
        self.geometry("590x232+470+300")
        self.resizable(False, False)
        self.overrideredirect(True)
        self.canvas = Canvas(self, width=590, height=232,
                             bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.img = PhotoImage(file='intro.png')
        self.canvas.create_image(0, 0, image=self.img, anchor=NW)
        Th1 = Thread(target=self.ProgressLine)
        Th1.start()
# --------------------------- Intro Line ------------------

    def ProgressLine(self):
        for i in range(590):
            self.canvas.create_rectangle(
                i, 230, i, 230, width=3, outline="#ff274b")
            sleep(0.005)
        self.withdraw()
        self.MainRoot()

# ----------------------------- Main Window -------------------

    def MainRoot(self):
        self.root = Toplevel()
        self.root.geometry('770x560+420+150')
        self.root.resizable(False, False)
        self.root.config(background='silver')
        self.root.title('Search Algorithm')
        self.root.iconbitmap('Logoi.ico')

# ------------------------------- map_widget -----------------

        MapFrame = customtkinter.CTkFrame(
            master=self.root, width=510, height=500, fg_color='white')
        MapFrame.place(x=230, y=30)

        map_widget = tkintermapview.TkinterMapView(
            MapFrame, width=440, height=440, corner_radius=0)
        map_widget.place(x=30, y=30)

        map_widget.set_position(30.5604755, 30.9293876, marker=False)
        map_widget.set_tile_server(
            "https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=30)
        map_widget.set_zoom(9)

        # ----------------------- creating marks on map ---------------
        nodes_list = []
        mark_list = []

        def create_marks(path, x):
            # map_widget.delete_all_marker()
            # map_widget.delete_all_path()
            for node in path:
                if x == 2:  # node=(name ,cost), name=node[0]  cost=node[1]

                    # nodes_list.append(coordinates.coordinates[node[0]])# c.name=(121546.23 , 5454646)
                    MarkedNode = map_widget.set_marker(
                        coordinates.coordinates[node[0]][0], coordinates.coordinates[node[0]][1], text=node)
                else:  # node=(name) name=node
                    # nodes_list.append(coordinates.coordinates[node]) #c.name=(112153212,6665656)
                    MarkedNode = map_widget.set_marker(  # (121546.23 , 5454646)
                        coordinates.coordinates[node][0], coordinates.coordinates[node][1], text=node)
                mark_list.append(MarkedNode)
        # -----------------------  drawing the path ---------------------
            for x in range(len(path)-1):
                p = map_widget.set_path(
                    [mark_list[x].position, mark_list[x+1].position])

# ---------------------------------- Control Frame -------------------

        ControlFrame = customtkinter.CTkFrame(
            self.root, width=170, height=500, fg_color='white')
        ControlFrame.place(x=30, y=30)

        TAlgorithms = Label(ControlFrame, text="ALGORITHM", font=(
            'Berlin Sans FB Demi Bold', 18, 'bold'), fg='#ff274b', bg='white')
        TAlgorithms.place(x=15, y=350)
        TSearch = Label(ControlFrame, text="Search", font=(
            'cocacola', 15), fg='black', bg='white')
        TSearch.place(x=15, y=330)

# -------------------------------- Search Function -------------------

        def search():

            start = SelectStart.get()
            goal = SelectGoal.get()
            Algorithm = SelectAlgorithm.get()
            Result_path = []
            if Algorithm == 'Breadth First Search':
                Result_path = BreadthFirstSearch.BFS(start, goal)
                x = 1
            elif Algorithm == 'Depth First Search':
                Result_path = DepthFirstSearch.DFS(start, goal)
                x = 1
            elif Algorithm == 'A_Star_Algorithm':
                Result_path = A_Star_Algorithm.a_star(start, goal)
                x = 2
            elif Algorithm == 'Uniform_Cost_Algorithm':
                Result_path = Uniform_Cost_Algorithm.UCS(start, goal)
                x = 1
# -------------------------------- Print The Path ---------------------
            OutLabel = Label(MapFrame, text=f"The Path is : {Result_path}", font=(
                'monospace', 10), fg='black', bg='white')
            OutLabel.place(x=30, y=470)
            create_marks(Result_path, x)

# -------------------------------- Option Menu -----------------------

        SelectStart = customtkinter.CTkOptionMenu(ControlFrame, values=['From', 'shebin', 'minuf', 'tala', 'birket as sab', 'el-bagour', 'ashmun', 'quwaysna', 'el sadat city', 'el shohada', 'Kafr El-Zayat', 'basioun',
                                                                        'tanta', 'qutur', 'El-Mahalla El-Kubra', 'As Santah', 'Samannoud', 'zefta', 'banha', 'qalyub', 'Al Qanatir Al Khayriyyah', 'Shubra Al Khaymah', 'el khankah', 'kafr shokr', 'shibin el qanatir', 'toukh'],
                                                  width=140, height=40, fg_color='silver', button_color='#ff274b', button_hover_color='#4E7779', text_color='black', text_color_disabled='#F4F4E9', dropdown_fg_color='#17202A', dynamic_resizing=False)
        SelectStart.place(x=15, y=30)

        SelectGoal = customtkinter.CTkOptionMenu(ControlFrame, values=['To', 'shebin', 'minuf', 'tala', 'birket as sab', 'el-bagour', 'ashmun', 'quwaysna', 'el sadat city', 'el shohada', 'Kafr El-Zayat', 'basioun',
                                                                       'tanta', 'qutur', 'El-Mahalla El-Kubra', 'As Santah', 'Samannoud', 'zefta', 'banha', 'qalyub', 'Al Qanatir Al Khayriyyah', 'Shubra Al Khaymah', 'el khankah', 'kafr shokr', 'shibin el qanatir', 'toukh'],

                                                 width=140, height=40, fg_color='silver', button_color='#ff274b', button_hover_color='#4E7779', text_color='black', text_color_disabled='#F4F4E9', dropdown_fg_color='#17202A', dynamic_resizing=False)
        SelectGoal.place(x=15, y=90)
        SelectAlgorithm = customtkinter.CTkOptionMenu(ControlFrame, values=['Algorithm', 'Breadth First Search', 'Depth First Search', 'A_Star_Algorithm', 'Uniform_Cost_Algorithm'],
                                                      #command=change_map ,
                                                      width=140, height=40, fg_color='silver', button_color='#ff274b', button_hover_color='#4E7779', text_color='black', text_color_disabled='#F4F4E9', dropdown_fg_color='#17202A', dynamic_resizing=False)
        SelectAlgorithm.place(x=15, y=150)
# -------------------------------------- Buttons ---------------------------
        SearchButton = customtkinter.CTkButton(
            master=ControlFrame, text='Search', width=140, height=40, fg_color='#ff274b', hover_color='black',  text_color='white', command=search)
        SearchButton.place(x=15, y=210)


window = App()
window.mainloop()
