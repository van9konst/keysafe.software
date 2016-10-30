import threading

__author__ = 'Volodymyr'
gifdir = "/home/pi/TEST_GUI/test_GUI_ver0.1"
import Tkinter
import tkMessageBox
import ttk
import sqlite3
import thread
import zmq
import time

class Main:
    def __init__(self, master):
        self.master = master
        #
        # self.igmGK = Tkinter.PhotoImage(file=gifdir+"/getkey.gif")
        # self.igmRK = Tkinter.PhotoImage(file=gifdir+"/lackkey.gif")
        # master.geometry('720x576')
        # master.GetKeyImg = PhotoImage(file="trail_hand_big.png", height=40, width=45),
        # master.RetKeyImg = PhotoImage(file="Security Key.png",height=40, width=45),image=master.RetKeyImg,
        buttons = Tkinter.Frame(self.master)
        getKey = Tkinter.Button(buttons)
        getKey.pack(side=Tkinter.LEFT)
        getKey.bind("<ButtonRelease-1>",self.openScreenGetKey)
        returnKey = Tkinter.Button(buttons)
        returnKey.pack(side=Tkinter.RIGHT)
        returnKey.bind("<ButtonRelease-1>",self.openScreenReturnKey)
        buttons.pack(fill=Tkinter.X)
        # remove title bar
        #master.overrideredirect(1)

        # fullscreen mode
        pad = 1
        self._geom = '848x480+0+0'
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))

    def openScreenGetKey(self, event):
        root.withdraw()
        ReadRFID()
        thread.start_new_thread( self.startReading,())
        
    def openScreenReturnKey(self, event):
        #root.withdraw()
        ScreenReturnKey()
        thread.start_new_thread( self.startReadingRoomCard,())

    def startReadingRoomCard(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://127.0.0.1:5555')
        socket.send("readRoomId")
        
    def startReading(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://127.0.0.1:5555')
        socket.send("readTeacherId")

class ReadRFID:
    def __init__(self):
        self.Read = Tkinter.Toplevel(root)
        self.Read.title('Read RFID')


        self.igmPL = Tkinter.PhotoImage(file=gifdir+"/please.gif")
        Tkinter.Label(self.Read, image=self.igmPL).pack(side=Tkinter.TOP, fill=Tkinter.X, pady=5)

        progressbar = ttk.Progressbar(self.Read, orient=Tkinter.HORIZONTAL, length=200)
        progressbar.pack(pady=10, fill=Tkinter.X)
        progressbar.config(mode='indeterminate')
        progressbar.after(5000, lambda: ReadRFID._destroy(self))  # Destroy the widget after 30 seconds

        # fullscreen mode
        pad = 3
        self.Read_geom = '848x480+0+0'
        self.Read.geometry("{0}x{1}+0+0".format(self.Read.winfo_screenwidth() - pad, self.Read.winfo_screenheight() - pad))
        # fullscreen mode

    def _destroy(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://127.0.0.1:5555')
        socket.send("getTeacherId")
        msg = socket.recv()
        if(msg != "0"):
          screenGetKey = ScreenGetKey(msg)
        else:
          root.deiconify()
        self.Read.destroy()

class CustomButton(Tkinter.Button):
    data = []
    """Button widget."""

    def __init__(self, master=None, cnf={}, **kw):
        """Construct a button widget with the parent MASTER.

        STANDARD OPTIONS

            activebackground, activeforeground, anchor,
            background, bitmap, borderwidth, cursor,
            disabledforeground, font, foreground
            highlightbackground, highlightcolor,
            highlightthickness, image, justify,
            padx, pady, relief, repeatdelay,
            repeatinterval, takefocus, text,
            textvariable, underline, wraplength

        WIDGET-SPECIFIC OPTIONS

            command, compound, default, height,
            overrelief, state, width
        """
        Tkinter.Widget.__init__(self, master, 'button', cnf, kw)

    def tkButtonEnter(self, *dummy):
        self.tk.call('tkButtonEnter', self._w)

    def tkButtonLeave(self, *dummy):
        self.tk.call('tkButtonLeave', self._w)

    def tkButtonDown(self, *dummy):
        self.tk.call('tkButtonDown', self._w)

    def tkButtonUp(self, *dummy):
        self.tk.call('tkButtonUp', self._w)

    def tkButtonInvoke(self, *dummy):
        self.tk.call('tkButtonInvoke', self._w)

    def flash(self):
        """Flash the button.

        This is accomplished by redisplaying
        the button several times, alternating between active and
        normal colors. At the end of the flash the button is left
        in the same normal/active state as when the command was
        invoked. This command is ignored if the button's state is
        disabled.
        """
        self.tk.call(self._w, 'flash')

    def invoke(self):
        """Invoke the command associated with the button.

        The return value is the return value from the command,
        or an empty string if there is no command associated with
        the button. This command is ignored if the button's state
        is disabled.
        """
        return self.tk.call(self._w, 'invoke')


class ScreenGetKey:
    keyRequested = False
    def __init__(self, teacher_id):
        self.ScrGK = Tkinter.Toplevel(root)
        self.ScrGK.title('Screen Get Key')
        self.teacher_id = teacher_id
        buttons = Tkinter.Frame(self.ScrGK)
        buttons.grid(column=0, row=0)
        with sqlite3.connect('visitors.db') as conn:
            cursor = conn.cursor()

            cursor.execute(
                'SELECT r.id AS id, r.room_name AS name, (SELECT h.status FROM history h WHERE h.room_id == r.id ORDER BY h.time DESC LIMIT 1) AS status FROM rooms AS r;')
            row_count = 0
            for row_values in cursor.fetchall():
                id, name, status = row_values

                button = CustomButton(buttons, font="16", bg="red" if status == 1 else "green", fg="white", text=name, height=5, width=19)
                button.data = row_values
                button.bind("<ButtonRelease-1>", self.pressButton)
                button.grid(column=int(row_count % 4), row=int(row_count / 4))
                row_count += 1

                # Label(buttons1, font="7", text='Hello', height=5, width=20).pack(side=TOP, fill=X)
                # Label(buttons2, font="7", text='TEACHER_NAME', height=5, width=20).pack(side=TOP, fill=X)
                # Label(buttons3, font="7", text='Teacher_Photo', height=5, width=40).pack(side=TOP, fill=X)

        # fullscreen mode
        pad = 1
        self._geom = '848x480+0+0'
        self.ScrGK.geometry("{0}x{1}+0+0".format(self.ScrGK.winfo_screenwidth() - pad, self.ScrGK.winfo_screenheight() - pad))
        threading.Timer(5.0, self.destroyScreen).start()
        #   fullscreen mode
        #self.ScrGK.grab_set()
        #self.ScrGK.focus_set()

        #self.ScrGK.wait_window()

    def destroyScreen(self):
        self.ScrGK.destroy()
        root.deiconify()


    def pressButton(self, event):
        parent_name = event.widget.winfo_parent()
        parentFrame = event.widget._nametowidget(parent_name)
        parent_name = parentFrame.winfo_parent()
        parentWindow = event.widget._nametowidget(parent_name)
        askquestion = tkMessageBox.askquestion("Confirm",self._geom(), "Get key from room " + str(event.widget.data[1]) + "?" )
        if askquestion == tkMessageBox.YES:
            keyRequested = True
            ScreenProgress()
            #Pochaly vydavaty kluch







            #vydano kluch
            conn = sqlite3.connect('visitors.db')
            c = conn.cursor()
            c.execute("INSERT INTO history (room_id, teacher_id, status) VALUES (" + str(event.widget.data[0]) + ", " + str(self.teacher_id) + ", 1)")
            conn.commit()
            conn.close()
            parentWindow.destroy()
            root.deiconify()

class ScreenProgress:
    def __init__(self):
        self.ScrProgress = Tkinter.Toplevel(root)
        self.ScrProgress.title('Screen Progress')

        progressbar = ttk.Progressbar(self.ScrProgress, orient=Tkinter.HORIZONTAL, length=200)
        Tkinter.Label(self.ScrProgress, font="15", text='Wait for the key!').pack(side=Tkinter.TOP, fill=Tkinter.X, pady=50)
        progressbar.pack(pady=50, fill=Tkinter.X)
        progressbar.config(mode='indeterminate')
        progressbar.after(5000, lambda: ScreenProgress._destroy(self))  # Destroy the widget after 30 seconds

        #   fullscreen mode
        pad = 1
        self._geom = '848x480+0+0'
        self.ScrProgress.geometry("{0}x{1}+0+0".format(self.ScrProgress.winfo_screenwidth() - pad,
                                                       self.ScrProgress.winfo_screenheight() - pad))
    def _destroy(self):
        self.ScrProgress.destroy()
        self.ScrProgress.command = Main



class ScreenReturnKey:
    def __init__(self):
        self.ScrRK = Tkinter.Toplevel(root)
        self.ScrRK.title('Screen Return Key')

        Tkinter.Label(self.ScrRK, text='Put your KEY!', font=("Helvetica", 16)).pack(side=Tkinter.TOP, fill=Tkinter.X, pady=50)
        Tkinter.Label(self.ScrRK).pack(side=Tkinter.TOP, fill=Tkinter.X, pady=50)

        progressbar = ttk.Progressbar(self.ScrRK, orient=Tkinter.HORIZONTAL, length=200)
        progressbar.pack(pady=50, fill=Tkinter.X)
        progressbar.config(mode='indeterminate')
        progressbar.after(5000, lambda: ScreenReturnKey._destroy(self))  # Destroy the widget after 30 seconds

        # fullscreen mode
        pad = 3
        self.ScrRK_geom = '848x480+0+0'
        self.ScrRK.geometry("{0}x{1}+0+0".format(self.ScrRK.winfo_screenwidth() - pad, self.ScrRK.winfo_screenheight() - pad))
        # fullscreen mode

    def _destroy(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://127.0.0.1:5555')
        socket.send("getRoomUpdateStatus")
        msg = socket.recv()
        print(msg)
        self.ScrRK.destroy()



root = Tkinter.Tk()
Main(root)
root.mainloop()
