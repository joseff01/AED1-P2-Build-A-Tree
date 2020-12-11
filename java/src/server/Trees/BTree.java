package server.Trees;

public class BTree extends Tree{

    int Owner;

    private Page root;
    private int M, height;

    public BTree(int order) {
        this.root = null;
        this.M = order;
        this.height = 0;
    }

    public void insert(int Key) {
        this.root = inserting(this.root, Key);
        this.root=setnewRoot(this.root);
    }
    public void reset(){
        this.root=null;
    }
    public int getHeight(){
        return this.height;
    }
    public Page getRoot(){
        return this.root;
    }

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
    private Page setnewRoot(Page page){
        while(page.parent!=null){
            //going up
            page=page.parent;
        }
        return page;
    }
    public int getOwner() {
        return Owner;
    }

    public void setOwner(int owner) {
        Owner = owner;
    }
}