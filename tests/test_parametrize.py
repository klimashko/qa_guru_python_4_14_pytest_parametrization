"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser


@pytest.mark.parametrize('browser_both_type', ['desktop'], indirect=True)
def test_github_desktop(browser_both_type):
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('browser_both_type', ['mobile'], indirect=True)
def test_github_mobile(browser_both_type):
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()