class CONSTANT(object):
    DATE_FORMAT = '%Y-%m-%d'
    TIMESTAMP_FORMAT = '%Y-%m-%d %X'
    TIMESTAMP_IN_INT = '%Y%m%d%H%M%S'

class DATABASE:
    USERNAME = "root"
    PASSWORD = "Tiger123"
    HOST = "localhost"
    PORT = 3307
    CHARSET = "utf8mb4"
    AUTOCOMMIT = True
    DATABASE = "itam"

class PROJECT(object):
    PROJECT_NAME = "ITAM"