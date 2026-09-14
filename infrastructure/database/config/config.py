from sqlalchemy import create_engine, sessionmaker

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = Session()