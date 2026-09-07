/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxDepth(TreeNode root) {
        // If the root is null, the tree is empty, so the depth is 0.
    if (root == null) return 0;

    // Initialize the depth level.
    int level = 0;

    // Initialize the queue and add the root node to it.
    Queue<TreeNode> queue = new LinkedList<>();
    queue.add(root);

    // Perform BFS traversal.
    while (!queue.isEmpty()) {
        // Increase the level as we are moving to a new level in the tree.
        level++;

        // Process all nodes at the current level.
        int size = queue.size();  // Get the number of nodes at this level.
        for (int i = 0; i < size; i++) {
            TreeNode current = queue.remove();

            // Add the children of the current node to the queue.
            if (current.left != null) {
                queue.add(current.left);
            }
            if (current.right != null) {
                queue.add(current.right);
            }
        }
    }

    // The final value of 'level' will be the maximum depth of the tree.
    return level;
    }
}
