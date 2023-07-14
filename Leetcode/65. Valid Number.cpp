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
/*
// --- Other --- comment: https://leetcode.com/problems/valid-number/solutions/23728/a-simple-solution-in-python-based-on-dfa/
// https://www.youtube.com/watch?v=RYNN-tb9WxI
class Solution(object):
  def isNumber(self, s):
      """
      :type s: str
      :rtype: bool
      """
      #define a DFA
      state = [{}, 
              {'blank': 1, 'sign': 2, 'digit':3, '.':4}, 
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9, 'E': 6},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}]
      currentState = 1
      for c in s:
          if c >= '0' and c <= '9':
              c = 'digit'
          if c == ' ':
              c = 'blank'
          if c in ['+', '-']:
              c = 'sign'
          if c not in state[currentState].keys():
              return False
          currentState = state[currentState][c]
      if currentState not in [3,5,8,9]:
          return False
      return True

*/
