#!/usr/bin/env python3
"""
Конфигурационный файл бота
"""

import os

# Токен бота (заменить на реальный токен)
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

# Настройки бота
BOT_SETTINGS = {
    'name': 'PokeBot',
    'version': '1.0.0',
    'description': 'Telegram bot for personal data lookup'
}

# Параметры поиска
SEARCH_CONFIG = {
    'max_results': 10,
    'min_match_ratio': 0.6
}
