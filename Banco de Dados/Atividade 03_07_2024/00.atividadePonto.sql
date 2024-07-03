CREATE TABLE Estudante (
nome VARCHAR(200),
idade INTEGER,
genero VARCHAR(1),
escolaridade VARCHAR(50),
exp_programacao INTEGER)

INSERT INTO Estudante (nome, idade, genero, escolaridade, exp_programacao) VALUES ("Ezequiel Leandro Jr", 32, "M", "Graduação", 1)
INSERT INTO Estudante (nome, idade, genero, escolaridade, exp_programacao) VALUES ("Jacqueline Navarro", 40, "F", "Graduação", 0)

SELECT * FROM Estudante

SELECT * FROM Estudante WHERE genero = "F"