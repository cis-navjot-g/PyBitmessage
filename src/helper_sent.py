"""
Insert values into sent table
"""

import uuid
from helper_sql import sqlExecute


def insert(t):
    """Perform an insert into the `sent` table"""
    msgid = uuid.uuid4().bytes
    temp = list(t)
    temp[0] = msgid
    t = tuple(temp)
    sqlExecute('''INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', *t)
