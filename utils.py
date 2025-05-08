from sqlalchemy import select
from models import Livro, Usuario,db_session

def livro():
    dados_livro = Livro(titulo_livro=str(input('Titulo livro: ')),
                  nome_autor=str(input('Nome autor: ')),
                  ISBN =str(input('ISBN:')),
                  resumo=str(input('Resumo: ')),
                )
    print(livro)
    dados_livro.save()


def usuario():
    dados_usuario = Usuario(nome=str(input('Nome do usuario: ')),
                      cpf=str(input('CPF: ')),
                      endereco =str(input('Endereço:')),
                )
    print(usuario)
    dados_usuario.save()

