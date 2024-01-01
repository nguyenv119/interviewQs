package DSA.Java.DP;

public class dp {
    public static void main(String[] args) {
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
