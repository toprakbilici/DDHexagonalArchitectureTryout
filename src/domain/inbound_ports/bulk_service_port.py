from abc import abstractmethod, ABC


class BulkServicePort(ABC):

    @abstractmethod
    def bulk_index(self, data, index_name, base_dir) -> str:
        pass
