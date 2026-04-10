class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length; 
        int[] prefixes = new int[n];
        int[] suffixes = new int[n]; 
        int[] output = new int[n]; 

        prefixes[0] = 1; 
        for (int i = 1; i < n; i++) {
            prefixes[i] = prefixes[i - 1] * nums[i - 1]; 
        }

        suffixes[n - 1] = 1; 
        for (int j = n - 2; j >=0; j--) {
            suffixes[j] = suffixes[j + 1] * nums[j + 1];
        }

        for (int k = 0; k < n; k++) {
            output[k] = prefixes[k] * suffixes[k]; 
        }

        return output;
    }
}  
