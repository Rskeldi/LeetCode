class Solution:
    def romanToInt(self, s: str) -> int:
        s = list(s)
        result = []
        roman_dict = {
            "O": 0,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        for x in range(len(s)):
            if x == len(s) - 1:
                result.append(roman_dict[s[x]])
            elif roman_dict.get(s[x] + s[x + 1]):
                result.append(roman_dict[s[x] + s[x+1]])
                s[x+1] = "O"
            else:
                result.append(roman_dict[s[x]])
        return sum(result)
