package server.Messages;

import java.util.Random;

/**
 * @author Jose Antonio Retana
 * Mensaje acerca del árbol Binario de búsqueda y el height necesario para el reto
 */
public class BSTMessage extends Message{

    int height;

    Random random = new Random();

    /**
     * @author Jose Antonio Retana
     * Constructor del mensaje con número random
     */
    public BSTMessage(){
        this.height = random.nextInt(4) + 2;
    }

    /**
     * @author Jose Antonio Retana
     * @return Altura elegida para el reto
     */
    public int getHeight() {
        return height;
    }

    /**
     * @author Jose Antonio Retana
     * Set de la altura elegida
     * @param height
     */
    public void setHeight(int height) {
        this.height = height;
    }

}
