from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Keyboard для функции 'cmd_start'
main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=str('Я определился со своим выбором!'))],
                                    [KeyboardButton(text=str('Ещё нет'))]],
                          resize_keyboard=True,
                          one_time_keyboard=True)

# Keyboard для функции 'not_chosen'
main_ex = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=str('Я определился со своим выбором!'))]],
                          resize_keyboard=True,
                          one_time_keyboard=True)

# Keyboard для функции 'register_metrdist'
walk = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=str('На транспорте'))],
    [KeyboardButton(text=str('Пешком'))]],
    resize_keyboard=True,
    one_time_keyboard=True)

# Keyboard для функции 'register_walk'
brick = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=str('Кирпич'))],
    [KeyboardButton(text=str('Монолит ж/б'))],
    [KeyboardButton(text=str('Другое'))]],
    resize_keyboard=True,
    one_time_keyboard=True)

# Keyboard для функции 'register_brick'
floor = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=str('Любой, кроме первого и последнего'))],
    [KeyboardButton(text=str('Иначе'))]],
    resize_keyboard=True,
    one_time_keyboard=True)

# Keyboard для функции 'not_chosen_yet'
chosen = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=str('Я определился со своим выбором!'))],
    [KeyboardButton(text=str('Всё ещё не определился'))]],
    resize_keyboard=True,
    one_time_keyboard=True)

# Keyboard для функции 'register_floor'
one_more_time = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=str('Да, хочу ещё раз попробовать'))],
    [KeyboardButton(text=str('Нет, с меня достаточно'))]],
    resize_keyboard=True,
    one_time_keyboard=True)
