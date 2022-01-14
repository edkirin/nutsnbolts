import os


class Config:
    port: str = os.environ.get('INTERNAL_PORT')
    workers: str = os.environ.get('WORKERS')
    db_host: str = os.environ.get('DB_HOST')
    db_port: str = os.environ.get('DB_PORT')
    db_name: str = os.environ.get('DB_NAME')
    db_user: str = os.environ.get('DB_USER')
    db_password: str = os.environ.get('DB_PASSWORD')
