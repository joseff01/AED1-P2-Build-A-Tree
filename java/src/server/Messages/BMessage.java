package server.Messages;

import java.util.Random;

/**
 * @author Jose Antonio Retana
 * Mensaje acerca del carro B con el órden y el level necesario para el reto
 */
public class BMessage extends Message{

    int order;

    int level;

    Random random = new Random();

    /**
     * @author Jose Antonio Retana
     *Constructor del mensaje del árbol B copn números random
     */
    public BMessage(){
        this.order = random.nextInt(3) + 3;
        this.level = random.nextInt(3) + 2;
    }

    /**
     * @author Jose Antonio Retana
     * @return Obtener el órden establecido en el constructor
     */
    public int getOrder() {
        return order;
    }

    /**
     * @author Jose Antonio Retana
     * Set del orden establecido
     * @param order
     */
    public void setOrder(int order) {
        this.order = order;
    }

    /**
     * @author Jose Antonio Retana
     * @return Nivel del árbil B
     */
    public int getLevel() {
        return level;
    }

    /**
     * @author Jose Antonio Retana
     * Set del nivel del árbol B
     * @param level
     */
    public void setLevel(int level) {
        this.level = level;
    }

}
