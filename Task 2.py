n = int(input("введите количество команд "))
i = 1
s = 1
N = n - 3
f = 1
S = 1
while i < n:
    i = i + 1
    s = s * i
print("Всевозможных распределений по всем местам = " + str(s))
while f < N:
    f = f + 1
    S = S * f
C = s / S
print ("возможных распределений по 3м местам = " + str(C))


