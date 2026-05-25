from enum import Enum
from typing import Self

from pydantic import BaseModel, EmailStr, FilePath, HttpUrl, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",  # Указываем, из какого файла читать настройки
        env_file_encoding="utf-8",  # Указываем кодировку файла
        env_nested_delimiter=".",  # Указываем разделитель для вложенных переменных
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    browser_state_file: FilePath

    # метод автоматически создаёт необходимые директории и файлы, если они отсутствуют
    @classmethod
    def initialize(cls) -> Self:  # Возвращает экземпляр класса Settings
        # Указываем пути
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        browser_state_file = FilePath("browser-state.json")

        # Создаем директории, если они не существуют
        videos_dir.mkdir(exist_ok=True)  # Если директория существует, то игнорируем ошибку
        tracing_dir.mkdir(exist_ok=True)
        # Создаем файл состояния браузера, если его нет
        browser_state_file.touch(exist_ok=True)  # Если файл существует, то игнорируем ошибку

        # Возвращаем модель с инициализированными значениями
        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            browser_state_file=browser_state_file
        )

# Проверка корректности настроек:
# print(Settings())

# Проверка инициализации директорий и файлов:
# print(Settings.initialize())

# Инициализируем настройки
settings = Settings.initialize()
