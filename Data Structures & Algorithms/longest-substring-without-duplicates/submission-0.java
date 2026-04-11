class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>(); 
        char[] arr = s.toCharArray(); 
        int longest = 0; 
        int n = arr.length; 
        int l = 0; 

        for (int r = 0; r < n; r++) {
            while (set.contains(arr[r])) {
                set.remove(arr[l]);
                l++;
            } 
            set.add(arr[r]);
            longest = Math.max(r - l + 1, longest); 
        }

        return longest; 
    }
}
