import requests
import tkinter
from tkinter import ttk
from ttkthemes import ThemedTk

api_key = "Insert Your Open Exchange Rates API Key Here"
first_currency = "USD"

url = f'https://open.er-api.com/v6/latest/{first_currency}?apikey={api_key}'
response = requests.get(url)
data = response.json()


interface = ThemedTk(theme='adapta')
interface.title('Currency Converter')

all_currencies = ["USD", "EUR", "RON", "GBP", "JPY", "MDL", "NOK", "UAH", "HUF"]

print(data)


def convert():
    selected_first_currency = first_currency.get()
    selected_second_currency = second_currency.get()

    if response.status_code == 200:
        rates = data['rates']
        currency_rate = rates[selected_second_currency]
        number_of_first_currency = float(number_insert.get())
        result_number = number_of_first_currency * currency_rate

        result_label.config(
            text=f"{number_of_first_currency:.2f} {selected_first_currency} = {result_number:.2f} {selected_second_currency}")
    else:
        result_label.config(text='Convert Error (API)')


# Building interface

number_label = ttk.Label(interface, text="Amount of currency", font=("Arial", 12))
number_insert = ttk.Entry(interface)

first_currency_label = ttk.Label(interface, text="First Currency", font=("Arial", 12))
first_currency = tkinter.StringVar(value="USD")
first_currency_gi = ttk.Combobox(interface, textvariable=first_currency, values=all_currencies)

second_currency_label = ttk.Label(interface, text="Second Currency", font=("Arial", 12))
second_currency = tkinter.StringVar(value="RON")
second_currency_gi = ttk.Combobox(interface, textvariable=second_currency, values=all_currencies)

result_label = ttk.Label(interface, text='Result')
convert_button = ttk.Button(interface, text='Convert', command=convert)

# Setting all elements positions

number_label.grid(row=0, column=0, padx=10, pady=10)
number_insert.grid(row=0, column=1, padx=10, pady=10)

first_currency_label.grid(row=1, column=0, padx=10, pady=10)
first_currency_gi.grid(row=1, column=1, padx=10, pady=10)

second_currency_label.grid(row=2, column=0, padx=10, pady=10)
second_currency_gi.grid(row=2, column=1, padx=10, pady=10)

result_label.grid(row=4, column=0, columnspan=2, pady=10)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

interface.mainloop()
