import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Список задач
tasks = []

# Команда /start
async def start(update: Update, context):
    await update.message.reply_text('Привет! Я бот для извлечения задач. Добавь меня в свои чаты и пиши задачи.')

# Команда /tasks для показа всех задач
async def list_tasks(update: Update, context):
    if tasks:
        await update.message.reply_text('\n'.join(tasks))
    else:
        await update.message.reply_text('Задач пока нет.')

# Функция для распознавания задач
async def detect_task(update: Update, context):
    message_text = update.message.text.lower()
    keywords = ['сделать', 'нужно', 'необходимо', 'задача', 'напоминание']

    # Если сообщение содержит ключевые слова, добавляем в список задач
    if any(keyword in message_text for keyword in keywords):
        tasks.append(update.message.text)
        await update.message.reply_text(f'Задача добавлена: {update.message.text}')

# Основная функция запуска бота
def main():
    # Здесь нужно вставить ваш TOKEN
    TOKEN = 'YOUR_BOT_TOKEN'

    # Создаем бота
    application = ApplicationBuilder().token(TOKEN).build()

    # Обработчики команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('tasks', list_tasks))

    # Обработчик сообщений для поиска задач
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, detect_task))

    # Запуск бота
    logger.info("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()f
