class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            char[] charArray = strs[i].toCharArray();
            Arrays.sort(charArray);
            String sortedStr = new String(charArray);
            if (!map.containsKey(sortedStr)) {
                List<String> unsorted = new ArrayList<>();
                unsorted.add(strs[i]);
                map.put(sortedStr, unsorted);
            }
            else {
                List<String> unsorted = map.get(sortedStr);
                unsorted.add(strs[i]);
                map.put(sortedStr, unsorted);
            }
        }

        return new ArrayList<>(map.values());
    }
}
