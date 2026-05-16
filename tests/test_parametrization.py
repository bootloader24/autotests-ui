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
