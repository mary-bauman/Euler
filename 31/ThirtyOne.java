import java.util.*;

public class ThirtyOne {
    public static void main(String[] args) {
        double[] dp = new double[201];
        int[] currency = {1, 2, 5, 10, 20, 50, 100, 200};
        dp[0] = 1;
        
        for (int coin : currency) {
            for (int i = coin; i <= 200; i++) {
                dp[i] += dp[i - coin];
            }
        }

        System.out.println((int) dp[200]);
    }
}
