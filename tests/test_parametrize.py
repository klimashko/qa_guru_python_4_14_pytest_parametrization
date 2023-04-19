
"""
Переопределите параметр с помощью indirect параметризации на уровне теста
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
        yield
        browser.quit()

    else:
        browser.config.hold_browser_open = True
        browser.config.window_width = 375
        browser.config.window_height = 667
        browser.open('https://github.com/')
        yield
        browser.quit()


@pytest.mark.parametrize('browser_both_type', ['desktop'], indirect=True)
def test_github_desktop(browser_both_type):
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('browser_both_type', ['mobile'], indirect=True)
def test_github_mobile(browser_both_type):
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()