result = []

def divider(a, b):
    if a < b:
        raise ValueError("Помилка: перше число менше другого!")

    if b > 100:
        raise IndexError("Помилка: число більше 100!")

    return a / b


data = {
    10: 2,
    2: 5,
    "123": 4,
    18: 0,
    8: 4,
    150: 101
}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
        print("Результат:", res)

    except ValueError as e:
        print("ValueError:", e)

    except IndexError as e:
        print("IndexError:", e)

    except TypeError as e:
        print("TypeError:", e)

    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)

print("Підсумковий список:", result)





























