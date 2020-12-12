package server.Trees;

/**
 * @author Marcelo Truque
 * Clase del Nodo del cuál se forman los árboles binarios
 */
public class Node {

    Node right,left;
    int key;
    int height;

    /**
     * @author Marcelo Truque
     * Builder del nodo requiere de un valor y debe saber si es
     * un árbol AVL para su cambio en la altura
     * @param Key
     * @param AVL
     */
    public Node(int Key,boolean AVL){
        this.key=Key;
        this.left=this.right=null;
        if (AVL){
            this.height=1;
        }else{
            this.height=0;
        }

    }

    /**
     * @author Marcelo Truque
     * @return Hijo derecho del nodo (Mayor)
     */
    public Node getRight() {
        return right;
    }

    /**
     * @author Marcelo Truque
     * @return Hijo izquierdo del nodo (menor)
     */
    public Node getLeft() {
        return left;
    }

    /**
     * @author Marcelo Truque
     * @return Valor del Nodo
     */
    public int getKey() {
        return key;
    }

    /**
     * @author Marcelo Truque
     * @return altura del nodo
     */
    public int getHeight() {
        return height;
    }

}