package server.Trees;
public class Node {
    Node right,left;
    int key,height;

    public Node(int Key){
        this.key=Key;
        this.left=this.right=null;
        this.height=0;

    }

}