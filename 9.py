num = int(input())
def numeral_word(num):
    numerals = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
        10: "десять",
        11: "одиннадцать",
        12: "двенадцать"
    }
    return numerals.get(num, "")

if __name__ == "__main__":
    for i in range(1, 13):
        print(numeral_word(i))
