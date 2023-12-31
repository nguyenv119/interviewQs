package DSA.Java.Trees;
 
class trees {
    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        TreeNode left = new TreeNode(2);
        TreeNode right = new TreeNode(3);

        root.left = left;
        root.right = right;

        trees t = new trees();
        System.out.println(t.diameterOfBinaryTree(root));
    }

    /**
     * maximum tree path
     */
    int maxPath = -1000;
    public int maxPathSum(TreeNode root) {
        if (root == null) return 0;
        getSums(root);
        return maxPath;
    }

    public int getSums(TreeNode root) {
        if (root == null) return 0;
        int maxPathLeft = getSums(root.left);
        int maxPathRight = getSums(root.right);

        int currMaxPath = Math.max(root.val + maxPathLeft + maxPathRight, root.val);
        currMaxPath = Math.max(root.val + maxPathRight, currMaxPath);
        currMaxPath = Math.max(root.val + maxPathLeft, currMaxPath);

        maxPath = Math.max(maxPath, currMaxPath);

        return Math.max(root.val, Math.max(maxPathLeft + root.val, maxPathRight + root.val));
    }

    /**
     * lowest common ancestor
     */
    TreeNode LCA = null;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        hasPorQ(root, p, q);
        return LCA;
    }

    public boolean hasPorQ(TreeNode curr, TreeNode p, TreeNode q) {
        if (curr == null) return false;
        boolean leftHas = hasPorQ(curr.left, p, q);
        boolean rightHas = hasPorQ(curr.right, p, q);

        if ((curr.val == p.val || curr.val == q.val) || (leftHas && rightHas)) {
            LCA = curr;
        }
        return (curr.val == p.val || curr.val == q.val) || (leftHas || rightHas);
    }

    /**
     * isBalanced
     */
    boolean balanced = true;
    public boolean isBalanced(TreeNode root) {
        /** balanced if abs(lH - rH) <= 1, return this and left and right. But need to get lH and rH before this */
        if (root == null) return true;
        getHeight(root); /** In calculating height of root, we have height of all others, no need to call again */
        return balanced;
    }

    public int getHeight(TreeNode root) {
        if (root == null) return 0;
        int lH = getHeight(root.left);
        int rH = getHeight(root.right);

        if (Math.abs(lH - rH) > 1) balanced = false;

        return 1 + Math.max(lH, rH);
    }
    
    /**
     * maxDiameter
     */
    int maxDiam = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) return 0;
        height(root);
        return maxDiam;
    }

    public int height(TreeNode root){
        if (root == null) return 0;
        int lH = height(root.left);
        int rH = height(root.right);
        int maxHeight;

        if (lH < rH) maxHeight = rH;
        else maxHeight = lH;

        if (maxDiam < lH + rH) maxDiam = (lH + rH);

        return 1 + maxHeight;
    }
}