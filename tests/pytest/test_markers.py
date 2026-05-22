import pytest


# Определение маркировок и запуск
# pytest -m smoke
# python -m pytest -m "smoke and regression"
# python -m pytest -m "smoke or regression"
@pytest.mark.smoke
def test_smoke_case():
    assert 1 + 1 == 2


@pytest.mark.regression
def test_regression_case():
    assert 2 * 2 == 4


# Использование маркировок для запуска сложных сценариев - быстрые и медленные тесты
# python -m pytest -m fast
@pytest.mark.fast
def test_fast():
    pass


@pytest.mark.slow
def test_slow():
    pass


# Применение маркировок к классам
@pytest.mark.smoke
class TestSuite:
    def test_case1(self):
        ...

    def test_case2(self):
        ...


# Маркировка класса и отдельных тестов внутри класса
# Запуск тестов, которые имеют маркировку regression и не имеют маркировки slow:
# pytest -m "regression and not slow"
@pytest.mark.regression  # действует на все тесты класса
class TestUserAuthentication:

    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):  # для запуска только этого теста: pytest -m "regression and slow"
        pass

    def test_logout(self):
        pass


# Несколько маркировок на одном тесте
# Запуск тестов с маркировкой critical: pytest -m "critical"
# Запуск всех smoke или critical тестов: pytest -m "smoke or critical"
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    pass


# Все тесты класса TestUserInterface помечены как ui-тесты
# Тест test_login_button также помечен как smoke и critical
# Тест test_forgot_password_link относится к регрессионным
# Тест test_signup_form помечен как smoke
# Запуск только smoke тестов: pytest -m "smoke"
# Запуск тестов, которые помечены как ui и одновременно относятся к regression: pytest -m "ui and regression"
@pytest.mark.ui
class TestUserInterface:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass

    @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass
