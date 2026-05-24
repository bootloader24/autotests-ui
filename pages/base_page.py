from typing import Pattern

import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    """
    Стратегии ожидания:
    networkidle — нет активных сетевых запросов. Хороший базовый вариант для перехода между страницами
    domcontentloaded — загружен DOM, но ресурсы могут ещё подгружаться. Быстрее, если не нужно ждать все ресурсы
    load — страница полностью загружена (включая ресурсы). Используется реже, когда важна полная загрузка страницы 
    """

    def visit(self, url: str):
        with allure.step(f'Opening the url "{url}"'):
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches pattern "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)
