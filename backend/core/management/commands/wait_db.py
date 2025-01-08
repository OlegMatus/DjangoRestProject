from django.core.management import BaseCommand
from django.db import OperationalError, connection
from django.db.backends.mysql.base import DatabaseWrapper
import time

connection: DatabaseWrapper = connection

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        con_db = False

        while not con_db:
            try:
                connection.ensure_connection()
                con_db = True
            except OperationalError:
                self.stdout.write("Database unavailable, wait 3 seconds...")
                time.sleep(3)
            # except OperationalError: #Якщо при запуску нашої команди connection до db не вдасться то спрацює цей except і чекатиме 3сек потім спрацює знову цикл поки не законектиться
        self.stdout.write(self.style.SUCCESS("Database available!"))
        #   якщо спрацює і ми вийдемо з циклу в такому разі Database available! і після цього запускатиметься апка
