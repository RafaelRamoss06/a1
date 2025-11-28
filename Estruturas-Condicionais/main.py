idade = int(input("Digite sua idade: ")) # o usuario está declarando o valor da variavel 

if idade < 18: # SE a idade do usuario for menor que 18, ele nao podera ir  
    print("Você não pode ir para o evento, tudo no seu tempo") # imprimindo
elif idade >= 50: # OU, mais velho que 50 anos de idade, ele nao poderá entrar 
    print("Você é velho para o evento") # imprimindo
else: # SE NAO, pode participar do evento. Caso ele tenha entre 18 e 49 anos 
    print("Você pode ir para o evento, aproveite a juventude!") # imprimindo