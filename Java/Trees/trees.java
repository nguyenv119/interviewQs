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