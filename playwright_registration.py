from playwright.sync_api import sync_playwright, expect  # Импорт Playwright для синхронного режима и проверки

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Создание контекста
    page = context.new_page() # Создание страницы

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Находим поле "Email" и заполняем его
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Находим поле "Username" и заполняем его
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    # Находим поле "Password" и заполняем его
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    # Находим кнопку "Registration" и кликаем на неё
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Проверяем, что произошёл редирект на страницу "Dashboard"
    expect(page).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")

# Остальной код регистрации нового пользователя без изменений
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json") # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    # Проверяем видимость и текст заголовка "Dashboard"
    dashboard_header = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_header).to_be_visible()  # Проверяем видимость заголовка
    expect(dashboard_header).to_have_text("Dashboard")  # Проверяем текст заголовка

    page.wait_for_timeout(5000)