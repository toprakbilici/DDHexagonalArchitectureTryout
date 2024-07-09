from typing import Dict, Tuple, Any
from abc import abstractmethod, ABC, abstractstaticmethod


class BulkServicePort(ABC):

    @abstractmethod
    def bulk_index(self, data, index_name, base_dir) -> str:
        pass
