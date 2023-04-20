
"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser


@pytest.fixture(params=['desktop', 'mobile'])
def browser_both_type(request):
    if request.param == 'desktop':
        browser.config.hold_browser_open = True
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open('https://github.com/')
        yield request.param
        browser.quit()

    else:
        browser.config.hold_browser_open = True
        browser.config.window_width = 375
        browser.config.window_height = 667
        browser.open('https://github.com/')
        yield request.param
        browser.quit()


def test_github_desktop(browser_both_type):
    if browser_both_type == 'desktop':
        browser.element('.HeaderMenu-link--sign-in').click()
    else:
        pytest.skip('Its desktop test')


def test_github_mobile(browser_both_type):
    if browser_both_type == 'mobile':
        browser.element('.Button-label').click()
        browser.element('.HeaderMenu-link--sign-in').click()
    else:
        pytest.skip('Its mobile test')
