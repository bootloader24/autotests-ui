from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    # Решение ошибки 3 с попыткой работы с элементом до его появления в DOM-дереве
    # page.goto(
    #     "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
    #     wait_until='networkidle'  # Ждем завершения сетевых запросов
    # )

    # Ошибка 1: Элемент/локатор не найден на странице
    # Пытаемся проверить, что несуществующий локатор виден на странице
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    # Ошибка 2: Некорректное взаимодействие с элементом
    # Пытаемся ввести текст в кнопку Login
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    # Ошибка 3: Работа с элементом до его появления в DOM-дереве
    # Пытаемся изменить текст заголовка
    page.evaluate("""
                  const title = document.getElementById('authentication-ui-course-title-text');
                  title.textContent = 'New Text';
                  """)