import requests
import json
import matplotlib.pyplot as plt
import numpy as np

wrl_string = "https://bank.gov.ua/NBU_Exchange/exchange_site?json&start=20241007&end=20241011&valcode=usd"

my_response = requests.get(wrl_string)

print(my_response)
print(my_response.content)

response_json = json.loads(my_response.content)

#Списки для збереження дат і курсів
dates = []
rates = []

print(response_json)

#Тепер заповнимо списки із наших данних
for item in response_json:
    print(item['rate'])
    dates.append(item['exchangedate'])
    rates.append(item['rate'])

#Використання стилю _mpl-gallery
plt.style.use('_mpl-gallery')

#Побудова лінійного графіку
fig, ax = plt.subplots()

ax.plot(dates, rates, marker='o', color='blue', linestyle='none' ) #Створення

ax.set(xlim=(0, len(dates)-1), ylim=(min(rates)-0.5, max(rates)+0.5)) #Налаштування осей

#Назви осей
ax.set_xlabel('Date')
ax.set_ylabel('Rate USD')
plt.xticks(range(len(dates)), dates, rotation=45)
plt.title('US dollar exchange rate(07.10.2024 - 11.10.2024)') #Назва графіка
plt.grid(True) #Додали сітку

#Відображення графіка
plt.tight_layout()
plt.show()