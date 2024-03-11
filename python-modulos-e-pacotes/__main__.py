import modulo_na_raiz
from pacote1 import modulo1_do_pacote1
from pacote2.subpacote1 import modulo1_do_subpacote1
from pacote2.subpacote1.classe1 import Classe1

modulo_na_raiz.funcao_do_modulo_na_raiz()
modulo1_do_pacote1.funcao_do_modulo1_do_pacote1()
modulo1_do_subpacote1.funcao_do_modulo1_do_subpacote1()
print(Classe1.metodo_estatico())
