class PalindromeExmaple {
    public static boolean isPalindrome1(String input) {
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) != input.charAt(input.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
    
    public static void main(String args[]) {
        System.out.println(isPalindrome1("abcba"));
        System.out.println(isPalindrome1("abc"));
    }
}
