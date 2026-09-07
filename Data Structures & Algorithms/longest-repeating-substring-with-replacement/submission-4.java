class Solution {
    public int characterReplacement(String s, int k) {
        
        HashMap<Character, Integer> map = new HashMap<>();

        int left = 0;
        int result = 0;
        int maxFreq = 0; // To track the frequency of the most frequent character in the current window

        for (int right = 0; right < s.length(); right++) {
            char eachChar = s.charAt(right);

            // Add the current character to the hashmap
            map.merge(eachChar, 1, Integer::sum);

            // Update maxFreq to reflect the frequency of the most frequent character in the window
            maxFreq = Math.max(maxFreq, map.get(eachChar));

            // If the current window size minus the max frequency is greater than k, shrink the window
            while ((right - left + 1) - maxFreq > k) {
                char leftChar = s.charAt(left);
                map.put(leftChar, map.get(leftChar) - 1);
                left++;
            }

            // Update the result with the size of the current valid window
            result = Math.max(result, right - left + 1);
        }

        return result;

    }
}
