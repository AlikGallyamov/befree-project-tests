from befree_tests.pages.login_page import LoginPage


def test_login(android_app_manage):
    login_page = LoginPage()
    login_page.open_page()
    login_page.auth()
    login_page.check_profile()
