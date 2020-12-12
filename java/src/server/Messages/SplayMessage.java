package server.Messages;

import java.util.Random;

/**
 * @author Jose Antonio Retana
 * Mensaje del árbol Splay con la cantidad de nodos necesarios para ganar el reto
 */
public class SplayMessage extends Message{

    int elementAmount;

    Random random = new Random();

    /**
     * @author Jose Antonio Retana
     * Constructor del Mensaje con número random
     */
    public SplayMessage(){
        this.elementAmount = random.nextInt(8) + 3;
    }

    /**
     * @author Jose Antonio Retana
     * @return cantidad de nodos requeridos para ganar un reto
     */
    public int getElementAmount() {
        return elementAmount;
    }

    /**
     * @author Jose Antonio Retana
     * Set de la cantidad de nodos requeridos para ganar un reto
     * @param elementAmount
     */
    public void setElementAmount(int elementAmount) {
        this.elementAmount = elementAmount;
    }
}
