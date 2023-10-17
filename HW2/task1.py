def to_hex(num):
    hex_digits = "0123456789ABCDEF"
    hex_str = ""
    while num > 0:
        hex_str = hex_digits[num % 16] + hex_str
        num = num // 16
    return hex_str

# Пример использования функции
num = 255
hex_str = to_hex(num)
print(f"Шестнадцатеричное представление числа: {hex_str}")
print(f'Проверка результата: {hex(num)}')