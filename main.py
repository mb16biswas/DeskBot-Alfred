from Utils.helpers.process import *
from Utils.helpers.operations import *
from tkinter import *
from ui_config import *
 
# GUI
root = Tk()
root.title("DESKBOT-ALFRED")
 

 
# Send function
def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send , 'user' )
 
    user = e.get().lower()

    encoding_ = process_text_bert(user)

    p = pred_bert(encoding_,)

 
    if (p == "Quary"):

        res =  Quary_F(user)

        txt.insert(END, res)
 
    elif (p == "Email"):

        res = "\nAlfred -> " + Email_F()

        txt.insert(END, res)
 
    elif (p == "Youtube"):

        res = "\nAlfred -> " + Youtube_F(user)

        txt.insert(END, res)
 
    elif (p == "Task"):

        res = "\nAlfred -> " + Task_F()
        
        txt.insert(END, res)
 
    else:

        res = "\nAlfred -> " + Random_F(user)

        txt.insert(END, res)
 
    e.delete(0, END)
 
 
lable1 = Label(root, bg=TOP_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)
 
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)
txt.tag_config('user', foreground= OUTPUT_COLOR)



 
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
 
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)
 
send = Button(root, text="Send", font=FONT_BOLD, bg=BG_BUTTON,
              command=send).grid(row=2, column=1)
 
root.mainloop()