--ATIVIDADE COMPLEMENTAR A atividade_semana_01.sql

---INSERINDO NOVOS MEMBROS
INSERT INTO membros(membro_id, nome, cargo, genero) VALUES(3, 'João Silva', 'Full Stack', 'M');
INSERT INTO membros(membro_id, nome, cargo, genero) VALUES(4, 'Maria Santos', 'Analista BD', 'F');
INSERT INTO membros(membro_id, nome, cargo, genero) VALUES(5, 'Pedro Oliveira', 'Eng. Software', 'M');
INSERT INTO membros(membro_id, nome, cargo, genero) VALUES(6, 'Ana Costa', 'Adm. de Redes', 'F');
INSERT INTO membros(membro_id, nome, cargo, genero) VALUES(7, 'Carlos Souza', 'Especialista S.I', 'M');


---INSERINDO TAREFAS ATRELADAS AOS NOVOS MEMBROS
INSERT INTO tarefas(tarefa_id, descricao, data_inicio, data_finalizacao, membro_id) VALUES(3, 'Desenvolver novo módulo de login para o sistema.', 20240617, 20240617, 3);
INSERT INTO tarefas(tarefa_id, descricao, data_inicio, data_finalizacao, membro_id) VALUES(4, 'Realizar manutenção preventiva nos servidores.', 20240617, 20240617, 4);
INSERT INTO tarefas(tarefa_id, descricao, data_inicio, data_finalizacao, membro_id) VALUES(5, 'Criar documentação técnica do projeto XYZ.', 20240617, 20240617, 5);
INSERT INTO tarefas(tarefa_id, descricao, data_inicio, data_finalizacao, membro_id) VALUES(6, 'Testar e validar integração com API externa.', 20240617, 20240617, 6);
INSERT INTO tarefas(tarefa_id, descricao, data_inicio, data_finalizacao, membro_id) VALUES(7, 'Implementar melhorias na interface do usuário.', 20240617, 20240617, 7);

---CONSULTANDO NA JUNÇÃO DAS TABELAS MEMBROS E ATIVIDADES, APENAS OS MEMBROS DO SEXO FEMININO: SEU NOME, DESCRICAO DA ATIVIDADE, INICIO E FIM DA ATIVIDADE
SELECT membros.nome, tarefas.descricao FROM membros INNER JOIN tarefas ON membros.membro_id=tarefas.membro_id WHERE membros.genero = 'F';