class Solution {
    public boolean isPalindrome(String s) {
        String word = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        int left = 0;
        int right = word.length()-1;
        while (left < right) {
            if (word.charAt(left) != word.charAt(right))
                return false;
            left++;
            right--;
        }
        return true;
    }
}
