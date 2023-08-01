import os


class Settings:
    dbname = os.getenv("pv_dbname")
    user = os.getenv("pv_user")
    password = os.getenv("pv_password")
    host = os.getenv("pv_host")
    port = os.getenv("pv_port")
