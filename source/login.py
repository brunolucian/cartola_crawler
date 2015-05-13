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


    def get_mercado(self, id):
        url_id = self.url_mercado % str(id)
        mercado = self.session.get(url_id)
        print mercado.text
        mercado_json = json.loads(mercado.text)
        self.pages = Cartola.create_all_pages(mercado_json['page'])
        return mercado_json


    @staticmethod
    def create_all_pages(page_dict):
        pages = range(int(page_dict['atual']), int(page_dict['total'])+1)
        return pages


    def checa_rodad_mysql(con, rodada):
        pass #if(rodada in sql)


    def processa_jogador(json):
        pass
