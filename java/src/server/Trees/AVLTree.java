package server.Trees;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(value = { "height" })

public class AVLTree extends Tree{

    int Owner;

    private Node root;
    private int Size =0;

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

    public int getSize(){
        return this.Size;
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
        //getting Children
        Node right = node.right;
        Node change = right.left;

        //Rotate
        right.left = node;
        node.right = change;

        //New heights
        node.height = Math.max(height(node.right), height(node.left));
        right.height = Math.max(height(right.right), height(right.left));

        return right;
    }

    private Node inserting(Node node, int key) {
        //Node insertion
        if (node == null) {
            this.Size++;
            return new Node(key,true);
        }
        //going left
        if (key < node.key)
            node.left = inserting(node.left, key);
        //Going right
        else if (key > node.key)
            node.right = inserting(node.right, key);
        //Node already in
        else
            return node;

        //Setting height
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
    public int getOwner() {
        return Owner;
    }
    public void setOwner(int owner) {
        Owner = owner;
    }

}