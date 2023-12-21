class arrays {
    /**
    Main Method for the Arrays class
     */
    public static void main(String[] args) {
        int[] nums1 = {4, 3, 1, 7, 6};
        System.out.println(arrays.reversePair(nums1) + "\n");
        int[] nums2 = {1, 3, 2, 3, 1};
        System.out.println(arrays.reversePair(nums2) + "\n");
        int[] nums3 = {2, 4, 3, 5, 1};
        System.out.println(arrays.reversePair(nums3) + "\n");
    }
    
    private static int reversePair(int[] nums) {
        /**
        Intuition: seeing O(nlogn), and given extra space of one array, immediantely think of
        Mergesort - now how can we use MS to know where the reversePairs are? It should be
        in the divide conquer aspect of it..

        [1,3,2,3,1] -> [1,2,3,3,1] when sorting the last 2, how do we know theres rev pair?
        When we sort it, we are comparing, make a little switch in the middle to check
        if revPair, increment count. But we need to increment count so that it accounts for
        elements after it, or else we lose it....eg - [3,4,5,1], when we see that {1,3} is
        revPair, we have to account for 4 and 5 too

        Since Div and Conquer, we can increment the count every time we mergeSort and merge

        but problem: [1,2,3,1,3], if we just use normal MS, when we sort the 2nd "1", we will
        compare it with only 2 and that is not a revPair, and then miss 3. So, we have to 
        go through the auxiliary arrays twice: once to check all 

        Still O(nlogn) since the extra steps still fit within the bounds of O(n) of the comparisons in the
        merge function */
        return arrays.mergeSort(nums, 0, nums.length - 1);
    }

    private static int mergeSort(int[] nums, int low, int high) {
        if (low >= high) return 0;

        int res = 0;
        int mid = (low + high) / 2;
        res += arrays.mergeSort(nums, low, mid);
        res += arrays.mergeSort(nums, mid + 1, high);
        res += arrays.merge(nums, low, mid, high);
        return res;
    }

    private static int merge(int[] nums, int low, int mid, int high) {
        int count = 0;
        int LSize = mid - low + 1;
        int RSize = high - mid;

        int[] L = new int[LSize];
        int[] R = new int[RSize];

        for (int i = 0; i < LSize; i++) L[i] = nums[low + i];
        for (int j = 0; j < RSize; j++) R[j] = nums[mid + j + 1];

        int i = 0, j = 0, index = low;
        while (i < LSize) {
            while (j < RSize && L[i] > 2 * R[j]) {
                count += LSize - i;

                for (int l = i; l < LSize; l++) {
                    System.out.println("Reverse Pair: (" + L[l] + ", " + R[j] + ")");
                }

                j++;
            }
            i++;
        }
        
        i = j = 0;
        index = low;

        while (i < LSize && j < RSize) {
            if (L[i] <= R[j]) nums[index++] = L[i++];
            else nums[index++] = R[j++];
            }

        while (i < LSize) nums[index++] = L[i++];
        while (j < RSize) nums[index++] = R[j++];

        return count;
    }
}