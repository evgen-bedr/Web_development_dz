from pydantic import BaseModel, EmailStr, Field, model_validator, ValidationError


class Address(BaseModel):
    city: str = Field(min_length=2)
    street: str = Field(min_length=3)
    house_number: int = Field(gt=0)


class UserRegistration(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    is_employed: bool
    address: Address

    @model_validator(mode='before')
    def check_age_and_employment(cls, values):
        age = values.get('age')
        is_employed = values.get('is_employed')

        if age is None or age < 1 or age > 120:
            raise ValueError("Возраст должен быть между 0 и 120")
        if is_employed is not None and is_employed is not True:
            raise ValueError("Статус 'is_employed' должен быть True")

        return values


def json_output(json_data: str):
    try:
        user = UserRegistration.parse_raw(json_data)
        return user.json()
    except ValidationError as err:
        return str(err)


valid_json = '''
{
    "name": "Евгений",
    "age": 30,
    "email": "evg@gmail.com",
    "is_employed": true,
    "address": {
        "city": "Киев",
        "street": "Халаменюка",
        "house_number": 12
    }
}
'''

invalid_json = '''
{
    "name": "Ольга",
    "age": 30,
    "email": "o.g@gmail.com",
    "is_employed": false,
    "address": {
        "city": "Одесса",
        "street": "Павлова",
        "house_number": 1
    }
}
'''

print("*** Успешная регистрация ***")
print(json_output(valid_json))
print("\n*** Ошибка валидации ***")
print(json_output(invalid_json))
