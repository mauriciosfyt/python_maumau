#Autor: maumau
# Data: 06/06/2024
# Versão: 1.0
# Descrição:faça um algoritimo que solicite para usuario a senha cadastrada 
#       ao sistema, ele tera no maximo tes tentativas para inseris a senha correta     
#       cadrastada (senai115),caso passe desse limite uyma mensagem de erro deve 
#       aparecer 
# 
# (senai115)
tentativas = 0
max_tentativas = 3
senha_cadastrada = "senai115"

while tentativas < max_tentativas:
    senha_usuario = input("Digite a senha cadastrada: ")
    if senha_usuario == senha_cadastrada:
        print("Senha correta! Bem-vindo ao sistema.")
        break
    else:
        tentativas += 1
        print("Senha incorreta. Você tem tentativas restantes."),max_tentativas - tentativas 
else:
    print("Erro: número máximo de tentativas excedido. Acesso negado.")
    