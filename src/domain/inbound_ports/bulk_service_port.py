from typing import Dict, Tuple, Any
from abc import abstractmethod, ABC, abstractstaticmethod


class BulkServicePort(ABC):

    @staticmethod
    @abstractmethod
    def bulk_index(data, index_name, base_dir, yep) -> str:
        pass
