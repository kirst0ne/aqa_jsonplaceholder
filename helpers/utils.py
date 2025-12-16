import json
import os
from typing import Dict, Any
from helpers.config import Config


def load_test_data(resource: str = None) -> Dict[str, Any]:
    """
    Загружает тестовые данные из JSON файлов

    Args:
        resource: Название ресурса ('posts', 'users', etc.)
                  Если None - возвращает все данные

    Returns:
        Словарь с тестовыми данными
    """
    data_dir = Config.PATH.test_data_dir

    if resource:
        # Загружаем один файл
        file_path = os.path.join(data_dir, f"{resource}.json")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Файл не найден: {file_path}")
            return {}
    else:
        # Загружаем все файлы
        all_data = {}
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                resource_name = filename.replace('.json', '')
                file_path = os.path.join(data_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    all_data[resource_name] = json.load(f)
        return all_data
