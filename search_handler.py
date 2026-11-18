#!/usr/bin/env python3
"""
Обработчик поисковых запросов
"""

import re
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

# Модель для хранения данных (в реальном приложении будет использоваться БД)
class PersonData:
    def __init__(self, full_name="", phone="", location="", additional_info=""):
        self.full_name = full_name
        self.phone = phone
        self.location = location
        self.additional_info = additional_info

# Пример базы данных (в реальном приложении это будет БД)
SAMPLE_DATABASE = [
    PersonData(
        full_name="Иванов Иван Иванович",
        phone="+79123456789",
        location="Москва, ул. Тверская, д. 10",
        additional_info="Работает в банке, Married"
    ),
    PersonData(
        full_name="Петрова Мария Сергеевна",
        phone="+79234567890",
        location="Санкт-Петербург, пр. Невский, д. 25",
        additional_info="Студентка, 22 года"
    ),
    PersonData(
        full_name="Сидоров Алексей Владимирович",
        phone="+79345678901",
        location="Екатеринбург, ул. Ленина, д. 5",
        additional_info="Инженер, Женат"
    ),
    PersonData(
        full_name="Козлова Анна Дмитриевна",
        phone="+79456789012",
        location="Новосибирск, пр. Ленина, д. 30",
        additional_info="Врач, Свободна"
    ),
    PersonData(
        full_name="Морозов Дмитрий Александрович",
        phone="+79567890123",
        location="Казань, ул. Кирова, д. 15",
        additional_info="Программист, Женат"
    )
]

async def search_handler(update: Update, context: CallbackContext) -> None:
    """Обрабатывает поисковые запросы"""
    query = update.message.text.strip()
    
    # Проверяем тип запроса
    if re.match(r'^Поиск:', query, re.IGNORECASE):
        await search_by_name(update, context, query)
    elif re.match(r'^Телефон:', query, re.IGNORECASE):
        await search_by_phone(update, context, query)
    elif re.match(r'^Местоположение:', query, re.IGNORECASE):
        await search_by_location(update, context, query)
    else:
        # Поиск по всем параметрам
        await search_general(update, context, query)

async def search_by_name(update: Update, context: CallbackContext, query: str) -> None:
    """Поиск по ФИО"""
    name = query[7:].strip()  # Убираем "Поиск:"
    
    if not name:
        await update.message.reply_text("Пожалуйста, укажите имя для поиска")
        return
    
    results = []
    for person in SAMPLE_DATABASE:
        if name.lower() in person.full_name.lower():
            results.append(person)
    
    await send_results(update, results, f"Результаты поиска по имени '{name}'")

async def search_by_phone(update: Update, context: CallbackContext, query: str) -> None:
    """Поиск по номеру телефона"""
    phone = query[9:].strip()  # Убираем "Телефон:"
    
    if not phone:
        await update.message.reply_text("Пожалуйста, укажите номер телефона для поиска")
        return
    
    results = []
    for person in SAMPLE_DATABASE:
        if phone in person.phone:
            results.append(person)
    
    await send_results(update, results, f"Результаты поиска по телефону '{phone}'")

async def search_by_location(update: Update, context: CallbackContext, query: str) -> None:
    """Поиск по местоположению"""
    location = query[15:].strip()  # Убираем "Местоположение:"
    
    if not location:
        await update.message.reply_text("Пожалуйста, укажите место для поиска")
        return
    
    results = []
    for person in SAMPLE_DATABASE:
        if location.lower() in person.location.lower():
            results.append(person)
    
    await send_results(update, results, f"Результаты поиска по местоположению '{location}'")

async def search_general(update: Update, context: CallbackContext, query: str) -> None:
    """Общий поиск по всем параметрам"""
    if not query:
        await update.message.reply_text("Пожалуйста, введите запрос для поиска")
        return
    
    results = []
    
    # Поиск по ФИО
    for person in SAMPLE_DATABASE:
        if query.lower() in person.full_name.lower():
            results.append(person)
    
    # Поиск по телефону
    for person in SAMPLE_DATABASE:
        if query in person.phone and person not in results:
            results.append(person)
            
    # Поиск по местоположению
    for person in SAMPLE_DATABASE:
        if query.lower() in person.location.lower() and person not in results:
            results.append(person)
    
    await send_results(update, results, f"Результаты общего поиска по запросу '{query}'")

async def send_results(update: Update, results: list, title: str) -> None:
    """Отправляет результаты поиска пользователю"""
    if not results:
        message = "К сожалению, ничего не найдено"
        await update.message.reply_text(message)
        return
    
    # Если найдено больше одного результата, предлагаем выбор
    if len(results) == 1:
        person = results[0]
        result_message = (
            f"🔍 {title}\n\n"
            f"📋 *Информация о человеке:*\n"
            f"🔹 Имя: {person.full_name}\n"
            f"📞 Телефон: {person.phone}\n"
            f"📍 Местоположение: {person.location}\n"
            f"📝 Дополнительно: {person.additional_info}"
        )
        
        await update.message.reply_text(result_message, parse_mode='Markdown')
    else:
        # Для множественного результата отправим список
        result_message = f"🔍 {title}\n\nНайдено {len(results)} результатов:\n\n"
        
        for i, person in enumerate(results[:5], 1):  # Показываем первые 5
            result_message += (
                f"{i}. {person.full_name}\n"
                f"   Телефон: {person.phone}\n"
                f"   Местоположение: {person.location}\n\n"
            )
        
        if len(results) > 5:
            result_message += "..."
            
        await update.message.reply_text(result_message)
