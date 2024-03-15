from os import getenv

import manticoresearch

manticore_config = manticoresearch.Configuration(
    host=getenv("MANTICORE_URI", "http://manticore:9308")
)