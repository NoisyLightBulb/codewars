def to_roman(number: int) -> str:
    int_to_roman = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
]

    roman_num = []

    #iterate through conversion list
    for (value, symbol) in int_to_roman:

        #check if number is greater/equal to the value in the dictionary
        while number >= value:
            #add symbol to current roman number
            roman_num.append(symbol)

            #subtract value of symbol from integer number
            number -= value

    #join and return list values
    return ''.join(roman_num)



def from_roman(roman_num: str) -> int:
    roman_to_int = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
        'CM': 900,
        'CD': 400,
        'XC': 90,
        'XL': 40,
        'IX': 9,
        'IV': 4
    }

    pos = 0
    sum = 0

    #iterate through the string
    while pos < len(roman_num):
        #check for multi character numbers
        if pos+1 < len(roman_num) and roman_num[pos:pos+2] in roman_to_int:
            #add multi character value to sum
            sum += roman_to_int[roman_num[pos:pos+2]]

            #increase position
            pos += 2

        else:
            #add single character number to sum
            sum += roman_to_int[roman_num[pos:pos+1]]

            #increase position
            pos += 1

    return sum






print(to_roman(1990))  # Output: 'MCMXC'
print(to_roman(2008))  # Output: 'MMVIII'
print(to_roman(1666))  # Output: 'MDCLXVI'



print(from_roman('MCMXC'))  # Output: 1990
print(from_roman('MMVIII')) # Output: 2008
print(from_roman('MDCLXVI')) # Output: 1666
