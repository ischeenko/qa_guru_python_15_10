from demoqa_tests.utils import path_generate
from selene import browser, have, command
from demoqa_tests.data.user import User


class RegistrationFormPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def choose_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element(
            '..').click()

    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def choose_subject_and_hobby(self, subject, hobby):
        browser.element('#subjectsInput').type(subject).press_enter()
        browser.all('.custom-checkbox').element_by(
            have.exact_text(hobby)).perform(
            command.js.scroll_into_view).click()

    def upload_file(self, value):
        browser.element('#uploadPicture').set_value(path_generate.generate_path(
            value))

    def fill_address(self, address, state, city):
        browser.element('#currentAddress').type(address)
        browser.element("#react-select-3-input").type(state).press_enter()
        browser.element('#react-select-4-input').type(city).press_enter()
        browser.element('#submit').click()

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.choose_gender(user.gender)
        self.fill_number(user.phone_number)
        self.fill_date_of_birth(user.date_of_birth_day,
                                user.date_of_birth_month,
                                user.date_of_birth_year)
        self.choose_subject_and_hobby(user.subject, user.hobby)
        self.upload_file(user.file)
        self.fill_address(user.address, user.state, user.city)

    def should_register_user_with(self, user: User):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.date_of_birth_day} {user.date_of_birth_month},{user.date_of_birth_year}',
            user.subject,
            user.hobby,
            user.file,
            user.address,
            f'{user.state} {user.city}'
        )
        )
