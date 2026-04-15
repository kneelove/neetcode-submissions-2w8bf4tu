class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }

        // Map to store the last index of each character seen
        HashMap<Character, Integer> charIndexMap = new HashMap<>();
        int maxLength = 0;
        int start = 0; // Start index of the current window

        for (int end = 0; end < s.length(); end++) {
            char currentChar = s.charAt(end);

            // If the character has been seen before and is within the current window
            if (charIndexMap.containsKey(currentChar)) {
                // Move the start to the right of the last occurrence of currentChar
                start = Math.max(start, charIndexMap.get(currentChar) + 1);
            }

            // Update the last index of the current character
            charIndexMap.put(currentChar, end);

            // Update the maximum length if needed
            maxLength = Math.max(maxLength, end - start + 1);
        }

        return maxLength;
    }
}
