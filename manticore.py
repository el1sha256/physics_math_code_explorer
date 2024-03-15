from __future__ import print_function

import json
import time
import manticoresearch
from manticoresearch import *
from manticoresearch.rest import ApiException
from pprint import pprint, pp

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host="http://127.0.0.1:9308"
)

def preprocess_media_name(media_name):
    media_name = str(media_name.rsplit(".", maxsplit=1)[0])
    return media_name.replace("_", " ")

# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the IndexApi API class
    api_instance = manticoresearch.IndexApi(api_client)
    utils_instance = manticoresearch.UtilsApi(api_client)
    http_api_instance = manticoresearch.SearchApi(api_client)

    # response = utils_instance.sql("CREATE TABLE posts(title text, media_name text, id int) min_infix_len='2' "
    #                               "min_prefix_len='2'")
    # print("Create table response", response)
    #
    # response = utils_instance.sql('SHOW TABLES')
    # print("Show tables response", response)
    with open('messages-copy.json', 'r') as f:
        messages = json.loads(f.read())

    # docs = [ \
    #     {"insert": {"index": "products", "id": 7, "doc": {"title": "Iphone 15 Pro Max 512GB"}}}, \
    #     # {"insert": {"index": "products", "id": 5, "doc": {"title": "Macbook Air 13 M2 256GB"}}}, \
    #     # {"insert": {"index": "products", "id": 6, "doc": {"title": "Apple Vision Pro 512GB"}}}
    # ]
    #
    # docs = [
    #     {"insert": {"index": "posts", "id": int(doc['id']),
    #                 "doc": {"title": str(doc['text']), "media_name": preprocess_media_name(str(doc['media_name'])),
    #                         }
    #                 }
    #      } for doc in messages
    # ]
    # #
    # res = api_instance.bulk('\n'.join(map(json.dumps, docs)))
    #
    # print(res)
    # start_time = time.time()
    # response = utils_instance.sql("SELECT * FROM products WHERE MATCH('\"Iphane 15 511gb\"/2');")
    # response = utils_instance.sql("ALTER TABLE products ;")
    # end_time = time.time()

    start_time = time.time()
    # response = http_api_instance.search()

    # response = utils_instance.sql("call qsuggest('iphine 15 pro', 'products');")
    # response = utils_instance.sql("ALTER TABLE products ADD COLUMN title INFIX;")
    response = http_api_instance.search({"index": "posts", "query": {"query_string": " \"*Криптография*\"~53", "sort": "descending"}})
    end_time = time.time()

    pprint(response)
    print("Execution time", end_time - start_time)
