import psycopg2

connection = psycopg2.connect(user="postgres", password="mestre", host="127.0.0.1", port="5432", database="lista2b")
cursor = connection.cursor()

Limpar_banco = '''drop table livro;
                drop table editora;'''
cursor.execute(Limpar_banco)

sql = '''create table editora (id_editora Integer PRIMARY KEY, nome Varchar(50), CNPJ Varchar(14) NOT NULL);
        create table livro (ISBN Integer, id_editora Integer, titulo Varchar(50), autor varchar(50), PRIMARY KEY (ISBN), FOREIGN KEY(id_editora) REFERENCES editora (id_editora))'''
cursor.execute(sql)
connection.commit()

insert = """insert into editora(id_editora, nome, CNPJ) VALUES (1, 'Viva', '14484827000122');
                insert into editora(id_editora, nome, CNPJ) VALUES (2, 'Letras',  '36043528000195');
                insert into editora(id_editora, nome, CNPJ) VALUES (3, 'Palavras', '76475878000145');
                insert into livro(ISBN, titulo, autor, id_editora) VALUES (12589, 'Fisica', 'Halliday', 1);
                insert into livro(ISBN, titulo, autor, id_editora) VALUES (36987, 'Mecanica', 'Moyses', 2);
                insert into livro(ISBN, titulo, autor, id_editora) VALUES (74589, 'Calculo', 'Diva', 3);
                insert into livro(ISBN, titulo, autor, id_editora) VALUES (32514, 'Integral', 'Stewart', 1);
                """
cursor.execute(insert)
connection.commit()

consulta = """select livro.titulo, livro.autor, editora.nome, editora.id_editora
        from editora
	    inner join livro on editora.id_editora = livro.id_editora"""
cursor.execute(consulta)
connection.commit()
recset = cursor.fetchall()
for rec in recset:
    print (rec)

delete = """DELETE FROM livro 
                                WHERE livro.titulo = 'Integral';"""
cursor.execute(delete)
connection.commit()

update = """UPDATE editora
                            SET nome = 'Exatas'
                            WHERE id_editora = 1"""
cursor.execute(update)
connection.commit()

consulta = """select livro.titulo, livro.autor, editora.nome, editora.id_editora
        from editora
	    inner join livro on editora.id_editora = livro.id_editora"""
cursor.execute(consulta)
connection.commit()
recset = cursor.fetchall()
for rec in recset:
    print (rec)