# Definição de funções CRUD
def create():
    raise NotImplementedError("")

def read():
    raise NotImplementedError("")

def update():
    raise NotImplementedError("")

def delete():
    raise NotImplementedError("")


# Programa principal
# Menu interativo
while True:

    print('Selecione qual operação deseja realizar?')
    print('1 - Create;')
    print('2 - Read;')
    print('3 - Update;')
    print('4 - Delete')
    print('5 - Finalizar')
    opcao = str(input())

    match opcao:
        case '1':
            create()
        case '2':
            read()
        case '3':
            update()
        case '4':
            delete()
        case '5':
            break
        case _:
            print('Opção inválida.')


