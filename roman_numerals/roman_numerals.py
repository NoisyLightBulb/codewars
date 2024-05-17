class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        int_to_roman = {
            1: 'I',
            4: 'IX',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        roman_num = []






        return roman_num



    @staticmethod
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
