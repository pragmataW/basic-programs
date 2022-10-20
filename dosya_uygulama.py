import os

class Student:
    passed = 'Hesaplanmadı'
    def __init__(self,number, name, lastName, classRoom, vice = 0, final = 0):
        self.number = number
        self.name = name
        self.lastName = lastName
        self.classRoom = classRoom
        self.vice = vice
        self.final = final
        self.average = (self.vice * 0.4) + (self.final * 0.6)

    def isPass(self):
        passingGrade = int(input("Okulunuzun geçme notunu giriniz... "))
        if self.average >= passingGrade:
            return 'Geçti'
        else:
            return 'Kaldı'

def studentRegistration():
    os.system('cls')
    number = input("Öğrenci numarasını giriniz... ")
    name = input("Öğrenci ismini giriniz... ")
    lastName = input("Öğrenci soyismini giriniz... ")
    classRoom = input("Öğrenci sınıfını giriniz... ")
    vice = int(input("Öğrenci vize notunu giriniz... (belli değilse 0 giriniz.)"))
    final = int(input("Öğrenci final notunu giriniz... (belli değilse 0 giriniz.)"))
    student = Student(number,name, lastName, classRoom, vice, final)
    

    with open("C:\\python\\Notlarım\\11-Dosya İşlemleri\\liste.txt", "a", encoding = 'utf-8') as file:
        file.write(f'{student.number},{student.name},{student.lastName},{student.classRoom},{student.vice},{student.final},{student.average},{student.isPass()}\n')
    os.system('cls')
    print('Öğrenci kaydı başarıyla yapıldı!')

def gradeRegistration():
    os.system('cls')

    numberInput = input('Lütfen notunu değiştirmek istediğiniz öğrencinin numarasını giriniz... ')
    examInput = input(f'Eğer {numberInput} numaralı öğrencinin vize notunu değiştirmek istiyorsanız \'v\', final notunu değiştirmek istiyorsanız \'f\' tuşuna basınız... ')

    file = open("C:\\python\\Notlarım\\11-Dosya İşlemleri\\liste.txt", "r", encoding = 'utf-8')
    i = 0
    while i <= fileLen():
        studentString = file.readline()
        studentArray = studentString.split(',')
        if numberInput in studentArray:
            if examInput == 'v':
                studentArray[4] = int(input('Yeni vize notunu giriniz... '))
            elif examInput == 'f':
                studentArray[5] = int(input('Yeni final notunu giriniz... '))
            break
        else:
            i+=1
    file.close()


    file = open("C:\\python\\Notlarım\\11-Dosya İşlemleri\\liste.txt", "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    for line in lines:
        tmp = line.strip()
        if numberInput in tmp:
            student = tmp

    file = open("C:\\python\\Notlarım\\11-Dosya İşlemleri\\liste.txt", "w", encoding="utf-8")
    for line in lines:
        if line != student+'\n':
            file.write(line)
    file.close

    studentObj = Student(studentArray[0],studentArray[1],studentArray[2],studentArray[3],int(studentArray[4]),int(studentArray[5])) 
    
    file = open("C:\\python\\Notlarım\\11-Dosya İşlemleri\\liste.txt", "a", encoding = 'utf-8')
    file.write(f'{studentObj.number},{studentObj.name},{studentObj.lastName},{studentObj.classRoom},{studentObj.vice},{studentObj.final},{studentObj.average},{studentObj.isPass()}\n')
    file.close()
    os.system('cls')
    print('Notlar başarıyla güncellendi!')

def studentDelete():
    os.system('cls')
    numberInput = input('Silmek istediğiniz öğrencinin numarasını giriniz... ')

    file = open("C:\\python\\Notlarım\\11-Dosya İşlemleri\\liste.txt", "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    for line in lines:
        tmp = line.strip()
        if numberInput in tmp:
            student = tmp

    file = open("C:\\python\\Notlarım\\11-Dosya İşlemleri\\liste.txt", "w", encoding="utf-8")
    for line in lines:
        if line != student+'\n':
            file.write(line)
    file.close
    os.system('cls')
    print('Silme işlemi başarılı')

def showList():
    os.system('cls')
    file = open("C:\\python\\Notlarım\\11-Dosya İşlemleri\\liste.txt", "r", encoding="utf-8")
    print(file.read())
    file.close()

    wait = input('Devam etmek için bir tuşa basınız...')
    os.system('cls')

def fileLen():
    file = open("C:\\python\\Notlarım\\11-Dosya İşlemleri\\liste.txt", "r", encoding="utf-8")
    counter = 0
    content = file.read()
    coList = content.split("\n")
    
    for i in coList:
        if i: 
            counter +=1
    return counter

while True:
    print("1- ÖĞRENCİ KAYIT\n2- NOT GİRİŞİ\n3- ÖĞRENCİ SİL\n4- LİSTE GÖRÜNTÜLE\n0- PROGRAMI KAPAT")
    operation = input("Yapacağınız İşlemi Seçiniz: ")

    if operation == '1':
        studentRegistration()
    elif operation == '2':
        gradeRegistration()
    elif operation == '3':
        studentDelete()
    elif operation == '4':
        showList()
    elif operation == '0': 
        os.system('cls')
        break