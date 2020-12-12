package server.Messages;

/**
 * Clase encargada del envío de Tokens del árbol Splay
 */
public class SplayToken extends Message{


    int number;

    int receiver;

    /**
     * @author Jose Antonio Retana
     * Constructor del Token del árbol Splay
     * @param number
     * @param receiver
     */
    public SplayToken(int number, int receiver){

        this.number = number;
        this.receiver = receiver;

    }
    /**
     * Llamada al método de la clase padre
     */
    public SplayToken(){
        super();
    }

    /**
     * @author Jose Antonio Retana
     * @return numero correspondiente al token del árbol Splay
     */
    public int getNumber() {
        return number;
    }

    /**
     * @author Jose Antonio Retana
     * Set del número correspondiente al Token
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
