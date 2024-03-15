from pprint import pprint

import manticoresearch
from manticore_utils.config import manticore_config


class SearchPosts:
    index = 'posts'

    @staticmethod
    def post_process_results(result):
        list_of_ids = [
            {"id": int(hit['_id']), "media_name": hit['_source']['media_name'], "description": hit['_source']['title']}
            for hit in result.hits.hits]
        return list_of_ids

    @classmethod
    def search(cls, tolerance, query_string):
        with manticoresearch.ApiClient(manticore_config) as client:
            search_client = manticoresearch.SearchApi(client)
            if tolerance == 0:
                result = search_client.search(
                    {"index": "posts", "query": {"query_string": f"\"*{query_string}*\"~2", "sort": "descending"}}
                )
                return cls.post_process_results(result)
