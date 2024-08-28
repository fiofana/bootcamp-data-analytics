import sqlite3

conexao = sqlite3.connect('banco_sql.db') 
cursor = conexao.cursor()

# Tabela de usuários
cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
cursor.execute('ALTER TABLE usuarios ADD COLUMN telefone INT;')

cursor.execute('INSERT INTO usuarios(id, nome, endereco, email, telefone) VALUES (1, "Isadora", "França", "isa@gmail.com", 123456);')
cursor.execute('INSERT INTO usuarios(id, nome, endereco, email, telefone) VALUES (2, "Maria", "Salvador", "maria@gmail.com", 879235);')
cursor.execute('INSERT INTO usuarios(id, nome, endereco, email, telefone) VALUES (3, "José", "Curitiba", "jose@gmail.com", 984123);')
cursor.execute('INSERT INTO usuarios(id, nome, endereco, email, telefone) VALUES (4, "Márcia", "São Paulo", "marcia@gmail.com", 124678);')
cursor.execute('INSERT INTO usuarios(id, nome, endereco, email, telefone) VALUES (8, "Cynthia", "São Paulo", "cynthia@gmail.com", 724524);')

cursor.execute('UPDATE usuarios SET endereco="São Paulo" WHERE nome="José";')

# Tabela de gerentes
cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES (1, "Camila", "Lisboa", "camila@gmail.com");')
cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES (2, "Rodrigo", "Pequim", "rodrigo@gmail.com");')
cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES (3, "Valéria", "São Paulo", "valeria@gmail.com");')
cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES (8, "Cynthia", "São Paulo", "cynthia@gmail.com");')

# Manipulação e visualização
print('Nome dos usuários:')
nome_usuarios = cursor.execute('SELECT nome FROM usuarios ORDER BY nome')
for nome in nome_usuarios:
    print(nome)
print('')

print('Endereços únicos dos usuários a partir do segundo:')
usuarios_por_endereco = cursor.execute('SELECT endereco FROM usuarios GROUP BY endereco HAVING id>1')
for usuario_dados in usuarios_por_endereco:
    print(usuario_dados)
print('')

print('Dados dos gerentes que são usuários:')
dados_gerentes_usuarios = cursor.execute('SELECT * FROM usuarios INNER JOIN gerentes ON usuarios.nome = gerentes.nome')
for gerente_usuario in dados_gerentes_usuarios:
    print(gerente_usuario)
print('')

print('Dados dos usuários, adicionando informações sobre gerentes:')
dados_usuarios_expandido = cursor.execute('SELECT * FROM usuarios LEFT JOIN gerentes ON usuarios.nome = gerentes.nome')
for usuario in dados_usuarios_expandido:
    print(usuario)
print('')

print('Dados dos gerentes, adicionando informações sobre usuários:')
dados_gerentes_expandido = cursor.execute('SELECT * FROM usuarios RIGHT JOIN gerentes ON usuarios.nome = gerentes.nome')
for gerente in dados_gerentes_expandido:
    print(gerente)
print('')

print('Dados dos usuários e gerentes:')
dados_expandido = cursor.execute('SELECT * FROM usuarios FULL JOIN gerentes ON usuarios.nome = gerentes.nome')
for pessoa in dados_expandido:
    print(pessoa)
print('')

print('Dados dos usuários que moram no mesmo endereço que algum dos gerentes:')
usuarios_local_gerentes = cursor.execute('SELECT * FROM usuarios WHERE endereco IN (SELECT endereco FROM gerentes);')
for usuario in usuarios_local_gerentes:
    print(usuario)

conexao.commit() 
conexao.close