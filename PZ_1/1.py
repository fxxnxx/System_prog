name = str("Имя:"+input('Введите Имя: '))
fname = str("Фамилия:"+input('Введите Фамилию: '))
old = str("Возраст:"+input('Введите возраст: '))
town = str('Город:'+input('Введите город: '))

F = [name, fname, old, town]
a1 = open("Work.txt", "w", encoding="utf-8")

for item in F:
        a1.write("%s\xa0" % item)

a1.write('\n')
a1.close()
a1 = open("Work.txt", "r", encoding="utf-8")
it = a1.read()

print(it)