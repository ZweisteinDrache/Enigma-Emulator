import customtkinter as ctk
from tkinter import filedialog







window = ctk.CTk()


filedir = None 


entry1_tvar= ctk.StringVar()
jumperentry2_tvar= ctk.StringVar()
jumperentry3_tvar= ctk.StringVar()
jumperentry4_tvar= ctk.StringVar()
jumperentry5_tvar= ctk.StringVar()
jumperentry6_tvar= ctk.StringVar()
dc1entry_tvar= ctk.StringVar()
dc2entry_tvar= ctk.StringVar()
dc3entry_tvar= ctk.StringVar()
dc4entry_tvar= ctk.StringVar()
dc5entry_tvar= ctk.StringVar()
dc6entry_tvar= ctk.StringVar()
plugboard_sw1_tvar= ctk.StringVar()
plugboard_ew1_tvar= ctk.StringVar()
plugboard_sw2_tvar= ctk.StringVar()
plugboard_ew2_tvar= ctk.StringVar()
plugboard_sw3_tvar= ctk.StringVar()
plugboard_ew3_tvar= ctk.StringVar()
plugboard_sw4_tvar= ctk.StringVar()
plugboard_ew4_tvar= ctk.StringVar()
plugboard_sw5_tvar= ctk.StringVar()
plugboard_ew5_tvar= ctk.StringVar()
plugboard_sw6_tvar= ctk.StringVar()
plugboard_ew6_tvar= ctk.StringVar()
plugboard_sw7_tvar= ctk.StringVar()
plugboard_ew7_tvar= ctk.StringVar()
plugboard_sw8_tvar= ctk.StringVar()
plugboard_ew8_tvar= ctk.StringVar()
plugboard_sw9_tvar= ctk.StringVar()
plugboard_ew9_tvar= ctk.StringVar()
plugboard_sw10_tvar= ctk.StringVar()
plugboard_ew10_tvar= ctk.StringVar()
discchoosentry_tvar= ctk.StringVar()
discstartingentry_tvar= ctk.StringVar()

entry1_tvar.set("Discorder")
jumperentry2_tvar.set("Jumper2")
jumperentry3_tvar.set("Jumper3")
jumperentry4_tvar.set("Jumper4")
jumperentry5_tvar.set("Jumper5")
jumperentry6_tvar.set("Jumper6")
dc1entry_tvar.set("discstartingpoint1")
dc2entry_tvar.set("discstartingpoint2")
dc3entry_tvar.set("discstartingpoint3")
dc4entry_tvar.set("discstartingpoint4")
dc5entry_tvar.set("discstartingpoint5")
dc6entry_tvar.set("discstartingpoint6")
plugboard_sw1_tvar.set("sw1")
plugboard_ew1_tvar.set("ew1")
plugboard_sw2_tvar.set("sw2")
plugboard_ew2_tvar.set("ew2")
plugboard_sw3_tvar.set("sw3")
plugboard_ew3_tvar.set("ew3")
plugboard_sw4_tvar.set("sw4")
plugboard_ew4_tvar.set("ew4")
plugboard_sw5_tvar.set("sw5")
plugboard_ew5_tvar.set("ew5")
plugboard_sw6_tvar.set("sw6")
plugboard_ew6_tvar.set("ew6")
plugboard_sw7_tvar.set("sw7")
plugboard_ew7_tvar.set("ew7")
plugboard_sw8_tvar.set("sw8")
plugboard_ew8_tvar.set("ew8")
plugboard_sw9_tvar.set("sw9")
plugboard_ew9_tvar.set("ew9")
plugboard_sw10_tvar.set("sw10")
plugboard_ew10_tvar.set("ew10")
discchoosentry_tvar.set("Choos Disc")
discstartingentry_tvar.set("Disc startingpoint")

def load_file():
    creatbutton.destroy()
    creatframe = ctk.CTkFrame(window)
    creatframe.grid(row=12, pady=10, padx=10, sticky = "ew")
    creatframe.columnconfigure((0,1), weight=1)
    updatebutton = ctk.CTkButton(creatframe, text="Update File", command= update_file)
    updatebutton.grid(row=0,column=0, sticky="ew",padx=5)
    save_as_new_button = ctk.CTkButton(creatframe, text="Save as new", command=creatfile)
    save_as_new_button.grid(row=0, column=1, sticky= "ew",padx=5)
    global filedir
    filedir = filedialog.askopenfilename(filetypes=[("text file","*.txt")])
    print (filedir)
    enc_txt.configure(text=filedir)
    fileobj=open(filedir,"r")
    list_of_lines = fileobj.readlines()
    print(list_of_lines)
    entry1_tvar.set(list_of_lines[0].replace("\n",""))
    jumperentry2_tvar.set(list_of_lines[1].replace("\n",""))
    jumperentry3_tvar.set(list_of_lines[2].replace("\n",""))
    jumperentry4_tvar.set(list_of_lines[3].replace("\n",""))
    jumperentry5_tvar.set(list_of_lines[4].replace("\n",""))
    jumperentry6_tvar.set(list_of_lines[5].replace("\n",""))
    dc1entry_tvar.set(list_of_lines[6].replace("\n",""))
    dc2entry_tvar.set(list_of_lines[7].replace("\n",""))
    dc3entry_tvar.set(list_of_lines[8].replace("\n",""))
    dc4entry_tvar.set(list_of_lines[9].replace("\n",""))
    dc5entry_tvar.set(list_of_lines[10].replace("\n",""))
    dc6entry_tvar.set(list_of_lines[11].replace("\n",""))
    plugboard_sw1_tvar.set(list_of_lines[12].replace("\n",""))
    plugboard_sw2_tvar.set(list_of_lines[13].replace("\n",""))
    plugboard_sw3_tvar.set(list_of_lines[14].replace("\n",""))
    plugboard_sw4_tvar.set(list_of_lines[15].replace("\n",""))
    plugboard_sw5_tvar.set(list_of_lines[16].replace("\n",""))
    plugboard_sw6_tvar.set(list_of_lines[17].replace("\n",""))
    plugboard_sw7_tvar.set(list_of_lines[18].replace("\n",""))
    plugboard_sw8_tvar.set(list_of_lines[19].replace("\n",""))
    plugboard_sw9_tvar.set(list_of_lines[20].replace("\n",""))
    plugboard_sw10_tvar.set(list_of_lines[21].replace("\n",""))
    plugboard_ew1_tvar.set(list_of_lines[22].replace("\n",""))
    plugboard_ew2_tvar.set(list_of_lines[23].replace("\n",""))
    plugboard_ew3_tvar.set(list_of_lines[24].replace("\n",""))
    plugboard_ew4_tvar.set(list_of_lines[25].replace("\n",""))
    plugboard_ew5_tvar.set(list_of_lines[26].replace("\n",""))
    plugboard_ew6_tvar.set(list_of_lines[27].replace("\n",""))
    plugboard_ew7_tvar.set(list_of_lines[28].replace("\n",""))
    plugboard_ew8_tvar.set(list_of_lines[29].replace("\n",""))
    plugboard_ew9_tvar.set(list_of_lines[30].replace("\n",""))
    plugboard_ew10_tvar.set(list_of_lines[31].replace("\n",""))
    discchoosentry_tvar.set(list_of_lines[32].replace("\n",""))
    discstartingentry_tvar.set(list_of_lines[33].replace("\n",""))

    
    eingabeprüfer()
def update_file():
    error_label.destroy()
    tester = True
    
    tester = eingabeprüfer()
    if tester == True:
        file_main = open(filedir,"w+")

        file_main.write(entry1_tvar.get()+"\n")
        file_main.write(jumperentry2_tvar.get()+"\n")
        file_main.write(jumperentry3_tvar.get()+"\n")
        file_main.write(jumperentry4_tvar.get()+"\n")
        file_main.write(jumperentry5_tvar.get()+"\n")
        file_main.write(jumperentry6_tvar.get()+"\n")
        file_main.write(dc1entry_tvar.get()+"\n")
        file_main.write(dc2entry_tvar.get()+"\n")
        file_main.write(dc3entry_tvar.get()+"\n")
        file_main.write(dc4entry_tvar.get()+"\n")
        file_main.write(dc5entry_tvar.get()+"\n")
        file_main.write(dc6entry_tvar.get()+"\n")
        file_main.write(plugboard_sw1_tvar.get()+"\n")
        file_main.write(plugboard_sw2_tvar.get()+"\n")
        file_main.write(plugboard_sw3_tvar.get()+"\n")
        file_main.write(plugboard_sw4_tvar.get()+"\n")
        file_main.write(plugboard_sw5_tvar.get()+"\n")
        file_main.write(plugboard_sw6_tvar.get()+"\n")
        file_main.write(plugboard_sw7_tvar.get()+"\n")
        file_main.write(plugboard_sw8_tvar.get()+"\n")
        file_main.write(plugboard_sw9_tvar.get()+"\n")
        file_main.write(plugboard_sw10_tvar.get()+"\n")
        file_main.write(plugboard_ew1_tvar.get()+"\n")
        file_main.write(plugboard_ew2_tvar.get()+"\n")
        file_main.write(plugboard_ew3_tvar.get()+"\n")
        file_main.write(plugboard_ew4_tvar.get()+"\n")
        file_main.write(plugboard_ew5_tvar.get()+"\n")
        file_main.write(plugboard_ew6_tvar.get()+"\n")
        file_main.write(plugboard_ew7_tvar.get()+"\n")
        file_main.write(plugboard_ew8_tvar.get()+"\n")
        file_main.write(plugboard_ew9_tvar.get()+"\n")
        file_main.write(plugboard_ew10_tvar.get()+"\n")
        file_main.write(discchoosentry_tvar.get()+"\n")
        file_main.write(discstartingentry_tvar.get()+"\n")
        

        file_main.close()          
def creatfile():
    
    error_label.destroy()
    tester = True
    
    tester = eingabeprüfer()
    if tester == True:
        file_init = filedialog.asksaveasfilename(filetypes=[("text file","*.txt")],defaultextension=(".txt"))
        enc_txt.configure(text=file_init)

        file_main = open(file_init,"w+")

        file_main.write(entry1_tvar.get()+"\n")
        file_main.write(jumperentry2_tvar.get()+"\n")
        file_main.write(jumperentry3_tvar.get()+"\n")
        file_main.write(jumperentry4_tvar.get()+"\n")
        file_main.write(jumperentry5_tvar.get()+"\n")
        file_main.write(jumperentry6_tvar.get()+"\n")
        file_main.write(dc1entry_tvar.get()+"\n")
        file_main.write(dc2entry_tvar.get()+"\n")
        file_main.write(dc3entry_tvar.get()+"\n")
        file_main.write(dc4entry_tvar.get()+"\n")
        file_main.write(dc5entry_tvar.get()+"\n")
        file_main.write(dc6entry_tvar.get()+"\n")
        file_main.write(plugboard_sw1_tvar.get()+"\n")
        file_main.write(plugboard_sw2_tvar.get()+"\n")
        file_main.write(plugboard_sw3_tvar.get()+"\n")
        file_main.write(plugboard_sw4_tvar.get()+"\n")
        file_main.write(plugboard_sw5_tvar.get()+"\n")
        file_main.write(plugboard_sw6_tvar.get()+"\n")
        file_main.write(plugboard_sw7_tvar.get()+"\n")
        file_main.write(plugboard_sw8_tvar.get()+"\n")
        file_main.write(plugboard_sw9_tvar.get()+"\n")
        file_main.write(plugboard_sw10_tvar.get()+"\n")
        file_main.write(plugboard_ew1_tvar.get()+"\n")
        file_main.write(plugboard_ew2_tvar.get()+"\n")
        file_main.write(plugboard_ew3_tvar.get()+"\n")
        file_main.write(plugboard_ew4_tvar.get()+"\n")
        file_main.write(plugboard_ew5_tvar.get()+"\n")
        file_main.write(plugboard_ew6_tvar.get()+"\n")
        file_main.write(plugboard_ew7_tvar.get()+"\n")
        file_main.write(plugboard_ew8_tvar.get()+"\n")
        file_main.write(plugboard_ew9_tvar.get()+"\n")
        file_main.write(plugboard_ew10_tvar.get()+"\n")
        file_main.write(discchoosentry_tvar.get()+"\n")
        file_main.write(discstartingentry_tvar.get()+"\n")
        

        file_main.close()
def eingabeprüfer():
    global error_label
    all_ok = True
    try:   
        discorder = int(entry1_tvar.get())
        jumper2 = int(jumperentry2_tvar.get())
        jumper3 = int(jumperentry3_tvar.get())
        jumper4 = int(jumperentry4_tvar.get())
        jumper5 = int(jumperentry5_tvar.get())
        jumper6 = int(jumperentry6_tvar.get())

        sw1 = int(plugboard_sw1_tvar.get())
        sw2 = int(plugboard_sw2_tvar.get())   
        sw3 = int(plugboard_sw3_tvar.get())
        sw4 = int(plugboard_sw4_tvar.get())
        sw5 = int(plugboard_sw5_tvar.get())
        sw6 = int(plugboard_sw6_tvar.get())
        sw7 = int(plugboard_sw7_tvar.get())
        sw8 = int(plugboard_sw8_tvar.get())
        sw9 = int(plugboard_sw9_tvar.get())
        sw10 = int(plugboard_sw10_tvar.get())
        ew1 = int(plugboard_ew1_tvar.get())
        ew2 = int(plugboard_ew2_tvar.get())
        ew3 = int(plugboard_ew3_tvar.get())
        ew4 = int(plugboard_ew4_tvar.get())
        ew5 = int(plugboard_ew5_tvar.get())
        ew6 = int(plugboard_ew6_tvar.get())
        ew7 = int(plugboard_ew7_tvar.get())
        ew8 = int(plugboard_ew8_tvar.get())
        ew9 = int(plugboard_ew9_tvar.get())
        ew10 = int(plugboard_ew10_tvar.get())
        rd = int(discchoosentry_tvar.get())
        dc1 = int(dc1entry_tvar.get())     
        dc2 = int(dc2entry_tvar.get())
        dc3 = int(dc3entry_tvar.get())
        dc4 = int(dc4entry_tvar.get())
        dc5 = int(dc5entry_tvar.get())
        dc6 = int(dc6entry_tvar.get())
    except:
        all_ok = False
        error_label = ctk.CTkLabel(window, text=("all entrys have to be an int"))
        error_label.grid(row=13, pady =10, padx =10)
        return all_ok
        

    







































    







    for e in[jumper2,jumper3,jumper4,jumper5,jumper6]:
        if e <1:
            all_ok = False
            error_label = ctk.CTkLabel(window, text="no jumper should be under 1")
            error_label.grid(row=13, pady =10, padx =10)
            return all_ok

    if jumper2 > 79_228_162_514_264_337_593_543_950_335:
        all_ok = False
        error_label = ctk.CTkLabel(window, text="jumper2 is to big")
        error_label.grid(row=13, pady =10, padx =10)
        return all_ok
    if jumper3 > 79_228_162_514_264_337_593_543_950_335:
        all_ok = False
        error_label = ctk.CTkLabel(window, text="jumper3 is to big")
        error_label.grid(row=13, pady =10, padx =10)
        return all_ok
    if jumper4 > 79_228_162_514_264_337_593_543_950_335:
        all_ok = False
        error_label = ctk.CTkLabel(window, text="jumper4 is to big")
        error_label.grid(row=13, pady =10, padx =10)
        return all_ok
    if jumper5 > 79_228_162_514_264_337_593_543_950_335:
        all_ok = False
        error_label = ctk.CTkLabel(window, text="jumper5 is to big")
        error_label.grid(row=13, pady =10, padx =10)
        return all_ok
    if jumper6 > 79_228_162_514_264_337_593_543_950_335:
        all_ok = False
        error_label = ctk.CTkLabel(window, text="jumper6 is to big")
        error_label.grid(row=13, pady =10, padx =10)
        return all_ok
    






    swews=[sw1,sw2,sw3,sw4, sw5, sw6,sw7,sw8, sw9,sw10,ew1,ew2,ew3,ew4,ew5,ew6,ew7,ew8,ew9,ew10]

    sewc=0
    for swew in (swews):

        sewc = sewc+1
        if swew < 0:
            
            all_ok = False
            error_label = ctk.CTkLabel(window, text=(swew, "is to small at the sw's and ew's"))
            error_label.grid(row=13, pady =10, padx =10)
            return all_ok
        if swew > 96:
            all_ok = False
            error_label = ctk.CTkLabel(window, text=(swew, "is to big at the sw's and ew's"))
            error_label.grid(row=13, pady =10, padx =10)
            return all_ok
        if swew != 96:
            if sewc == 1:
                if ew1==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set ew1 or set sw1 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 2:
                if ew2==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set ew2 or set sw2 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 3:
                if ew3==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set ew3 or set sw3 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 4:
                if ew4==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set ew4 or set sw4 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 5:
                if ew5==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set ew5 or set sw5 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 6:
                if ew6==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set ew6 or set sw6 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 7:
                if ew7==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set ew7 or set sw7 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 8:
                if ew8==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set ew8 or set sw8 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 9:
                if ew9==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set ew9 or set sw9 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 10:
                if ew10==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set ew10 or set sw10 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 11:
                if sw1==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set sw1 or set ew1 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 12:
                if sw2==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set sw2 or set ew2 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 13:
                if sw3==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set sw3 or set ew3 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 14:
                if sw4==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set sw4 or set ew4 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 15:
                if sw5==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set sw5 or set ew5 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 16:
                if sw6==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set sw6 or set ew6 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 17:
                if sw7==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set sw7 or set ew7 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 18:
                if sw8==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set sw8 or set ew8 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 19:
                if sw9==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set sw9 or set ew9 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
            if sewc == 20:
                if sw10==96:
                    all_ok = False
                    error_label = ctk.CTkLabel(window, text=("you also have to set sw10 or set ew10 to 96 to swich it of"))
                    error_label.grid(row=13, pady =10, padx =10)
                    return all_ok
    swewdub=0
    for i in (swews):
        swewdub=0
        if i != 96:
            for l in (swews):
                if i == l:
                    swewdub = swewdub+1
            if swewdub != 1:
                all_ok = False
                error_label = ctk.CTkLabel(window, text=("it is not allowed that a number is twise in the sw's and ew's exept vor 96"))
                error_label.grid(row=13, pady =10, padx =10)
                return all_ok

    if rd == 1 or 2 or 3:
        print("")
    else:
        all_ok = False
        error_label = ctk.CTkLabel(window, text=("the revers disc has to be choosen with 1,2 or 3"))
        error_label.grid(row=13, pady =10, padx =10)
        return all_ok
        

    for f in [dc1,dc2,dc3,dc4,dc5,dc6]:
        if f < 0:
            all_ok = False
            error_label = ctk.CTkLabel(window, text=("no discstartinpoint is allowed to be under 0"))
            error_label.grid(row=13, pady =10, padx =10)
            return all_ok
        if f > 95:
            all_ok = False
            error_label = ctk.CTkLabel(window, text=("no discstartinpoint is allowed to be over 95"))
            error_label.grid(row=13, pady =10, padx =10)
            return all_ok

    
    if discorder>999999:
        all_ok = False
        error_label = ctk.CTkLabel(window, text=("the discorder is not allowed to be over 999999"))
        error_label.grid(row=13, pady =10, padx =10)
        return all_ok
    if discorder<111111:
        all_ok = False
        error_label = ctk.CTkLabel(window, text=("the discorder is not allowed to be under 111111"))
        error_label.grid(row=13, pady =10, padx =10)
        return all_ok




    sch1 = scheibenzuteiler(discorder, 100_000)
    discorder = discorder-(sch1*100_000)
    sch2 = scheibenzuteiler(discorder, 10000)
    discorder = discorder-(sch2*100_00)
    sch3 = scheibenzuteiler(discorder, 1000)
    discorder = discorder-(sch3*100_0)
    sch4 = scheibenzuteiler(discorder, 100)
    discorder = discorder-(sch4*100)
    sch5 = scheibenzuteiler(discorder, 10)
    discorder = discorder-(sch5*10)
    sch6 = scheibenzuteiler(discorder, 1)
    tester = scheibenreihungspruefung(sch1, sch2, sch3, sch4, sch5, sch6)
    if tester == False:
        all_ok = False
        error_label = ctk.CTkLabel(window, text=("the discorder is unrealistic"))
        error_label.grid(row=13, pady =10, padx =10)
        return all_ok
    tester = True
    return all_ok
def scheibenzuteiler(discorder,int):
    value = round((discorder/int)-0.49)
    return value
def scheibenreihungspruefung(sch1,sch2,sch3,sch4,sch5,sch6):
    pr = True
    if sch1==sch2:
        pr = False
    if sch1==sch3:
        pr = False
    if sch1==sch4:
        pr = False
    if sch1==sch5:
        pr = False
    if sch1==sch6:
        pr = False
    if sch2==sch3:
        pr = False
    if sch2==sch4:
        pr = False
    if sch2==sch5:
        pr = False
    if sch2==sch6:
        pr = False
    if sch3==sch4:
        pr = False
    if sch3==sch5:
        pr = False
    if sch3==sch6:
        pr = False
    if sch4==sch5:
        pr = False
    if sch4==sch6:
        pr = False
    if sch5==sch6:
        pr = False
    return pr


window.title("Efe")
window.geometry("1150x900")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


window.grid_columnconfigure(0,weight=1)


baumhaus_big = ctk.CTkFont("Bauhaus 93", 30)
label = ctk.CTkLabel(window, text="Encription file editor",font=baumhaus_big)

fileframe = ctk.CTkFrame(window)

fileframe.grid(row =1, pady =10, padx=10)

label.grid(row=0, pady=10,padx=10,)

load_file = ctk.CTkButton(fileframe, text= "load file", command=load_file)

load_file.grid(row=1, column =0,pady=10, padx=10)

enc_txt= ctk.CTkLabel(fileframe, text = "#####.txt")
enc_txt.grid(row=1, column = 1, pady= 10, padx=10, sticky ="ew")

entry1 = ctk.CTkEntry(window, textvariable=entry1_tvar)

disctext = ctk.CTkLabel(window, text="this number is used to determine the order of the discs, there must be 6 numbers, and these must be between 1 and 9, e.g.: 638924")
disctext.grid(row=2, pady=10,padx=10,sticky = "ew")
entry1.grid(pady=10,padx=10,row = 3,)

jumpertext = ctk.CTkLabel(window, text="With these jumps you define at which points the discs 2-6 continue to rotate.The number must be between 1 and (2 to the power of 96)-1")
jumpertext.grid(row=4, pady=10,padx=10,sticky = "ew")


jumperframe= ctk.CTkFrame(window)
jumperframe.grid_columnconfigure(0, weight=1)
jumperframe.grid(pady=0,padx=10,row = 5,)
jumperentry2 = ctk.CTkEntry(master=jumperframe, textvariable=jumperentry2_tvar)
jumperentry2.grid(pady=10,padx=10,row = 1,column =0,sticky="ew")
jumperentry3 = ctk.CTkEntry(master=jumperframe, textvariable=jumperentry3_tvar)
jumperentry3.grid(pady=10,padx=10,row = 1,column =1,sticky="ew")
jumperentry4 = ctk.CTkEntry(master=jumperframe, textvariable=jumperentry4_tvar)
jumperentry4.grid(pady=10,padx=10,row = 1,column =2,sticky="ew")
jumperentry5 = ctk.CTkEntry(master=jumperframe, textvariable=jumperentry5_tvar)
jumperentry5.grid(pady=10,padx=10,row = 1,column =3,sticky="ew")
jumperentry6 = ctk.CTkEntry(master=jumperframe, textvariable=jumperentry6_tvar)
jumperentry6.grid(pady=10,padx=10,row = 1,column =4,sticky="ew")

discstarttext = ctk.CTkLabel(window, text="the dc is the value used to determine in which position the discs start (between 0-95)")
discstarttext.grid(row=6, pady=10,padx=10)



dcframe=ctk.CTkFrame(window)
dcframe.grid_columnconfigure(0,weight=1)
dcframe.grid(row=7,pady =10,padx=10)
dc1entry=ctk.CTkEntry(dcframe,textvariable=dc1entry_tvar)
dc1entry.grid(row=1, pady=10,padx=10, column=0)
dc2entry=ctk.CTkEntry(dcframe,textvariable=dc2entry_tvar)
dc2entry.grid(row=1, pady=10,padx=10, column=1)
dc3entry=ctk.CTkEntry(dcframe,textvariable=dc3entry_tvar)
dc3entry.grid(row=1, pady=10,padx=10, column=2)
dc4entry=ctk.CTkEntry(dcframe,textvariable=dc4entry_tvar)
dc4entry.grid(row=1, pady=10,padx=10, column=3)
dc5entry=ctk.CTkEntry(dcframe,textvariable=dc5entry_tvar)
dc5entry.grid(row=1, pady=10,padx=10, column=4)
dc6entry=ctk.CTkEntry(dcframe,textvariable=dc6entry_tvar)
dc6entry.grid(row=1, pady=10,padx=10, column=5)

plugboardtext = ctk.CTkLabel(window, text="characters in the plugboard can be swapped with sw and ew (sw and ew must be between 0 and 95). 96 means that the following plug is not active. If sw1 is active, ew1 must also be active, etc.")
plugboardtext.grid(row = 8, pady=10, padx= 10)
plugboardframe = ctk.CTkFrame(window)
plugboardframe.grid(row = 9, pady=10,padx=10)


plugboard_sw1 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_sw1_tvar)
plugboard_sw1.grid(row = 0, column = 0, pady =10, padx=10)
plugboard_sw2 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_sw2_tvar)
plugboard_sw2.grid(row = 0, column = 1, pady =10, padx=10)
plugboard_sw3 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_sw3_tvar)
plugboard_sw3.grid(row = 0, column = 2, pady =10, padx=10)
plugboard_sw4 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_sw4_tvar)
plugboard_sw4.grid(row = 0, column = 3, pady =10, padx=10)
plugboard_sw5 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_sw5_tvar)
plugboard_sw5.grid(row = 0, column = 4, pady =10, padx=10)
plugboard_sw6 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_sw6_tvar)
plugboard_sw6.grid(row = 1, column = 0, pady =10, padx=10)
plugboard_sw7 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_sw7_tvar)
plugboard_sw7.grid(row = 1, column = 1, pady =10, padx=10)
plugboard_sw8 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_sw8_tvar)
plugboard_sw8.grid(row = 1, column = 2, pady =10, padx=10)
plugboard_sw9 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_sw9_tvar)
plugboard_sw9.grid(row = 1, column = 3, pady =10, padx=10)
plugboard_sw10 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_sw10_tvar)
plugboard_sw10.grid(row = 1, column = 4, pady =10, padx=10)
plugboard_ew1 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_ew1_tvar)
plugboard_ew1.grid(row = 2, column = 0, pady =10, padx=10)
plugboard_ew2 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_ew2_tvar)
plugboard_ew2.grid(row = 2, column = 1, pady =10, padx=10)
plugboard_ew3 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_ew3_tvar)
plugboard_ew3.grid(row = 2, column = 2, pady =10, padx=10)
plugboard_ew4 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_ew4_tvar)
plugboard_ew4.grid(row = 2, column = 3, pady =10, padx=10)
plugboard_ew5 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_ew5_tvar)
plugboard_ew5.grid(row = 2, column = 4, pady =10, padx=10)
plugboard_ew6 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_ew6_tvar)
plugboard_ew6.grid(row = 3, column = 0, pady =10, padx=10)
plugboard_ew7 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_ew7_tvar)
plugboard_ew7.grid(row = 3, column = 1, pady =10, padx=10)
plugboard_ew8 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_ew8_tvar)
plugboard_ew8.grid(row = 3, column = 2, pady =10, padx=10)
plugboard_ew9 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_ew9_tvar)
plugboard_ew9.grid(row = 3, column = 3, pady =10, padx=10)
plugboard_ew10 = ctk.CTkEntry(plugboardframe, textvariable=plugboard_ew10_tvar)
plugboard_ew10.grid(row = 3, column = 4, pady =10, padx=10)


switchdisctext = ctk.CTkLabel(window, text="With ds the revers disc can be selected (1-3). With kss the reversing disc position can be selected (0-95)")
switchdisctext.grid(row = 10, pady=10, padx=10)
switchdiscframe = ctk.CTkFrame(window)
switchdiscframe.grid(row=11, pady =10, padx=10)
discchoosentry= ctk.CTkEntry(switchdiscframe, textvariable=discchoosentry_tvar)
discchoosentry.grid(pady=10,padx=10)
discstartingentry= ctk.CTkEntry(switchdiscframe, textvariable=discstartingentry_tvar)
discstartingentry.grid(row=0,column=1, pady=10, padx=10)

creatbutton= ctk.CTkButton(window, text="Creat File", command=creatfile)
creatbutton.grid(row =12, pady=10, padx=10, sticky = "ew")
upfile = ctk.CTkButton(window, text="Update file")
error_label = ctk.CTkLabel(window, text= "")

window.mainloop()

