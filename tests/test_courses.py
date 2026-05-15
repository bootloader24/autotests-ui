import pytest  # Импортируем библиотеку pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression  # Добавляем маркировку regression
@pytest.mark.courses  # Добавляем маркировку courses
def test_empty_courses_list(chromium_page_with_state: Page):
    # Переходим на страницу списка курсов
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем наличие и текст заголовка "Courses"
    courses_list_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_list_title).to_be_visible()
    expect(courses_list_title).to_have_text("Courses")

    # Проверяем наличие и видимость иконки пустого блока
    empty_list_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_list_icon).to_be_visible()

    # Проверяем наличие и текст блока "There is no results"
    empty_list_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_list_title).to_be_visible()
    expect(empty_list_title).to_have_text("There is no results")

    # Проверяем наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    empty_list_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_list_description).to_be_visible()
    expect(empty_list_description).to_have_text("Results from the load test pipeline will be displayed here")
