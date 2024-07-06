
from src.infra.elasticsearch_adapter import ElasticsearchAdapter
from src.domain.helpers.bulk_data_constructor import BulkDataConstructor
from src.domain.inbound_ports.bulk_service_port import BulkServicePort


class BulkIndexService(BulkServicePort):

    def __init__(self):
        self.es = ElasticsearchAdapter()

    def bulk_index(self, data: str, index_name: str, base_dir: str) -> None:
        bulk_data = BulkDataConstructor.construct_bulk_data(data, base_dir)
        self.es.bulk_index_data(bulk_data, index_name)




