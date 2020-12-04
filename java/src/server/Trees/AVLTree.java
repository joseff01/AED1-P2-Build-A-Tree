package server.Trees;

public class AVLTree {
    Node root;

    public void insert(int key) {

        this.root = inserting(this.root, key);
    }

    public void reset() {
        this.root = null;
    }

    public int getHeight() {
        return this.root.height;
    }

    public Node getRoot() {
        return this.root;
    }

    private int height(Node node) {
        if (node == null) {
            return 0;
        }
        return node.height;
    }

    private int getBalance(Node node) {
        if (node == null) {
            return 0;
        }
        return height(node.left) - height(node.right);
    }

    private Node rightRotate(Node node) {
        //getting children
        Node left = node.left;
        Node change = left.right;

        //rotation
        left.right = node;
        node.left = change;

        //new heights
        node.height = Math.max(height(node.left), height(node.right));
        left.height = Math.max(height(left.left), height(left.right));

        return left;
    }

    private Node leftRotate(Node node) {
        Node right = node.right;
        Node change = right.left;

        right.left = node;
        node.right = change;

        node.height = Math.max(height(node.right), height(node.left));
        right.height = Math.max(height(right.right), height(right.left));

        return right;
    }

    private Node inserting(Node node, int key) {
        if (node == null) {
            return new Node(key);
        }
        if (key < node.key)
            node.left = inserting(node.left, key);
        else if (key > node.key)
            node.right = inserting(node.right, key);
        else
            return node;

        node.height = 1 + Math.max((height(node.left)), height(node.right));

        int balance = getBalance(node);

        //left left
        if (balance > 1 && key < node.left.key)
            return rightRotate(node);
        //right right
        if (balance < -1 && key > node.right.key)
            return leftRotate(node);

        //left right
        if (balance > 1 && key > node.left.key) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }
        // right left
        if (balance < -1 && key < node.right.key) {
            node.right = rightRotate(node.right);
            return leftRotate(node);

        }

        return node;
    }
}