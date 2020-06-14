from sqlalchemy import *

meta = MetaData()

quiz = Table(
    'quiz', meta,
    Column('id', Integer, primary_key=True),
    Column('stem', Text),
    Column('reference', Text)
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    quiz.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    quiz.drop()
