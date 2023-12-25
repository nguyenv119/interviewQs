class twoPointers {
    public static void main(String[] args) {
        int[] height1 = {1,8,6,2,5,4,8,3,7};
        System.out.println(twoPointers.mostWater(height1));
    }

    private static long mostWater(int[] height) {
        if (height == null) return 0;

        long maxArea = 0;
        int l = 0;
        int r = height.length - 1;
        int minHeight;

        // Keep looping while we can still calculate area
        while (l < r) {
            // Get the minimum height
            if (height[l] <= height[r]) {
                minHeight = height[l];
            } else {
                minHeight = height[r];
            }
            // Calculate areas
            long area = (r - l) * minHeight;
            if (area > maxArea) {
                maxArea = area;
            }
            // increment and decrement pointers
            if (height[l] < height[r]) {
                l++;
            } else r --;
        }
        return maxArea;
    }
}