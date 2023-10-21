import ast
import redis
import os



if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

uri = Config.REDIS_URI

from urllib.parse import urlparse


result = urlparse(uri)
password = result.password
hostname = result.hostname
port = int(result.port)

DB = redis.StrictRedis(
    host=hostname,
    port=port,
    password=password,
    charset="utf-8",
    decode_responses=True,
)


def get_stuff(WHAT):
    n = []
    cha = DB.get(WHAT)
    if not cha:
        cha = "{}"
    n.append(ast.literal_eval(cha))
    return n[0]
