import os

from proses import UserInterface

class menu():
    name = "unknown"
    op = ""
    
    def login(self):
        print("-"*8,"selamat datang,","-"*8)
        name = input("masukkan nama anda: ")
        os.system("cls")
        print("selamat datang",name)
        self.__opsi()
        
    
    
    def __opsi(self):
        print("1.multiplication\n2.subtraction\n3.addition\n4.division")
        op = input("masukkan _operation_ : ")
        match op:
            case "1":
                self.op= "*"
                self.__ins("multiplication")
            case "2":
                self.op = "-"
                self.__ins("subtraction")
            case "3": 
                self.op = "+"
                self.__ins("addition")
            case "4":
                self.op = "/"
                self.__ins("division")
        
    def __ins(self,text):
        print(f"1.show {text} list\n2.practice")
        a = input(": ")
        if a == "2":
            jumlahSoal = int(input("masukkan jumlah soal: "))
            ui = UserInterface(self.op)
            ui.mainInThisClass()
            ui.generatePrablem(jumlahSoal)
                 

main = menu()
main.login()