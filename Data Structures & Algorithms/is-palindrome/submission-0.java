class Solution {
    public boolean isPalindrome(String s) {
        char[] letters = s.toCharArray();
        int length = s.length();
        int start = 0;  
        int end = length - 1; 

        while (start < end) {
            if (!Character.isLetterOrDigit(letters[start])) {
                start++;
                continue;
            }

            if (!Character.isLetterOrDigit(letters[end])) {
                end--;
                continue;
            }

            if (Character.toLowerCase(letters[start]) != Character.toLowerCase(letters[end])) {
                return false;  
            } else {
                start++;
                end--; 
            }
        }

        return true; 
    }
}
