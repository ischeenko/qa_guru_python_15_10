from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth_year: str
    date_of_birth_month: str
    date_of_birth_day: str
    subject: str
    hobby: str
    file: str
    address: str
    state: str
    city: str


user_data = User(
    first_name='Alexander',
    last_name='Ischenko',
    email='ischeenko@gmail.com',
    gender='Male',
    phone_number='7978150151',
    date_of_birth_year='1994',
    date_of_birth_month='January',
    date_of_birth_day='13',
    subject='English',
    hobby='Sports',
    file='images.jpeg',
    address='Saki',
    state='NCR',
    city='Delhi'
)