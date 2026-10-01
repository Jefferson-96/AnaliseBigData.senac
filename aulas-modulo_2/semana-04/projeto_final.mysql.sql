USE meu_ecommerce;

CREATE TABLE fator_contribuinte (
    codigo_ocorrencia3 INT,
    fator_nome VARCHAR(100),
    fator_aspecto VARCHAR(100),
    fator_condicionante VARCHAR(100),
    fator_area VARCHAR(100)
);

CREATE TABLE aeronave (
    codigo_ocorrencia2 INT,
    aeronave_matricula VARCHAR(10),
    aeronave_tipo_equipamento VARCHAR(50),
    aeronave_fabricante VARCHAR(100),
    aeronave_modelo VARCHAR(100),
    aeronave_tipo_icao VARCHAR(20),
    aeronave_motor_tipo VARCHAR(50),
    anv_motor_qtd INT,
    anv_motor_descricao_qtd VARCHAR(30),
    aeronave_pmd INT,
    aeronave_assentos INT,
    aeronave_ano_fabricacao INT,
    aeronave_pais_fabricante VARCHAR(50),
    aeronave_pais_registro VARCHAR(50),
    aeronave_voo_origem VARCHAR(150),
    aeronave_voo_destino VARCHAR(150),
    aeronave_fase_operacao VARCHAR(100),
    aeronave_tipo_operacao VARCHAR(50),
    aeronave_nivel_dano VARCHAR(50),
    aeronave_fatalidades_total INT
);

DROP TABLE ocorrencia_tipo;

CREATE TABLE ocorrencia (
    codigo_ocorrencia INT,
    codigo_ocorrencia1 INT,
    codigo_ocorrencia2 INT,
    codigo_ocorrencia3 INT,
    codigo_ocorrencia4 INT,
    ocorrencia_classificacao VARCHAR(50),
    ocorrencia_latitude DECIMAL(10,6),
    ocorrencia_longitude DECIMAL(10,6),
    ocorrencia_cidade VARCHAR(100),
    ocorrencia_uf VARCHAR(2),
    ocorrencia_pais VARCHAR(50),
    ocorrencia_aerodromo VARCHAR(20),
    ocorrencia_dia VARCHAR(10),
    ocorrencia_hora VARCHAR(10),
    investigacao_aeronave_liberada VARCHAR(10),
    investigacao_status VARCHAR(50),
    divulgacao_relatorio_numero VARCHAR(50),
    divulgacao_relatorio_publicado VARCHAR(10),
    divulgacao_dia_publicacao VARCHAR(10),
    total_recomendacoes INT,
    total_aeronaves_envolvidas INT,
    ocorrencia_saida_pista VARCHAR(10)
);

CREATE TABLE ocorrencia_tipo (
    codigo_ocorrencia1 INT,
    ocorrencia_tipo VARCHAR(200),
    taxonomia_tipo_icao VARCHAR(50)
);

CREATE TABLE recomendacao (
    codigo_ocorrencia4 INT,
    recomendacao_numero VARCHAR(50),
    recomendacao_dia_assinatura DATE,
    recomendacao_dia_encaminhamento DATE,
    recomendacao_dia_feedback DATE,
    recomendacao_conteudo TEXT,
    recomendacao_status VARCHAR(50),
    recomendacao_destinatario_sigla VARCHAR(30),
    recomendacao_destinatario VARCHAR(200)
);


SHOW TABLES;

DESCRIBE fator_contribuinte;
