import requests
import tkinter as tk
from tkinter import ttk, messagebox

URL = "https://open.er-api.com/v6/latest/"


CURRENCIES = {
    "RUB": "Российский рубль",
    "USD": "Американский доллар",
    "EUR": "Евро",
    "GBP": "Британский фунт",
    "CNY": "Китайский юань",
    "KZT": "Казахстанский тенге",
}


def get_rate(base, target):
    """Возвращает курс валюты base к валюте target (или None при ошибке)."""
    try:
        response = requests.get(URL + base)
        data = response.json()
        return data["rates"][target]
    except requests.RequestException:
        messagebox.showerror("Ошибка", "Не удалось получить данные с сервера.")
        return None
    except KeyError:
        messagebox.showerror("Ошибка", f"Нет курса {base} -> {target}.")
        return None


def exchange():
    """Запрашивает курсы для обеих базовых валют и выводит их."""
    base1 = combo_base1.get()
    base2 = combo_base2.get()
    target = combo_target.get()

    if base1 == target or base2 == target:
        messagebox.showwarning("Внимание", "Базовая и целевая валюты не должны совпадать.")
        return

    rate1 = get_rate(base1, target)
    rate2 = get_rate(base2, target)

    if rate1 is None or rate2 is None:
        return

    label_base1.config(text=f"{CURRENCIES.get(base1, base1)}: 1 {base1} = {rate1:.4f} {target}")
    label_base2.config(text=f"{CURRENCIES.get(base2, base2)}: 1 {base2} = {rate2:.4f} {target}")



window = tk.Tk()
window.title("Курсы обмена валют")
window.geometry("400x380")


label_title1 = tk.Label(window, text="Базовая валюта")
label_title1.pack()
combo_base1 = ttk.Combobox(window, values=list(CURRENCIES.keys()))
combo_base1.set("EUR")
combo_base1.pack(pady=5)
label_base1 = tk.Label(window, text="")
label_base1.pack(pady=5)


label_title2 = tk.Label(window, text="Вторая базовая валюта")
label_title2.pack()
combo_base2 = ttk.Combobox(window, values=list(CURRENCIES.keys()))
combo_base2.set("USD")
combo_base2.pack(pady=5)
label_base2 = tk.Label(window, text="")
label_base2.pack(pady=5)


label_title3 = tk.Label(window, text="Целевая валюта")
label_title3.pack()
combo_target = ttk.Combobox(window, values=list(CURRENCIES.keys()))
combo_target.set("RUB")
combo_target.pack(pady=5)


button = tk.Button(window, text="Получить курс обмена", command=exchange)
button.pack(pady=10)

window.mainloop()
