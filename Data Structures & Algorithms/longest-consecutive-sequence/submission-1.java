class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> sets = new HashSet<>(); 
        int n = nums.length; 
        int longest = 0;
        
        for (int i = 0; i < n; i++) {
            sets.add(nums[i]); 
        }

        for (int num : sets) {
            if (!sets.contains(num - 1)) {
                int curr = num; 
                int length = 1;

                while (sets.contains(num + length)) {
                    length++; 
                } 
                longest = Math.max(length, longest);
            }
        }
        return longest; 
    }
}
