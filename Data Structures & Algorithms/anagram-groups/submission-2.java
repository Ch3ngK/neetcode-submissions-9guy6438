class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>(); 
        int n = strs.length; 
        for (int i = 0; i < n; i++) {
            int[] chars = new int[26];
            String curr = strs[i]; 
            char[] arr = curr.toCharArray(); 
            for (char c : arr) {
                int index = c - 'a';
                chars[index]++; 
            }
            String key = Arrays.toString(chars);
            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(curr);
        }
        return new ArrayList<>(map.values()); 
    }
}
