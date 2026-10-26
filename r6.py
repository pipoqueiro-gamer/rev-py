#se voce usar monte de if por exemplo se vai cria 50 if se a primeira condição for verdadeira a maquina ira ver se as outras 49 estão certas o elif faz com que iss não aconteça pq o elif ele cria uma outra codinção dentro do if sem precisa a maquina fica pergutando sobre todos os ifs o elif serve para que não aconteça esse tipo de problema que o programa so vai termina o programa quando termina de pergunta todos os if
print("----digite um numero para falar qual dia da semana,(domingo,segunda,terça,quarta,quinta,sexta,sabado)------")
dia=int(input("digite um numero de 1 a 7:"))
if dia==1:
    print("domingo")
elif dia==2:
    print("segunda")   
elif dia==3:
    print("terça") 
elif dia==4:
    print("quarta") 
elif dia==5:
    print("quinta")
elif dia==6:
    print("sexta") 
elif dia==7:
    print("sabado") 
else:
    print("invalido")     