class Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length; 
        int[] prefixes = new int[length]; 
        int[] suffixes = new int[length]; 
        int[] output = new int[length]; 

        prefixes[0] = 1;
        //Compute all the prefixes
        for (int i = 1; i < length; i++) {
            prefixes[i] = prefixes[i - 1] * nums[i - 1]; 
        } 

        suffixes[length - 1] = 1;
        for (int j = length - 2; j >= 0; j--) {
            suffixes[j] = suffixes[j + 1] * nums[j + 1]; 
        }
        
        for (int k = 0; k < length; k++) {
            output[k] = prefixes[k] * suffixes[k];
        }
        return output; 
    }
}  
