import os
from selene import have, command
from selene.support.shared import browser
import tests


def test_successful_fill_form(open_browser):
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        have.size_greater_than_or_equal(3)
    )
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
    browser.element('#firstName').type('Alexandra')
    browser.element('#lastName').type('Ilina')
    browser.element('#userEmail').type('tixa@tixa.com')
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    browser.element('#userNumber').type('8911121212')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('August')
    browser.element('.react-datepicker__year-select').type('1987')
    browser.element(f'.react-datepicker__day--0{23}').click()
    browser.element('#subjectsInput').type('Chemistry').press_enter()
    browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#currentAddress').type('Rozino BB')
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), 'resources/приветственное фото1.jpg')
        )
    )
    browser.element('#submit').press_enter()
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Alexandra Ilina',
            'tixa@tixa.com',
            'Female',
            '8911121212',
            '23 August,1987',
            'Chemistry',
            'Reading',
            'приветственное фото1.jpg',
            'Rozino BB',
            'NCR Delhi',
        )
    )
