#!/usr/bin/env python3
"""
Скрипт настройки Telegram PokeBot
"""

import os
import sys
import subprocess

def setup_environment():
    """Настройка окружения"""
    print("🔧 Настройка среды...")
    
    # Проверяем наличие виртуального окружения
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Виртуальное окружение не активировано")
        print("Создаем и активируем виртуальное окружение...")
        
        try:
            subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)
            print("✅ Виртуальное окружение создано")
            
            # Установка зависимостей
            if os.name == 'nt':  # Windows
                pip_path = 'venv\\Scripts\\pip'
            else:  # Linux/Mac
                pip_path = 'venv/bin/pip'
                
            subprocess.run([pip_path, 'install', '-r', 'requirements.txt'], check=True)
            print("✅ Зависимости установлены")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Ошибка при настройке: {e}")
            return False
            
    return True

def create_env_file():
    """Создание файла с переменными окружения"""
    env_content = '''# Конфигурация Telegram PokeBot
TELEGRAM_BOT_TOKEN=your_bot_token_here
'''
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✅ Создан файл .env с примером конфигурации")
    return True

def main():
    """Основная функция настройки"""
    print("🚀 Настройка Telegram PokeBot")
    
    # Проверяем зависимости
    try:
        import telegram
        print("✅ Зависимости уже установлены")
    except ImportError:
        print("⬇️  Установка зависимостей...")
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'python-telegram-bot>=20.0'], 
                          check=True, capture_output=True)
            print("✅ Зависимости установлены")
        except subprocess.CalledProcessError as e:
            print(f"❌ Ошибка при установке зависимостей: {e}")
            return False
    
    # Создаем файл .env
    create_env_file()
    
    print("\n🎉 Настройка завершена!")
    print("1. Получите токен у @BotFather в Telegram")
    print("2. Замените 'your_bot_token_here' в файле .env на ваш токен")
    print("3. Запустите бота командой: python run_bot.py")

if __name__ == '__main__':
    main()
