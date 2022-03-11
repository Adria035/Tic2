from easyinput import read

entrada = read(int)
cadena = str(entrada)
longitud = len(cadena)
sortida=''
for i in range(longitud - 1,-1,-1):
    sortida += cadena[i]
print(sortida)