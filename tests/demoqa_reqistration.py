from selene import have
from selene.support.shared import browser


def successful_fill_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Alexandra')
    browser.element('#lastName').type('Ilina')
    browser.element('#userEmail').type('Ilina')
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    browser.element('#userNumber').type('89111212121')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('August')
    browser.element('.react-datepicker__year-select').type('1987')
    browser.element(f'.react-datepicker__day--0{23}').click()


    browser.element('#subjectsInput').type('Chemistry').press_enter()
    #browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
    #browser.element('[for=hobbies-checkbox-1]').click()
    browser.all('[type=checkbox]').element_by(have.text('Sports')).click()


'''
    // BirthDay Window
        $("#dateOfBirthInput").click();
        $(".react-datepicker__month-select").selectOption("August");
        $(".react-datepicker__year-select").selectOption("1987");
        $(".react-datepicker__day--023").click();

        $("#subjectsInput").setValue(subjects).pressEnter();
        $("#hobbiesWrapper").$(byText("Sports")).click();

        $("#uploadPicture").uploadFile(new File("src/test/resources/приветственное фото.jpg"));
        $("#currentAddress").setValue(current_Address);
        $("#state").click();
        $("#stateCity-wrapper").$(byText("NCR")).click();
        $("#city").click();
        $("#stateCity-wrapper").$(byText("Gurgaon")).click();
        $("#submit").click();

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
browser.element('.table').should(have.text('Alexandra'))