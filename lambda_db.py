import os
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# db_string = "postgres://{}:{}@{}:5432/{}".format(os.environ['DB_USER'],
#                                                  os.environ['DB_PASSWORD'],
#                                                  os.environ['DB_HOST'],
#                                                  os.environ['DB_NAME'])

db_string = "postgres://{}:@{}:5432/{}".format('nayanjain',
                                                 'localhost',
                                                 'test')

db = create_engine(db_string)
base = declarative_base()


class Science(base):
    """The class of the table in the database."""
    __tablename__ = 'science'

    id = Column(Integer, primary_key=True)
    file_name = Column(VARCHAR)
    directory_path = Column(VARCHAR)
    file_size = Column(Integer)
    mod_date = Column(TIMESTAMP)
    instrument_id = Column(VARCHAR)
    data_level = Column(VARCHAR)
    timetag = Column(TIMESTAMP)
    descriptor = Column(VARCHAR)
    mode = Column(VARCHAR)
    version = Column(Integer)
    file_root = Column(VARCHAR)
    pred_rec = Column(VARCHAR)
    revision = Column(Integer)
    absolute_version = Column(Integer)
    md5checksum = Column(VARCHAR)
    released = Column(Integer)


Session = sessionmaker(db)
session = Session()

