package server.Trees;

public class SplayTree {
    private Node root;
    private int size=0;

    public Node getRoot(){return this.root; }
    public int getSize(){return this.size;}
    public void reset(){
        this.root=null;
    }
    public void insert(int key){
        this.root=inserting(this.root,key);
        this.root=splay(this.root,key);
    }

    private Node inserting(Node node, int key){
        if (node == null){
            this.size++;
            return new Node(key);
        }
        if (key < node.key)
            node.left = inserting(node.left, key);
        else if (key > node.key)
            node.right = inserting(node.right, key);
        else
            return node;

        return node;
    }
    private Node splay(Node node, int key){
        if (node == null||   node.key==key)
            return node;
        if (node.key>key){
            if (node.left==null)
                return node;
            //zig zag
            if (node.left.key<key) {
                node.left.right = splay(node.left.right, key);
                if (node.left.right != null)
                    node.left = leftRotate(node.left);
            }
            // zig zig
            else if (node.left.key>key){
                node.left.left=splay(node.left.left,key);
                node=rightRotate(node);
            }
            return (node.left==null) ? node:rightRotate(node);
        }else{
            if(node.right==null)
                return node;
            //Zag zig
            if (node.right.key > key){
                node.right.left = splay(node.right.left,key);
                if(node.right.left!= null)
                    node.right=rightRotate(node.right);

            }
            //Zag zag
            else if (node.right.key<key){
                node.right.right=splay(node.right.right,key);
                node=leftRotate(node);
            }
            return (node.right==null) ? node:leftRotate(node);
        }
    }
    private Node rightRotate(Node node){
        //getting children
        Node left= node.left;
        Node change= left.right;

        //rotation
        left.right=node;
        node.left=change;
        return left;
    }
    private  Node leftRotate(Node node){
        //getting children
        Node right=node.right;
        Node change=right.left;

        //rotation
        right.left=node;
        node.right=change;

        return right;
    }
}
