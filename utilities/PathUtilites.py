from pathlib import Path


class PathUtilities:
    BASE_DIR = Path(__file__).resolve().parent.parent

    @classmethod
    def get_test_data_path(cls, filename):
        """Return the absolute path of a file inside testData."""
        return cls.BASE_DIR / "testData" / filename

    @classmethod
    def get_project_path(cls, *paths):
        return cls.BASE_DIR.joinpath(*paths)