CREATE SCHEMA IF NOT EXISTS aula;

CREATE TABLE IF NOT EXISTS aula.alunos_raw (
    id INTEGER,
    nome VARCHAR(150),
    curso VARCHAR(100),
    idade INTEGER,
    email VARCHAR(150),
    nota VARCHAR(20),
    data_carga TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS aula.alunos_tratados (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(150),
    curso VARCHAR(100),
    idade INTEGER,
    email VARCHAR(150),
    nota NUMERIC(5,2),
    status_validacao VARCHAR(20),
    classificacao VARCHAR(20),
    data_processamento TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS aula.alunos_invalidos (
    id INTEGER,
    nome VARCHAR(150),
    curso VARCHAR(100),
    idade INTEGER,
    email VARCHAR(150),
    nota VARCHAR(20),
    motivo_erro VARCHAR(255),
    data_processamento TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO aula.alunos_raw (id, nome, curso, idade, email, nota) VALUES
(1, 'Ana', 'ADS', 20, 'ana@email.com', '8.5'),
(2, 'Carlos', 'Direito', 17, 'carlos@email', '7.0'),
(3, NULL, 'Engenharia', 22, 'maria@email.com', '9.1'),
(4, 'João', 'ADS', 19, 'joao@email.com', 'abc'),
(5, 'Beatriz', 'Medicina', 21, 'bia@email.com', '9.8'),
(6, 'Pedro', 'Agronomia', 18, 'pedro@email.com', '6.4');