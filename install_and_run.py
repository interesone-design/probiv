#!/usr/bin/env python3
"""
Установка и запуск Telegram-бота для пробива
"""

import os
import subprocess
import sys

def install_dependencies():
    """Установка зависимостей"""
    print("🔧 Установка зависимостей...")
    
    try:
        # Проверяем, установлен ли python-telegram-bot
        import telegram
        print("✅ Библиотека python-telegram-bot уже установлена")
    except ImportError:
        print("⬇️  Установка python-telegram-bot...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", "python-telegram-bot>=20.0"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Библиотека успешно установлена")
        else:
            print(f"❌ Ошибка при установке: {result.stderr}")
            return False
    
    return True

def check_token():
    """Проверка наличия токена"""
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token or token == 'YOUR_BOT_TOKEN_HERE':
        print("⚠️  Внимание: Необходимо установить токен бота!")
        print("1. Получите токен у @BotFather в Telegram")
        print("2. Установите переменную окружения:")
        print("   export TELEGRAM_BOT_TOKEN=ваш_токен_здесь")
        print("   или на Windows:")
        print("   set TELEGRAM_BOT_TOKEN=ваш_токен_здесь")
        return False
    return True

def main():
    """Основная функция"""
    print("🚀 Telegram PokeBot - установка и запуск")
    
    # Установка зависимостей
    if not install_dependencies():
        print("❌ Не удалось установить зависимости")
        return
    
    # Проверка токена
    if not check_token():
        print("\nПожалуйста, установите токен бота и перезапустите скрипт")
        return
    
    print("\n✅ Все готово! Запуск бота...")
    
    # Запуск основного бота
    try:
        from bot import main
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Бот остановлен")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == '__main__':
    main()
