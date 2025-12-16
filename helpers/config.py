from dataclasses import dataclass

@dataclass
class APIConfig:
    """Конфигурация API"""
    base_url: str
    timeout: int

@dataclass
class FilePaths:
    """Пути к файлам"""
    test_data_dir: str
    reports_dir: str

class Config:
    """Основной класс конфигурации"""

    # Конфигурация API
    API = APIConfig(
        base_url = "https://jsonplaceholder.typicode.com",
        timeout = 5
    )

    # Пути к файлам (относительно корня проекта)
    PATH = FilePaths(
        test_data_dir = "data",
        reports_dir = "reports"
    )
