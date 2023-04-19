"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser
import time


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


def test_github_desktop(browser_desktop):
    time.sleep(5)
    browser.element('.HeaderMenu-link--sign-in').click()
    time.sleep(5)


def test_github_mobile(browser_mobile):
    time.sleep(5)
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    time.sleep(5)

