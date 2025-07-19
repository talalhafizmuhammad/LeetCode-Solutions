class Solution {
public:
    bool isValid(string word) {
        if (word.length() < 3) return false;

        int vowels = 0;
        int consonants = 0;

        for (char ch : word) {
            if (!isalnum(ch)) return false;

            if (isalpha(ch)) {
                char lower = tolower(ch);
                if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
                    vowels++;
                } else {
                    consonants++;
                }
            }
        }

        return vowels > 0 && consonants > 0;
    }
};
