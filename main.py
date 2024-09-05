def binario_para_decimal(numero):
    return int(numero, 2)

def octal_para_decimal(numero):
    return int(numero, 8)

def hexadecimal_para_decimal(numero):
    return int(numero, 16)

def decimal_para_binario(numero):
    return bin(numero).replace("0b", "")

def decimal_para_octal(numero):
    return oct(numero).replace("0o", "")

def decimal_para_hexadecimal(numero):
    return hex(numero).replace("0x", "")

def informacoes_do_grupo():
    informacoes = """
    Diogo Kranz de Araújo Corrêa
    """
    print(informacoes)

while True:
    print("\nMenu:")
    print("1) Converter de binário/octal/hexadecimal para decimal")
    print("2) Converter de decimal para binário/octal/hexadecimal")
    print("3) Informações do grupo")
    print("4) Sair")

    opcao = input("Digite uma opção: ")

    if opcao == '1':
        tipo = input("Digite o tipo (2 para binário, 8 para octal, 16 para hexadecimal): ")
        numero = input("Digite o número: ")
        if tipo == '2':
            resultado = binario_para_decimal(numero)
        elif tipo == '8':
            resultado = octal_para_decimal(numero)
        elif tipo == '16':
            resultado = hexadecimal_para_decimal(numero)
        else:
            print("Tipo inválido! Por favor, digite 2, 8 ou 16.")
            continue
        print(f"O resultado é: {resultado}")

    elif opcao == '2':
        numero = int(input("Digite o número decimal: "))
        tipo = input("Digite o tipo (2 para binário, 8 para octal, 16 para hexadecimal): ")
        if tipo == '2':
            resultado = decimal_para_binario(numero)
        elif tipo == '8':
            resultado = decimal_para_octal(numero)
        elif tipo == '16':
            resultado = decimal_para_hexadecimal(numero)
        else:
            print("Tipo inválido! Por favor, digite 2, 8 ou 16.")
            continue
        print(f"O resultado é: {resultado}")

    elif opcao == '3':
        informacoes_do_grupo()

    elif opcao == '4':
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")