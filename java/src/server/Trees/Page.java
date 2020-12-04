package server.Trees;

import java.util.ArrayList;

public class Page {
    ArrayList<Integer> keys=new ArrayList<Integer>();
    ArrayList<Page> Branches=new ArrayList<Page>();
    Page parent;

    public Page(){
        this.parent=null;
    }
    public int search(int key){
        //Variable de índice donde se debe colocar
        int accsess=this.keys.size();
        //Busca el index oportuno
        for(int i = this.keys.size()-1; i>=0;i--){
            //Encuentra el index
            if (this.keys.get(i)<key){
                break;
            }else if (this.keys.get(i)==key){
                accsess=-1;
                break;
            }
            accsess--;
        }
        return accsess;
    }
    public void insertbranch(Page page, int index){
        while(index!=this.Branches.size()+1){
            if(index == this.Branches.size()){
                this.Branches.add(index,page);
                break;
            }else{
                Page mover = this.Branches.get(index);
                Branches.set(index, page);
                index++;
                page = mover;
            }
        }
    }

    public void insertkey(int Key){
        //La página no tiene elementos
        if (this.keys.size()==0){
            this.keys.add(0,Key);
        }
        else{
            //Dónde se debe insertar en la página
            int inserter=search(Key);
            //La llave ya está en al página
            if (inserter<0){
                return;
            }
            else{
                //Recorre la página haciendo el cambio oportuno
                while(inserter!=this.keys.size()+1){
                    //Último elemento en la página
                    if(inserter==this.keys.size()){
                        this.keys.add(inserter,Key);
                        break;
                    } else{
                        int mover = this.keys.get(inserter);
                        keys.set(inserter, Key);
                        inserter++;
                        Key = mover;
                    }
                }
            }
        }
    }
}