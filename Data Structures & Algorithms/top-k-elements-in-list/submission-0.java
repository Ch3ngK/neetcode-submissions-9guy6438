class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int length = nums.length; 
        int[] output = new int[k];
        HashMap<Integer, Integer> map = new HashMap<>(); 

        for (int i = 0; i < length; i++) {
            int curr = nums[i];
            map.put(curr, map.getOrDefault(curr, 0) + 1); 
        }

        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            (a, b) -> b[1] - a[1]
        ); 

        for (int key : map.keySet()) {
            maxHeap.add(new int[] {key, map.get(key)});
        }
        
        for (int i = 0; i < k; i++) {
            output[i] = maxHeap.poll()[0]; 
        }
        return output;
    }
}
