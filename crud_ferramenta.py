"""
Created: 03/09/2022 11:54
@author: jamison.queiroz
Size: 5,39 kB
Type: Python
"""
#----------------------------------------------------------------------------------------------------------------------
# Classe de conexão com SQLite tabela ferramenta
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
# Selecionar todos os tecnicos
#----------------------------------------------------------------------------------------------------------------------
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_select_query = "SELECT * FROM ferramenta ORDER BY id"
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()

        except (Exception, sqlite3.Error) as error:
            print("Falha ao selecionar ferramentas", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
            return registros
#----------------------------------------------------------------------------------------------------------------------
# Inserir ferramenta
#----------------------------------------------------------------------------------------------------------------------
    def inserirDados(self, descricao, fabricante, voltagem, serial, tamanho, tipo, tempo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_insert_query = "INSERT INTO ferramenta(descricao, fabricante, voltagem, serial, tamanho, tipo, tempo) " \
                               "VALUES (:descricao, :fabricante, :voltagem, :serial, :tamanho, :tipo, :tempo)"
            record_to_insert = {'descricao':descricao, 'fabricante':fabricante, 'voltagem':voltagem, 'serial':serial,
                               'tamanho':tamanho, 'tipo':tipo, 'tempo':tempo}
            cursor.execute(sql_insert_query, record_to_insert)
            self.connection.commit()
        except (Exception, sqlite3.Error) as error:
            print("Falha ao inserir ferramenta na tabela", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
#----------------------------------------------------------------------------------------------------------------------
# Atualizar ferramenta
#----------------------------------------------------------------------------------------------------------------------
    def atualizarDados(self, codigo, descricao, fabricante, voltagem, serial, tamanho, tipo, tempo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_update_query = "UPDATE ferramenta SET descricao=:descricao, fabricante=:fabricante, voltagem=:voltagem, " \
                               "serial=:serial,tamanho=:tamanho, tipo=:tipo, tempo=:tempo WHERE id=:id"
            cursor.execute(sql_update_query, {'descricao':descricao, 'fabricante':fabricante, 'voltagem':voltagem,
                                              'serial':serial,'tamanho':tamanho, 'tipo':tipo, 'tempo':tempo,'id':codigo})
            self.connection.commit()
        except (Exception, sqlite3.Error) as error:
            print("Falha ao Atualizar", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
#----------------------------------------------------------------------------------------------------------------------
# Excluir ferramenta
#----------------------------------------------------------------------------------------------------------------------
    def excluirDados(self, id):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_delete_query = "DELETE FROM ferramenta WHERE id=:id"
            cursor.execute(sql_delete_query, {'id':id})
            self.connection.commit()
        except (Exception, sqlite3.Error) as error:
            print("Falha ao Excluir", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()


