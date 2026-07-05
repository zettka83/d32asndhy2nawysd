from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Выполнить задание"),
            KeyboardButton(text="⭐ Мой баланс")
        ],
        [
            KeyboardButton(text="🎁 Магазин"),
            KeyboardButton(text="👥 Пригласить друзей")
        ],
        [
            KeyboardButton(text="🏆 Топ пользователей"),
            KeyboardButton(text="📜 Правила")
        ]
    ],
    resize_keyboard=True
)