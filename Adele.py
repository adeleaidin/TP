class C:
    def __init__(self, n, p, m):
        self.n = n
        self.p = p
        self.m = m
class Contacts:
    def __init__(self, bd):
        self.bd = [[],[],[],[],[],[]]
    def __add__(self, other, bd):
        self.bd[0].append(len(self.bd[0])+1)
        fio = c.n.split(" ")
    while len(fio)< 3:
        fio.append(None)
    self.bd[1].append(fio[0])
    self.bd[2].append(fio[1])
    self.bd[3].append(fio[2])
    if c.p != '':
        self.bd[4].append(c.p)
    else:
        self.bd[4].append(None)
    if c.m != '':
        self.bd[5].append(c.m)
    else:
        self.bd[5].append(None)
    def getContact(self, id):
        ans = "ID - " + str(self.bd[0][id])+"\n"
        if self.bd[1][id] != None:
            ans += "ФИО: " + self.bd[1][id]
        if self.bd[2][id] != None:
            ans += " " + self.bd[2][id]
        if self.bd[3][id] != None:
            ans += " " + self.bd[3][id]
        if self.bd[4][id] != None:
            ans += "\n " + "Номер телефона: " + self.bd[4][id]
        else:
            ans += "\n " + "НОмер телефона: " + "-"
        if self.bd[5][id] != None:
            ans += "\n " + "Почта: " + self.bd[5][id] +"\n"
        else:
            ans += "\n " + "Почта: " + "-" +"\n"
        return ans
    def pSearch(self, p):
        if self.bd[4].__contains__(p):
            id = self.bd[4].index(p)
            print(self.getContact(id))
        else:
            print("Ничего не найдено. ")
    def mSearch(self, m):
        if self.bd[5].__contains__(m):
            id = self.bd[5].index(m)
            print(self.getContact(id))
        else:
            print("Ничего не найдено. ")
    def search(self, fio):
        ids =[]
        if fio[0] != None:
            for i in range(len(self.bd[1])):
                if fio[0] == self.bd[1][i]:
                    ids.append(self.bd[0][i] - 1)
        if fio[1] != None:
            if fio[0]!= None:
                for id in ids:
                    if fio[1]!=self.bd[2][id]:
                        ids.remove(id)
        else:
            for i in range(len(self.bd[2])):
                if fio[1]==self.bd[2][i]:
                    ids.append(self.bd[0][i]-1)
        if fio[2] != None:
            if fio[0] != None or fio[1] != None:
                for id in ids:
                    if fio[2]!=self.bd[3][id]:
                        ids.remove(id)
        else:
            for i in range(len(self.bd[3])):
                if fio[2]==self.bd[2][i]:
                    ids.append(self.bd[0][i]-1)
        if len(ids)==0:
            print("Ничего не найдено. ")
        else:
            for id in ids:
                print(self.getContact(id))
    def getWithoutPhoneOrMail(self, numb):
        if numb == 1:
            for i in range(len(self.bd[4])):
                if self.bd[4][i] == None:
                    print(self.getContact(i))
            return
        if numb == 2:
            for i in range(len(self.bd[5])):
                if self.bd[5][i] == None:
                    print(self.getContact(i))
            return
        if numb == 3:
            for i in range(len(self.bd[4])):
                if self.bd[4][i] == None and self.bd[5][i] == None:
                    print(self.getContact(i))
            return

    def change(self, id, c):
        id -= 1
        fio = c.n.split(" ")
        while len(fio) < 3:
            fio.append(None)
        self.bd[1][id] = fio[0]
        self.bd[2][id] = fio[1]
        self.bd[3][id] = fio[2]
        if len(c.p) > 0:
            self.bd[4][id] = c.p
        else:
            self.bd[4][id] = None
        if len(c.m) > 0:
            self.bd[5][id] = c.m
        else:
            self.bd[5][id] = None

    def printAll(self):
        for i in range(len(self.bd[0])):
            print(self.getContact(i))

def printCommands():
    print("Список доступных команд: ")
    print("1 - Вывести все контакты", "2 - Поиск по телефону", "3 - Поиск по почте", "4 - Поиск по ФИО","5 - поиск по отсутствию номера/почты", "6 - Изменение контакта", "7 - остановить программу", sep="\n")

print("Введите название файла ")
fn = input()
f = open(fn, encoding='utf-8')
base = Contacts()
for stroka in f:
    arr = stroka.split(",")
    c = C(arr[0], arr[1].replace(" ", ""), arr[2].replace(" ", "").replace("\n", ""))
    base.__add__(c)
print("База сформирована.")
printCommands()
abc = int(input())
while abc != "akdna@@@kdn":
    if abc == 1:
        base.printAll()
    elif abc == 2:
        print("Введите телефон ")
        p = input()
        base.pSearch(p)
    elif abc == 3:
        print("Введите почту ")
        m = input()
        base.mSearch(m)
    elif abc == 4:
        fio = []
        print("Введите фамилию, либо оставьте пустую строку ")
        f = input()
        if f == '':
            fio.append(None)
        else:
            fio.append(f)
        print("Введите имя, либо оставьте пустую строку ")
        i = input()
        if i == '':
            fio.append(None)
        else:
            fio.append(i)
        print("Введите отчество, либо оставьте пустую строку ")
        o = input()
        if o == '':
            fio.append(None)
        else:
            fio.append(o)
        base.search(fio)
    elif abc == 5:
        print("Введите по чему хотите искать: ", "1 - без номера", "2 - без почты", "3 - без обоих", sep="\n")
        num = int(input())
        base.getWithoutPhoneOrMail(num)
    elif abc== 6:
        print("Введите id контакта, который хотите изменить и новые данные для него", "(в две разные строки)", sep="\n")
        id = int(input())
        q = input().split(",")
        c = Contacts(q[0], q[1].replace(" ", ""), q[2].replace(" ", "").replace("\n", ""))
        base.change(id, c)
    elif abc == 7:
        "Вы закрыли программу"
        break
    print()
    printCommands()
    abc = int(input())
