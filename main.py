import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publishers, Books, Shops, Stocks, Sales
import os


name = os.getenv('name')
password = os.getenv('password')
db = os.getenv('db')


DSN = f'postgresql://{name}:{password}@localhost:5432/{db}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publishers(name='Publisher#1')
book1 = Books(title='Book#1', publisher=publisher1)
shop1 = Shops(name='Shops#1')
stock1 = Stocks(books=book1, shops=shop1)
sale1 = Sales(price='100$', date_sale='12.11.22', stocks=stock1, count='5') #поставить тип Время

session.add_all([publisher1, book1, shop1, stock1, sale1])
session.commit()


question = input('Введите идентификатор или имя:')
for c in session.query(Publishers).filter((Publishers.name==question) | (Publishers.id==question)).all():
    print(c)
session.close()
