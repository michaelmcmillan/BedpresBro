import sqlite3
from config import configuration
from .mapper import Mapper

class Brain:

    connection = sqlite3.connect(
        configuration['database']['location'],
        check_same_thread=False,
        detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES
    )

    @classmethod
    def setup(cls):
        Brain.connection.row_factory = sqlite3.Row
        cur = Brain.connection.cursor()
        cur.execute('''create table if not exists events(
            id text primary key,
            title text,
            notification_sent int(1),
            enrollment_date timestamp,
            date timestamp
        )''')

    @classmethod
    def create(cls, event):
        cur = Brain.connection.cursor()
        try:
            cur.execute('insert into events values (:id, :title, :notification_sent, :enrollment_date, :date)', Mapper.to_row(event))
        except sqlite3.IntegrityError:
            return None
        Brain.connection.commit()
        return cur.lastrowid

    @classmethod
    def read(cls, event_id):
        cur = Brain.connection.cursor()
        cur.execute('select * from events where id="%s"' % event_id)
        row = cur.fetchone()
        if row:
            return Mapper.to_event(row)
        else:
            return None

    @classmethod
    def update(cls, event):
        cur = Brain.connection.cursor()
        row = Mapper.to_row(event)
        cur.execute('''update events set
            id = :id,
            title = :title,
            date = :date,
            enrollment_date = :enrollment_date,
            notification_sent = :notification_sent
            where id=:id''', row
        )
        Brain.connection.commit()
        return cur.lastrowid

    @classmethod
    def all(cls):
        cur = Brain.connection.cursor()
        cur.execute('select * from events')
        rows = cur.fetchall()
        events = [Mapper.to_event(row) for row in rows]
        return events
