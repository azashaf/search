n = int(input("Введите количество утверждений: "))
saga = list()
zap = list()
count = 0
for i in range(n):
    saga.append(input("Утверждение: "))
m = int(input("Введите количество слов: ")) 
for i in range(m):
    zap.append(input("Текст: "))
for x in saga:
    count = 0
    for y in zap:
        if y.lower() in x.lower():
            count += 1
            if count == m:
                print(x)
                count = 0