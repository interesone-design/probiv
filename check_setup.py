#!/usr/bin/env python3
"""
Проверка установки Telegram PokeBot
"""

import sys
import os

def check_python_version():
    """Проверка версии Python"""
    print("🔍 Проверка версии Python...")
    version = sys.version_info
    if version >= (3, 7):
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - подходит")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - не подходит (нужно 3.7+)")
        return False

def check_dependencies():
    """Проверка зависимостей"""
    print("🔍 Проверка зависимостей...")
    
    try:
        import telegram
        print("✅ python-telegram-bot - установлен")
        
        # Проверяем версию
        version = telegram.__version__
        if version >= '20.0':
            print(f"✅ Версия библиотеки: {version}")
        else:
            print(f"⚠️  Рекомендуется версия 20.0+, у вас: {version}")
            
        return True
    except ImportError as e:
        print(f"❌ Не удалось импортировать telegram: {e}")
        return False

def check_environment():
    """Проверка переменных окружения"""
    print("🔍 Проверка переменных окружения...")
    
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        print("⚠️  TELEGRAM_BOT_TOKEN не установлен")
        return False
    elif token == 'YOUR_BOT_TOKEN_HERE':
        print("⚠️  TELEGRAM_BOT_TOKEN содержит пример значение")
        return False
    
    print("✅ Все переменные окружения установлены")
    return True

def check_files():
    """Проверка наличия необходимых файлов"""
    print("🔍 Проверка файлов...")
    
    required_files = [
        'bot.py',
        'run_bot.py', 
        'requirements.txt',
        '.env.example'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file}")
            missing_files.append(file)
            
    return len(missing_files) == 0

def main():
    """Основная функция проверки"""
    print("🔍 Проверка установки Telegram PokeBot")
    print("=" * 50)
    
    checks = [
        check_python_version,
        check_dependencies,
        check_environment,
        check_files
    ]
    
    results = []
    for check in checks:
        try:
            result = check()
            results.append(result)
            print()
        except Exception as e:
            print(f"❌ Ошибка при проверке {check.__name__}: {e}")
            results.append(False)
            print()
    
    print("=" * 50)
    if all(results):
        print("🎉 Все проверки пройдены! Бот готов к использованию.")
        print("Запустите бота командой: python run_bot.py")
    else:
        print("❌ Некоторые проверки не пройдены. Пожалуйста, исправьте ошибки.")

if __name__ == '__main__':
    main()
