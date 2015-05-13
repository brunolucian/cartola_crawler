# -*- coding: utf-8 -*-

from source.login import *
from settings import *

if __name__ == "__main__":

    cartola = Cartola()
    cartola.login(CARTOLA_EMAIL, CARTOLA_PASS)
    mercado_pagina = cartola.get_mercado(1)
    #for jogador in mercado_pagina['atleta']
