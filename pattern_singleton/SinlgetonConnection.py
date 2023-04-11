import psycopg2


class SingletonConnect(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]


class DataBaseConnection(metaclass=SingletonConnect):
    conn = None

    def create_connect(self, connection_string):
        if self.conn is None:
            self.conn = psycopg2.connect(**connection_string)
        print('Соединение открыто')
        return self.conn

    def close_connect(self):
        self.conn.close()
        print('Соединение закрыто')


connection_str = {
    "host": "localhost",
    "port": '5432',
    "dbname": 'test',
    "user": 'test',
    "password": 'test'
}
c1 = DataBaseConnection()
my_conn = c1.create_connect(connection_string=connection_str)

my_conn1 = c1.create_connect(connection_string=connection_str)
print(type(c1), c1, id(c1))
print(type(my_conn), id(my_conn))
print(type(my_conn1), id(my_conn1))
#
c2 = DataBaseConnection()
my_conn2 = c2.create_connect(connection_string=connection_str)
print(type(c2), c2, id(c2))
print(type(my_conn2), id(my_conn2))
