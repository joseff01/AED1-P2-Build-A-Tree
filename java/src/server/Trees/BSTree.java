package server.Trees;

public class BSTree {
    Node root;
    public void insert(int key){
        this.root=inserting(this.root,key);
    }
    public void reset(){
        this.root=null;
    }
    public int getHeight(){
        return this.root.height;
    }
    public Node getRoot(){return this.root;}

    private int height(Node node){
        if (node==null){
            return 0;
        }
        return node.height;
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

        node.height = 1+Math.max((height(node.left)),height(node.right));

        return node;
    }
}