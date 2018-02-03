from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("""postgres://stucwlpmyfovvx:310b7dd6b0793868468866558043b0ffaadbc5685ba76bd45846dacd2b64367a@ec2-50-16-231-2.compute-1.amazonaws.com:5432/dbf8uo3mahb4ok
""", convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)
