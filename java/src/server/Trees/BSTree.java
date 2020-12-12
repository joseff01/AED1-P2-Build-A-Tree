package server.Trees;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(value = { "height" })
/**
 * @author Marcelo Truque
 * Clase del Árbol binario de búsqueda
 */
public class BSTree extends Tree{

    int Owner;

    Node root;

    /**
     * @author Marcelo Truque
     * inserción de un key en el árbol
     * @param key
     */
    public void insert(int key){
        this.root=inserting(this.root,key);
    }

    /**
     * @author Marcelo Truque
     * Reseteo del árbol
     */
    public void reset(){
        this.root=null;
    }

    /**
     * @author Marcelo Truque
     * @return altura del árbol
     */
    public int getHeight(){
        return this.root.height;
    }

    /**
     * @author Marcelo Truque
     * @return raíz del árbol
     */
    public Node getRoot(){return this.root;}

    /**
     * @author Marcelo Truque
     * @param node
     * @return devluelve la altura del nodo, si es null devuelve 0
     */
    private int height(Node node){
        if (node==null){
            return 0;
        }
        return node.height;
    }

    /**
     * @author Marcelo Truque
     * Manejo de la inserción del nodo en el árbol
     * @param node
     * @param key
     * @return Nodo con el que se incializa con sus cambios respectivos
     */
    private Node inserting(Node node, int key) {
        //Key insertion
        if (node == null) {
            return new Node(key,false);
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

    /**
     * @author Jose Antonio Retana
     * @return el dueño del árbol
     */
    public int getOwner() {
        return Owner;
    }

    /**
     * @author Jose Antonio Retana
     * Set del dueño del árbol
     * @param owner
     */
    public void setOwner(int owner) {
        Owner = owner;
    }
}