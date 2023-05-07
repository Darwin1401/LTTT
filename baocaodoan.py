from tkinter import *

def variables_input():
    # Nhap tap cac bien, Tap V
    flag = False
    Variables = set() # Tao tap rong
    while flag == False:
        str = input("Nhap vao tap cac bien(V) (phan cach bang dau khoang cach): ") # Nhap vao 1 chuoi
        if str == "":
            print("Khong duoc de tap cac bien(V) rong!")
            a = input("Nhan Y/y de nhap lai tap V: ") #Dung de nhap lai hoac thoat chuong trinh
            if a[0] == "Y" or a[0] == "y":
                continue
            else:
                exit()
        L = str.split() # Tach cac chuoi con theo dau khoang cach luu vao 1 list
        for i in L: # Kiem tra cac chuoi con chi chua 1 ky tu
            if len(i) > 1:
                print("Chi duoc nhap cac ky tu!")
                a = input("Nhan Y/y de nhap lai tap V: ") #Dung de nhap lai hoac thoat chuong trinh
                if a[0] == "Y" or a[0] == "y":
                    flag = False
                    break
                else:
                    exit()
            flag = True
    for i in L: # them cac ky tu vao tap V
        Variables.add(i)
    return Variables

def terminal_input(Variables):
    # Nhap vao cac ky tu ket thuc, tap T
    flag = False
    Terminal = set() # Tao tap rong
    while flag == False:
        str = input("Nhap vao tap cac ky hieu ket thuc(T) (phan cach bang dau khoang cach): ") # Nhap vao 1 chuoi
        if str == "":
            print("Khong duoc de tap cac ky hieu ket thuc(T) rong!")
            a = input("Nhan Y/y de nhap lai tap T: ") #Dung de nhap lai hoac thoat chuong trinh
            if a[0] == "Y" or a[0] == "y":
                continue
            else:
                exit()
        L = str.split() # Tach cac chuoi con theo dau khoang cach luu vao 1 list
        for i in L: # Kiem tra cac chuoi con chi chua 1 ky tu
            if len(i) > 1 or i in Variables:
                if len(i) > 1:
                    print("Chi duoc nhap cac ky tu!")
                else:
                    print("Khong duoc nhap trung ky tu voi tap V!")
                a = input("Nhan Y/y de nhap lai tap T: ") #Dung de nhap lai hoac thoat chuong trinh
                if a[0] == "Y" or a[0] == "y":
                    flag = False
                    break
                else:
                    exit()
            flag = True
    for i in L: # Them cac ky tu vao tap T
        Terminal.add(i)
    return Terminal

def production_input(Variables, Terminal):
    # Nhap vao tap cac luat sinh P
    Production = list() # List luu cac quy tac sinh
    print("Nhap vao cac quy tac sinh theo dinh dang {} -> {}(go stop de dung nhap): ")
    while True:
        while True:
            flag = False
            a = input("Nhap vao luat sinh ben trai(khong duoc nhap dau khoang cach): ") # Nhap vao cac quy tac sinh ben trai
            if a == "stop":
                break
            a = a.replace(" ", "") # Loai bo dau khoang cach
            for i in a:
                if i in Variables:
                    flag = True
                    break
            if not flag: # Kiem tra luat sinh ben trai phai co it nhat 1 ky tu thuoc tap V
                print("Luat sinh phai co it nhat 1 ky tu bien trong tap V!")
                c = input("Nhan Y/y de nhap lai luat sinh nay: ")
                if c[0] == "Y" or c[0] =="y":
                    continue
                else:
                    exit()
            flag = True
            for i in a:
                if i not in Variables.union(Terminal):
                    print("Luat sinh ben trai phai thuoc tap hop (V hop T)*")
                    flag = False
                    break
            if not flag: # Kiem tra luat sinh ben trai phai thuoc tap hop (V hop T)*
                c = input("Nhan Y/y de nhap lai luat sinh nay: ")
                if c[0] == "Y" or c[0] =="y":
                    continue
                else:
                    exit()
            b = input("Nhap vao ket qua sinh ben phai(bo trong neu la epsilon)(khong duoc nhap dau khoang cach)(neu co nhieu ket qua sinh thi cach nhau bang dau khoang cach): ") # Nhap vao cac quy tac sinh ben phai
            if len(b) == 0:
                b = "Epsilon"
                if {a:b} not in Production: # them vao P 1 dictionary
                    Production.append({a:b})
            else:
                b = b.strip().split()
                for str in b:
                    flag = True
                    for i in str:
                        if i not in Variables.union(Terminal):
                            print("Luat sinh ben phai phai thuoc tap hop (V hop T)*")
                            flag = False
                            break
                    if not flag: break
                    else:
                        if {a:str} not in Production:
                            Production.append({a:str})
            if not flag: # Kiem tra luat sinh ben phai phai thuoc tap hop (V hop T)*
                c = input("Nhan Y/y de nhap lai luat sinh nay: ")
                if c[0] == "Y" or c[0] =="y":
                    continue
                else:
                    exit()
        if len(Production) == 0:
            print("Khong duoc de tap luat sinh rong!")
            c = input("Nhan Y/y de nhap lai tap cac luat sinh(P): ")
            if c[0] == "Y" or c[0] == "y":
                continue
            else:
                exit()
        else:
            break
    return Production

def start_input(Variables):
    while True:
        Start = input("Nhap vao ky tu bat dau(S)(chi 1 ky tu thuoc tap V): ") # Nhap vao bien khoi dau
        if Start == "":
            print("Khong duoc de trong ky tu bat dau(S)!")
            a = input("Nhan Y/y de nhap lai tap V: ") #Dung de nhap lai hoac thoat chuong trinh
            if a[0] == "Y" or a[0] == "y":
                continue
            else:
                exit()
        Start = Start[0]
        if Start not in Variables: # Kiem tra S phai thuoc tap V
            print("Ky tu bat dau phai thuoc tap V!")
            a = input("Nhan Y/y de nhap lai ky tu bat dau(S): ") #Dung de nhap lai hoac thoat chuong trinh
            if a[0] == "Y" or a[0] == "y":
                continue
            else:
                exit()
        break
    return Start

def grammar_input():
    print("Nhap vao 1 van pham hinh thuc (Grammar): ")
    Variables = variables_input()
    Terminal = terminal_input(Variables)

    while True:
        Production = production_input(Variables, Terminal)
        Start = start_input(Variables)

        key = list()
        for item in Production:
            for i in item.keys():
                key.append(i)
        if Start not in key: # Kiem tra trong cac quy tac sinh phai co quy tac sinh ra tu bien khoi dau
            print("Luat sinh ben trai phai co ky tu bien khoi dau \"S\"!")
            a = input("Nhan Y/y de nhap lai tap P va S: ")
            if a[0] == "Y" or a[0] == "y":
                continue
            else: exit()

        break
    return Variables, Terminal, Production, Start

def is_valid_grammar(Variables, Terminal, Production, Start):

    if len(Variables) == 0:
        return False

    for character in Variables:
        if len(character) > 1:
            return False
        
    if len(Terminal) == 0:
        return False
        
    for character in Terminal:
        if len(character) > 1:
            return False
    
    for i in Terminal:
        if i in Variables:
            return False
    
    if len(Production) == 0:
        return False

    for item in Production:
        for key in item.keys():
            flag = False
            for i in key:
                if i in Variables:
                    flag = True
                    break
            if not flag: return False
    
    for item in Production:
        for key, value in item.items():
            for i in key:
                if i not in Variables and i not in Terminal:
                    return False
            for i in value:
                if i not in Variables and i not in Terminal:
                    return False
    
    if len(Start) == 0 or Start not in Variables:
        return False
    
    key = list()
    for item in Production:
        for i in item.keys():
            key.append(i)
    if Start not in key: # Kiem tra trong cac quy tac sinh phai co quy tac sinh ra tu bien khoi dau
        return False
    
    return True

def is_CSG(Variables, Terminal, Production, Start): # Kiem tra phai van pham loai 1 khong
    if is_valid_grammar(Variables, Terminal, Production, Start):
        for item in Production:
            for key, value in item.items():
                if value == "Epsilon":
                    value = ""
                if len(value) < len(key):
                    return False
        return True
    else:
        return False

def is_CFG(Variables, Terminal, Production, Start): # Kiem tra phai van pham loai 2 khong
    if is_CSG(Variables, Terminal, Production, Start):
        for item in Production:
            for key in item.keys():
                if len(key) != 1:
                    return False
        return True
    else:
        return False

def is_right_linear_grammar(Variables, Production): # Kiem tra tuyen tinh phai
    for item in Production:
        for value in item.values():
            if value != "Epsilon":
                for i in value:
                    if i in Variables:
                        if value[-1] != i or i in value[:-1]:
                            return False
    return True

def is_left_linear_grammar(Variables, Production): # Kiem tra tuyen tinh trai
    for item in Production:
        for value in item.values():
            if value != "Epsilon":
                for i in value:
                    if i in Variables:
                        if value[0] != i or i in value[1:]:
                            return False
    return True

def is_regular_grammar(Variables, Terminal, Production, Start):
    if is_CFG(Variables, Terminal, Production, Start):
        if(is_left_linear_grammar(Variables, Production) or is_right_linear_grammar(Variables, Production)):
            return True
        else:
            return False
    else:
        return False

def get_regular_grammar_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines() # Doc cac dong cua file

            Variables = set() # Tao set rong luu cac bien
            line = lines[0] # dong dau tien la dong luu cac bien
            line = line.strip().split() # bo ky tu xuong hang va tach theo dau khoang cach
            for character in line: # luu cac ky tu trong line vao tap V
                Variables.add(character)
            
            Terminal = set() # Tuong tu o tren
            line = lines[1]
            line = line.strip().split()
            for character in line:
                Terminal.add(character)

            Production = list()
            for line in lines[2:-1]:
                line = line.strip().split()
                a = line[0]
                for b in line[1:]:
                    if {a:b} not in Production:
                        Production.append({a:b})
            
            Start = lines[-1][0]

            if is_valid_grammar(Variables, Terminal, Production, Start):
                if is_regular_grammar(Variables, Terminal, Production, Start):
                    print("Day la van pham chinh quy")
                    return Variables, Terminal, Production, Start
                else:
                    print("Khong phai la 1 van pham chinh quy!")
                    return set(), set(), list(), ""
            else:
                print("Khong thoa dieu kien cua 1 van pham hinh thuc!")
                return set(), set(), list(), ""
    except FileNotFoundError:
        print("That file was not found!")
        return set(), set(), list(), ""
    
def submit():
    Variables = set()
    str = variables_entry.get()
    if str == "":
        print("Vui long nhap vao tap cac bien!")
    else:
        str = str.strip().split()
        for i in str:
            Variables.add(i)

    Terminal = set()
    str = terminal_entry.get()
    if str == "":
        print("Vui long nhap vao tap cac ky hieu ket thuc!")
    else:
        str = str.strip().split()
        for i in str:
            Terminal.add(i)

    Production = list()
    str = production_text.get("1.0", END)
    if len(str) == 0:
        print("Vui long nhap vao cac quy tac sinh!")
    else:
        str = str.split("\n")
        if "" in str:
            str.remove("")
        for item in str:
            L = item.split("->")
            a = L[0].replace(" ", "")
            B = L[1].split("|")
            for b in B:
                b = b.replace(" ", "")
                if {a:b} not in Production:
                    Production.append({a:b})
        for item in Production:
            for key, value in item.items():
                if value == "":
                    item.update({key:"Epsilon"})

    Start = start_entry.get()
    if Start == "":
        print("Vui long nhap vao ky tu khoi dau!")
    else:
        Start = Start[0]

    if is_regular_grammar(Variables, Terminal, Production, Start):
        print("Day la van pham chinh quy!")
    else:
        print("Day khong phai van pham chinh quy")
    
if __name__ == "__main__":
    # V, T, P, S = grammar_input() # Dung de nhap truc tiep tu Terminal
    # if is_regular_grammar(V, T, P, S):
    #     print("Day la van pham chinh quy")
    # else:
    #     print("Day khong phai van pham chinh quy")
    
    window = Tk() # Dung de nhap tu giao dien GUI
    window.title("Regular Grammar")
    window.geometry("500x500")

    label = Label(window,
                  text="Nhập vào tập các biến(V)(phân cách bằng dấu khoảng cách): ",
                  font=("Times New Roman", 15))
    label.pack()

    variables_entry = Entry(window,
                  font=("Times New Roman", 15))
    variables_entry.pack()

    label = Label(window,
                  text="Nhập vào tập các ký hiệu kết thúc(T)(phân cách bằng dấu khoảng cách): ",
                  font=("Times New Roman", 15))
    label.pack()

    terminal_entry = Entry(window,
                  font=("Times New Roman", 15))
    terminal_entry.pack()

    label = Label(window,
                  text="Nhập vào tập các luật sinh(P) với dạng \"<> -> <> | [<>] ...\" với <> là 1 chuỗi, <> đầu tiên là luật sinh, các <> sau là các kết quả sinh: ",
                  font=("Times New Roman", 15))
    label.pack()

    production_text = Text(window,
                font=("Times New Roman", 15),
                height=10,
                width=25)
    production_text.pack()

    label = Label(window,
                  text="Nhâp vào ký tự bắt đầu(S), chỉ nhận ký tự đầu tiên: ",
                  font=("Times New Roman", 15))
    label.pack()

    start_entry = Entry(window,
                        font=("Times New Roman", 15))
    start_entry.pack()

    submit_button = Button(window,
                           text="Submit",
                           font=("Times New Roman", 15),
                           command=submit)
    submit_button.pack()

    window.mainloop()