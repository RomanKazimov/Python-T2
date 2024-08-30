def choose_process(process):

    def sum(x, y):
        print(x + y)

    def sub(x, y):
        print(x - y)

    def mul(x, y):
        print(x * y)

    def power(x, y):
        print(x ** y)

    
    if process == "TOPLAMA":
        return sum
    elif process == "CIXMA":
        return sub
    elif process == "VURMA":
        return mul
    elif process == "QUVVET":
        return power
    



# while True:
#     process = input("Proses seçin: ")
#     if process == "TOPLAMA" or  process == "ÇIXMA" or process == "VURMA" or process == "QÜVVƏT":
#         break
#     else:
#         print("Duzgun daxil edin")
#         process = input("Proses seçin: ")



process = None
while process not in ("TOPLAMA", "CIXMA", "VURMA", "QUVVET"):
        print ('Prosesi secin (TOPLAMA, CIXMA, VURMA, QUVVET):\n')
        try:
            process = input("Yuxardakilarin birini yazin: ")
        except ValueError:
            print("Duzgun daxil etmediniz")
            



num1 = int(input("Birinci reqemi seçin: "))
num2 = int(input("İkinci reqemi seçin: "))

choose_process(process)(num1, num2)

