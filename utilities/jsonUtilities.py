import json

from Exceptions.framework_exceptions import jsonReaderException
from utilities.PathUtilites import PathUtilities


class JsonUtilities:

    @staticmethod
    def read_json(file_name):
        try:
            file_path = PathUtilities.get_test_data_path(file_name)
            with open(file_path, "r") as file:
                return json.load(file)
        except Exception as e:
            raise jsonReaderException(f"file not found: {file_name}, Error {e}") from e