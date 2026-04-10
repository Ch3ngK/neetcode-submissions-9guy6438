class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagrams = new HashMap<>(); 
        int size = strs.length;
        for (int i = 0; i < size; i++) {
            String curr = strs[i]; 
            int[] count = new int[26];
            curr.toCharArray(); 
            for (int j = 0; j < curr.length(); j++) {
                char letter = curr.charAt(j); 
                int position = letter - 'a'; 
                count[position]++; 
            }
            String key = Arrays.toString(count); 
            anagrams.putIfAbsent(key, new ArrayList<>());
            anagrams.get(key).add(curr); 
        }
        return new ArrayList<>(anagrams.values()); 
    }
}
