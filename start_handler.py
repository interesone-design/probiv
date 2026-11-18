#!/usr/bin/env python3
"""
Обработчик команды /start
"""

from telegram import Update
from telegram.ext import CallbackContext

async def start_handler(update: Update, context: CallbackContext) -> None:
    """Отправляет приветственное сообщение при запуске бота"""
    welcome_text = (
        "👋 *Добро пожаловать в PokeBot!*\n\n"
        "Я - мощный инструмент для поиска информации о людях. 🕵️\n\n"
        "Что я умею:\n"
        "• 🔍 Поиск по ФИО (полное или частичное)\n"
        "• 📞 Поиск по номеру телефона\n"
        "• 📍 Поиск по местоположению\n"
        "• 🧾 Поиск по другим параметрам\n\n"
        "Просто отправьте мне запрос, например:\n"
        "«Поиск: Иванов Иван Иванович»\n"
        "«Телефон: +79123456789»\n"
        "«Местоположение: Москва»\n\n"
        "Для подробной информации используйте команду /help"
    )
    
    await update.message.reply_text(welcome_text, parse_mode='Markdown')
