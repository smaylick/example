import pytest
from selene import browser, have

@pytest.fixture()
def open_login_form():
    browser.open('http://users.bugred.ru/user/login/index.html')

    yield
    print('Я выполнился после теста')
def test_authorization_2(open_login_form):
    browser.element('[name=login]').click().type('smaylickserik1@mail.ru')
    browser.element('/html/body/div[3]/div[1]/div[1]/form/table/tbody/tr[2]/td[2]/input').click().type('123')
    browser.element('[value=Авторизоваться]').click()
    browser.element('[data-toggle=dropdown]').should(have.exact_text('smaylickserik'))
