import json
import os


class BulkDataConstructor:

    @staticmethod
    def construct_bulk_data(filename: str, base_dir=None):
        if base_dir is None:
            raise ValueError("Base directory 'base_dir' must be provided.")

        file_path = os.path.join(base_dir, filename)

        print(file_path)
        with open(file_path, 'r') as file:
            bulk_data = []
            for line in file:
                line = line.strip()
                if line:  
                    bulk_data.append(json.loads(line))
            return bulk_data
