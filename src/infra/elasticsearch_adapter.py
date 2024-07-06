from elasticsearch import Elasticsearch, helpers
from src.entities.constants import Constants
from src.domain.outbound_ports.elasticsearch_adapter_port import ElasticsearchAdapterPort
from dotenv import load_dotenv
from pathlib import Path
import os


class ElasticsearchAdapter(ElasticsearchAdapterPort):

    def __init__(self):
        self.es_client = self.connect_to_es()

    @staticmethod
    def connect_to_es() -> Elasticsearch:
        try:
            dotenv_path = Path(Constants.dot_env_file_path)
            load_dotenv(dotenv_path=dotenv_path)

            client = Elasticsearch(
                Constants.es_port_url,
                ca_certs=Constants.ca_cert_file_path,
                basic_auth=(os.getenv('ES_USERNAME'), os.getenv('ES_PASSWORD'))
            )
            print(client.info)
            if client.ping():
                return client
            else:
                raise Exception
        except Exception as e:
            print(e)

    def bulk_index_data(self, bulk_data, index_name):
        es_client = self.es_client
        actions = []
        for i in range(0, len(bulk_data), 2):
            action = {
                "_op_type": "index",
                "_index": index_name,
                "_id": bulk_data[i]["index"]["_id"],
                "_source": bulk_data[i + 1]
            }
            actions.append(action)
        helpers.bulk(es_client, actions)
        print(f"Successfully indexed {len(actions)} documents into '{index_name}' index.")
