from connection import Connection
import contextlib


class Transaction:
    def __init__(self, connection):
        self.connection = connection
        self.xid = connection._start_transaction()

    def commit(self):
        self.connection._commit_transaction(self.xid)

    def rollback(self):
        self.connection._rollback_transaction(self.xid)


@contextlib.contextmanager
def start_transaction(connection):
    tx = Transaction(connection)
    try:
        yield tx
    except:
        tx.rollback()
        raise
    tx.commit()


def main():
    connection = Connection()
    xact = Transaction(connection)
    xact.commit()
    print()

    conn = Connection()
    try:
        with start_transaction(conn) as tx:
            x = 1 + 1
            y = x + 2
            print('transaction 1 = ', x, y)
    except ValueError: 
        print('Oops! Transaction 0 failed.')


if __name__ == '__main__':
    main()