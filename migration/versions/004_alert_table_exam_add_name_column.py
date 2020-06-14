from sqlalchemy import *


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta = MetaData(bind=migrate_engine)
    exam = Table('exam', meta, autoload=True)
    Column('name', String(255)).create(exam)


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta = MetaData(bind=migrate_engine)
    exam = Table('exam', meta, autoload=True)
    Column('name').drop(exam)
