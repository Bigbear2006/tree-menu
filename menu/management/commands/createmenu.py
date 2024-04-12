from django.core.management import BaseCommand

from menu.models import Menu


class Command(BaseCommand):
    def handle(self, *args, **options):
        ru = Menu.objects.create(title='Россия')

        mo = Menu.objects.create(title='Московская область', parent=ru)
        kk = Menu.objects.create(title='Краснодарский край', parent=ru)
        ro = Menu.objects.create(title='Ростовская область', parent=ru)

        msk = Menu.objects.create(title='Москва', parent=mo)
        bal = Menu.objects.create(title='Балашиха', parent=mo)

        krs = Menu.objects.create(title='Краснодар', parent=kk)

        rnd = Menu.objects.create(title='Ростов-на-Дону', parent=ro)
        tag = Menu.objects.create(title='Таганрог', parent=ro)

        arb = Menu.objects.create(title='Арбат', parent=msk)
        basm = Menu.objects.create(title='Басманный район', parent=msk)

        vor = Menu.objects.create(title='Ворошиловский район', parent=rnd)
        ln = Menu.objects.create(title='Ленинский район', parent=rnd)

        print('Меню успешно создано')
