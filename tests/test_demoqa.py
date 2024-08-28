import allure
from demoqa_tests.pages.registration_page import RegistrationFormPage
from demoqa_tests.data import user

@allure.title("Success fill form")
def test_fill_registration_form():
    alex = user.user_data
    register_page = RegistrationFormPage()

    with allure.step("Open Registration Page"):
        register_page.open()
    with allure.step("Fill form"):
        register_page.register(alex)
    with allure.step("Check results"):
        register_page.should_register_user_with(alex)
