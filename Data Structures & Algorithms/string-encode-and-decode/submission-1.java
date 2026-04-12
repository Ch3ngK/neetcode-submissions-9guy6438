class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder(""); 
        int n = strs.size(); 
        for (int i = 0; i < n; i++) {
            res.append(strs.get(i).length()).append('#').append(strs.get(i));
        }
        return res.toString(); 
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>(); 
        int length = str.length(); 
        int i = 0;
        while (i < length) {
            int j = i; 
            while (str.charAt(j) != '#') {
                j++; 
            }

            int n = Integer.parseInt(str.substring(i,j)); //extract the length of the current string
            i = j + 1; //shift the i pointer to iterate through each character of the string 
            j = i + n; //shift the j pointer to the end of the string
            res.add(str.substring(i, j)); //add the string to result list
            i = j; 
        }
        return res; 
    }
}
