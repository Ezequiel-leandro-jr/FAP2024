## CRIANDO E USANDO A BASE DE DADOS ##
CREATE DATABASE startup2;
USE startup2;

## CRIANDO TABELAS ##
CREATE_TABLE membros(
membro_id INT PRIMARY KEY,
nome VARCHAR(20),
cargo VARCHAR(20)
);
CREATE TABLE tarefas(
tarefa_id INT PRIMARY KEY,
descricao VARCHAR(50),
membro_id INT,
FOREIGN KEY (membro_id)  REFERENCES membros(membro_id)
);

## INSERINDO OS VALORES DE NOVOS MEMBROS E TAREFAS NAS COLUNAS DAS RESPECTIVAS TABELAS ##
INSERT INTO membros(membro_id, nome, cargo) VALUES(2,'Paulo','Programador 1');
INSERT INTO tarefas(tarefa_id, descricao, membro_id) VALUES(1, 'Criar classe produto', 1);

## SELECIONANDO COLUNAS DAS TABELAS PARA VISUALIZAÇÃO ##
SELECT nome, cargo FROM membros;
SELECT descricao FROM tarefas;
SELECT * FROM membros; #O ASTERISCO JÁ MOSTRA TODAS COLUNAS DA TABELA SELECIONADA

## VISUALIZANDO UMA JUNÇÃO DAS COLUNAS DAS DUAS COLUNAS ##
SELECT membros.nome, tarefas.descricao FROM membros INNER JOIN tarefas ON membros.membro_id=tarefas.membro_id;

##ALTERANDO TABELAS ##

## ADICIONANDO A COLUNA GÊNERO NA TABELA MEMBROS E A COLUNA data_inicio NA TABELA tarefas ##
ALTER TABLE membros ADD genero CHAR(1);
ALTER TABLE tarefas ADD data_inicio DATE;

## ATUALIZANDO O PRIMEIRO MEMBRO DA TABELA, SEU nome E genero ##
UPDATE membros SET nome = 'André Luiz', genero = 'M' WHERE membro_id = 1;

## EXCLUINDO O SEGUNDO MEMBRO DA TABELA MEMBROS ##
DELETE FROM membros WHERE membro_id = 1;

## CRIAR A COLUNA data_finalizacao NA TABELA tarefas ##
ALTER TABLE tarefas ADD data_finalizacao DATE;

## ATUALIZANDO A data_inicio E data_finalizacao DA TABELA atividades, PARA HOJE ##
UPDATE tarefas SET data_inicio = 20240617, data_finalizacao = 20240617 WHERE tarefa_id = 1;

## INSERINDO NOVO MEMBRO E TAREFA PARA UMA DESENVOLVEDORA FEMININA ##
INSERT INTO membros(membro_id, nome, cargo, genero) VALUES(2, 'Jacque', 'Desenvolvedora Backend', 'F');
INSERT INTO tarefas(tarefa_id, descricao, data_inicio, data_finalizacao) VALUES(2, 'Criar banco de dados', 20240617, 20240617);

## CONSULTANDO A TABELA MEMBROS, ONDE O GENERO SEJA FEMININO ##
SELECT * FROM membros WHERE genero = 'F';
