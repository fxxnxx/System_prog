import threading
def zp(okl, prem):
        zp1 = okl + prem
        with open('ЗП1.txt', 'w+', encoding='utf-8') as file:
            file.write(f'ЗП с учетом премии: {zp1} рублей\n')
            print(f'ЗП с учетом премии: {zp1} рублей\n')


def zpx(okl, prem, priz):
    zp2 = okl + prem + priz
    with open('ЗП2.txt', 'w+', encoding='utf-8') as file:
        file.write(f'ЗП с учетом премии и призовых: {zp2} рублей\n')
        print(f'ЗП с учетом премии и призовых: {zp2} рублей\n')

def zpy(okl, prem, priz, sht):
    zp3 = okl + prem + priz - sht
    with open('ЗП3.txt', 'w+', encoding='utf-8') as file:
        file.write(f'Полная ЗП с учетом шрафов: {zp3} рублей\n')
        print(f'Полная ЗП с учетом шрафов: {zp3} рублей\n')
with open('Отчетность по ЗП.txt', 'w+', encoding='windows-1251') as fil:
    f1 = open('ЗП1.txt','r')
    f2 = open('ЗП2.txt','r')
    f3 =open('ЗП3.txt','r')
    print( f1.read(), '\n', f2.read(), '\n', f3.read(),'\n', '\n', file=fil)

ev1 = threading.Event()
ev2 = threading.Event()
ev3 = threading.Event()

th1 = threading.Thread(target=zp, args=(10000 , 3500))
th2 = threading.Thread(target=zpx, args=(10000 , 3500, 25000))
th3 = threading.Thread(target=zpy, args=(10000 , 3500, 25000, 5000))

th1.start()
th2.start()
th3.start()


