import pytest
from selene import browser


@pytest.fixture
def browser_desktop():
    browser.config.hold_browser_open = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com/')
    yield
    browser.quit()


@pytest.fixture
def browser_mobile():
    browser.config.hold_browser_open = True
    browser.config.window_width = 375
    browser.config.window_height = 667
    browser.open('https://github.com/')
    yield
    browser.quit()


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
