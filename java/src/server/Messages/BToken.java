package server.Messages;

/**
 * @author Jose Antonio Retana
 * Clase para enviar el Token del árbol B
 */
public class BToken extends Message{

    int number;

    int receiver;

    /**
     * @author Jose Antonio Retana
     * Constructor del Token del árbol B
     * @param number
     * @param receiver
     */
    public BToken(int number, int receiver){

        this.number = number;
        this.receiver = receiver;

    }

    /**
     * @author Jose Antonio Retana
     * LLamada al método de la clase padre
     */
    public BToken(){
        super();
    }

    /**
     * @author Jose Antonio Retana
     * @return Número coprrespondiente al token
     */
    public int getNumber() {
        return number;
    }

    /**
     * @author Jose Antonio Retana
     * Set del número correspondiente al token
     * @param number
     */
    public void setNumber(int number) {
        this.number = number;
    }

    /**
     * @author Jose Antonio Retana
     * @return quién lo recibió
     */
    public int getReceiver() {
        return receiver;
    }

    /**
     * @author Jose Antonio Retana
     * Set de quién lo recibió
     * @param receiver
     */
    public void setReceiver(int receiver) {
        this.receiver = receiver;
    }

}
