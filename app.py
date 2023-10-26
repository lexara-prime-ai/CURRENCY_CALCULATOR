# Program: Simple Currency Converter
# Author: Irfan Ghat
# Version: 1.0.0
# License: MIT
# Features: USD -> KES
# Rates: USD -> KES 150.20, euro -> kes 180.0

rates: [str, float] = {
    "usd": 150.20,
    "euro": 180.0
}


def display_rates() -> ():
    print("* * * Available rates * * *")
    for key, value in rates.items():
        print(f"{key}: {value}")


def __init__() -> ():
    display_rates()
    print("* * * Currency calculator * * *")
    currency: str = input("Please provide a currency to convert to > e.g KES-USD, USD-KES, KES-EURO etc \n")
    currency_value: str = input("Please provide a value to convert > e.g 69 \n")

    validate_input(currency, currency_value)


def validate_input(currency: str, currency_value: str) -> ():
    if len(currency) > 0 and len(currency_value) > 0:
        perform_conversion(currency.lower(), float(currency_value))
    else:
        __init__()


def display_selected_currency(selected_currency: str, currency_value: float) -> ():
    print(f"Selected currency {selected_currency.upper()}")
    print(f"Value to convert: {currency_value}")


def perform_conversion(selected_currency: str, currency_value: float) -> ():
    if selected_currency.upper() == "KES-USD":
        display_selected_currency(selected_currency, currency_value)
        print(f"Converted {currency_value} -> {currency_value / rates.get('usd')}")
    elif selected_currency.upper() == "USD-KES":
        display_selected_currency(selected_currency, currency_value)
        print(f"Converted {currency_value} -> {currency_value * rates.get('usd')}")
    else:
        print("INVALID INPUT...\n")
        __init__()


if __name__ == '__main__':
    __init__()
