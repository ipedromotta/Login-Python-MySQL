from Controller.CriptografiaController import CriptografiaController


class AdminModel:

    @staticmethod
    def consultar_usuarios(conn):
        try:
            query = "SELECT * FROM dados"
            cursor = conn.cursor()
            cursor.execute(query)
            usuarios = cursor.fetchall()

            return usuarios
        except:
            return None

    @staticmethod
    def consultar_usuario(id, conn):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dados WHERE ID =" + str(id))
            usuario = cursor.fetchall()
            
            return usuario
        except:
            return None

    @staticmethod
    def atualizar_usuario(nome, usuario, senha, admin, numero_id, conn):
        try:
            senha_criptografada = CriptografiaController().criptografar(senha)
            if not senha_criptografada:
                return False

            cursor = conn.cursor()
            cursor.execute("UPDATE dados SET NOME = '{}', USUARIO = '{}', SENHA = '{}', BL_ADM = {} WHERE ID = {}".format(
                        nome, usuario, senha_criptografada, admin, numero_id))
            conn.commit()
            return True

        except Exception as ex:
            print(ex)
            return False

    @staticmethod
    def excluir_usuario(id, conn):
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM dados WHERE ID =" + str(id))
            conn.commit()
        except Exception as ex:
            print(f'Erro ao deletar: {ex}')