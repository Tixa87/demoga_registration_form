from selene import have
from selene.support.shared import browser


def successful_fill_form():
    browser.open('/automation-practice-form')
    #WHEN
    browser.element('#firstName').type('Alexandra')
    browser.element('#lastName').type('Ilina')
    browser.element('#userEmail').type('Ilina')
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()


'''
    $("#firstName").setValue(firstName);
    $("#lastName").setValue(lastName);
    $("#userEmail").setValue(userEmail);
    $("#genterWrapper").$(byText("Female")).click();
    $("#userNumber").setValue(numberMobile);
'''
 # THAN
''' 
 browser.element('.table').should(have.text(firstName))
'''