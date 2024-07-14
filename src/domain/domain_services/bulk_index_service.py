
from src.domain.helpers.bulk_data_constructor import BulkDataConstructor
from src.domain.inbound_ports.bulk_service_port import BulkServicePort
from src.domain.outbound_ports.elasticsearch_adapter_port import ElasticsearchAdapterPort


class BulkIndexService(BulkServicePort):

    def __init__(self):
        self.es = ElasticsearchAdapterPort()

    def bulk_index(self, data: str, index_name: str, base_dir: str) -> None:
        bulk_data = BulkDataConstructor.construct_bulk_data(data, base_dir)
        self.es.bulk_index_data(bulk_data, index_name)




