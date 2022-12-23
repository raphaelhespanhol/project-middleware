from datetime import datetime
import logging
import os
from sqlalchemy import create_engine, insert, MetaData, Table, Column, Integer, Boolean, Date, Time
from sqlalchemy.orm import mapper
from sqlalchemy.sql import select
from models.status_model import Status

class DatabaseHelper:
    def __init__(self):
        self.engine = create_engine(os.getenv("DATABASE_URL"))
        self.conn = self.engine.connect()
        self.metadata = MetaData()
        try:
            self.Status = Table('status', self.metadata,
              Column('id', Integer(),primary_key=True),
              Column('active', Boolean(), default=True),
              Column('date', Date, nullable=False),
              Column('hour', Time, nullable=False)
              )
            self.metadata.create_all(self.engine)
            logging.info("New status table generated with success")
        except Exception as e:
            logging.error(f"Table status already exists in database! Details: {e}")

    def insert_status(self, data):
        try:
            status = True if data['status'] == "ACTIVE" else False 
            date_time = datetime.strptime(data['timestamp'], '%Y-%m-%dT%H:%M:%S%z')
            date = date_time.strftime("%Y-%m-%d")
            time = date_time.strftime("%H:%M:%S")

            query = insert(self.Status).values(id=data['id'], active=status, date=date, hour=time)
            self.conn.execute(query)
            logging.info("A new record was saved in status table")
        except Exception as e:
            logging.error(f"Error to save status in database! Details: {e}")