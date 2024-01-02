package DSA.Java.DP;

public class dp {
    public static void main(String[] args) {
    }

    /**
     * coinChange
     */
    public int coinChange(int[] coins, int amount) {
        /**
        1. We want the minimum number of coins needed to sum to a certain amount from our stash of coins

        2. numCoins(amount) = 1 + min(numCoins(amount - coin) for coin in coins)

        3. BC is when negative, means there is no amount, just let it be infinite. 1 + min(numCoins(-1)) = 1 - 1
        when numCoins(0) return 0. If at the end is 0, return -1

        DP. We need a way to store things so that we have accounted for numCoins(amount) before. Just start from 1 to amount, 
        increment and calculate every time then return dp[amount]
        */
        int[] dp = new int[amount + 1];

        for (int i = 1; i <= amount; i++) {
            int minSoFar = Integer.MAX_VALUE;
            for (int coin : coins) {
                int dpValue;

                if (i - coin < 0 || dp[i - coin] == Integer.MAX_VALUE) {
                    dpValue = Integer.MAX_VALUE;
                } else {
                    dpValue = 1 + dp[i - coin];
                }

                minSoFar = Math.min(minSoFar, dpValue);
            }
            dp[i] = minSoFar;
        }
        if (dp[amount] == Integer.MAX_VALUE) return -1;
        return dp[amount];
    }

    /**
     * climbStairs
     */
    public int climbStairs(int n) {
        /**
        1. Need to find numWays(n) where n is level of stairs
        2. climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2). But lets say CS(5) = CS(4) - CS(3), but CS(3) is within the same tree as CS(4), so this would be redundant if we did it recursively. Need a way to store: note that we only need the most 2 recent ways, so we can go from the ground up, starting from CS(2) all the way to n
        3. BC: when n = -1, there is no way, so we have to start with n = 0 and n = 1, both being 1
         */
        int[] ways = {1, 1};
        for (int i = 2; i <= n; i++) {
            int temp = ways[1];
            ways[1] = ways[0];
            ways[0] += temp;
        }
        return ways[0];
    }
}