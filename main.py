from torre import Torre
from config import Config

def move_op(torre1, torre2):
    torre2.empilha(torre1.primeiro())
    torre1.desempilha()

def mover(torre1, torre2):
    if torre2.sem_disco():
        move_op(torre1, torre2)
        return True
    
    elif torre1.sem_disco():
        print('\nA torre selecionada não tem mais discos')
        return False
    
    elif torre1.primeiro().peso_disco() < torre2.primeiro().peso_disco():
        move_op(torre1, torre2)
        return True

    else:
        print('\nOperação invalida')
        config.status_torres(torres)
        return False

def menu(torres, config, numero_movimentos):
    print('### Opções ###')
    print('\nOpção 1 - Mover')
    print('\nOpção 2 - Fechar programa')
    opcao = int(input('\nOpção: '))

    if(opcao == 1):
        torre1 = int(input('Torre de origem: '))
        torre2 = int(input('Torre de destino: '))
        x = mover(torres[torre1], torres[torre2])
        if x:
            config.status_torres(torres)
        
        numero_movimentos += 1
        print('Numero de movimentos: ' + str(numero_movimentos))
        print('')

        menu(torres, config, numero_movimentos)

    elif(opcao == 2):
        exit


if __name__ == '__main__':
    numero_movimentos = 0


    print('#### Torre de Hanoi ####')

    torres = []
    torres.extend([Torre(1), Torre(2), Torre(3)])

    config = Config()

    config.adiciona_discos(torres[0])
    config.status_torres(torres)

    menu(torres, config, numero_movimentos)