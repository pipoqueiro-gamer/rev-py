while True:
    idade=int(input("digite sua idade:"))
    if idade >=18:
        print(f'{idade} maior idade')
    else:
        print(f'{idade} menor idade ')
    digite=input("digite continuar ou sair:")
    if digite =="sair":
        break
