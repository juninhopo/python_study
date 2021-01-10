manipulador = open('arquivo.txt','r')
print("\nMétodo read() :\n")
print(manipulador.read())

manipulador.seek(0) #volta para o inicio do arquivo

print("\nMetodo readline() :\n")
print(manipulador.readline())
print(manipulador.readline())

manipulador.seek(0)

print("\nMetodo realines() :\n")
print(manipulador.readlines())

manipulador.close()