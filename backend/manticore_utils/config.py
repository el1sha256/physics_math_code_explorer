from os import getenv

import manticoresearch

manticore_config = manticoresearch.Configuration(
    host=getenv("MANTICORE_URI", "http://127.0.0.1:9308")
)