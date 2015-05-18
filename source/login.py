# -*- coding: utf-8 -*-
import requests
import json
import MySQLdb as db

from settings import *

CARTOLA_EMAIL = settings['cartola']['email']
CARTOLA_PASS = settings['cartola']['pass']
CARTOLA_URL_LOGIN = settings['cartola']['url_login']

MYSQL_HOST = settings['mysql']['host']
MYSQL_USER = settings['mysql']['user']
MYSQL_PASS = settings['mysql']['pass']
MYSQL_DB = settings['mysql']['db']

URL_MERCADO = 'http://cartolafc.globo.com/mercado/filtrar.json?page=%s'


class Cartola(object):

    def __init__(self):
         self.session = requests.session() # Cria uma sessão do requests
         self.url_mercado = URL_MERCADO
         #self.db_con = db.Connect(host=MYSQL_HOST, user=MYSQL_USER,
        #                passwd='613722', db=MYSQL_DB)


    def login(self, email, senha):
        dados = {'login-passaporte':email, 'senha-passaporte':senha,
            'usar-sso':'true', 'botaoacessar':'ENTRAR'}
        self.session.post(CARTOLA_URL_LOGIN, data=dados)


    def get_all_mercado(self):
        self.get_mercado(1)
        self.atletas = map(self.get_mercado, self.pages)


    def get_mercado(self, id):
        url_id = self.url_mercado % str(id)
        mercado = self.session.get(url_id)
        mercado_json = json.loads(mercado.text)
        self.rodada_id = mercado_json['rodada_id']
        self.pages = Cartola.create_all_pages(mercado_json['page'])
        return mercado_json['atleta']


    @staticmethod
    def create_all_pages(page_dict):
        pages = range(int(page_dict['atual']), int(page_dict['total'])+1)
        return pages


class ManagerAtletas(object):

    def __init__(self, json_jogadores):
        self.jogadores = todos_jogadores



class ProcessaJogador(object):

    def __init__(self, pagina_atletas):
     self.all_scouts =  {x: 0 for x in ['FS', 'PE', 'A', 'FT',
                        'FD', 'FF', 'G', 'I', 'PP', 'RB', 'FC',
                        'GC', 'CA', 'CV', 'SG', 'DD', 'DP', 'GS']}

    def checa_rodad_mysql(con, rodada):
        pass #if(rodada in sql)


    def processa_jogador(json):
        scouts = self.all_scouts.copy()
        scouts_rodada = json['scout']
        scouts.update({s['nome']:s['quantidade']} for s in scout_rodada)
        return scouts
