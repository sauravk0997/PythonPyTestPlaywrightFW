class FrameworkException(Exception):
    """Base exception for the automation framework."""
    pass

class configReaderException(FrameworkException):
    """Raised when configuration file reading or retrieval fails."""
    pass

class jsonReaderException(FrameworkException):
    """Raised when json file reading or retrieval fails."""
    pass

class csvReaderException(FrameworkException):
    """Raised when csv file reading or retrieval fails."""
    pass