import math

def intToRoman(num: int) -> str:
    romans = ""
    symbols = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    for symbol, value in symbols.items():
        if num % value < num:
            romans += math.floor(num/value) * symbol
            num = num % value
    return romans
        

if __name__ == "__main__":
    print(intToRoman(58))
    print(intToRoman(244))