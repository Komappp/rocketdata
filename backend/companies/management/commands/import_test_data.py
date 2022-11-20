""" для генерации рандомных данных использую библиотеку mimesis
Cайт: https://mimesis.name/en/master/index.html """
from random import randint

from companies.models import Company, Product
from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand
from mimesis import Address, Datetime, Finance, Person, Transport
from mimesis.enums import Gender
from mimesis.locales import Locale
from users.models import User

# Настройки mimesis для локализации данных и гендера
LOCALES = [Locale.RU, Locale.DE, Locale.PL, Locale.EN_GB]
GENDERS = [Gender.FEMALE, Gender.MALE]
# Количество данных
COMPANY_COUNT = 15
EMPLOYEES_COUNT = 50
PRODUCT_COUNT = 100
# Пароль для сотрудников будет одинаковым для удобства тестирования
PASSWORD = make_password('1')


class Command(BaseCommand):
    help = "Loads test data"

    def handle(self, *args, **options):
        print('Загрузка тестовых данных в БД')
        transport = Transport()
        date = Datetime()

        products = []
        for _ in range(PRODUCT_COUNT):
            # создаем продукцию. Не нашел ничего более внятного, чем авто
            # поэтому не удивляйтесь если завод Макдональдс
            # выпускает Maybach.
            
            products.append(Product(
                name=transport.manufacturer(),
                model=transport.car(),
                release_date=date.date()
            ))
        Product.objects.bulk_create(products)
        users = []
        for _ in range(COMPANY_COUNT):
            # выбираем случайную страну и создаем объекты mimesis
            locale = LOCALES[randint(0, len(LOCALES)-1)]
            person = Person(locale)
            finance = Finance(locale)
            address = Address(locale)
            # первый объект обязательно завод
            if not Company.objects.exists():
                hierarchy = 0
            else:
                hierarchy = randint(0, 4)
            company = Company(
                hierarchy=hierarchy,
                name=finance.company(),
                email=person.email(),
                country=address.country(),
                city=address.city(),
                street=address.street_name(),
                house_number=randint(1, 200)
            )
            company.save()

            # Если не завод связываем компанию со случайным поставщиком
            # стоящим выше по иерархии, добавляем продукцию и долг
            if company.hierarchy != 0:
                company.provider = Company.objects.filter(
                    hierarchy__lt=company.hierarchy
                ).order_by("?").first()
                company.debt = (randint(0, 5000))
                company.save()
                provider_prod = Product.objects.filter(
                        сompanies=company.provider
                )
                length = len(provider_prod)
                # немного уменьшим количество продуктов у дистрибьютеров
                provider_prod = provider_prod[:randint(length//2, length)]
                for product in provider_prod:
                    company.products.add(product)
            # если завод связываем со случайным количеством продукции
            else:
                for _ in range(randint(PRODUCT_COUNT/2, PRODUCT_COUNT)):
                    company.products.add(Product.objects.order_by("?").first())

            # количество работников зависит от размера компании
            employees = (EMPLOYEES_COUNT//(company.hierarchy+1))
            for _ in range(employees):
                gender = GENDERS[randint(0, 1)]
                users.append(User(
                    username=person.username(),
                    password=PASSWORD,
                    first_name=person.first_name(gender=gender),
                    last_name=person.last_name(gender=gender),
                    email=person.email(),
                    company=company
                ))
        User.objects.bulk_create(users)
