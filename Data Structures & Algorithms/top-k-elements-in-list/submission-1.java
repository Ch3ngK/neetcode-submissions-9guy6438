class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int length = nums.length; 
        List<Integer>[] freqs = new List[length + 1]; 
        int[] output = new int[k]; 
        int index = 0; 
        HashMap<Integer, Integer> map = new HashMap<>(); 
        
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        for (int key : map.keySet()) {
            int f = map.get(key); 
            if (freqs[f] == null) {
                freqs[f] = new ArrayList<>(); 
                freqs[f].add(key); 
            } else { 
                freqs[f].add(key); 
            }
        }

        for (int j = length; j >= 0 && index < k; j--) {
            if (freqs[j] != null) {
                for (int n : freqs[j]) {
                    output[index] = n;
                    index++; 
                    if (index == k) {
                        break; 
                    }
                }
            }
        }
        return output; 
    }
}
