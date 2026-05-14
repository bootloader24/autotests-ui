import pytest  # Импортируем библиотеку pytest
from playwright.sync_api import expect, Page


# Запуск только этого теста: python -m pytest -m registration -s -v
@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.registration  # Добавили маркировку registration
def test_successful_registration(chromium_page: Page):
    # Переходим на страницу регистрации
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Находим поле "Email" и заполняем его
    email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Находим поле "Username" и заполняем его
    username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    # Находим поле "Password" и заполняем его
    password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    # Находим кнопку "Registration" и кликаем на неё
    registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Проверяем, что произошёл редирект на страницу "Dashboard"
    expect(chromium_page).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    # Проверяем заголовок страницы "Dashboard"
    dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
