x = [1,2,3,4]

for item in x:
    print(item)

for c in "marco":
    if c == "m":
        continue
    print(c)
    if c == "r":
        break

for i in range(10, 12, 2):
    print(i)
#è possibile usare else con i cicli per effettuare operazioni alla fine del ciclo
else:
    print("ciclo for finito")

#range(initialValue, lastValue, passo)

