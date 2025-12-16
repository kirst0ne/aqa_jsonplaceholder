import logging

def get_logger(name):
    """Возвращает настроенный логгер"""
    logger = logging.getLogger(name)
    if not logger.handlers:  # Чтобы не дублировать handlers
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger