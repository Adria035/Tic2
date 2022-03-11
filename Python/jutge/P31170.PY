x = int(input())
sortida = ''
for i in range(1, 11):
    r = i*x
    if sortida == '':
        sortida += str(x) + "*" + str(i) + " = " + str(r)
    else:
        sortida += '\n' + str(x) + "*" + str(i) + " = " + str(r)
print(sortida)