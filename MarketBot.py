
""" Your Steam Web API Key
Key: 270541FF47E90A83A1DC2E337E3BD222
Domain Name: music.tim-schweizer.de """

from Tkinter import *    #vers. 3.4
import steamapi

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

    # quits the program
def quit():
    root.quit()

    # creating the window
root = Tk()

    # modify the window
root.title("Steam Market Bot inc")
root.geometry("1600x900")

    # create a toplevel menu
menubar = Menu(root)

    # File Menu options in menubar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
# End of File Menu

settingsmenu = Menu(menubar, tearoff=0)

settingsmenu.add_separator()

settingsmenu.add_command(label="Options", command=donothing)
settingsmenu.add_command(label="Account", command=donothing)
settingsmenu.add_command(label="Bot-Settings", command=donothing)
settingsmenu.add_command(label="Themes", command=donothing)

menubar.add_cascade(label="Settings", menu=settingsmenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)
# EVTL NOCH DATENBANK 




# display the menubar
root.config(menu=menubar)




app = Frame(root)
app.grid()
label = Label(app, text= "Exit Button in the file menu crashes the program")
label.grid()


root.mainloop()
