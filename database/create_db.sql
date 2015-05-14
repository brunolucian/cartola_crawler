CREATE DATABASE cartola;
USE cartola;
CREATE TABLE info_jogador(
    rodada INT,
    apelido CHAR(30),
    clube CHAR(30), # outro json
    foto CHAR(160),
    id INT ,
    media DOUBLE,
    partida_clube_casa CHAR(30), # outro json
    partida_clube_visitante CHAR(30), # outro json
    partida_data CHAR(30),
    pontos DOUBLE,
    pontuacao_acumulada DOUBLE,
    posicao CHAR(30), # outro json,
    preco DOUBLE,
    scout_FS INT,
    scout_PE INT,
    scout_A INT,
    scout_FT INT,
    scout_FD INT,
    scout_FF INT,
    scout_G INT,
    scout_I INT,
    scout_PP INT,
    scout_RB INT,
    scout_FC INT,
    scout_GC INT,
    scout_CA INT,
    scout_CV INT,
    scout_SG INT,
    scout_DD INT,
    scout_DP INT,
    scout_GS INT,
    status CHAR(30),
    status_id INT,
    variacao DOUBLE,
    jogos INT );
