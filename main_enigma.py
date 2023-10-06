"""main Enigma code"""
class Stock:
    """Stock of hard coded variables"""
    def give_return_discs(self):
        """storing and donating the return_discs"""
        foo_return_disc_list = [
                       [66, 18, 11, 54, 85, 20, 45, 80, 43, 44, 89,  2, 83,
                        40, 41, 16, 15, 73,  0, 84,  5, 74, 31, 88, 72, 61,
                        49, 92, 76, 37, 52, 22, 70, 77, 67, 71, 39, 29, 53,
                        36, 13, 14, 55,  8,  9,  6, 86, 59, 87, 26, 69, 65,
                        30, 38,  3, 42, 90, 82, 94, 47, 62, 25, 60, 64, 63,
                        51,  1, 34, 79, 50, 32, 35, 24, 17, 21, 91, 28, 33,
                        93, 68,  7, 95, 57, 12, 19,  4, 46, 48, 23, 10, 56,
                        75, 27, 78, 58, 81],
                       [59, 55, 71, 31, 43, 36, 84, 44, 54, 58, 53, 41, 75,
                        50, 22, 17, 79, 15, 70, 28, 56, 78, 14, 30, 80, 77,
                        86, 83, 19, 61, 23,  3, 88, 45, 91, 68,  5, 46, 95,
                        72, 92, 11, 73,  4,  7, 33, 37, 57, 94, 67, 13, 93,
                        82, 10,  8,  1, 20, 47,  9,  0, 62, 29, 60, 74, 66,
                        89, 64, 49, 35, 76, 18,  2, 39, 42, 63, 12, 69, 25,
                        21, 16, 24, 90, 52, 27,  6, 87, 26, 85, 32, 65, 81,
                        34, 40, 51, 48, 38],
                       [30, 84,  6, 32, 78, 12,  2, 94, 53, 40, 58, 42,  5,
                        63, 51, 81, 33, 22, 23, 60, 87, 28, 17, 18, 85, 71,
                        47, 86, 21, 69,  0, 62,  3, 16, 92, 89, 90, 74, 77,
                        57,  9, 65, 11, 82, 66, 76, 67, 26, 91, 55, 56, 14,
                        72,  8, 70, 49, 50, 39, 10, 64, 19, 75, 31, 13, 59,
                        41, 44, 46, 83, 29, 54, 25, 52, 79, 37, 61, 45, 38,
                         4, 73, 95, 15, 43, 68,  1, 24, 27, 20, 93, 35, 36,
                        48, 34, 88,  7, 80]
                        ]
        return foo_return_disc_list
    def give_transport_discs(self):
        """storing and donating the transport_discs"""
        foo_transport_disc_list = [
                       [50, 40, 56, 47, 62, 61, 83,  4, 37, 80, 15, 12, 63,
                        59,  9, 64,  8, 71, 39, 82, 88, 86, 75, 79,  6, 27,
                        30, 73, 48,  5, 33, 68, 93, 52, 19, 25, 94, 29, 69,
                        41, 76, 87, 22, 77, 55, 14,  2, 46, 13, 95, 78, 42,
                        18, 10, 91, 31,  3, 54, 81, 89, 24, 84, 70, 58, 53,
                        44, 43, 49, 35,  1, 45, 26, 92,  0, 23, 51, 57, 28,
                        66, 67, 72, 36, 65, 90, 21, 17, 11, 38, 60, 34,  7,
                        16, 74, 32, 20, 85],
                       [67,  6,  7, 14, 94, 93, 15, 77, 42, 56, 83, 28, 21,
                        36, 89,  4, 41, 63, 58, 62, 60, 91, 79, 87, 82, 61,
                        19, 70,  2, 95, 90, 22, 26, 84, 80, 88, 23,  3,  5,
                        78, 16, 85, 37, 57, 65, 71, 50, 66, 46, 27, 52, 86,
                        25, 68, 20,  0, 74, 35, 73, 10, 49, 75, 72,  1, 51,
                        17,  9, 45, 33, 11, 54, 34, 92, 29, 48, 12, 31, 13,
                        59, 44, 64, 32, 24, 76, 47, 53, 18, 69,  8, 81, 38,
                        55, 30, 43, 40, 39],
                       [29, 78, 44, 48, 40, 38, 55, 81, 54, 83, 75, 14, 15,
                         5, 93, 24, 67, 41,  8, 43,  9, 18, 27, 62, 53, 77,
                        21, 94, 34, 51,  1, 33, 37, 56, 22, 69, 88, 23, 20,
                        74, 13,  0, 72, 28, 76,  6, 64, 19, 47, 82, 60, 17,
                        70, 91, 59, 89, 30, 61,  3,  2, 35, 66,  7, 92, 16,
                        57, 39, 46, 68, 12, 31, 45, 49, 52, 26, 65, 63, 36,
                        80, 42, 50, 32, 86, 84, 71,  4, 73, 10, 85, 87, 95,
                        58, 90, 25, 79, 11],
                       [14,  7, 34, 88, 57, 29, 90, 71, 44, 85, 62, 38, 40,
                        78,  6, 74,  3, 43, 76, 49,  4, 39, 27, 80, 73, 22,
                        54, 84, 41, 91, 86, 24, 21, 51, 66, 65, 69,  8, 70,
                        13, 55, 31, 48, 10, 19, 12, 50, 36, 23,  9, 93, 42,
                        95, 61, 59, 83, 58, 20, 94, 63, 46, 68, 77, 89, 87,
                        33, 75, 17, 16, 45, 81,  1, 82, 18, 47, 92, 56, 37,
                        52, 32, 53, 11, 15,  0, 35,  5, 28, 64, 60, 67, 26,
                        30, 25, 72, 2, 79],
                       [61, 15, 40, 88, 70, 38,  1, 59, 28, 72, 19, 31,  2,
                        45, 47, 16, 73, 82, 67,  3, 93, 48, 58, 87, 57, 89,
                        12, 85, 80, 66, 54, 94, 56, 29, 83, 62, 90, 32, 92,
                        37, 76,  5, 17, 52, 20, 41, 84, 74, 53,  7, 63, 91,
                        43,  8, 11, 34, 77, 30, 75, 51, 79, 44, 42, 49, 24,
                        50, 55, 10, 26, 39, 69, 18, 60, 68,  0, 25,  9, 36,
                        64, 86, 65, 13, 71,  4, 21, 14, 95, 33, 22, 35,  6,
                        81, 78, 23, 46, 27],
                       [69, 95, 21, 82, 37, 78, 75, 87, 93, 27, 67, 38, 20,
                        16, 42, 55, 94, 77, 11, 60, 22, 58, 61, 76, 52, 46,
                        12, 32, 57, 34, 81, 68,  2, 35, 73, 48, 29, 51, 79,
                        56,  8,  6, 63, 84, 19, 31, 33, 17, 47,  7, 13, 62,
                        36, 85, 90, 14, 49, 18, 39,  4, 28,  5, 44,  1, 59,
                        65, 91, 70, 72, 86, 71, 54, 23, 45, 88,  9, 24, 15,
                        41, 89, 53, 43, 40,  3, 80, 74, 50, 83, 64, 26, 66,
                         0, 10, 25, 30, 92],
                       [93, 71, 80, 94,  5,  9, 30, 84, 47,  0,  6, 73, 72,
                        33, 86, 38, 10, 74, 51, 23, 39, 83, 25, 78, 36, 14,
                        50, 26, 57, 91, 59, 15, 48, 56, 35, 12, 66, 79, 20,
                        37, 32, 34, 67, 52, 18, 63, 21, 53, 58, 54,  7, 41,
                        62, 68, 76, 55, 43, 22, 19, 77, 65, 29, 89, 17, 11,
                        45, 24, 69, 27, 64, 70, 49, 13, 16,  1,  4, 90,  2,
                        88,  3, 87, 60, 82, 95, 31, 85, 46, 61, 42, 28, 81,
                         8, 75, 92, 40, 44],
                       [10, 42,  9, 19, 13, 54, 76,  2, 50, 39, 33, 59, 62,
                        94, 11, 48, 12,  8, 17, 37, 52, 75, 23, 67, 72,  0,
                        43, 89,  4, 69, 63, 25, 51, 36, 83, 35, 55, 82, 45,
                        73, 18, 21, 41, 91, 38, 32, 20, 27, 47, 29, 81, 65,
                        57,  3, 87, 34, 68, 70, 53, 40,  7, 85, 44, 58, 86,
                        77, 66, 93, 60, 28, 92, 78, 88, 16, 22, 64,  5, 95,
                        15, 74, 46, 49, 61, 14, 84, 79, 80, 56, 31, 24, 90,
                        30, 71,  1,  6, 26],
                       [61, 26, 64, 15, 57, 53, 14, 79, 28, 25, 33, 41, 31,
                        21, 94, 46, 42, 29, 69, 58, 49, 78, 60, 92, 84, 35,
                        22, 40, 39, 20,  1,  0, 34, 55, 11, 89, 48, 24, 44,
                        23, 80, 90, 75, 50, 32, 72, 77, 66, 17, 12, 70, 63,
                        74, 51, 54, 52, 95, 88, 85, 93, 45, 76,  7, 68, 16,
                        87, 81, 82,  9, 86, 38, 18, 37,  8, 62, 10, 36, 73,
                         4,  2, 43, 13, 56, 47, 65,  6, 30, 19, 59, 67, 71,
                        83,  5, 27, 91,  3],
                       [83, 58,  1,  7, 81, 10, 16, 12, 33, 25, 80, 13, 47,
                        59, 93, 49,  2, 35, 63,  5, 78, 26, 68, 36, 15, 86,
                        85, 91, 79, 46,  4, 52, 17, 29, 40, 94, 11, 75, 62,
                        71, 57, 54, 74, 77, 88, 72,  9, 87, 64, 19, 22, 48,
                        39, 53, 69, 66, 31, 89, 14, 61, 70, 84, 45, 32, 20,
                        51, 67, 24, 44, 90, 21, 38, 82, 42, 30, 73,  3, 18,
                        50,  6, 37, 34, 56, 60,  0, 76, 41, 23, 55, 27, 43,
                        65, 95,  8, 28, 92]
                        ]
        return foo_transport_disc_list
    def give_caracters(self):
        """storing and donating the caracters"""
        foo_caracters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "ß",
                         "q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "ü",
                         "+", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ö",
                         "ä", "\n", "<", "y", "x", "c", "v", "b", "n", "m", ",",
                         ".", "-", "!", '"', "§", "$", "%", "&", "/", "(", ")",
                         "=", "?", "Q", "W", "E", "R", "T", "Z", "U", "I", "O",
                         "P", "Ü", "*", "A", "S", "D", "F", "G", "H", "J", "K",
                         "L", "Ö", "Ä", "–", ">", "Y", "X", "C", "V", "B", "N",
                         "M", ";", ":", "_", "@", " ", "€", "°", "~"]
        return foo_caracters

class Enigma:
    """creats an Enigma in a spesific configuration"""
    def __init__(self,disc_info,notch_boards,plugboard):
        self.enig_stock = Stock()
        self.enig_characters = self.enig_stock.give_caracters()
        self.enig_libery = Libery()
        self.disc_holder = self.enig_libery.make_holder(disc_info)
        self.disc_info = disc_info
        self.notch_board = notch_boards
        self.plugboard = plugboard
    def convert(self, in_put):
        """encribts or decribts the text""" 
        inputlist = self.enig_libery.string_to_int(in_put,self.enig_characters)
        outputlist = []
        for i in inputlist:
            self.disc_info = self.enig_libery.turner(self.disc_info, self.notch_board)
            if self.plugboard[i] != 96:
                i = self.plugboard[i]
            i = (i+self.disc_info[1][0])%96
            i = self.disc_holder[0][0][i]
            i = (i+self.disc_info[1][1])%96
            i = self.disc_holder[0][1][i]
            i = (i+self.disc_info[1][2])%96
            i = self.disc_holder[0][2][i]
            i = (i+self.disc_info[1][3])%96
            i = self.disc_holder[0][3][i]
            i = (i+self.disc_info[1][4])%96
            i = self.disc_holder[0][4][i]
            i = (i+self.disc_info[1][5])%96
            i = self.disc_holder[0][5][i]
            i = self.disc_holder[1][0][i]
            i = self.disc_holder[2][5][i]
            i = (i-self.disc_info[1][5]+96)%96
            i = self.disc_holder[2][4][i]
            i = (i-self.disc_info[1][4]+96)%96
            i = self.disc_holder[2][3][i]
            i = (i-self.disc_info[1][3]+96)%96
            i = self.disc_holder[2][2][i]
            i = (i-self.disc_info[1][2]+96)%96
            i = self.disc_holder[2][1][i]
            i = (i-self.disc_info[1][1]+96)%96
            i = self.disc_holder[2][0][i]
            i = (i-self.disc_info[1][0]+96)%96
            if self.plugboard[i] != 96:
                i = self.plugboard[i]
            outputlist.append(i)
        out_put = self.enig_libery.int_to_string(outputlist, self.enig_characters)
        return out_put

class Libery:
    """stores most of the important funktiones"""
    def flip_discs (self, disc_holder):
        """filpes the discs so that they can be used in the way back"""
        counter_1=0
        while counter_1 < 6:
            normal_disc = disc_holder[0][counter_1]
            fliped_disc = []
            wanted = 0
            while wanted < 96:
                counter_2 = 0
                while counter_2 < 96:
                    if wanted == normal_disc[counter_2]:
                        fliped_disc.append(counter_2)
                        break
                    counter_2 = counter_2 + 1
                wanted = wanted + 1
            disc_holder[2][counter_1] = fliped_disc
            counter_1=counter_1+1
        return disc_holder

    def flip_disc_control (self):
        """checks if the flipdisc were flipt correctly"""
        # counter_1=0

        # while counter_1 < 10:
        #     print(f'lengt of transportdisc {counter_1} = {len(my_transport_discs[counter_1])}')
        #     print(f'lengt of flipdisc {counter_1} = {len(my_fliped_discs[counter_1])}')
        #     counter_2=0
        #     while counter_2<96:
        #         number_1=my_transport_discs[counter_1][counter_2]
        #         number_2=my_fliped_discs[counter_1][number_1]
        #         if number_2 != counter_2:
        #             print(f'fucked by flipdisc {counter_1} in the {number_1} position')
        #             quit()
        #         counter_2=counter_2+1
        #     counter_1=counter_1+1

    def notch_maker(self, notch_numers):
        """converts the notch_numbers into a list of Booleans"""

        counter = 0
        foo_notch_boards = []
        while counter < 5:
            counter_1 = 95
            notch_number = notch_numers[counter]
            notchboard = []
            while counter_1 >= 0:
                if notch_number >= 2**counter_1:
                    notchboard.append(True)
                    notch_number = notch_number - 2**counter_1
                    counter_1 = counter_1-1
                else:
                    notchboard.append(False)
                    counter_1 = counter_1-1
            counter = counter +1
            foo_notch_boards.append(notchboard)
        return foo_notch_boards

    def plugboard_maker(self, pre_plugboard):
        """generates the plugboard as a list out of the pre_plugboard"""
        foo_plugboard=[]
        count=0
        while count < 96:
            count=count+1
            foo_plugboard.append(96)
        for i in pre_plugboard:
            if i[0]==96:
                continue
            if i[1]==96:
                continue
            foo_plugboard[i[0]]=i[1]
            foo_plugboard[i[1]]=i[0]
        return foo_plugboard

    def plugboard_checker(self, pre_plugboard):
        "checks if the plugboard in given correctly"
        true_false = True
        checker_list = []
        counter=0
        while counter < 96:
            checker_list.append(False)
            counter = counter +1
        for i in pre_plugboard:
            if i[0] != 96:
                if i[1] == 96:
                    print("if you use the plugboard you have to use both sides")
                    true_false=False
                    break
                if checker_list[i[0]] is False:
                    checker_list[i[0]] = i[0]
                else:
                    print("no number can be used twise")
                    true_false=False
                    break
                if checker_list[i[1]] is False:
                    checker_list[i[1]] = i[1]
                else:
                    print("no number can be used twise")
                    true_false=False
                    break
            if i[1] != 96:
                if i[0] == 96:
                    print("if you use the plugboard you have to use both sides")
                    true_false=False
                    break

        return true_false

    def make_holder(self, disc_info):
        """creates the disc_holder"""
        foo_disc_holder = [[0,0,0,0,0,0],[0],[0,0,0,0,0,0]]
        foo_stock = Stock()
        foo_libery = Libery()
        foo_transport_discs = foo_stock.give_transport_discs()
        foo_return_discs = foo_stock.give_return_discs()
        disc_order = [0,0,0,0,0,0]
        count=0
        while count<6:
            disc_order[count]=round((disc_info[0]/(100_000/(10**count)))-0.49)
            disc_info[0]=(disc_info[0]-(disc_order[count]*(100_000/(10**count))))
            foo_disc_holder[0][count]=foo_transport_discs[disc_order[count]]
            count=count+1
        foo_disc_holder[1][0] = foo_return_discs[disc_info[2]]
        foo_disc_holder = foo_libery.flip_discs(foo_disc_holder)
        return foo_disc_holder

    def string_to_int(self,starttext,characters):
        """converts the starttext into the startlist """
        foo_startlist = []
        for i in starttext:
            true_false = True
            counter = 0
            while true_false:
                if i == characters[counter]:
                    foo_startlist.append(counter)
                    true_false = False
                else:
                    counter = counter+1
                if counter == 96:
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",i,
                          "is not in the characters"
                          "pleas removed ove replace it"
                          " with of of this",characters)
                    quit()
        return foo_startlist

    def int_to_string(self,endlist,characters):
        """converts the endlist into the endtext"""
        endtext = ""
        for i in endlist:
            foo_character = characters[i]
            endtext = endtext + foo_character
        return endtext

    def turner(self, disc_info, notch_board):
        """turnes the discs"""
        disc_info[1][0]=(disc_info[1][0]+1)%96
        counter = 0
        while counter < 5:
            if notch_board[counter][disc_info[1][counter]]:
                disc_info[1][counter+1]=(disc_info[1][counter+1]+1)%96
            counter = counter+1
        return disc_info

my_stock = Stock()

my_libery=Libery()
# Plugboard (P) constands
P_0A=96
P_1A=96
P_2A=96
P_3A=96
P_4A=96
P_5A=96
P_6A=96
P_7A=96
P_8A=96
P_9A=96
P_0B=96
P_1B=96
P_2B=96
P_3B=96
P_4B=96
P_5B=96
P_6B=96
P_7B=96
P_8B=96
P_9B=96
jumper2 = 1
jumper3 = 1
jumper4 = 1
jumper5 = 1
jumper6 = 1

while 1==1:
    my_discs_info = [123456,[91,5,0,4,8,0],2,94]
    notch_nums = [jumper2,jumper3,jumper4,jumper5,jumper6]
    my_notch_boards = my_libery.notch_maker(notch_nums)


    my_pre_plugboard=[(P_0A,P_0B),(P_1A,P_1B),(P_2A,P_2B),(P_3A,P_3B),(P_4A,P_4B),
                    (P_5A,P_5B),(P_6A,P_6B),(P_7A,P_7B),(P_8A,P_8B),(P_9A,P_9B)]


    my_libery.plugboard_checker(my_pre_plugboard)
    my_plugboard = my_libery.plugboard_maker(my_pre_plugboard)

    my_enigma = Enigma(my_discs_info,my_notch_boards,my_plugboard)
    Starttext=input("Enter Text:")
    converted_text = my_enigma.convert(Starttext)
    print(converted_text)
