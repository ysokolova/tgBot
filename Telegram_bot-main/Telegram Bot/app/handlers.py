from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import logging
import numpy as np
import app.keyboards as kb

# Настройка логгера
logging.basicConfig(filename='bot.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.ERROR)
logger = logging.getLogger(__name__)  # Создаём экземпляр логгера с именем текущего модуля для записи сообщений в файл

router = Router()

# Определяем класс Register, который содержит 8 состояний
class Register(StatesGroup):
    totsp = State()
    livesp = State()
    kitsp = State()
    dist = State()
    metrdist = State()
    walk = State()
    brick = State()
    floor = State()

# Обработчик реагирует только на команду '/start'
@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer('Привет! Я бот, который умеет предсказывать цену стоимости квартиры в Москве в зависимости от Ваших пожеланий.\n'
                         'Вы уже определились с тем, какую квартиру хотите приобрести?',reply_markup=kb.main)


@router.message(F.text == str('Ещё нет'))
async def not_chosen_yet(message: Message):
    await message.answer(
        'Ничего страшного! Мы поможем Вам принять решение. Для этого Вам нужно решить 8 мини-задачек.')
    await message.answer(
        'Задача №1\nПодумайте, какая общая площадь квартиры была бы для вас желанной\n'
        'Задача №2\nА жилая площадь квартиры?\n'
        'Задача №3\nКухня - неотъемлемая составляющая квартиры. Чему должна равняться площадь идеальной кухни?\n'
        'Задача №4\nКак близко вы хотите жить к центру города?\n'
        'Задача №5\nМетро - лучший транспорт Москвы. Сколько бы времени Вы хотели тратить на дорогу до метро?\n'
        'Задача №6\nИ вообще, как Вы хотите добираться до метро?\n'
        'Задача №7\nКирпич, монолит ж/б... или что-то другое? Материал изготовления дома какой выбирать будем?\n'
        'Задача №8\nЖить на верхних этажах (чуть ли не пентхаус) или на первом? Или в принципе без разницы?')
    await message.answer(
        'После того, как решите эти 8 мини-задачек, выберите "Я определился со своим выбором!", если вы полностью определились с выбором.\n'
        'В ином случае мы предлагаем Вам ещё подумать.', reply_markup=kb.chosen)

@router.message(F.text == str('Всё ещё не определился'))
async def not_chosen(message: Message):
    await message.answer(
        'Не расстраивайтесь! Мы Вас ждём!\n\n'
        'Когда определитесь со своим выбором, выберите единственный пункт меню',reply_markup=kb.main_ex)

@router.message(F.text.in_(['Я определился со своим выбором!','Да, хочу ещё раз попробовать']))
async def already_chosen(message: Message, state:FSMContext):
    await message.answer(
        'Отлично!\nДля того чтобы определить стоимость квартиры, Вам нужно ответить на ряд вопросов, и, чтобы '
        'наш Бот сделал предсказание корректным, пожалуйста, указывайте данные именно в предложенном Вам формате.')
    await message.answer(
        'Итак, первый вопрос!')
    await state.set_state(Register.totsp)
    await message.answer(
        'Вопрос №1\nУкажите общую площадь квартиры в квадратных метрах.\nФормат ввода: 17')

@router.message(Register.totsp)
async def register_totsp(message: Message, state: FSMContext):
    try:
        # Проверяем, что пользователь ввёл целое число
        total_area = int(message.text.strip())

        if total_area <= int(0):
            raise ValueError("Общая площадь должна быть положительным числом.")

        await state.update_data(totsp=total_area)
        await state.set_state(Register.livesp)
        await message.answer(
            'Вопрос №2\nУкажите жилую площадь квартиры в квадратных метрах.\nФормат ввода: 23')

    except ValueError:
        await message.reply("Пожалуйста, введите положительное число для общей площади квартиры.")

@router.message(Register.livesp)
async def register_livesp(message: Message, state: FSMContext):
    try:
        # Проверяем, что пользователь ввёл целое число
        live_area = int(message.text.strip())

        if live_area <= int(0):
            raise ValueError("Жилая площадь должна быть положительным числом.")

        await state.update_data(livesp=message.text)
        await state.set_state(Register.kitsp)
        await message.answer(
            'Вопрос №3\nУкажите площадь кухни в квадратных метрах.\nФормат ввода: 10')

    except ValueError:
        await message.reply("Пожалуйста, введите положительное число для жилой площади квартиры.")

@router.message(Register.kitsp)
async def register_kitsp(message: Message, state: FSMContext):
    try:
        # Проверяем, что пользователь ввёл целое число
        kit_area = int(message.text.strip())

        if kit_area <= int(0):
            raise ValueError("Площадь кухни должна быть положительным числом.")

        await state.update_data(kitsp=message.text)
        await state.set_state(Register.dist)
        await message.answer(
            'Вопрос №4\nУкажите расстояние от центра города в километрах.\nФормат ввода: 5')

    except ValueError:
        await message.reply("Пожалуйста, введите положительное число для площади кухни.")

@router.message(Register.dist)
async def register_dist(message: Message, state: FSMContext):
    try:
        # Проверяем, что пользователь ввёл целое число
        distantion = int(message.text.strip())

        if distantion <= int(0):
            raise ValueError("Расстояние от центра города должно быть положительным числом.")

        await state.update_data(dist=message.text)
        await state.set_state(Register.metrdist)
        await message.answer(
            'Вопрос №5\nУкажите расстояние до метро в минутах.\nФормат ввода: 11')

    except ValueError:
        await message.reply("Пожалуйста, введите положительное число расстояния от центра города.")


@router.message(Register.metrdist)
async def register_metrdist(message: Message, state: FSMContext):
    try:
        # Проверяем, что пользователь ввёл целое число
        metro = int(message.text.strip())

        if metro <= int(0):
            raise ValueError("Расстояние до метро должно быть положительным числом.")

        await state.update_data(metrdist=message.text)
        await state.set_state(Register.walk)
        await message.answer(
            'Вопрос №6\nКак Вы хотите добираться до квартиры: на транспорте или пешком?\nВыберите один из вариантов.',
            reply_markup=kb.walk)

    except ValueError:
        await message.reply("Пожалуйста, введите положительное число расстояния до метро.")


@router.message(Register.walk, F.text.in_([str("На транспорте"), str("Пешком")]))
async def register_walk(message: Message, state: FSMContext):
    await state.update_data(walk=message.text)
    await state.set_state(Register.brick)
    await message.answer(
        'Вопрос №7\nВыберите из предложенных вариантов материал, из которого должен быть изготовлен дом.', reply_markup=kb.brick)

@router.message(Register.walk)
async def invalid_walk_input(message: Message):
    await message.reply("Пожалуйста, выберите один из предложенных вариантов: 'На транспорте' или 'Пешком'.")

@router.message(Register.brick, F.text.in_([str("Кирпич"), str("Монолит ж/б"), str("Другое")]))
async def register_brick(message: Message, state: FSMContext):
    await state.update_data(brick=message.text)
    await state.set_state(Register.floor)
    await message.answer(
        'Вопрос №8\nВыберите из предложенных вариантов этаж, на котором Вы хотите жить.', reply_markup=kb.floor)

@router.message(Register.brick)
async def invalid_brick_input(message: Message):
    await message.reply("Пожалуйста, выберите один из предложенных вариантов: 'Кирпич', 'Монолит ж/б' или 'Другое'.")

@router.message(Register.floor, F.text.in_([str("Любой, кроме первого и последнего"), str("Иначе")]))
async def register_floor(message: Message, state: FSMContext):
    await state.update_data(floor=message.text)
    data = await state.get_data()

    # Переменные 'walk', 'brick', 'floor' являются категориальными, поэтому они могут принимать только значения '0' и '1'
    if data['walk'] == str('На транспорте'):
        data['walk'] = int(0)
    elif data['walk'] == str('Пешком'):
        data['walk'] = int(1)

    if data['brick'] == str('Кирпич'):
        data['brick'] = int(1)
    elif data['brick'] == str('Монолит ж/б'):
        data['brick'] = int(1)
    elif data['brick'] == str('Другое'):
        data['brick'] = int(0)

    if data['floor'] == str('Любой, кроме первого и последнего'):
        data['floor'] = int(1)
    elif data['floor'] == str('Иначе'):
        data['floor'] = int(0)

    test = [
        int(data['totsp']),
        int(data['livesp']),
        int(data['kitsp']),
        int(data['dist']),
        int(data['metrdist']),
        int(data['walk']),
        int(data['brick']),
        int(data['floor'])
    ]

    # Создаем двумерный массив для передачи в модель
    test_data = np.array([test])

    # Загружаем catboost
    from catboost import CatBoostRegressor
    model = CatBoostRegressor().load_model('D:/Python projects/Telegram Bot/app/model/catboost_model.cbm')

    try:
        # Предсказываем значение
        predictions = model.predict(test_data)
        await state.clear()
        if len(predictions) > int(0):
            predicted_price = predictions[int(0)]
            await message.answer(f'Предсказанная стоимость квартиры: {round(predicted_price*int(1000)*float(103.95))} рублей.\n\n'
                                 f'Хотите ещё раз воспользоваться нашими услугами?',reply_markup=kb.one_more_time)
        else:
            await message.answer("Модель не вернула результатов. Попробуйте позже.")
            logger.error("Модель не вернула результатов.")
    except Exception as e:
        await message.answer("Произошла ошибка при предсказании стоимости квартиры. Попробуйте позже.")
        logger.error(f"Произошла ошибка при предсказании стоимости квартиры: {e}")

@router.message(Register.floor)
async def invalid_floor_input(message: Message):
    await message.reply("Пожалуйста, выберите один из предложенных вариантов: 'Любой, кроме первого и последнего', 'Иначе'.")

@router.message(F.text == str('Нет, с меня достаточно'))
async def already_chosen(message: Message):
    await message.answer(
        'Спасибо что воспользовались нашим ботом. Надеемся, что мы смогли вам помочь\n\n'
        'Для того чтобы воспользоваться услугами бота ещё раз, напишите команду /start')