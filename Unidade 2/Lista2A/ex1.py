comando = ' '

with open('ex1.txt', 'w') as f:
    while comando != 'sair':  # comando para sair do loop é digitar 'sair'
        comando = input('>')
        f.write(comando + '\n')
    f.close()

# open and read the file after the appending:
f = open("ex1.txt", "r")
print(f.read())
