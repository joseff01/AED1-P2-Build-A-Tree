package server.Trees;

/**
 * @author Marcelo Truque
 * Clase que contiene el árbol Splay
 */
public class SplayTree extends Tree{

    private int Owner;

    private Node root;
    private int size=0;
    private int height=0;

    /**
     * @author Marcelo Truque
     * @return La altura del árbol.
     */
    public int getHeight(){return this.height; }

    /**
     * @author Marcelo Truque
     * @return La raíz del árbol
     */
    public Node getRoot(){return this.root; }

    /**
     * @author Marcelo Truque
     * @return Devuelve la cantidad de nodos dentro del árbol
     */
    public int getSize(){return this.size;}

    /**
     * @author Marcelo Truque
     * Resetea el árbol
     */
    public void reset(){
        this.root=null;
    }

    /**
     *@author Marcelo Truque
     * Inserción de un valor en el árbol y su acomode
     * @param key
     */
    public void insert(int key){
        this.root=inserting(this.root,key);
        this.root=splay(this.root,key);
        this.height=findHeight(this.root)-1;
        if (this.height < 0) {
            this.height = 0;
        }
    }

    /**
     * @author Marcelo Truque
     * Función que recorre el árbol
     * @param node
     * @return Depth del árbol
     */
    private int findHeight (Node node){
        if (node==null){
            return 0;
        }
        else{
            return Math.max(findHeight(node.left),findHeight(node.right))+1;
        }
    }

    /**
     * @author Marcelo Truque
     * Manejo de la inserción en el árbol
     * @param node
     * @param key
     * @return Nodo incial de la inserción
     */
    private Node inserting(Node node, int key){
        if (node == null){
            this.size++;
            return new Node(key,false);
        }
        if (key < node.key)
            node.left = inserting(node.left, key);
        else if (key > node.key)
            node.right = inserting(node.right, key);
        else
            return node;

        return node;
    }

    /**
     * @author Marcelo Truque
     * Splay del árbol
     * @param node
     * @param key
     * @return Nodo conteniente del key indicado y todos los cambios en el árbol
     */
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

    /**
     * @author Marcelo Truque
     * Rotación hacia la derecha del un nodo
     * @param node
     * @return Nodo nuevo despuñes de la rotación
     */
    private Node rightRotate(Node node){
        //getting children
        Node left= node.left;
        Node change= left.right;

        //rotation
        left.right=node;
        node.left=change;
        return left;
    }

    /**
     * @author Marcelo Truque
     * Rotación hacia la izquierda de un nodo
     * @param node
     * @return Nodo nuevo depués de la rotación
     */
    private  Node leftRotate(Node node){
        //getting children
        Node right=node.right;
        Node change=right.left;

        //rotation
        right.left=node;
        node.right=change;

        return right;
    }

    /**
     * @author Jose Antonio Retana
     * @return El dueño del árbol
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
