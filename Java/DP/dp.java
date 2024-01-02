package DSA.Java.DP;

public class dp {
    public static void main(String[] args) {
    }

    /**
     * UniquePaths
     */
    public int uniquePaths(int m, int n) {
    /**
    1. Want waysTo(m - 1, n - 1) is the number of ways we can move to the m - 1 and n - 1 grid
    2. waysTo(m - 1, n - 1) = waysTo(one up) + waysTo(one left)
    3. BC: When we are out of the grid: waysTo(a, b) = 0
    4. DP: We want to store the # ways where we have gotten to already, use dp matrix? Use 2 for loops
     */
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) dp[0][0] = 1;
                else {
                    int up;
                    int left;

                    if (i - 1 < 0) up = 0;
                    else up = dp[i - 1][j];

                    if (j - 1 < 0) left = 0;
                    else left = dp[i][j - 1];

                    dp[i][j] = up + left;
                }
            }
        }
        return dp[m - 1][n - 1];
    }

    /**
     * combinationSumIV
     */
    public int combinationSum4(int[] nums, int target) {
        /**
        1. numCombs(target) want to find number of ways get to target with given nums
        2. numCombs(target) = sum of numCombs(target - num) for num in nums
        3. BC: numCombs(a - a) = numCombs(0) = 1. Also, numCombs(<0) = 0
        4. DP: get rid of redundancy if weve seen numCombs before by dp array, go from 1 to target

        [0, 1, 2, 4, 7]
         */
        int[] dp = new int[target + 1];

        for (int i = 1; i < target + 1; i++) {
            int numWaysIndividual = 0;
            for (int num: nums) {
                if (i - num > 0) numWaysIndividual += dp[i - num];
                else if (i - num == 0) numWaysIndividual++;
            }
            dp[i] = numWaysIndividual;
        }
        return dp[target];
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
