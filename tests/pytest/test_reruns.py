# используется плагин pytest-rerunfailures https://github.com/pytest-dev/pytest-rerunfailures
# pip install pytest-rerunfailures

import random

import pytest

PLATFORM = "Linux"


@pytest.mark.flaky(reruns=3, reruns_delay=2)  # Перезапуски реализуются на уровне маркировки flaky
def test_reruns():
    assert random.choice([True, False])  # Случайный выбор для демонстрации нестабильного теста


# Использование @pytest.mark.flaky для классов
@pytest.mark.flaky(reruns=3, reruns_delay=2)  # Добавили тестовый класс
class TestReruns:
    def test_rerun_1(self):
        assert random.choice([True, False])

    def test_rerun_2(self):
        assert random.choice([True, False])


# Использование @pytest.mark.flaky с условиями
@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == "Windows")  # Перезапуск при выполнении условия
def test_rerun_with_condition():
    assert random.choice([True, False])
