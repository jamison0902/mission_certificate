"""
Created: 03/09/2022 11:54
@author: jamison.queiroz
Size: 5,39 kB
Type: Python
"""
#----------------------------------------------------------------------------------------------------------------------
# Classe de conexão com SQLite
#----------------------------------------------------------------------------------------------------------------------
import sqlite3

class AppBD:
    def __init__(self):
        print("Método Construtor")

    def abrirConexao(self):
        try:
            self.connection = sqlite3.connect('banco_scf.db')
        except(Exception, sqlite3.Error) as error:
            if(self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)
#----------------------------------------------------------------------------------------------------------------------
# Selecionar todos os produtos
#----------------------------------------------------------------------------------------------------------------------
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_select_query = "SELECT * FROM tecnico ORDER BY id"
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()

        except (Exception, sqlite3.Error) as error:
            print("Falha ao selecionar técnicos", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
            return registros
#----------------------------------------------------------------------------------------------------------------------
# Inserir produto
#----------------------------------------------------------------------------------------------------------------------
    def inserirDados(self, nome, cpf, celular, turno, equipe, tipo_user, login, senha):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_insert_query = "INSERT INTO tecnico(nome,cpf,celular,turno,equipe,tipo_user,login,senha) " \
                               "VALUES (:nome,:cpf,:celular,:turno,:equipe,:tipo_user,:login,:senha)"
            record_to_insert = {'nome':nome, 'cpf':cpf, 'celular':celular, 'turno':turno,
                                'equipe':equipe, 'tipo_user':tipo_user, 'login':login, 'senha':senha}
            cursor.execute(sql_insert_query, record_to_insert)
            self.connection.commit()

        except (Exception, sqlite3.Error) as error:
            print("Falha ao inserir produto na tabela", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
#----------------------------------------------------------------------------------------------------------------------
# Atualizar produto
#----------------------------------------------------------------------------------------------------------------------
    def atualizarDados(self, codigo, nome, cpf, celular, turno, equipe, tipo_user, login, senha):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_update_query = "UPDATE tecnico SET nome=:nome,cpf=:cpf,celular=:celular,turno=:turno,equipe=:equipe" \
                               ",tipo_user=:tipo_user,login=:login,senha=:senha WHERE id=:id"
            cursor.execute(sql_update_query, {'nome':nome, 'cpf':cpf, 'celular':celular, 'turno':turno,
                                'equipe':equipe, 'tipo_user':tipo_user, 'login':login, 'senha':senha, 'id':codigo})
            self.connection.commit()
        except (Exception, sqlite3.Error) as error:
            print("Falha ao Atualizar", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
#----------------------------------------------------------------------------------------------------------------------
# Excluir produto
#----------------------------------------------------------------------------------------------------------------------
    def excluirDados(self, id):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_delete_query = "DELETE FROM tecnico WHERE id=:id"
            cursor.execute(sql_delete_query, {'id':id})
            self.connection.commit()
        except (Exception, sqlite3.Error) as error:
            print("Falha ao Excluir", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()


