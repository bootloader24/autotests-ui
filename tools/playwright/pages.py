import allure
from playwright.sync_api import Playwright, Page

from config import settings # импорт настроек

"""
Параметры context.tracing.start():
    - screenshots=True: записываются скриншоты каждого шага.
    - snapshots=True: сохраняются снапшоты DOM и стилей страницы.
    - sources=True: записываются исходные коды (например, сценарии тестов или JavaScript).
"""

def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        storage_state: str | None = None
) -> Page:
    browser = playwright.chromium.launch(headless=settings.headless)
    # Создаем контекст для новой сессии браузера с указанием директории для сохранения видеозаписей
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Включаем трейсинг
    # Отдельная переменная page требуется для получения доступа к пути к видеозаписи
    page = context.new_page()

    yield page  # Открываем новую страницу в контексте

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))  # Сохраняем трейсинг в файл
    browser.close()  # Закрываем браузер

    # Прикрепляем файл с трейсингом к Allure отче
    allure.attach.file(settings.tracing_dir.joinpath(f'{test_name}.zip'), name='trace', extension='zip')
    # Прикрепляем видео автотеста к Allure отчету
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
