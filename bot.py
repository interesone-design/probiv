#!/usr/bin/env python3
"""
Telegram bot for personal data lookup (pokebot)
"""

import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Импортируем обработчики
from handlers.search_handler import search_handler
from handlers.start_handler import start_handler
from config import BOT_TOKEN

# Токен бота (заменить на реальный токен)
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

async def help_command(update: Update, context: CallbackContext) -> None:
    """Отправляет сообщение с инструкцией по использованию бота"""
    help_text = (
        "🤖 *Добро пожаловать в PokeBot!*\n\n"
        "Я могу помочь вам найти информацию о людях по различным данным:\n\n"
        "• 🔍 Поиск по ФИО (полное или частичное)\n"
        "• 📞 Поиск по номеру телефона\n"
        "• 📍 Поиск по местоположению\n"
        "• 🧾 Поиск по другим параметрам\n\n"
        "Просто отправьте мне запрос в формате:\n"
        "«Поиск: Иванов Иван Иванович»\n"
        "«Телефон: +79123456789»\n"
        "«Местоположение: Москва»\n\n"
        "💡 *Советы*:\n"
        "- Можно искать по частичным данным\n"
        "- Проверяйте корректность ввода\n"
        "- Используйте команду /search для поиска"
    )
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def main() -> None:
    """Запуск бота"""
    # Создание Application с токеном
    application = Application.builder().token(BOT_TOKEN).build()

    # Регистрация обработчиков
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_handler))

    # Запуск бота
    logger.info("Запуск Telegram-бота...")
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
