"""
Created: 03/09/2022 11:54
@author: jamison.queiroz
Size: 5,39 kB
Type: Python
"""
#----------------------------------------------------------------------------------------------------------------------
# Classe de conexão com SQLite Tabela reserva
#----------------------------------------------------------------------------------------------------------------------
import sqlite3
from tkinter import messagebox

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
# Selecionar todos as reservas
#----------------------------------------------------------------------------------------------------------------------
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_select_query = "SELECT * FROM reserva ORDER BY id"
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            self.connection.commit()

        except (Exception, sqlite3.Error) as error:
            print("Falha ao selecionar reservas", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
            return registros
#----------------------------------------------------------------------------------------------------------------------
# Inserir reserva
#----------------------------------------------------------------------------------------------------------------------
    def inserirDados(self, ferramenta_id, descricao, data, horar, horad, tecnico_id):
        try:
            if(self.verificaReserva(ferramenta_id, data, horar, horad)):
                self.abrirConexao()
                cursor = self.connection.cursor()
                sql_insert_query = "INSERT INTO reserva(ferramenta_id, descricao, data, horar, horad, tecnico_id) " \
                                   "VALUES (:ferramenta_id, :descricao, :data, :horar, :horad, :tecnico_id)"
                record_to_insert = {'ferramenta_id':ferramenta_id, 'descricao':descricao, 'data':data, 'horar':horar,
                                    'horad':horad, 'tecnico_id':tecnico_id}
                cursor.execute(sql_insert_query, record_to_insert)
                self.connection.commit()
        except (Exception, sqlite3.Error) as error:
            print("Falha ao inserir reserva na tabela", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
#----------------------------------------------------------------------------------------------------------------------
# Atualizar reserva
#----------------------------------------------------------------------------------------------------------------------
    def atualizarDados(self, codigo, ferramenta_id, descricao, data, horar, horad, tecnico_id):
        try:
            if (self.verificaReservaAtualizar(codigo, ferramenta_id, data, horar, horad)):
                self.abrirConexao()
                cursor = self.connection.cursor()
                sql_update_query = "UPDATE reserva SET ferramenta_id=:ferramenta_id, descricao=:descricao, data=:data," \
                                   " horar=:horar, horad=:horad, tecnico_id=:tecnico_id WHERE id=:id"
                cursor.execute(sql_update_query, {'ferramenta_id':ferramenta_id, 'descricao':descricao,'data':data,
                                                  'horar':horar, 'horad':horad, 'tecnico_id':tecnico_id, 'id':codigo})
                self.connection.commit()
        except (Exception, sqlite3.Error) as error:
            print("Falha ao Atualizar", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
#----------------------------------------------------------------------------------------------------------------------
# Excluir reserva
#----------------------------------------------------------------------------------------------------------------------
    def excluirDados(self, id):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_delete_query = "DELETE FROM reserva WHERE id=:id"
            cursor.execute(sql_delete_query, {'id':id})
            self.connection.commit()
        except (Exception, sqlite3.Error) as error:
            print("Falha ao Excluir", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
#----------------------------------------------------------------------------------------------------------------------
# Selecionar ferramenta
#----------------------------------------------------------------------------------------------------------------------
    def comboFerramenta(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_select_query = "SELECT id, descricao FROM ferramenta ORDER BY id"
            cursor.execute(sql_select_query)
            registros = dict(cursor.fetchall())
        except (Exception, sqlite3.Error) as error:
            print("Falha ao selecionar ferramenta", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
            return registros
#----------------------------------------------------------------------------------------------------------------------
# Seleciona Tecnico
#----------------------------------------------------------------------------------------------------------------------
    def comboTecnico(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_select_query = "SELECT id, nome FROM tecnico ORDER BY id"
            cursor.execute(sql_select_query)
            registros = dict(cursor.fetchall())
        except (Exception, sqlite3.Error) as error:
            print("Falha ao selecionar técnicos", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
            return registros
#----------------------------------------------------------------------------------------------------------------------
# Verifica Reserva
#----------------------------------------------------------------------------------------------------------------------
    def verificaReserva(self, ferramenta_id, data, horar, horad):
        try:
            registro = False
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_verifica_query = "SELECT count(*),horar,horad,id FROM reserva WHERE ferramenta_id=:ferramenta_id AND " \
                                 "data=:data AND horar<=:horad AND horad >= :horar"
            cursor.execute(sql_verifica_query, {'ferramenta_id':ferramenta_id, 'data':data, 'horar':horar, 'horad':horad})
            reg_verifica = cursor.fetchone()
            #print(reg_verifica)
            if (int(reg_verifica[0]) == 1):
                messagebox.showinfo(title="Alerta", message="Ferramenta já reservada nesse período e data")
            else:
                query_time = "SELECT tempo FROM ferramenta WHERE descricao=:descricao"
                cursor.execute(query_time, {'descricao':ferramenta_id})
                reg_time = cursor.fetchone()
                #print(reg_time)
                if ((int(horad) - int(horar)) <= int(reg_time[0])):
                    registro = True
                else:
                    messagebox.showinfo(title="Alerta", message=f"O período de utilização da ferramenta é de {reg_time[0]} horas")
            self.connection.commit()
        except (Exception, sqlite3.Error) as error:
            print("Falha ao verificar reserva", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
            return registro
#----------------------------------------------------------------------------------------------------------------------
# Verifica Reserva
#----------------------------------------------------------------------------------------------------------------------
    def verificaReservaAtualizar(self, codigo, ferramenta_id, data, horar, horad):
        try:
            registro = False
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_verifica_query = "SELECT count(*),horar,horad,id FROM reserva WHERE id!=:id AND ferramenta_id=:ferramenta_id " \
                                 "AND data=:data AND horar<=:horad AND horad >= :horar"
            cursor.execute(sql_verifica_query, {'id':codigo, 'ferramenta_id':ferramenta_id, 'data':data, 'horar':horar,
                                                'horad':horad})
            reg_verifica = cursor.fetchone()
            #print(reg_verifica)
            if (int(reg_verifica[0]) == 1):
                messagebox.showinfo(title="Alerta", message="Ferramenta já reservada nesse período e data")
            else:
                query_time = "SELECT tempo FROM ferramenta WHERE descricao=:descricao"
                cursor.execute(query_time, {'descricao':ferramenta_id})
                reg_time = cursor.fetchone()
                #print(reg_time)
                if ((int(horad) - int(horar)) <= int(reg_time[0])):
                    registro = True
                else:
                    messagebox.showinfo(title="Alerta", message=f"O período de utilização da ferramenta é de {reg_time[0]} horas")
            self.connection.commit()
        except (Exception, sqlite3.Error) as error:
            print("Falha ao verificar reserva", error)
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
            return registro


