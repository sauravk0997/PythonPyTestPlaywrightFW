from configparser import ConfigParser

from Exceptions.framework_exceptions import configReaderException
from utilities.PathUtilites import PathUtilities


# config = ConfigParser()
# config.read('config.ini')
# print(config.get("basic info", "browserName"))
# print(config.get("basic info", "URL"))
# print(config.get("mobile", "executionOS"))
class configReader:

    @classmethod
    def readConfig(cls, section, key):
        try:
            CONFIG_PATH = PathUtilities.get_test_data_path("config.ini")
            config = ConfigParser()
            file_read = config.read(CONFIG_PATH)
            if not file_read:
                raise configReaderException(f"Unable to read configuration file: {CONFIG_PATH}")
            value = config.get(section, key)
        except Exception as e:
            raise configReaderException(f"unable to read configuration file: , ERROR: {e}") from e
        return value

# print(readConfig('basic info', 'browserName'))
# print(readConfig('basic info', 'URL'))
# print(readConfig("mobile", "executionOS"))