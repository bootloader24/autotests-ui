import pytest  # Импортируем библиотеку pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression  # Добавляем маркировку regression
@pytest.mark.courses  # Добавляем маркировку courses
def test_empty_courses_list(courses_list_page: CoursesListPage):
    # Переход на страницу списка курсов
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка отображения компонента Navbar
    courses_list_page.navbar.check_visible("username")

    # Проверка отображения компонента Sidebar
    courses_list_page.sidebar.check_visible()

    # Проверка отображения заголовка "Courses"
    courses_list_page.check_visible_courses_title()
    # Проверка отображения кнопки создания курса
    courses_list_page.check_visible_create_course_button()
    # Проверка отображения пустого блока с текстом "There is no results"
    courses_list_page.check_visible_empty_view()


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    # 1. Открыть страницу создания курса
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    # 2. Проверить наличие заголовка "Create course"
    create_course_page.check_visible_create_course_title()
    # 3. Проверить, что кнопка создания курса недоступна для нажатия
    create_course_page.check_disabled_create_course_button()
    # 4. Убедиться, что отображается пустой блок для предпросмотра изображения
    create_course_page.check_visible_image_preview_empty_view()
    # 5. Проверить, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    # 6. Проверить, что форма создания курса отображается и содержит значения по умолчанию.
    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0",
    )
    # 7. Проверить наличие заголовка "Exercises"
    create_course_page.check_visible_exercises_title()
    # 8. Проверить наличие кнопки создания задания
    create_course_page.check_visible_create_exercise_button()
    # 9. Убедиться, что отображается блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()

    # 10. Загрузить изображение для превью курса
    create_course_page.upload_preview_image("./testdata/files/image.png")
    # 11. Убедиться, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    # 12. Заполнить форму создания курса значениями
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10",
    )
    # 13. Нажать на кнопку создания курса
    create_course_page.click_create_course_button()

    # 14. После редиректа на страницу со списком курсов проверить наличие заголовка "Courses"
    courses_list_page.check_visible_courses_title()
    # 15. Проверить наличие кнопки создания курса
    courses_list_page.check_visible_create_course_button()
    # 16. Проверить корректность отображаемых данных на карточке курса
    courses_list_page.check_visible_course_card(
        index=1,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )
