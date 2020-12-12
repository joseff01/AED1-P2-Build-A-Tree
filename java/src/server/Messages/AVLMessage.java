package server.Messages;

import java.util.Random;

/**
 * @author Jose Antonio Retana
 * Mensaje del árbol AVL con la cantidad de  nodos que debe de obtener para el reto
 */
public class AVLMessage extends Message{

    int elementAmount;

    Random random = new Random();

    /**
     * @author Jose Antonio Retana
     * Constructor del mensaje con un número random
     */
    public AVLMessage(){
        this.elementAmount = random.nextInt(8) + 3;
    }

    /**
     * @author Jose Antonio Retana
     * @return La cantidad de nodos que debe tener el árbol para cumplir el reto
     */
    public int getElementAmount() {
        return elementAmount;
    }

    /**
     * @author Jose Antonio Retana
     * Set del la cantidad de elementos que debe tener el árbol
     * @param elementAmount
     */
    public void setElementAmount(int elementAmount) {
        this.elementAmount = elementAmount;
    }

}
