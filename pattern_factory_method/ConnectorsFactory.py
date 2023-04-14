import json
from enum import Enum


class ConnectorType(Enum):
    SINK = 'sink',
    SOURCE = 'source',
    ENRICHMENT = 'enrichment',
    LOOKUP = 'lookup'


class Connector:
    def __init__(self, connector, connector_type):
        self.connector = connector
        self.connector_type = connector_type


class ConnectorInitError(Exception):
    def __init__(self, connector: str):
        self.message = f'Хьюстон у нас проблемы, не могу создать коннектор ' \
                       f'для {connector}. Ошибочкэ'
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ClickhouseConnector(Connector):
    def __init__(self,
                 connector_type: str,
                 table: str | None = None,
                 url: str | None = None,
                 connector: str = 'clickhouse',
                 sink_parallelism: str = '1',
                 username: str | None = None,
                 password: str | None = None
                 ):
        super().__init__(connector, connector_type)
        self.table = table
        self.url = url
        self.sink_parallelism = sink_parallelism
        self.username = username
        self.password = password


class KafkaConnector(Connector):
    def __init__(self,
                 topic: str = None,
                 properties_bootstrap_servers: str = None,
                 connector: str = 'kafka',
                 connector_type: str = 'sink',
                 scan_startup_mode: str = None,
                 format: str = None):
        super().__init__(connector, connector_type)
        self.topic = topic
        self.properties_bootstrap_servers = properties_bootstrap_servers,
        self.scan_startup_mode = scan_startup_mode
        self.format = format


class JdbcConnector(Connector):
    def __init__(self,
                 connector_type: str,
                 table_name: str | None = None,
                 url: str | None = None,
                 connector: str = 'jdbc',
                 sink_parallelism: str = '1',
                 username: str | None = None,
                 password: str | None = None,
                 sink_max_retries: str | None = None,
                 connection_max_retry_timeout: str | None = None
                 ):
        super().__init__(connector, connector_type)
        self.table_name = table_name
        self.url = url
        self.sink_parallelism = sink_parallelism
        self.username = username
        self.password = password
        self.sink_max_retries = sink_max_retries
        self.connection_max_retry_timeout = connection_max_retry_timeout


# мысли
class ConnectorSerializer:
    def serializer(self, connector: Connector, connector_type: ConnectorType,
                   format: str):
        if format == 'JSON':
            return self._serializer_to_json(connector=connector)

    @staticmethod
    def _serializer_to_json(connector):
        payload = {
            'connector': connector.connector
        }
        return json.dumps(payload)


class ConnectorFactory:
    def get_connector(self, connector: str, connector_type: str):
        if connector == 'clickhouse' and connector_type == 'sink':
            return ClickhouseConnector(connector=connector,
                                       connector_type=connector_type)
        elif connector == 'jdbc' and connector_type == 'sink':
            return JdbcConnector(connector=connector,
                                 connector_type=connector_type)
        elif connector == 'kafka' and connector_type in ['source', 'sink']:
            return KafkaConnector(connector=connector,
                                  connector_type=connector_type)
        else:
            raise ConnectorInitError(connector=connector)


factory = ConnectorFactory()
clickhouse_connector = factory.get_connector(connector='clickhouse',
                                             connector_type='sink')
clickhouse_connector.url = 'jdbc:clickhouse://clickhouse:8123/default'
clickhouse_connector.table = 'test_table'
clickhouse_connector.sink_parallelism = 1

print(clickhouse_connector.__dict__)

kafka_connector = factory.get_connector(connector_type='source',
                                        connector='kafka')

print(kafka_connector.__dict__)
