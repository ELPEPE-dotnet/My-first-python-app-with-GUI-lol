import tkinter as tk
from tkinter import PhotoImage, filedialog, Text
import os

window = tk.Tk()

oa = "" # Open apps text
sa = "" # Select apps text
ti = "" # app title text
sawt = "" # Select app title 
aft = "" # All files text 
ft= "" # exectubles text


if os.path.isfile("config.txt"):
    with open("config.txt","r") as f:
        lang = f.read(2)
        lang.split(",")
        #print("languaje selected: "+lang)
        if lang == "en":
            with open("./langs/en.lang") as l:
                oa = l.read(17)
                sa = l.read(17*2-10)
                ti = l.read(17)
                sawt = l.read(17*2-10)
                aft = l.read(17-6)
                ft = l.read()
                #print("Open applications button text is "+oa+"\n")
                #print("Search for apps button text is "+sa+"\n")
                #print("Window title is "+ti+"\n")
                #print("Select app window title is" + sawt+"\n")
                #print("Executables file text is "+ft+"\n")
                #print("All files text is " + aft+"\n")
        else:
            if lang == "es":
                with open("./langs/es.lang") as l:
                    oa = l.read(18)
                    sa = l.read(21)
                    ti = l.read(12)
                    sawt = l.read(27)
                    aft = l.read(19)
                    ft = l.read()
                    #print("Open applications button text is "+oa+"\n")
                    #print("Search for apps button text is "+sa+"\n")
                    #print("Window title is "+ti+"\n")
                    #print("Select app window title is" + sawt+"\n")
                    #print("Executables file text is "+ft+"\n")
                    #print("All files text is " + aft+"\n")
            else:
                if lang == "pr":
                    with open("./langs/pr.lang") as l:
                        oa = l.read(11)
                        sa = l.read(15)
                        ti = l.read(12)
                        sawt = l.read(29)
                        aft = l.read(18)
                        ft = l.read()
                        #print("Open applications button text is "+oa+"\n")
                        #print("Search for apps button text is "+sa+"\n")
                        #print("Window title is "+ti+"\n")
                        #print("Select app window title is" + sawt+"\n")
                        #print("Executables file text is "+ft+"\n")
                        #print("All files text is " + aft+"\n")
                else:
                    if lang == "fr":
                        with open("./langs/fr.lang") as l:
                            oa = l.read(24)
                            sa = l.read(28)
                            ti = l.read(11)
                            sawt = l.read(41)
                            aft = l.read(19)
                            ft = l.read()
                            #print("Open applications button text is "+oa+"\n")
                            #print("Search for apps button text is "+sa+"\n")
                            #print("Window title is "+ti+"\n")
                            #print("Select app window title is" + sawt+"\n")
                            #print("Executables file text is "+ft+"\n")
                            #print("All files text is " + aft+"\n")
                    else:
                        print("Select a valid languaje")
                        
window.title(ti)
apps = []

print("for changing the languaje just change the first line in config.txt file")
if os.path.isfile("apps.txt"):
    with open("apps.txt", "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
        
    filename = filedialog.askopenfilename(initialdir="/",title=sawt, filetypes=((ft+" (.exe)","*.exe"),(aft+" (.*)","*,*")))

    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="#ff0000")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)




canvas = tk.Canvas(window, height=480, width=480, bg="#468a50")
canvas.pack()

frame = tk.Frame(window, bg="white")
frame.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)

openfile = tk.Button(window, text=sa, padx=10, pady=5,fg="white", bg="#468a50", command=addApp)
openfile.pack()

runApps = tk.Button(window, text=oa, padx=10, pady=5,fg="white", bg="#468a50", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame,text=app)
    label.pack()
#print("loaded app lol")
icon = PhotoImage(file="./logo.png")
window.iconphoto(True, icon)

window.mainloop()

with open("apps.txt", "w") as f:
    for app in apps:
        f.write(app + ",")