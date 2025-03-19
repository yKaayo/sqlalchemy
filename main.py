from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

db = create_engine("sqlite:///database.db", echo=True)

Session = sessionmaker(bind=db)
session = Session()

class Base(DeclarativeBase):
    pass

class Farmacia(Base):
    __tablename__ = 'farmacias'

    cnpj = Column("cnpj", Integer, primary_key=True)
    nome = Column("nome", String(30))
    telefone = Column("telefone", Integer)
    endereco = Column("endereco", String(45))
    
    def __init__(self, cnpj, nome, telefone, endereco):
        self.cnpj = cnpj
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def __repr__(self):
        return f"Farmacia(cnpj={self.cnpj}, nome='{self.nome}', telefone={self.telefone}, endereco={self.endereco})"

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    valor = Column("valor", Integer)
    qntd = Column("qntd", Integer)
    cnpj_farmacia = Column("cnpj_farmacia", ForeignKey("farmacias.cnpj"))

    def __init__(self, valor, qntd, cnpj_farmacia):
        self.valor = valor
        self.qntd = qntd
        self.cnpj_farmacia = cnpj_farmacia

    def __repr__(self):
        return f"Produto(id={self.id}, valor='{self.valor}', qntd={self.qntd}, cnpj_farmacia={self.cnpj_farmacia})"

class Farmaceutico(Base):
    __tablename__ = 'farmaceuticos'

    cpf = Column("cpf", Integer, primary_key=True)
    nome = Column("nome", String(30))
    cnpj_farmacia = Column("cnpj_farmacia", ForeignKey("farmacias.cnpj"))

    def __init__(self, cpf, nome, cnpj_farmacia):
        self.cpf = cpf
        self.nome = nome
        self.cnpj_farmacia = cnpj_farmacia

    def __repr__(self):
        return f"Farmaceutico(cpf={self.cpf}, nome='{self.nome}', cnpj_farmacia={self.cnpj_farmacia})"

Base.metadata.create_all(bind=db)

# CRUD

# CREATE
farmacia = Farmacia(00000000000000, 'Ultrafarma', 1198765432, 'Bairro logo ali, rua quebrando a esquerda')
session.add(farmacia)
session.commit()

# READ
farmacias = session.query(Farmacia).all()
print(farmacias[0])

farmacia_especifica = session.query(Farmacia).filter_by(nome='Megafarma').first()
print(farmacia_especifica)

# UPDATE
farmacia_especifica.nome = "Megafarma"
session.add(farmacia_especifica)
session.commit()

# DELETE
session.delete(farmacia_especifica)
session.commit()
