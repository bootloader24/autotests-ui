from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()  # Создание контекста
        page = context.new_page()  # Создание страницы

        # Переходим на страницу регистрации
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполняем поле "Email"
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

        # Заполняем поле "Username"
        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill("username")

        # Заполняем поле "Password"
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("password")

        # Кликаем на кнопку "Registration"
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
        context.storage_state(path="browser-state.json")

    # Создаем новый экземпляр браузера с новым контекстом
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        # Переходим на страницу списка курсов
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверяем наличие и текст заголовка "Courses"
        courses_list_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_list_title).to_be_visible()
        expect(courses_list_title).to_have_text("Courses")

        # Проверяем наличие и видимость иконки пустого блока
        empty_list_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_list_icon).to_be_visible()

        # Проверяем наличие и текст блока "There is no results"
        empty_list_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(empty_list_title).to_be_visible()
        expect(empty_list_title).to_have_text("There is no results")

        # Проверяем наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
        empty_list_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(empty_list_description).to_be_visible()
        expect(empty_list_description).to_have_text("Results from the load test pipeline will be displayed here")
