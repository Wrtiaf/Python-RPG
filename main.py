def parse_amount(text):
    """Возвращает сумму."""
    text = text.strip().replace(',', '.').replace(' ', '')
    try:
        amount = float(text)
    except ValueError:
        return None
    if amount <= 0:
        return None
    return round(amount, 2)


def add_expense(expenses, category, amount):
    """Добавляет сумму в категорию."""
    category = category.strip().lower()
    if not category:
        print("Категория не может быть пустой")
        return None

    if category in expenses:
        total = expenses[category] + amount
    else:
        total = amount
    expenses[category] = round(total, 2)
    return expenses[category]


def print_report(expenses):
    """Печатает отчёт по категориям."""
    if not expenses:
        print("Расходов пока нет")
        return

    print()
    print("Категория".ljust(16), "Сумма, монеты")
    print('-' * 30)
    total = 0
    for category, amount in expenses.items():
        print(category.ljust(16), amount)
        total += amount
    print('-' * 30)
    print("Итого:".ljust(16), round(total, 2))


expenses = {}

print("Трекер расходов")

while True:
    print()
    print("1. Добавить расход")
    print("2. Показать отчёт")
    print("0. Выход")
    choice = input("Выберите пункт: ").strip()

    if choice == '1':
        category = input("Категория: ").strip().lower()
        amount = parse_amount(input("Сумма: "))
        if amount is None:
            print("Нужна положительная сумма, например 100")
            continue
        total = add_expense(expenses, category, amount)
        if total is not None:
            print("\nРасход добавлен!")
    elif choice == '2':
        print_report(expenses)
    elif choice == '0':
        print("\nДо свидания!")
        break
    else:
        print("Нет такого пункта")
