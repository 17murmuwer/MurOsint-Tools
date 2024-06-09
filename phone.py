import phonenumbers as pnumb
import json
import requests
import time
import os
from sys import stderr
import phonenumbers as pnumb

from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
print('''

• ▌ ▄ ·. ▄• ▄▌▄▄▄  • ▌ ▄ ·. ▄• ▄▌▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄       ▄▄▄· ▄ .▄       ▐ ▄ ▄▄▄ .▄▄▄▄▄▄▄▄   ▄▄▄·  ▄▄· ▄ •▄ 
·██ ▐███▪█▪██▌▀▄ █··██ ▐███▪█▪██▌██· █▌▐█▀▄.▀·▀▄ █·    ▐█ ▄███▪▐█▪     •█▌▐█▀▄.▀·•██  ▀▄ █·▐█ ▀█ ▐█ ▌▪█▌▄▌▪
▐█ ▌▐▌▐█·█▌▐█▌▐▀▀▄ ▐█ ▌▐▌▐█·█▌▐█▌██▪▐█▐▐▌▐▀▀▪▄▐▀▀▄      ██▀·██▀▐█ ▄█▀▄ ▐█▐▐▌▐▀▀▪▄ ▐█.▪▐▀▀▄ ▄█▀▀█ ██ ▄▄▐▀▀▄·
██ ██▌▐█▌▐█▄█▌▐█•█▌██ ██▌▐█▌▐█▄█▌▐█▌██▐█▌▐█▄▄▌▐█•█▌    ▐█▪·•██▌▐▀▐█▌.▐▌██▐█▌▐█▄▄▌ ▐█▌·▐█•█▌▐█ ▪▐▌▐███▌▐█.█▌
▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀▀▀  █▪▀▀▀ ▀▀▀  ▀▀▀▀ ▀▪ ▀▀▀ .▀  ▀    .▀   ▀▀▀ · ▀█▄▀▪▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀ ·▀  ▀
''')
number = input("Введите номер: ")
parsing = pnumb.parse(number, "ID")

print("Инфо ", parsing)
print("Международный формат:", pnumb.format_number(parsing, pnumb.PhoneNumberFormat.INTERNATIONAL))
print("Национальный формат:", pnumb.format_number(parsing, pnumb.PhoneNumberFormat.NATIONAL))
print("Номер действителен:", pnumb.is_valid_number(parsing))
print("Можно связаться на международном уровне:", pnumb.is_possible_number(parsing))

# Define loc, isp, and tz before using them
loc = pnumb.geocoder.description_for_number(parsing, "en")
isp = pnumb.carrier.name_for_number(parsing, "en")
tz = pnumb.timezone.time_zones_for_number(parsing)

print("Расположение", loc)
print("Номер кода города", pnumb.region_code_for_number(parsing))
print("Тип номера:", pnumb.number_type(parsing))
print("Это конкретный оператор:", pnumb.is_carrier_specific(parsing))
print("Интернет-провайдер:", isp)
print("Часовой пояс:", tz)

parsed_number = pnumb.parse(number, "ID")
region_code = pnumb.region_code_for_number(parsed_number)
jenis_provider = pnumb.carrier.name_for_number(parsed_number, "en")
location = pnumb.geocoder.description_for_number(parsed_number, "en")
is_valid_number = pnumb.is_valid_number(parsed_number)
is_possible_number = pnumb.is_possible_number(parsed_number)
formatted_number = pnumb.format_number(parsed_number, pnumb.PhoneNumberFormat.INTERNATIONAL)
formatted_number_for_mobile = pnumb.format_number_for_mobile_dialing(parsed_number, "ID", with_formatting=True)
number_type = pnumb.number_type(parsed_number)
timezone1 = pnumb.timezone.time_zones_for_number(parsed_number)
timezoneF = ', '.join(timezone1)

print("==========Информация о номере")
print(f"Локация             : {location}")
print(f"Код Региона         : {region_code}")
print(f"Временная зона      : {timezoneF}")
print(f"Оператор            : {jenis_provider}")
print(f"Валидность номера   : {is_valid_number}")
print(f"Возможный номер     : {is_possible_number}")
print(f"Интернациональный формат: {formatted_number}")
print(f"Мобильный формат    : {formatted_number_for_mobile}")
print(f"Оригинальный номер  : {parsed_number.national_number}")
print(f"E164 формат         : {pnumb.format_number(parsed_number, pnumb.PhoneNumberFormat.E164)}")
print(f"Страны код          : {parsed_number.country_code}")
print(f"Локальный номер     : {parsed_number.national_number}")
if number_type == pnumb.PhoneNumberType.MOBILE:
    print("Type               : This is a mobile number")
elif number_type == pnumb.PhoneNumberType.FIXED_LINE:
    print("Type               : This is a fixed-line number")
else:
    print("Type               : This is another type of number")
