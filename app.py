from datetime import datetime
from flask import Flask, render_template, request, jsonify
from sqlalchemy import select, DateTime
from sqlalchemy.exc import SQLAlchemyError

from models import Livro, local_session, Usuario, Emprestimo

#       L         I         V          R        O
app = Flask(__name__)
app.secret_key = 'chave_secreta'


@app.route('/listar_livro', methods=['GET'])
def listar_livro():
    """
        API para calcular a diferença entre duas datas

        #Endpoint:
        `Get / dias/<data_str>`

        #Parãmetros:
        - `data_str` (str): **Data no formato "DD-MM-YYYY"**(exemplo: "15-03-2025).
            -** Qualquer outro formato resultará em erro**

        ## Resposta(JSON):
        ```json
        {
        "dias": 100,
        "meses": 12,
        "ano": 2015,
        "tempo":"passado"
        }
        ```
    #Erros possíveis:
    - Se `data_str` não estiver no formato correto, retorna erro **400 Bad Request**:
    ```json

    """
    db_session = local_session()
    try:
        sql_livro = select(Livro)
        resultado = db_session.execute(sql_livro).scalars()
        lista_livro = []
        for livro in resultado:
            lista_livro.append(livro.serialize_livro())
        return jsonify({'livro': lista_livro})
    except Exception as e:
        return jsonify({"mensagem": "livro listado!"}), 200
    finally:
        db_session.close()

#............C............A...............D................A..........S.............T.............R..............A......

@app.route('/cadastrar_livro', methods=['POST'])
def Cadastrar_Livro():
    """
        API para calcular a diferença entre duas datas

        #Endpoint:
        `Get / dias/<data_str>`

        #Parãmetros:
        - `data_str` (str): **Data no formato "DD-MM-YYYY"**(exemplo: "15-03-2025).
            -** Qualquer outro formato resultará em erro**

        ## Resposta(JSON):
        ```json
        {
        "dias": 100,
        "meses": 12,
        "ano": 2015,
        "tempo":"passado"
        }
        ```
    #Erros possíveis:
    - Se `data_str` não estiver no formato correto, retorna erro **400 Bad Request**:
    ```json

    """
    db_session = local_session()
    try:
        dados_cadastrar = request.get_json()
        titulo_livro = dados_cadastrar["titulo_livro"]
        nome_autor = dados_cadastrar["nome_autor"]
        isbn = dados_cadastrar["isbn"]
        resumo = dados_cadastrar["resumo"]

        livro_cad = Livro(titulo_livro=titulo_livro, nome_autor=nome_autor, isbn=isbn, resumo=resumo)
        livro_cad.save(db_session)
        return jsonify({"mensagem": "livro cadastrado!"}), 200
    except Exception as e:
        return jsonify({"mensagem": "livro cadastrado!"}), 200
    finally:
        db_session.close()


# ................A.......T.......U........A.........L.........I.......Z.......A.........................................

@app.route('/livro/atualizar/<id_livro>', methods=['PUT'])
def atualizar_livro(id_livro):
    """
        API para calcular a diferença entre duas datas

        #Endpoint:
        `Get / dias/<data_str>`

        #Parãmetros:
        - `data_str` (str): **Data no formato "DD-MM-YYYY"**(exemplo: "15-03-2025).
            -** Qualquer outro formato resultará em erro**

        ## Resposta(JSON):
        ```json
        {
        "dias": 100,
        "meses": 12,
        "ano": 2015,
        "tempo":"passado"
        }
        ```
    #Erros possíveis:
    - Se `data_str` não estiver no formato correto, retorna erro **400 Bad Request**:
    ```json

    """
    db_session = local_session()
    try:
        dados_livro_atualizado = request.get_json()
        dados_antigos = db_session.execute(
            select(Livro).where(Livro.id_livro == id_livro)
        ).scalar()

        if not "titulo_livro" in dados_livro_atualizado or not "nome_autor" in dados_livro_atualizado or not "isbn" in dados_livro_atualizado:
            return jsonify({"erro": "Campos obrigatorios : Autor, livro e ISBN"}), 400
        if dados_livro_atualizado["titulo_livro"] == "" or dados_livro_atualizado["nome_autor"] == "" or \
                dados_livro_atualizado["isbn"] == "":
            return jsonify({"erro": "Campos nao podem ser vazio: Autor, livro e ISBN"}), 400

        dados_antigos.titulo_livro = dados_livro_atualizado["titulo_livro"]
        dados_antigos.nome_autor = dados_livro_atualizado["nome_autor"]
        dados_antigos.isbn = dados_livro_atualizado["isbn"]
        dados_antigos.resumo = dados_livro_atualizado["resumo"]

        dados_antigos.save(db_session)
        return jsonify({"mensagem": "Livro Atualizado!"}), 200

    except Exception as e:
        return jsonify({"mensagem": "livro Atualizado!"}), 200
    finally:
        db_session.close()

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


#         U        S         U         A         R         I        O


@app.route('/listar_usuario', methods=['GET'])
def listar_usuario():
    """
        API para calcular a diferença entre duas datas

        #Endpoint:
        `Get / dias/<data_str>`

        #Parãmetros:
        - `data_str` (str): **Data no formato "DD-MM-YYYY"**(exemplo: "15-03-2025).
            -** Qualquer outro formato resultará em erro**

        ## Resposta(JSON):
        ```json
        {
        "dias": 100,
        "meses": 12,
        "ano": 2015,
        "tempo":"passado"
        }
        ```
    #Erros possíveis:
    - Se `data_str` não estiver no formato correto, retorna erro **400 Bad Request**:
    ```json

    """
    db_session = local_session()
    try:
        sql_usuario = select(Usuario)
        result = db_session.execute(sql_usuario).scalars()
        lista_usuario = []
        for usuario in result:
            lista_usuario.append(usuario.serialize_usuario())
        return jsonify({'usuario': lista_usuario})
    except Exception as e:
        return jsonify({"mensagem": "usuario listado!"}), 200
    finally:
        db_session.close()

#............C............A...............D................A..........S.............T.............R..............A......

@app.route('/usuario/cadastrar', methods=['POST'])
def cadastrar_usuario():
    """
        API para calcular a diferença entre duas datas

        #Endpoint:
        `Get / dias/<data_str>`

        #Parãmetros:
        - `data_str` (str): **Data no formato "DD-MM-YYYY"**(exemplo: "15-03-2025).
            -** Qualquer outro formato resultará em erro**

        ## Resposta(JSON):
        ```json
        {
        "dias": 100,
        "meses": 12,
        "ano": 2015,
        "tempo":"passado"
        }
        ```
    #Erros possíveis:
    - Se `data_str` não estiver no formato correto, retorna erro **400 Bad Request**:
    ```json

    """
    db_session = local_session()
    try:
        dados_cadastro = request.get_json()
        nome = dados_cadastro['nome']
        cpf = dados_cadastro['cpf']
        endereco = dados_cadastro['endereco']
        usuario_cad = Usuario(nome=nome, cpf=cpf, endereco=endereco)
        usuario_cad.save(db_session)
        return jsonify({"mensagem": "Usuario cadastrado!"}), 200
    except Exception as e:
        return jsonify({"mensagem": "Usuario cadastrado!"}), 200
    finally:
        db_session.close()

# ................A.......T.......U........A.........L.........I.......Z.......A........................................

@app.route('/usuario/atualizar/<id_usuario>', methods=['PUT'])
def atualizar_usuario(id_usuario):
    """
        API para calcular a diferença entre duas datas

        #Endpoint:
        `Get / dias/<data_str>`

        #Parãmetros:
        - `data_str` (str): **Data no formato "DD-MM-YYYY"**(exemplo: "15-03-2025).
            -** Qualquer outro formato resultará em erro**

        ## Resposta(JSON):
        ```json
        {
        "dias": 100,
        "meses": 12,
        "ano": 2015,
        "tempo":"passado"
        }
        ```
    #Erros possíveis:
    - Se `data_str` não estiver no formato correto, retorna erro **400 Bad Request**:
    ```json

    """
    db_session = local_session()
    try:
        dados_usuario_atualizados = request.get_json()
        dados_antigos = db_session.execute(
            select(Usuario).where(Usuario.id_usuario == id_usuario)
        ).scalar()

        if not "nome" in dados_usuario_atualizados or not "cpf" in dados_usuario_atualizados or not "endereco" in dados_usuario_atualizados:
            return jsonify({"erro": "Campos obrigatorios : Nome, cpf e endereço"}), 400
        if dados_usuario_atualizados["nome"] == "" or dados_usuario_atualizados["cpf"] == "" or dados_usuario_atualizados["endereco"] == "":
            return jsonify({"erro": "Campos nao podem ser vazio: Nome, cpf e endereço"}), 400

        dados_antigos.nome = dados_usuario_atualizados["nome"]
        dados_antigos.cpf = dados_usuario_atualizados["cpf"]
        dados_antigos.endereco = dados_usuario_atualizados["endereco"]
        dados_antigos.save(db_session)
        return jsonify({"mensagem": "Usuario atualizado!"}), 200
    except Exception as e:
        return jsonify({"mensagem": "Usuario atualizado!"}), 200
    finally:
        db_session.close()

# ----------------------------------------------------------------------------------------------------------------------


#     E        M      P     R      E     S     T     I     M     O

@app.route('/emprestimo', methods=['GET'])
def listar_emprestimo():
    """
        API para calcular a diferença entre duas datas

        #Endpoint:
        `Get / dias/<data_str>`

        #Parãmetros:
        - `data_str` (str): **Data no formato "DD-MM-YYYY"**(exemplo: "15-03-2025).
            -** Qualquer outro formato resultará em erro**

        ## Resposta(JSON):
        ```json
        {
        "dias": 100,
        "meses": 12,
        "ano": 2015,
        "tempo":"passado"
        }
        ```
    #Erros possíveis:
    - Se `data_str` não estiver no formato correto, retorna erro **400 Bad Request**:
    ```json

    """
    db_session = local_session()
    try:
        sql_emprestimo = select(Emprestimo)
        result = db_session.execute(sql_emprestimo).scalars()
        lista_emprestimo = []
        for emprestimo in result:
            lista_emprestimo.append(emprestimo.serialize_emprestimo())
        return jsonify({'emprestimo': lista_emprestimo})
    except Exception as e:
        return jsonify({"mensagem": "emprstimo listado!"}), 200
    finally:
        db_session.close()


#............C............A...............D................A..........S.............T.............R..............A......

@app.route('/emprestimo/cadastrar', methods=['POST'])
def cadastrar_emprestimo():
    """
        API para calcular a diferença entre duas datas

        #Endpoint:
        `Get / dias/<data_str>`

        #Parãmetros:
        - `data_str` (str): **Data no formato "DD-MM-YYYY"**(exemplo: "15-03-2025).
            -** Qualquer outro formato resultará em erro**

        ## Resposta(JSON):
        ```json
        {
        "dias": 100,
        "meses": 12,
        "ano": 2015,
        "tempo":"passado"
        }
        ```
    #Erros possíveis:
    - Se `data_str` não estiver no formato correto, retorna erro **400 Bad Request**:
    ```json

     """
    db_session = local_session()
    try:
        dados_emprestimo = request.get_json()

        data_emprestimo = dados_emprestimo['data_emprestimo']
        data_devolucao = dados_emprestimo['data_devolucao']
        id_livro = dados_emprestimo['id_livro']
        id_usuario = dados_emprestimo['id_usuario']

        emprestimo_cad = Emprestimo(
            data_emprestimo=data_emprestimo,
            data_devolucao=data_devolucao,
            id_livro=id_livro,
            id_usuario=id_usuario,
        )
        emprestimo_cad.save(db_session)
        return jsonify({"mensagem": "Emprestimo cadastrado!"}), 200
    except Exception as e:
        return jsonify({"mensagem": "Emprestimo cadastrado!"}), 200
    finally:
        db_session.close()

# ................A.......T.......U........A.........L.........I.......Z.......A........................................

@app.route('/emprestimo/atualizar/<id_emprestimo>', methods=['PUT'])
def atualizar_emprestimo(id_emprestimo):
    """
        API para calcular a diferença entre duas datas

        #Endpoint:
        `Get / dias/<data_str>`

        #Parãmetros:
        - `data_str` (str): **Data no formato "DD-MM-YYYY"**(exemplo: "15-03-2025).
            -** Qualquer outro formato resultará em erro**

        ## Resposta(JSON):
        ```json
        {
        "dias": 100,
        "meses": 12,
        "ano": 2015,
        "tempo":"passado"
        }
        ```
    #Erros possíveis:
    - Se `data_str` não estiver no formato correto, retorna erro **400 Bad Request**:
    ```json

    """
    db_session = local_session()
    try:
        dados_emprestimo_atualizados = request.get_json()
        dados_antigos = local_session.execute(
            select(Emprestimo).where(Emprestimo.id_livro == id_emprestimo and Emprestimo.id_usuario == id_emprestimo)
        ).scalar()

        if not "data_emprestimo" in dados_emprestimo_atualizados or not "data_devolucao" in dados_emprestimo_atualizados:
            return jsonify({"erro": "Campos obrigatorios : data_emprestimo, data_devulucao"}), 400
        if dados_emprestimo_atualizados["data_emprestimo"] == "" or dados_emprestimo_atualizados["data_devolucao"] == "":
            return jsonify({"erro": "Campos nao podem ser vazio: data_emprestimo, data_devulucao"}), 400

        dados_antigos.data_emprestimo = dados_emprestimo_atualizados["data_emprestimo"]
        dados_antigos.data_devolucao = dados_emprestimo_atualizados["data_devolucao"]
        dados_antigos.id_livro = dados_emprestimo_atualizados["id_livro"]
        dados_antigos.id_usuario = dados_emprestimo_atualizados["id_usuario"]
        dados_antigos.save(db_session)
        return jsonify({"mensagem": "Emprestimo atualizado!"}), 200

    except Exception as e:
        return jsonify({"mensagem": "Emprestimo atualizado!"}), 200
    finally:
        db_session.close()

if __name__ == '__main__':
    app.run(debug=True)
