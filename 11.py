def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    user_input = int(input("Введите целое число: "))
    result = is_prime(user_input)
    print(f"Является ли число простым: {result}")
