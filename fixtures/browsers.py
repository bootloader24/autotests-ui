import pytest  # Импортируем pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, \
    Page  # Импортируем класс страницы, будем использовать его для аннотации типов

from pages.authentication.registration_page import RegistrationPage

"""
Параметры context.tracing.start():
    - screenshots=True: записываются скриншоты каждого шага.
    - snapshots=True: сохраняются снапшоты DOM и стилей страницы.
    - sources=True: записываются исходные коды (например, сценарии тестов или JavaScript).
"""

@pytest.fixture  # Используем фикстуру playwright
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:  # Аннотируем возвращаемое фикстурой значение
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Создаем контекст для новой сессии браузера
    context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Включаем трейсинг

    yield context.new_page()  # Открываем новую страницу в контексте

    # В данном случае request.node.name содержит название текущего автотеста
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')  # Сохраняем трейсинг в файл
    browser.close()  # Закрываем браузер

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()  # Создание контекста
    page = context.new_page()  # Создание страницы

    # Работаем с регистрационной страницей через Page Object
    registration_page = RegistrationPage(page=page)
    # Переходим на страницу регистрации
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    # Заполняем форму регистрации
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    # Кликаем на кнопку "Registration"
    registration_page.click_registration_button()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")
    # Закрываем браузер
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Создаем контекст для новой сессии браузера
    context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Включаем трейсинг

    yield context.new_page()  # Открываем новую страницу в контексте

    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')  # Сохраняем трейсинг в файл
    browser.close()  # Закрываем браузер
