#!/usr/bin/env python3
"""
Запуск Telegram-бота для пробива
"""

import asyncio
import os
from bot import main
from config import BOT_TOKEN

async def run_bot():
    """Основная функция запуска бота"""
    print("🚀 Запуск Telegram-бота для пробива...")
    
    # Проверяем наличие токена
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token or token == 'YOUR_BOT_TOKEN_HERE':
        print("⚠️  Внимание: Необходимо установить токен бота!")
        print("Пожалуйста, получите токен у @BotFather в Telegram")
        print("Затем задайте переменную окружения:")
        print("   TELEGRAM_BOT_TOKEN=ваш_токен_здесь")
        return
    
    try:
        await main()
    except KeyboardInterrupt:
        print("\n🛑 Бот остановлен пользователем")
    except Exception as e:
        print(f"❌ Ошибка при запуске бота: {e}")

if __name__ == '__main__':
    asyncio.run(run_bot())
