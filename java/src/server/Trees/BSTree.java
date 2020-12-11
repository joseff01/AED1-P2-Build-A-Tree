package server.Trees;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(value = { "height" })
public class BSTree extends Tree{

    int Owner;

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
        //Key insertion
        if (node == null) {
            return new Node(key);
        }
        //Going left
        if (key < node.key)
            node.left = inserting(node.left, key);
        //Going right
        else if (key > node.key)
            node.right = inserting(node.right, key);
        //Node already in
        else
            return node;
        //New height
        node.height = 1+Math.max((height(node.left)),height(node.right));

        return node;
    }
    public int get
    Owner() {
        return Owner;
    }

    public void setOwner(int owner) {
        Owner = owner;
    }
}