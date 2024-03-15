import manticoresearch
from manticore_utils.config import manticore_config


def init_tables():
    with manticoresearch.ApiClient(manticore_config) as client:
        sql_instance = manticoresearch.UtilsApi(client)

        response = sql_instance.sql(
            "CREATE TABLE IF NOT EXISTS posts(title TEXT, media_name TEXT) min_infix_len='2' min_prefix_len ='2' ingore_chars='.,_' ")

        return response



