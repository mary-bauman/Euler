public class four {
    public static boolean isPalindrome(int n) {
        String s = Integer.toString(n);
        int len = s.length();
        for (int i = 0; i < len / 2; i++) {
            if (s.charAt(i) != s.charAt(len - 1 - i)) {
                return false;
            }
        }
        return true;
    }



    public static void main(String[] args) {
        int small = 99; //091
        int big = 99; //099
        int best = 9009;
        for (int i = small; i <= 1000; i++) {
            for (int j = small; j <=1000; j++) {
                if (isPalindrome(i * j)) {
                    if (i * j > best) {
                        best = i * j;
                    }
                }
            }
        }
        System.out.println(best);
    }
}
