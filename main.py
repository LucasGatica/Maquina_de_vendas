import menu
from maquina import MaquinaDeVendas


if __name__ == '__main__':

    maquina = MaquinaDeVendas(menu.inicializa())

    menu.mostrar_menu(maquina)



