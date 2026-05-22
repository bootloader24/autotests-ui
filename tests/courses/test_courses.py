import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        # Переход на страницу списка курсов
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверка отображения компонента Navbar
        courses_list_page.navbar.check_visible("username")

        # Проверка отображения компонента Sidebar
        courses_list_page.sidebar.check_visible()

        # Проверка отображения компонента заголовка "Courses"
        courses_list_page.toolbar_view.check_visible()
        # Проверка отображения пустого блока с текстом "There is no results"
        courses_list_page.check_visible_empty_view()

    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        # Открыть страницу создания курса
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        # Проверить отображение компонента панели управления курсом
        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
        # Убедиться, что отображается пустой блок для предпросмотра и загрузки изображения
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        # Проверить, что форма создания курса отображается и содержит значения по умолчанию.
        create_course_page.create_course_form.check_visible(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0",
        )
        # Проверить отображение компонента панели управления "Exercises"
        create_course_page.create_course_exercises_toolbar_view.check_visible()
        # Убедиться, что отображается блок с пустыми заданиями
        create_course_page.check_visible_exercises_empty_view()

        # Загрузить изображение для превью курса
        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        # Убедиться, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        # Заполнить форму создания курса значениями
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10",
        )
        # Нажать на кнопку создания курса
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # После редиректа на страницу со списком курсов проверить наличие компонента заголовка "Courses"
        courses_list_page.toolbar_view.check_visible()
        # Проверить корректность отображаемых данных на карточке курса
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        # Открыть страницу создания курса
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        # Заполнить форму создания курса валидными данными, загрузить изображение и нажать кнопку создания курса.
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10",
        )
        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # Проверить, что на странице с курсами отображается карточка ранее созданного курса.
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

        # Через меню карточки курса нажать на кнопку "Edit".
        courses_list_page.course_view.menu.click_edit(index=0)

        # Изменить поля: title, estimated time, description, max score, min score, нажать на кнопку сохранения изменений
        create_course_page.create_course_form.fill(
            title="Selenium",
            estimated_time="3 weeks",
            description="Selenium",
            max_score="120",
            min_score="20",
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # Проверить, что на странице с курсами отображается карточка курса с обновленными данными.
        courses_list_page.course_view.check_visible(
            index=0,
            title="Selenium",
            max_score="120",
            min_score="20",
            estimated_time="3 weeks"
        )
