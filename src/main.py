import os

from src.domain.domain_services.bulk_index_service import BulkIndexService
from src.entities.constants import Constants

if __name__ == "__main__":

    try:
        bulk_index_service = BulkIndexService()
        print(os.path.dirname(os.path.abspath(__file__)))
        bulk_index_service.bulk_index(
            Constants.bulk_data_file_name, Constants.index_name, os.path.dirname(os.path.abspath(__file__))
        )

    except Exception as e:
        print(f"Error: {str(e)}")
