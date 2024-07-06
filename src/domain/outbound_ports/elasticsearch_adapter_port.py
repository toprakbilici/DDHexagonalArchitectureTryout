from abc import ABC, abstractmethod


class ElasticsearchAdapterPort(ABC):

    @abstractmethod
    def bulk_index_data(self, bulk_data, index_name):
        pass
