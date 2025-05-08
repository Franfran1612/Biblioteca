from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, declarative_base

# configurar banco
# criando conexão
engine = create_engine('sqlite:///base_biblioteca(2).sqlite3')
# db_session = scoped_session(sessionmaker(bind=engine))
local_session = sessionmaker(bind=engine)

# base_declarative ela permite q define classe phyton que representa tabela de bancos de dados de
# forma dedeclarativa, sem necessidade de configurar manualmente a relação entre as classes e as tabelas
Base = declarative_base()
# Base.query = db_session.query_property()

# projeto pessoas que tem atividades
# unique: unico
# string tamanho de letras(quantidades de letras)
# indexpara fazer pesquisa
# self: quer dizer ele mesmo


class Livro(Base):
    __tablename__ = 'TAB_LIVRO'
    id_livro = Column(Integer, primary_key=True)
    titulo_livro = Column(String(25), nullable=False, index=True)
    nome_autor = Column(String(25), nullable=False, index=True)
    isbn = Column(String(11), nullable=True, index=True)
    resumo = Column(String(11), nullable=False, index=True)


    # representação classe
    def __repr__(self):
        return '<Livro: {} {} {} {}>'.format(self.titulo_livro, self.nome_autor,
                                             self.isbn,self.resumo, self.id_livro)

    def save(self, db_session):
        try:
            db_session.add(self)
            db_session.commit()
        except SQLAlchemyError as e:
            db_session.rollback()
            raise


    def serialize_livro(self):
        dados_livro = {
            "id_livro": self.id_livro,
            "titulo_livro": self.titulo_livro,
            "nome_autor": self.nome_autor,
            "isbn": self.isbn,
            "resumo": self.resumo
        }
        return dados_livro


class Usuario(Base):
    __tablename__ = 'TAB_USUARIO'
    id_usuario = Column(Integer, primary_key=True)
    nome = Column(String(25), nullable=False, index=True)
    cpf = Column(String(25), nullable=False, index=True, unique=True)
    endereco = Column(String(11), nullable=True, index=True)


    # representação classe
    def __repr__(self):
        return '<Usuario: {} {} {} {}>'.format(self.nome, self.cpf,
                                             self.endereco,self.id_usuario)

    def save(self, db_session):
        try:
            db_session.add(self)
            db_session.commit()
        except SQLAlchemyError as e:
            db_session.rollback()
            raise

    def serialize_usuario(self):
        dados_usuario = {
            "id_usuario": self.id_usuario,
            "nome": self.nome,
            "cpf": self.cpf,
            "endereco": self.endereco
        }
        return dados_usuario

class Emprestimo(Base):
    __tablename__ = 'TAB_EMPRESTIMO'
    id_emprestimo = Column(Integer, primary_key=True)
    data_emprestimo = Column(String(25), nullable=False, index=True)
    data_devolucao = Column(String(25), nullable=False, index=True)
    id_livro = Column(Integer, ForeignKey('TAB_LIVRO.id_livro'))
    livros = relationship('Livro', backref='emprestimo')
    id_usuario = Column(Integer, ForeignKey('TAB_USUARIO.id_usuario'))
    usuarios = relationship('Usuario', backref='emprestimo')


    # representação classe
    def __repr__(self):
        return '<Emprestimo: {} {}>'.format(self.data_emprestimo, self.data_devolucao)

    def save(self, db_session):
        try:
            db_session.add(self)
            db_session.commit()
        except SQLAlchemyError as e:
            db_session.rollback()
            raise

    def serialize_emprestimo(self):
        dados_emprestimo = {
            "id_emprestimo": self.id_emprestimo,
            "data_emprestimo": self.data_emprestimo,
            "data_devolucao": self.data_devolucao,
            "id_livro": self.id_livro,
            "id_usuario": self.id_usuario,

        }
        return dados_emprestimo


# evitar que alguem entre na sua aplicação sem sua autorização
def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()