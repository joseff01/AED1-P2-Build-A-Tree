package server.Trees;

/**
 * @author Marcelo Truque
 * Clase que contiene al árbol tipo B
 */
public class BTree extends Tree{

    int Owner;

    private Page root;
    private int M, height;

    /**
     * @author Marcelo Truque
     * Builder del árbol
     * @param order
     */
    public BTree(int order) {
        this.root = null;
        this.M = order;
        this.height = 0;
    }

    /**
     * @author Marcelo Truque
     * Inserción de una llave dentro del árbol
     * @param Key
     */
    public void insert(int Key) {
        this.root = inserting(this.root, Key);
        this.root=setnewRoot(this.root);
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
     * @return La altura del árbol
     */
    public int getHeight(){
        return this.height;
    }

    /**
     * @author Marcelo Truque
     * @return devuelve la raíz del árbol
     */
    public Page getRoot(){
        return this.root;
    }

    /**
     * @author Marcelo Truque
     * Manejo de la inserción de la llave en el árbol
     * @param page
     * @param Key
     * @return Nodo que se incializó con los cambios pertinentes
     */
    private Page inserting(Page page, int Key) {
        //Caso se este construyendo un árbol
        if (page == null) {
            Page raiz = new Page();
            raiz.insertkey(Key);
            return raiz;
        }
        //Estamos en una hoja donde se hacen las insersciones
        else if (page.Branches.size() == 0) {
            page.insertkey(Key);
            check(page);
        }
        //No estamos en una hoja y hay que seguir bajando
        else {
            int bajar = page.search(Key);
            inserting(page.Branches.get(bajar), Key);
        }
        return page;
    }

    /**
     * @author Marcelo Truque
     * Revisión de la cantidad de ramas en la página versus
     * el orden del árbol y eventual partición si se excede
     * @param page
     */
    private void  check(Page page) {
        //llegó a su capacidad
        if (page.keys.size() == M) {
            //El tope es en la raíz
            if (page.parent == null) {
                Page newroot = new Page();
                this.height++;
                Page menor = new Page();
                int cutindex = Math.round(M / 2);
                int i = 0;
                while (i != cutindex + 1) {
                    if (i == cutindex) {
                        //Cambios en newroot
                        int newkey = page.keys.get(0);
                        newroot.insertkey(newkey);
                        newroot.insertbranch(menor, 0);
                        newroot.insertbranch(page, 1);
                        //cambios en la antigua root
                        page.keys.remove(0);
                        page.parent = newroot;
                        i++;
                    } else {
                        //cambios en menor
                        menor.parent = newroot;
                        int newkey = page.keys.get(0);
                        menor.insertkey(newkey);
                        page.keys.remove(0);
                        if (page.Branches.size() == 0) {
                            i++;
                            continue;
                        } else {
                            Page newbranch = page.Branches.get(0);
                            menor.insertbranch(newbranch, i);
                            page.Branches.remove(0);
                            if (i+1==cutindex){
                                Page  newBranch2=page.Branches.get(0);
                                menor.insertbranch(newBranch2,i+1);
                                page.Branches.remove(0);
                            }
                            i++;
                        }
                    }
                }
            }
            //El tope es en una rama
            else {
                int cutindex = Math.round(M / 2);
                Page menor = new Page();
                menor.parent = page.parent;
                int i = 0;
                int cutaux = cutindex;
                while (i != cutindex + 1) {
                    if (i == cutindex) {
                        //Cambios en parent
                        int newKey = page.keys.get(0);
                        int indexParent = page.parent.search(newKey);
                        page.parent.insertkey(newKey);
                        page.parent.insertbranch(menor, indexParent);
                        page.keys.remove(0);
                        if(page.Branches.size()==0){
                            i++;
                            check(page.parent);
                            continue;
                        }else{
                            page.Branches.remove(0);
                            check(page.parent);
                            i++;
                        }
                    }//Cambios en menor
                    else {
                        menor.parent = page.parent;
                        int newkey = page.keys.get(0);
                        menor.insertkey(newkey);
                        page.keys.remove(0);
                        cutaux--;
                        if (page.Branches.size() == 0) {
                            i++;
                            continue;
                        } else {
                            Page newBranch = page.Branches.get(0);
                            menor.insertbranch(newBranch, i);
                            page.Branches.remove(0);
                            if (i+1==cutindex){
                                Page newBranch2 = page.Branches.get(0);
                                menor.insertbranch((newBranch2),i+1);
                                page.Branches.remove(0);
                            }
                            i++;
                        }
                    }
                }
            }
        }
    }

    /**
     * @author Marcelo Truque
     * Busqueda de una página sin parent (root)
     * @param page
     * @return página sin parent
     */
    private Page setnewRoot(Page page){
        while(page.parent!=null){
            //going up
            page=page.parent;
        }
        return page;
    }

    /**
     * @author Jose Antonio Retana
     * @return Dueño del árbol
     */
    public int getOwner() {
        return Owner;
    }

    /**
     * @author Jose Antionio Retana
     * Set del dueño del árbol
     * @param owner
     */
    public void setOwner(int owner) {
        Owner = owner;
    }
}