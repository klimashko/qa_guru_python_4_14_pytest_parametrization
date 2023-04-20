"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from selene import browser


def test_github_desktop(browser_desktop):
    browser.element('.HeaderMenu-link--sign-in').click()



def test_github_mobile(browser_mobile):
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()


