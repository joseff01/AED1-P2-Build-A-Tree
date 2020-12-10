package server.Trees;
public class Node {

    Node right,left;
    int key;
    int height;

    public Node(int Key){
        this.key=Key;
        this.left=this.right=null;
        this.height=0;

    }

    public Node getRight() {
        return right;
    }

    public Node getLeft() {
        return left;
    }

    public int getKey() {
        return key;
    }

    public int getHeight() {
        return height;
    }

}