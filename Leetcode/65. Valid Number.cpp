class Solution {
public:
    bool isNumber(string s) {
        bool numSeen = false;
        bool eSeen = false; 
        bool dotSeen = false;

        for (int i = 0; i < s.length(); ++i){
            char c = s[i];
            if (isdigit(c)){
                numSeen = true;
            }
            else if (c == 'e' || c == 'E'){
                if (eSeen || !numSeen) return false;
                eSeen = true;
                numSeen = false; // we still need number following 'e'
            }
            else if (c == '.'){
                if (eSeen || dotSeen) return false; // dot can be after e as it is the power
                dotSeen = true;
            }
            else if (c == '-' || c == '+'){
                if (i != 0 && s[i-1] != 'e' && s[i-1] != 'E') return false; // +6e-1
            }
            else return false;
        }
        return numSeen;
    }
};
// Test Cases:
// "0"
// "e"
// "."
// "2"
// "3."
// ".1"
// "3E+7"
// "+6e-1"
