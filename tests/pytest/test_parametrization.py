import pytest
from _pytest.fixtures import SubRequest


# Базовый случай
@pytest.mark.parametrize("number", [1, 2, 3, -1])  # Параметризируем тест
# Название "number" в декораторе "parametrize" и в аргументах автотеста должны совпадать
def test_numbers(number: int):
    assert number > 0


# Несколько параметров
@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
# В данном случае в качестве данных используется список с кортежами
def test_several_numbers(number: int, expected: int):
    # Возводим число number в квадрат и проверяем, что оно равно ожидаемому
    assert number ** 2 == expected


# Перемножение параметров
@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])  # Параметризируем по операционной системе
@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])  # Параметризируем по браузеру
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0  # Проверка указана для примера


# Параметризация фикстур
@pytest.fixture(params=["chromium", "webkit", "firefox"])
# Фикстура будет возвращать три разных браузера
# Соответственно все автотесты использующие данную фикстуру будут запускаться три раза
def browser(request: SubRequest) -> str:
    return request.param  # Внутри атрибута param находится одно из значений "chromium", "webkit", "firefox"


# В самом автотесте уже не нужно добавлять параметризацию, он будет автоматически параметризован из фикстуры
def test_open_browser(browser: str):
    # Используем фикстуру в автотесте, она вернет нам браузер в виде строки
    print(f"Running test on browser: {browser}")


# Параметризация классов
# Для тестовых классов параметризация указывается для самого класса
@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    # Параметр "user" передается в качестве аргумента в каждый тестовый метод класса

    # Параметризироваться также могут тестовые методы внутри класса - параметры будут перемножаться
    @pytest.mark.parametrize("account", ["Credit card", "Debit card"])
    def test_user_with_operations(self, user: str, account: str):
        print(f"User with operations: {user}")

    # Аналогично тут передается "user"
    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")


# Идентификаторы
# Словарь пользователей: номер телефона — ключ, описание — значение
users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}


@pytest.mark.parametrize(
    "phone_number",
    users.keys(),  # Передаем список номеров телефонов
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"  # Генерируем идентификаторы динамически
)
def test_identifiers(phone_number: str):
    pass


# --------------------------------------------------
# Примеры (корректно)

# 1. Авто - идентификаторы(эквивалентно ids = None)
# @pytest.mark.parametrize("x", [10, 20])  # ids не указаны → сгенерируются автоматически
# def test_auto_ids(x):
#     ...


# 2. Список строк
# @pytest.mark.parametrize("role", ["admin", "user"], ids=["ADMIN", "USER"])
# def test_roles(role):
#     ...


# 3. Кортеж строк
# @pytest.mark.parametrize("n", [0, 255], ids=("min", "max"))
# def test_bounds(n):
#     ...


# 4. Функция(один аргумент). При нескольких параметрах в тесте приходит КОРТЕЖ значений.
# @pytest.mark.parametrize(
#     "params",
#     [(200, {"ok": True}), (400, {"error": "bad"})],
#     ids=lambda p: f"status={p[0]}"
# )
# def test_api(params):
#     ...


# 5. Функция может вернуть None — для такого кейса будет авто - id
# @pytest.mark.parametrize("x", [0, 1, 2], ids=lambda v: "zero" if v == 0 else None)
# def test_mixed_ids(x):
#     ...


# 6. Точечные id через pytest.param
# @pytest.mark.parametrize(
#     "name",
# [
#     pytest.param("", id="empty"),
#     pytest.param("x" * 255, id="max-len"),
# ],
# )
# def test_name(name):
#     ...


# --------------------------------------------------
# Анти - примеры (и как исправить)

# 1. Длины не совпадают — НЕКОРРЕКТНО
# @pytest.mark.parametrize("a", [10, 20, 30], ids=["ten", "twenty"])
# def test_bad_len(a): ...
# Исправление:
# ids=["ten", "twenty", "thirty"]


# 2. Функция принимает два позиционных аргумента — НЕКОРРЕКТНО
# @pytest.mark.parametrize("a, b", [(1, "A"), (2, "B")], ids=lambda a, b: f"{a}-{b}")
# def test_bad_callable(a, b): ...
# Исправление:
# ids=lambda p: f"{p[0]}-{p[1]}"


# 3. Технически сработает, но плохой стиль: нестроковые id
# @pytest.mark.parametrize("x", [1, 2], ids=[1, 2])
# def test_int_ids(x): ...
# Рекомендация: использовать строки:
# ids=["one", "two"]  # или ids=["1", "2"]
