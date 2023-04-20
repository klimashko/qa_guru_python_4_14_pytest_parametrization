"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser


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
