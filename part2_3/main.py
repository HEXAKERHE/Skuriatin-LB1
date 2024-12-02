import requests
import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET

def get_data(end_date: str = "20241130", start_date: str = "20241124") -> str:
    response = requests.get(f'https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode=usd&sort=exchangedate&order=desc')
    return response.text


def plot_exchange_rate(xml_data):
    root = ET.fromstring(xml_data)
    
    dates = []
    rates = []
    
    for currency in root.findall('currency'):
        date = currency.find('exchangedate').text
        rate = float(currency.find('rate').text)
        dates.append(date)
        rates.append(rate)
    
    plt.figure(figsize=(10, 6))
    plt.plot(dates[::-1], rates[::-1], marker='o', color='b', label='Курс долара США', linestyle='-', linewidth=2)

    plt.title('Зміна курсу долара США', fontsize=14)
    plt.xlabel('Дата', fontsize=12)
    plt.ylabel('Курс (UAH за 1 USD)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    plt.legend()
    plt.show()


def main():
    data = get_data()
    # data = get_data(end_date="20241030", start_date="20241024")
    print("Task2:")
    print(data)

    print("\n\nTask3:")
    plot_exchange_rate(data)


if __name__ == "__main__":
    main()