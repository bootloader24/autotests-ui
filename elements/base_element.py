from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    # Метод принимает кейворд аргументы (kwargs)
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:  # объект Locator для взаимодействия с элементом
        # Инициализирует объект локатора, подставляя динамические значения в локатор.
        locator = self.locator.format(**kwargs)
        # Возвращаем объект локатора c индексом nth
        return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        # "Лениво" инициализируем локатор
        locator = self.get_locator(nth, **kwargs)  # передаем nth в get_locator
        # Выполняем нажатие на элемент
        locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        # Инициализируем локатор "лениво"
        locator = self.get_locator(nth, **kwargs)
        # Проверяем, что элемент виден на странице
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_text(text)
