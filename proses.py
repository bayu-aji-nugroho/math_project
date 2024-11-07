import os
import random




class Proses():
    set = []
    point = 50
    wrongPoint = 0
    def __init__(self,operation):
        self.operation = operation
        
    def _generateSet(self,data:list):
        """berisi soal soal yang diberikan
        Args:
            [list] data [[a,b=0]-> [A,B=0]]
        """
        n = data[0][1]
        for i in range(data[0][0],data[1][0]+1):
            for x in range(10):
                self.set.append([i,n])
                n += 1
                if n == 10:
                    n = 0
                    break
                if data[1] in self.set:
                    break
       
           
        
    def _exercise(self):
        setquestions = random.choice(self.set)
        if self.operation == "+":
            print(f"{setquestions[0]} + {setquestions[1]} = ? ")
            return setquestions[0] + setquestions[1]
        elif self.operation == "-":
            print(f"{setquestions[0]} - {setquestions[1]} = ? ")
            return setquestions[0] - setquestions[1]
        elif self.operation == "*":
            print(f"{setquestions[0]} x {setquestions[1]} = ? ")
            return setquestions[0] * setquestions[1]
        elif self.operation == "/":
            print(f"{setquestions[0]} / {setquestions[1]} = ? ")
            return setquestions[0] / setquestions[1]
        
            

class UserInterface(Proses):
    def __init__(self, operation):
        super().__init__(operation)
        

        
    def mainInThisClass(self):
        while True:
            os.system("cls")
            a = int(input(f"masukan _{self.operation}_ -> _{self.operation}_ : "))
            b = int(input(f"masukan {a}{self.operation}_ -> _{self.operation}_ : "))
            os.system("cls")
            A = int(input(f"masukan {a}{self.operation}{b} -> _{self.operation}_ : "))
            B = int(input(f"masukan {a}{self.operation}{b} -> {A}{self.operation}_ : "))
            os.system("cls")
            print(f"masukan {a}{self.operation}{b} -> {A}{self.operation}{B}")
            print("y/n")
            inp = input(": ")
            #angka pertama awal tidak boleh lebih besar sama dengan dari angka kedua
            if inp == "y":
                if A > a:
                    os.system("cls")
                    self._generateSet([[a,b],[A,B]])
                    break
               
    def generatePrablem(self,jumlah_soal):
        for i in range(jumlah_soal):
            os.system("cls")
            print("="*20)
            print(f"{i}. poin: {self.point}") 
            print("="*20)
            answer = self._exercise()
            your_answer = input("jawaban: ")
            if float(your_answer) == float(answer):
                self.point += 10
                print(answer)
                input()
            else:
                self.point -= 10
                print(answer)
                input()
            if self.point == 0:
                break
    
    def kalah(self):
        os.system("cls")
        print("kamu kalah!")
        print(f"score kamu: {self.point}")
    
    def menang(self):
        os.system("cls")
        print("kamu menang!")
        print(f"score kamu: {self.point}")
        
    def Show(self):
        for i,data in enumerate(self.set):
            if i % 8 == 0:
                print("")
            match self.operation:
                case "+":
                    print(f"{data[0]} {self.operation} {data[1]} = {data[0] + data[1]}\t|", end="")
                case "-":
                    print(f"{data[0]} {self.operation} {data[1]} = {data[0] - data[1]}\t|", end="")
                case "*":
                    print(f"{data[0]} {self.operation} {data[1]} = {data[0] * data[1]}\t|", end="")
                case "/":
                    print(f"{data[0]} {self.operation} {data[1]} = {data[0] / data[1]}\t|", end="")
                case _:
                    print("error")
            
               
                