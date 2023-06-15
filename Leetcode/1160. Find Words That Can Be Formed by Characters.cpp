class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int result = 0;
        vector <int> char_freq(26, 0);
        for (char c : chars){
            char_freq[c - 'a']++;
        }
        for (string word : words){
            vector <int> word_freq(26, 0);
            for (char c : word){
                word_freq[c - 'a']++;
            }
            bool good = true;
            for (int i = 0; i < 26; i++){
                if (word_freq[i] > char_freq[i]){
                    good = false;
                    break;
                }
            }
            if (good){
                result += word.size();
            }
        }
        return result;
    }
};

// Python
/*
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        char_freq = [0] * 26
        for c in chars:
            char_freq[ord(c) - ord('a')] += 1
        for word in words:
            word_freq = [0] * 26
            for c in word:
                word_freq[ord(c) - ord('a')] += 1
            if all(word_freq[i] <= char_freq[i] for i in range(26)):
                result += len(word)
        return result
        
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        char_count = collections.Counter(chars)
        for word in words:
            word_count = collections.Counter(word)
            if all(word_count[c] <= char_count[c] for c in word_count):
                result += len(word)
        return result
        
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            if Counter(word) <= Counter(chars):
                ans += len(word)
        return ans
*/
