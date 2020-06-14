from sqlalchemy import *

meta = MetaData()

quiz_option = Table(
    'quiz_option', meta,
    Column('id', Integer, primary_key=True),
    Column('quiz_id', Integer),
    Column('text', Text),
    Column('correct', Boolean)
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    quiz_option.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    quiz_option.drop()
