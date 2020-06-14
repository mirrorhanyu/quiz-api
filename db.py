from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:iJt2rHAfU6uJDWCT@localhost/quiz', echo=True)

# metadata = MetaData()
#
# metadata.create_all(engine)
