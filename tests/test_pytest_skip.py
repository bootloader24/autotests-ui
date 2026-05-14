import pytest


@pytest.mark.skip(reason="Фича в разработке")  # Указываем маркировку, которая пропустит данный автотест
def test_feature_in_development():
    pass


@pytest.mark.skip(reason="Фича в разработке")  # Можно аналогично маркировать классы целиком
class TestSuiteSkip:
    def test_feature_in_development_1(self):
        pass

    def test_feature_in_development_2(self):
        pass
