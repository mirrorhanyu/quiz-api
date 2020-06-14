from sqlalchemy import *

meta = MetaData()

exam = Table(
    'exam', meta,
    Column('id', Integer, primary_key=True),
    Column('quizzes', JSON),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    exam.create()



def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    exam.create()

