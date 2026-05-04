class Solution {
    public boolean isAnagram(String s, String t) {
        int[] charsArr = new int[26];
        
        for (char c : s.toCharArray()) {
            charsArr[c - 'a']++;
        }
        for (char c : t.toCharArray()) {
            charsArr[c - 'a']--;
        }
        
        for (int n : charsArr) {
            if (n != 0)
                return false;
        }
        
        return true;

    }
}
