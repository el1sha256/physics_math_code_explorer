import json
import sys

import manticoresearch
from manticore_utils.config import manticore_config
from _logger import logger




def preprocess_media_name(media_name):
    media_name = str(media_name.rsplit(".", maxsplit=1)[0])
    return media_name.replace("_", " ")


def fill_manticore(data: list[dict]):
    with manticoresearch.ApiClient(manticore_config) as client:
        sql_client = manticoresearch.UtilsApi(client)
        index_client = manticoresearch.IndexApi(client)

        result = sql_client.sql("SELECT COUNT(*) AS num_rows FROM posts;")
        num_entities = result[0]['data'][0]['num_rows']

        if len(data) == int(num_entities):
            logger.info(f"Database already populated with {num_entities} documents")
            return True


        sql_client.sql("TRUNCATE TABLE posts;")
        docs = [
            {"insert": {"index": "posts", "id": int(doc['id']),
                        "doc": {"title": str(doc['text']), "media_name": preprocess_media_name(str(doc['media_name'])),
                                }
                        }
             } for doc in data
        ]
        try:
            index_client.bulk('\n'.join(map(json.dumps, docs)))
            logger.info(f"Successfully Indexed {len(docs)}")
        except Exception as e:
            raise e

        return True
