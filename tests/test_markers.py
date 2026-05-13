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
