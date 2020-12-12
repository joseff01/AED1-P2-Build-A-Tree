package server.Messages;

/**
 * @author Jose Antonio Retana
 * Envío del token correspondiente al BST a la interfaaz
 */
public class BSTToken extends Message{

    int number;

    int receiver;

    /**
     * @author Jose Antonio Retana
     * Builder del Token que se debe de enviar
     * @param number
     * @param receiver
     */
    public BSTToken(int number, int receiver){

        this.number = number;
        this.receiver = receiver;

    }

    /**
     * @author Jose Antonio Retana
     * LLamada al método de la clase padre
     */
    public BSTToken(){
        super();
    }

    /**
     * @author Jose Antonio Retana
     * @return Numero del token
     */
    public int getNumber() {
        return number;
    }

    /**
     * Set del número del token
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
