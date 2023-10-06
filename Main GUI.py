import customtkinter as ctk
from tkinter import filedialog

window = ctk.CTk()
window.title("Enigma")
window.geometry("1150x850")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
window.grid_columnconfigure(0,weight=1)
filedir=None
def load_file():
    
    
    global filedir, list_of_lines
    filedir = filedialog.askopenfilename(filetypes=[("text file","*.txt")])
    print (filedir)
    filename.configure(text=filedir)
    global jumper2,jumper3,jumper4,jumper5,jumper6,dc1,dc2,dc3,dc4,dc5,dc6,sw1,sw2,sw3,sw4,sw5,sw6,sw7,sw8,sw9,sw10,ew1,ew2,ew3,ew4,ew5,ew6,ew7,ew8,ew9,ew10,rd,rdc,discorder
    fileobj=open(filedir,"r")
    list_of_lines = fileobj.readlines()
    try:
        discorder = int(list_of_lines[0].replace("\n",""))
        jumper2 = int(list_of_lines[1].replace("\n",""))
        jumper3 = int(list_of_lines[2].replace("\n",""))
        jumper4 = int(list_of_lines[3].replace("\n",""))
        jumper5 = int(list_of_lines[4].replace("\n",""))
        jumper6 = int(list_of_lines[5].replace("\n",""))
        dc1 = int(list_of_lines[6].replace("\n",""))
        dc2 = int(list_of_lines[7].replace("\n",""))
        dc3 = int(list_of_lines[8].replace("\n",""))
        dc4 = int(list_of_lines[9].replace("\n",""))
        dc5 = int(list_of_lines[10].replace("\n",""))
        dc6 = int(list_of_lines[11].replace("\n",""))
        sw1 = int(list_of_lines[12].replace("\n",""))
        sw2 = int(list_of_lines[13].replace("\n",""))
        sw3 = int(list_of_lines[14].replace("\n",""))
        sw4 = int(list_of_lines[15].replace("\n",""))
        sw5 = int(list_of_lines[16].replace("\n",""))
        sw6 = int(list_of_lines[17].replace("\n",""))
        sw7 = int(list_of_lines[18].replace("\n",""))
        sw8 = int(list_of_lines[19].replace("\n",""))
        sw9 = int(list_of_lines[20].replace("\n",""))
        sw10 = int(list_of_lines[21].replace("\n","")) 
        ew1 = int(list_of_lines[22].replace("\n",""))
        ew2 = int(list_of_lines[23].replace("\n",""))
        ew3 = int(list_of_lines[24].replace("\n",""))
        ew4 = int(list_of_lines[25].replace("\n",""))
        ew5 = int(list_of_lines[26].replace("\n",""))
        ew6 = int(list_of_lines[27].replace("\n",""))
        ew7 = int(list_of_lines[28].replace("\n",""))
        ew8 = int(list_of_lines[29].replace("\n",""))
        ew9 = int(list_of_lines[30].replace("\n",""))
        ew10 = int(list_of_lines[31].replace("\n","")) 
        rd = int(list_of_lines[32].replace("\n",""))
        rdc = int(list_of_lines[33].replace("\n",""))
    except:
        repair_file.grid(column=0, row=0, sticky ="ew", padx =5)
        main_output.configure(state="normal")
        main_output.delete("0.0","end")
        main_output.insert("0.0","The file is damaget you have to repair it")
        main_output.configure(state="disabled")
    

    prüfer =False
    prüfer = eingabeprüfer2()

    
    if prüfer == False:
        repair_file.grid(column=0, row=0, sticky ="ew", padx =5)
        main_output.configure(state="normal")
        main_output.delete("0.0","end")
        main_output.insert("0.0","The file is damaget you have to repair it")
        main_output.configure(state="disabled")
    if prüfer == True:
        main_output.configure(state="normal")
        main_output.delete("0.0","end")
        main_output.configure(state="disabled")
        repair_file.grid_remove()
        start_enigma.configure(state="normal")
def umkaerscheibenplatz(ctbs, ks,ksc):
    if (ks == 1):
        ctbs = kaerscheibe(ctbs,ksc,ks1)
    if (ks == 2):
        ctbs = kaerscheibe(ctbs,ksc,ks2)
    if (ks == 3):
        ctbs = kaerscheibe(ctbs,ksc,ks3)
    return ctbs
def stringtoint(starttex, zeich):
    l = []
    for xx in starttex:
        tf = True
        c = 0
        while tf == True:
            if xx == zeich[c]:
                l.append(c)
                tf = False
            else:
                c = c+1
            if c == 96:
                main_output.configure(state="normal")
                main_output.delete("0.0","end")
                main_output.insert("0.0",(xx,"is sadly not in the carakter list. Pleace remove it or change it with one of them:", zeich))
                main_output.configure(state="disabled")
    return l

def scheibenplatz(ctbs,sch,sc,hzt):
    if hzt == 1:
        if (sch == 1):
            ctbs = scheibehin(ctbs, sc, ts1, hzt)
        if (sch == 2):
            ctbs = scheibehin(ctbs, sc, ts2, hzt)
        if (sch == 3):
            ctbs = scheibehin(ctbs, sc, ts3, hzt)
        if (sch == 4):
            ctbs = scheibehin(ctbs, sc, ts4, hzt)
        if (sch == 5):
            ctbs = scheibehin(ctbs, sc, ts5, hzt)
        if (sch == 6):
            ctbs = scheibehin(ctbs, sc, ts6, hzt)
        if (sch == 7):
            ctbs = scheibehin(ctbs, sc, ts7, hzt)
        if (sch == 8):
            ctbs = scheibehin(ctbs, sc, ts8, hzt)
        if (sch == 9):
            ctbs = scheibehin(ctbs, sc, ts9, hzt)
    if hzt == 2:
        if (sch == 1):
            ctbs = scheibehin(ctbs, sc, ts1I, hzt)
        if (sch == 2):
            ctbs = scheibehin(ctbs, sc, ts2I, hzt)
        if (sch == 3):
            ctbs = scheibehin(ctbs, sc, ts3I, hzt)
        if (sch == 4):
            ctbs = scheibehin(ctbs, sc, ts4I, hzt)
        if (sch == 5):
            ctbs = scheibehin(ctbs, sc, ts5I, hzt)
        if (sch == 6):
            ctbs = scheibehin(ctbs, sc, ts6I, hzt)
        if (sch == 7):
            ctbs = scheibehin(ctbs, sc, ts7I, hzt)
        if (sch == 8):
            ctbs = scheibehin(ctbs, sc, ts8I, hzt)
        if (sch == 9):
            ctbs = scheibehin(ctbs, sc, ts9I, hzt)



    return ctbs
def kaerscheibe(ctbs,ksc,ks):
    ctbs = ctbs + ksc
    ctbs = ctbs % 96
    ctbs = ks[ctbs]
    ctbs = ctbs - ksc
    ctbs = ctbs + 96
    ctbs = ctbs % 96
    return ctbs
def inttostring(endlist, zeichn):
    et = ""
    for xx in endlist:
        s = zeichn[xx]
        et = et + s
    return et
def scheibehin(zz1,sc,tauscher,hz):
    if hz == 1:
        zz1 = zz1+sc

    zz1 = zz1 % 96
    zz1 = tauscher[zz1]

    if hz == 2:
        zz1 = (zz1-sc) + 96
        zz1 = zz1 % 96
    return zz1
def eingabeprüfer2():
    global discorder, jumper2



    all_ok = True
    
    for e in[jumper2,jumper3,jumper4,jumper5,jumper6]:
        if e <1:
            all_ok = False
            return all_ok

    if jumper2 > 79_228_162_514_264_337_593_543_950_335:
        all_ok = False
        return all_ok
    if jumper3 > 79_228_162_514_264_337_593_543_950_335:
        all_ok = False
        return all_ok
    if jumper4 > 79_228_162_514_264_337_593_543_950_335:
        all_ok = False
        return all_ok
    if jumper5 > 79_228_162_514_264_337_593_543_950_335:
        all_ok = False
        return all_ok
    if jumper6 > 79_228_162_514_264_337_593_543_950_335:
        all_ok = False
        return all_ok
    






    swews=[sw1,sw2,sw3,sw4, sw5, sw6,sw7,sw8, sw9,sw10,ew1,ew2,ew3,ew4,ew5,ew6,ew7,ew8,ew9,ew10]

    sewc=0
    for swew in (swews):

        sewc = sewc+1
        if swew < 0:
            
            all_ok = False
            return all_ok
        if swew > 96:
            all_ok = False
            return all_ok
        if swew != 96:
            if sewc == 1:
                if ew1==96:
                    all_ok = False
                    return all_ok
            if sewc == 2:
                if ew2==96:
                    all_ok = False
                    return all_ok
            if sewc == 3:
                if ew3==96:
                    all_ok = False
                    return all_ok
            if sewc == 4:
                if ew4==96:
                    all_ok = False
                    return all_ok
            if sewc == 5:
                if ew5==96:
                    all_ok = False
                    return all_ok
            if sewc == 6:
                if ew6==96:
                    all_ok = False
                    return all_ok
            if sewc == 7:
                if ew7==96:
                    all_ok = False
                    return all_ok
            if sewc == 8:
                if ew8==96:
                    all_ok = False
                    return all_ok
            if sewc == 9:
                if ew9==96:
                    all_ok = False
                    return all_ok
            if sewc == 10:
                if ew10==96:
                    all_ok = False
                    return all_ok
            if sewc == 11:
                if sw1==96:
                    all_ok = False
                    return all_ok
            if sewc == 12:
                if sw2==96:
                    return all_ok
            if sewc == 13:
                if sw3==96:
                    all_ok = False
                    return all_ok
            if sewc == 14:
                if sw4==96:
                    all_ok = False
                    return all_ok
            if sewc == 15:
                if sw5==96:
                    all_ok = False
                    return all_ok
            if sewc == 16:
                if sw6==96:
                    all_ok = False
                    return all_ok
            if sewc == 17:
                if sw7==96:
                    all_ok = False
                    return all_ok
            if sewc == 18:
                if sw8==96:
                    all_ok = False
                    return all_ok
            if sewc == 19:
                if sw9==96:
                    all_ok = False
                    return all_ok
            if sewc == 20:
                if sw10==96:
                    all_ok = False
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
                return all_ok

    if rd == 1 or 2 or 3:
        print("")
    else:
        all_ok = False
        return all_ok
        

    for f in [dc1,dc2,dc3,dc4,dc5,dc6]:
        if f < 0:
            all_ok = False
            return all_ok
        if f > 95:
            all_ok = False
            return all_ok

    
    if discorder>999999:
        all_ok = False
        return all_ok
    if discorder<111111:
        all_ok = False
        return all_ok



    global sch1,sch2,sch3,sch4,sch5,sch6
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
def enigma_start():
    
    global jumper2,jumper3,jumper4,jumper5,jumper6,dc1,dc2,dc3,dc4,dc5,dc6,sw1,sw2,sw3,sw4,sw5,sw6,sw7,sw8,sw9,sw10,ew1,ew2,ew3,ew4,ew5,ew6,ew7,ew8,ew9,ew10,rd,rdc,discorder
    global starttext
    starttext = main_input.get("0.0","end")
    
    startlist = stringtoint(starttext, characters)
    print (startlist)
    del startlist[(len(startlist))-1]
    print (startlist)
    kerbenboard2 = kerbenmacher(jumper2)
    kerbenboard3 = kerbenmacher(jumper3)
    kerbenboard4 = kerbenmacher(jumper4)
    kerbenboard5 = kerbenmacher(jumper5)
    kerbenboard6 = kerbenmacher(jumper6)
    dc1 = int(list_of_lines[6].replace("\n",""))
    dc2 = int(list_of_lines[7].replace("\n",""))
    dc3 = int(list_of_lines[8].replace("\n",""))
    dc4 = int(list_of_lines[9].replace("\n",""))
    dc5 = int(list_of_lines[10].replace("\n",""))
    dc6 = int(list_of_lines[11].replace("\n",""))
    
    ue2 = False
    ue3 = False
    ue4 = False
    ue5 = False
    ue6 = False
    endlist = []
    cc=0

    while(cc<len(startlist)):

        if dc1 != 0:
            ue2 = kerbenpruefer((dc1 % 96), kerbenboard2)
        if dc2 != 0:
            ue3 = kerbenpruefer((dc2 % 96), kerbenboard3)
        if dc3 != 0:
            ue4 = kerbenpruefer((dc3 % 96), kerbenboard4)
        if dc4 != 0:
            ue5 = kerbenpruefer((dc4 % 96), kerbenboard5)
        if dc5 != 0:
            ue6 = kerbenpruefer((dc5 % 96), kerbenboard6)

        if ue2 == True:
            dc2 = dc2 + 1
        if ue3 == True:
            dc3 = dc3 + 1
        if ue4 == True:
            dc4 = dc4 + 1
        if ue5 == True:
            dc5 = dc5 + 1
        if ue6 == True:
            dc6 = dc6 + 1
        ctbs = startlist[cc]



        ctbs = tauschboard(ctbs)
        ctbs = scheibenplatz(ctbs, sch1, dc1, 1)
        ctbs = scheibenplatz(ctbs, sch2, dc2, 1)
        ctbs = scheibenplatz(ctbs, sch3, dc3, 1)
        ctbs = scheibenplatz(ctbs, sch4, dc4, 1)
        ctbs = scheibenplatz(ctbs, sch5, dc5, 1)
        ctbs = scheibenplatz(ctbs, sch6, dc6, 1)
        ctbs = umkaerscheibenplatz(ctbs, rd, rdc)
        ctbs = scheibenplatz(ctbs, sch6, dc6, 2)
        ctbs = scheibenplatz(ctbs, sch5, dc5, 2)
        ctbs = scheibenplatz(ctbs, sch4, dc4, 2)
        ctbs = scheibenplatz(ctbs, sch3, dc3, 2)
        ctbs = scheibenplatz(ctbs, sch2, dc2, 2)
        ctbs = scheibenplatz(ctbs, sch1, dc1, 2)
        ctbs = tauschboard(ctbs)





        
        endlist.append(ctbs)




        dc1 = dc1 + 1
        cc = cc + 1
    endtext = inttostring(endlist, characters)
    main_output.configure(state="normal")
    main_output.delete("0.0","end")
    main_output.insert("0.0",endtext)
    main_output.configure(state="disabled")
def kerbenmacher(uebers):
    h = 95
    b = []
    while h >= 0:
        if uebers >= 2**h:
            b.append(True)
            uebers = uebers - 2**h
            h = h-1
        else:
            b.append(False)
            h = h-1
    return b
def kerbenpruefer(sz,kerbenboa):
    sp = False
    if kerbenboa[sz] == True:
        sp = True
    return sp
def tauschboard(ctbs):
    if(ctbs==sw1):
        return ew1
    if(ctbs==sw2):
        return ew2
    if(ctbs==sw3):
        return ew3
    if(ctbs==sw4):
        return ew4
    if(ctbs==sw5):
        return ew5
    if(ctbs==sw6):
        return ew6
    if(ctbs==sw7):
        return ew7
    if(ctbs==sw8):
        return ew8
    if(ctbs==sw9):
        return ew9
    if(ctbs==sw10):
        return ew10
    
    #cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    if(ctbs==ew1):
        return sw1
    if(ctbs==ew2):
        return sw2
    if(ctbs==ew3):
        return sw3
    if(ctbs==ew4):
        return sw4
    if(ctbs==ew5):
        return sw5
    if(ctbs==ew6):
        return sw6
    if(ctbs==ew7):
        return sw7
    if(ctbs==ew8):
        return sw8
    if(ctbs==ew9):
        return sw9
    if(ctbs==ew10):
        return sw10
    return ctbs
def tI(t):
    k1 = []
    gesucht = 0
    while gesucht < 96:

        counter = 0
        while counter < 96:
            if gesucht == t[counter]:
                k1.append(counter)
                break
            else:
                counter = counter + 1
        gesucht = gesucht + 1
    return k1
def open_efe():
    None
addiction_50 =ctk.CTkFont("Addiction", 100)
sevensegment =ctk.CTkFont("Seven Segment", 25)


title = ctk.CTkLabel(window, text="Enigma", font=addiction_50)
title.grid(row=0, pady = 10, padx=10)

input_text=ctk.CTkLabel(window, text="Place your text here:", font=sevensegment)
input_text.grid(row =1, pady=0, padx=10, sticky="w")

main_input=ctk.CTkTextbox(window)
main_input.grid(row=2,sticky= "ew", pady=10, padx=10)

middle_frame = ctk.CTkFrame(window)
middle_frame.grid(row=3)

choose_file = ctk.CTkButton(middle_frame, text="Choose file", command=load_file)
choose_file.grid(column=0, row=0)

filename= ctk.CTkLabel(middle_frame, text="#####.txt")
filename.grid(column=1,row=0)

output_text=ctk.CTkLabel(window, text="Output:", font=sevensegment)
output_text.grid(row =4, pady=0, padx=10, sticky="w")

main_output=ctk.CTkTextbox(window)
main_output.grid(row=5,sticky= "ew", pady=10, padx=10)
main_output.configure(state="disabled")

lower_frame = ctk.CTkFrame(window)
lower_frame.grid(row=6, sticky ="ew")
lower_frame.columnconfigure((0,1),weight=1)

start_enigma = ctk.CTkButton(lower_frame, text="Start Enigma", command=enigma_start)
start_enigma.grid(column=0, row=0, sticky ="ew", padx =5)
start_enigma.configure(state="disabled")
repair_file = ctk.CTkButton(lower_frame, text= "Repair file", command= None)

creat_encription_file= ctk.CTkButton(lower_frame, text="Creat Encription File", command=open_efe)
creat_encription_file.grid(column=1,row=0, sticky ="ew",padx=5)































characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "ß", "q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "ü", "+", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "\n", "<", "y", "x", "c", "v", "b", "n", "m", ",", ".", "-", "!", '"', "§", "$", "%", "&", "/", "(", ")", "=", "?", "Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ü", "*", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä", "–", ">", "Y", "X", "C", "V", "B", "N", "M", ";", ":", "_", "@", " ", "€", "°", "~"]
ks1 = [18, 66, 11, 54, 85, 20, 45, 80, 43, 44, 89, 2, 83, 40, 41, 16, 15, 73, 0, 84, 5, 74, 31, 88, 72, 61, 49, 92, 76, 37, 52, 22, 70, 77, 67, 71, 39, 29, 53, 36, 13, 14, 55, 8, 9, 6, 86, 59, 87, 26, 69, 65, 30, 38, 3, 42, 90, 82, 94, 47, 62, 25, 60, 64, 63, 51, 1, 34, 79, 50, 32, 35, 24, 17, 21, 91, 28, 33, 93, 68, 7, 95, 57, 12, 19, 4, 46, 48, 23, 10, 56, 75, 27, 78, 58, 81]
ks2 = [59, 55, 71, 31, 43, 36, 84, 44, 54, 58, 53, 41, 75, 50, 22, 17, 79, 15, 70, 28, 56, 78, 14, 30, 80, 77, 86, 83, 19, 61, 23, 3, 88, 45, 91, 68, 5, 46, 95, 72, 92, 11, 73, 4, 7, 33, 37, 57, 94, 67, 13, 93, 82, 10, 8, 1, 20, 47, 9, 0, 62, 29, 60, 74, 66, 89, 64, 49, 35, 76, 18, 2, 39, 42, 63, 12, 69, 25, 21, 16, 24, 90, 52, 27, 6, 87, 26, 85, 32, 65, 81, 34, 40, 51, 48, 38]
ks3 = [30, 84, 6, 32, 78, 12, 2, 94, 53, 40, 58, 42, 5, 63, 51, 81, 33, 22, 23, 60, 87, 28, 17, 18, 85, 71, 47, 86, 21, 69, 0, 62, 3, 16, 92, 89, 90, 74, 77, 57, 9, 65, 11, 82, 66, 76, 67, 26, 91, 55, 56, 14, 72, 8, 70, 49, 50, 39, 10, 64, 19, 75, 31, 13, 59, 41, 44, 46, 83, 29, 54, 25, 52, 79, 37, 61, 45, 38, 4, 73, 95, 15, 43, 68, 1, 24, 27, 20, 93, 35, 36, 48, 34, 88, 7, 80]
ts1 = [50, 40, 56, 47, 62, 61, 83, 4, 37, 80, 15, 12, 63, 59, 9, 64, 8, 71, 39, 82, 88, 86, 75, 79, 6, 27, 30, 73, 48, 5, 33, 68, 93, 52, 19, 25, 94, 29, 69, 41, 76, 87, 22, 77, 55, 14, 2, 46, 13, 95, 78, 42, 18, 10, 91, 31, 3, 54, 81, 89, 24, 84, 70, 58, 53, 44, 43, 49, 35, 1, 45, 26, 92, 0, 23, 51, 57, 28, 66, 67, 72, 36, 65, 90, 21, 17, 11, 38, 60, 34, 7, 16, 74, 32, 20, 85]
ts2 = [67, 6, 7, 14, 94, 93, 15, 77, 42, 56, 83, 28, 21, 36, 89, 4, 41, 63, 58, 62, 60, 91, 79, 87, 82, 61, 19, 70, 2, 95, 90, 22, 26, 84, 80, 88, 23, 3, 5, 78, 16, 85, 37, 57, 65, 71, 50, 66, 46, 27, 52, 86, 25, 68, 20, 0, 74, 35, 73, 10, 49, 75, 72, 1, 51, 17, 9, 45, 33, 11, 54, 34, 92, 29, 48, 12, 31, 13, 59, 44, 64, 32, 24, 76, 47, 53, 18, 69, 8, 81, 38, 55, 30, 43, 40, 39]
ts3 = [29, 78, 44, 48, 40, 38, 55, 81, 54, 83, 75, 14, 15, 5, 93, 24, 67, 41, 8, 43, 9, 18, 27, 62, 53, 77, 21, 94, 34, 51, 1, 33, 37, 56, 22, 69, 88, 23, 20, 74, 13, 0, 72, 28, 76, 6, 64, 19, 47, 82, 60, 17, 70, 91, 59, 89, 30, 61, 3, 2, 35, 66, 7, 92, 16, 57, 39, 46, 68, 12, 31, 45, 49, 52, 26, 65, 63, 36, 80, 42, 50, 32, 86, 84, 71, 4, 73, 10, 85, 87, 95, 58, 90, 25, 79, 11]
ts4 = [14, 7, 34, 88, 57, 29, 90, 71, 44, 85, 62, 38, 40, 78, 6, 74, 3, 43, 76, 49, 4, 39, 27, 80, 73, 22, 54, 84, 41, 91, 86, 24, 21, 51, 66, 65, 69, 8, 70, 13, 55, 31, 48, 10, 19, 12, 50, 36, 23, 9, 93, 42, 95, 61, 59, 83, 58, 20, 94, 63, 46, 68, 77, 89, 87, 33, 75, 17, 16, 45, 81, 1, 82, 18, 47, 92, 56, 37, 52, 32, 53, 11, 15, 0, 35, 5, 28, 64, 60, 67, 26, 30, 25, 72, 2, 79]
ts5 = [61, 15, 40, 88, 70, 38, 1, 59, 28, 72, 19, 31, 2, 45, 47, 16, 73, 82, 67, 3, 93, 48, 58, 87, 57, 89, 12, 85, 80, 66, 54, 94, 56, 29, 83, 62, 90, 32, 92, 37, 76, 5, 17, 52, 20, 41, 84, 74, 53, 7, 63, 91, 43, 8, 11, 34, 77, 30, 75, 51, 79, 44, 42, 49, 24, 50, 55, 10, 26, 39, 69, 18, 60, 68, 0, 25, 9, 36, 64, 86, 65, 13, 71, 4, 21, 14, 95, 33, 22, 35, 6, 81, 78, 23, 46, 27]
ts6 = [69, 95, 21, 82, 37, 78, 75, 87, 93, 27, 67, 38, 20, 16, 42, 55, 94, 77, 11, 60, 22, 58, 61, 76, 52, 46, 12, 32, 57, 34, 81, 68, 2, 35, 73, 48, 29, 51, 79, 56, 8, 6, 63, 84, 19, 31, 33, 17, 47, 7, 13, 62, 36, 85, 90, 14, 49, 18, 39, 4, 28, 5, 44, 1, 59, 65, 91, 70, 72, 86, 71, 54, 23, 45, 88, 9, 24, 15, 41, 89, 53, 43, 40, 3, 80, 74, 50, 83, 64, 26, 66, 0, 10, 25, 30, 92]
ts7 = [93, 71, 80, 94, 5, 9, 30, 84, 47, 0, 6, 73, 72, 33, 86, 38, 10, 74, 51, 23, 39, 83, 25, 78, 36, 14, 50, 26, 57, 91, 59, 15, 48, 56, 35, 12, 66, 79, 20, 37, 32, 34, 67, 52, 18, 63, 21, 53, 58, 54, 7, 41, 62, 68, 76, 55, 43, 22, 19, 77, 65, 29, 89, 17, 11, 45, 24, 69, 27, 64, 70, 49, 13, 16, 1, 4, 90, 2, 88, 3, 87, 60, 82, 95, 31, 85, 46, 61, 42, 28, 81, 8, 75, 92, 40, 44]
ts8 = [10, 42, 9, 19, 13, 54, 76, 2, 50, 39, 33, 59, 62, 94, 11, 48, 12, 8, 17, 37, 52, 75, 23, 67, 72, 0, 43, 89, 4, 69, 63, 25, 51, 36, 83, 35, 55, 82, 45, 73, 18, 21, 41, 91, 38, 32, 20, 27, 47, 29, 81, 65, 57, 3, 87, 34, 68, 70, 53, 40, 7, 85, 44, 58, 86, 77, 66, 93, 60, 28, 92, 78, 88, 16, 22, 64, 5, 95, 15, 74, 46, 49, 61, 14, 84, 79, 80, 56, 31, 24, 90, 30, 71, 1, 6, 26]
ts9 = [61, 26, 64, 15, 57, 53, 14, 79, 28, 25, 33, 41, 31, 21, 94, 46, 42, 29, 69, 58, 49, 78, 60, 92, 84, 35, 22, 40, 39, 20, 1, 0, 34, 55, 11, 89, 48, 24, 44, 23, 80, 90, 75, 50, 32, 72, 77, 66, 17, 12, 70, 63, 74, 51, 54, 52, 95, 88, 85, 93, 45, 76, 7, 68, 16, 87, 81, 82, 9, 86, 38, 18, 37, 8, 62, 10, 36, 73, 4, 2, 43, 13, 56, 47, 65, 6, 30, 19, 59, 67, 71, 83, 5, 27, 91, 3]
ts1I = tI(ts1)
ts2I = tI(ts2)
ts3I = tI(ts3)
ts4I = tI(ts4)
ts5I = tI(ts5)
ts6I = tI(ts6)
ts7I = tI(ts7)
ts8I = tI(ts8)
ts9I = tI(ts9)

window.mainloop()
