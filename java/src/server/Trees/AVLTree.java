package server.Trees;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(value = { "height" })
/**
 *Clase del árbol AVL
 * @author Marcelo Truque
 */
public class AVLTree extends Tree{

    int Owner;

    private Node root;
    private int Size =0;

    /**
     *insersción de una llave en un árbol
     * @param key
     * @author Marcelo Truque
     */
    public void insert(int key) {

        this.root = inserting(this.root, key);
    }

    /**
     * Borra por completo
     * @author Marcelo Truque
     */
    public void reset() {
        this.root = null;
    }

    /**
     * @author Marcelo Truque
     * @return la altura del árbol
     */
    public int getHeight() {
        return this.root.height;
    }

    /**
     * @author Marcelo Truque
     * @return la raíz del árbol
     */
    public Node getRoot() {
        return this.root;
    }

    /**
     * @author Marcelo Truque
     * @return La cantidad de nodos en el árbol
     */
    public int getSize(){
        return this.Size;
    }

    /**
     * @author Marcelo Truque
     * @param node
     * @return La altura del nodo, si es null edvuelve 0
     */
    private int height(Node node) {
        if (node == null) {
            return 0;
        }
        return node.height;
    }

    /**
     * @author Marcelo Truque
     * @param node
     * @return El valor del balance del nodo
     */
    private int getBalance(Node node) {
        if (node == null) {
            return 0;
        }
        return height(node.left) - height(node.right);
    }

    /**
     * @author Marcelo Truque
     * Rotación hacia la derecha de un nodo
     * @param node
     * @return nuevo nodo después de la rotación
     */
    private Node rightRotate(Node node) {
        //getting children
        Node left = node.left;
        Node change = left.right;

        //rotation
        left.right = node;
        node.left = change;

        //new heights
        node.height = Math.max(height(node.left), height(node.right))+1;
        left.height = Math.max(height(left.left), height(left.right))+1;

        return left;
    }

    /**
     * @author Marcelo Truque
     * Rotación hacia la izquierda de un nodo
     * @param node
     * @returnnuevo nodo después de la rotación
     */
    private Node leftRotate(Node node) {
        //getting Children
        Node right = node.right;
        Node change = right.left;

        //Rotate
        right.left = node;
        node.right = change;

        //New heights
        node.height = Math.max(height(node.right), height(node.left))+1;
        right.height = Math.max(height(right.right), height(right.left))+1;

        return right;
    }

    /**
     * @author Marcelo Truque
     * Manejo de la inserción y las rotaciones en el árbol AVL
     * @param node
     * @param key
     * @return Nodo donde se incializó con los cambios pertinentes
     */
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

    /**
     * @author Jose Retana
     * @return El dueño del árbol
     */
    public int getOwner() {
        return Owner;
    }

    /**
     * @author Jose Retana
     * set del  dueño de este árbol
     * @param owner
     */
    public void setOwner(int owner) {
        Owner = owner;
    }

}