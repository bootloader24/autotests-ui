import pytest  # Импортируем pytest
from playwright.sync_api import Playwright, \
    Page  # Импортируем класс страницы, будем использовать его для аннотации типов


@pytest.fixture  # Используем фикстуру playwright
def chromium_page(playwright: Playwright) -> Page:  # Аннотируем возвращаемое фикстурой значение
    # Ниже идет инициализация и открытие новой страницы
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False)

    # Передаем страницу для использования в тесте
    yield browser.new_page()

    # Закрываем браузер после выполнения тестов
    browser.close()
