import json


def to_ounce(n, unit):
    """g or ct to ounce calculator"""
    ounce = 0
    if unit == "g":
        ounce = n / 28.34952
    elif unit == "ct":
        ounce = (n/5) / 28.34952
    return ounce


with open('kategorie.json') as f:
    categories = json.load(f)

with open('zbiór_wejściowy.json') as f:
    data = json.load(f)
    for mineral in data:
        category = [cat for cat in categories if mineral["Typ"] == cat["Typ"] and mineral["Czystość"] == cat["Czystość"]]
        if len(category) == 0:
            mineral["price"] = 0
            continue
        category = category[0]
        if "g" in mineral["Masa"]:
            ounces = to_ounce(float(mineral["Masa"][:-1].replace(",", ".")), mineral["Masa"][-1])
        elif "ct" in mineral["Masa"]:
            ounces = to_ounce(float(mineral["Masa"][:-2].replace(",", ".")), mineral["Masa"][-2:])
        mineral["price"] = round(category["Wartość za uncję (USD)"] * ounces, 2)

sorted_data = sorted(data, key=lambda x: x['price'], reverse=True)

print("Minerały o największej wartości to:\n")
for i in range(5):
    print(f"{i+1}: {sorted_data[i]['Typ']} z {sorted_data[i]['Pochodzenie']}, {sorted_data[i]['Właściciel']}.")
    print(f" - Masa: {sorted_data[i]['Masa']}")
    print(f" - Barwa: {sorted_data[i]['Barwa']}")
    print(f" - Czystość: {sorted_data[i]['Czystość']}")
    print(f"Wartość rynkowa: {sorted_data[i]['price']} USD")
    print("========================")