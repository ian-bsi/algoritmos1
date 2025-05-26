x = 0
numeros = []
while x<10:
    num = int(input("Digite 10 numeros: "))
    numeros.append(num)
    x += 1

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
    