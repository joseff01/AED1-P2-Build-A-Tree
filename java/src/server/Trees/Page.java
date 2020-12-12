package server.Trees;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import java.util.ArrayList;

@JsonIgnoreProperties(value = { "parent" })
/**
 * @author Marcelo Truque
 * Clase de las páginas especialmente para el árbol B
 */
public class Page {

    ArrayList<Integer> keys=new ArrayList<Integer>();
    ArrayList<Page> Branches=new ArrayList<Page>();
    Page parent;

    /**
     * @author Marcelo Truque
     *Builder de la hoja
     */
    public Page(){
        this.parent=null;
    }

    /**
     * @author Marcelo Truque
     * Clase para buscar en una lista un valor, devolverá el índice ya sea del valor,
     * o del branch al que se debe de acceder para encontrarlo
     * @param key
     * @return index
     */
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

    /**
     * @author Marcelo Truque
     * Inserción de una rama y su eventual ajuste para mantener el orden
     * @param page
     * @param index
     */
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

    /**
     * @author Marcelo Truque
     * Inserción de una llave en la lista de llaves y
     * cambios para mantener el orden
     * @param Key
     */
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

    /**
     * @author Marcelo Truque
     * @return Arreglo con las llaves
     */
    public ArrayList<Integer> getKeys() {
        return keys;
    }

    /**
     * @author Marcelo Truque
     * @return Arreglo con las ramas
     */
    public ArrayList<Page> getBranches() {
        return Branches;
    }

}
