class Solution {
public:
    string intToRoman(int num) {
        int val[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string syb[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX" ,"V", "IV" ,"I"};
        string roman_num = "";
        int i = 0;
        while (num > 0){
            for (int j = num/val[i]; j > 0; j--){
                roman_num += syb[i];
                num -= val[i];
            }
            i++;
        }
        return roman_num;
    }
};

/*

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
            50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
        result = ''
        for value, symbol in sorted(roman_dict.items(), reverse=True):
            while num >= value:
                result += symbol
                num -= value
        return result
        
class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ""
        i = 0
        while num > 0:
            for _ in range(num//val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
*/
