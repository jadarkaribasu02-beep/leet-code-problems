class Solution {
    public String smallestPalindrome(String s) {
        int[] letterCount = new int[26];

        // Count frequency of each character
        for (char ch : s.toCharArray()) {
            letterCount[ch - 'a']++;
        }

        StringBuilder leftSide = new StringBuilder();
        StringBuilder middleChar = new StringBuilder();

        // Build left half and middle character if needed
        for (int i = 0; i < 26; i++) {
            int count = letterCount[i];

            if (count % 2 != 0) {
                // Only one odd character can be in the middle
                if (middleChar.length() == 0) {
                    middleChar.append((char) (i + 'a'));
                }
                count--; // reduce count to make it even
            }

            for (int j = 0; j < count / 2; j++) {
                leftSide.append((char) (i + 'a'));
            }
        }

        // Construct palindrome
        StringBuilder result = new StringBuilder();
        result.append(leftSide);
        result.append(middleChar);
        result.append(new StringBuilder(leftSide).reverse());

        return result.toString();
    }
}
