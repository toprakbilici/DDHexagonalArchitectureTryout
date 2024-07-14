import os

from src.entities.constants import Constants
from src.domain.inbound_ports.bulk_service_port import BulkServicePort

if __name__ == "__main__":

    try:
        bulk_index_service_port = BulkServicePort()
        print(os.path.dirname(os.path.abspath(__file__)))
        bulk_index_service_port.bulk_index(
            Constants.bulk_data_file_name, Constants.index_name, os.path.dirname(os.path.abspath(__file__))
        )

    except Exception as e:
        print(f"Error: {str(e)}")
