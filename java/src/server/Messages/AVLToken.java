package server.Messages;

import java.util.Random;

/**
 * @author Jose Antonio Retana
 * Mensaje a la interdaz de que el token que debe de caer del cielo del árbol AVL
 */
public class AVLToken extends Message{

    int number;

    int receiver;

    /**
     * @author Jose Antonio Retana
     * Constructor del token que se enviará
     * @param number
     * @param receiver
     */
    public AVLToken(int number, int receiver){

        this.number = number;
        this.receiver = receiver;

    }

    /**
     * @author Jose Antonio Retana
     * Llamada al constructor de la clase padre
     */
    public AVLToken(){
        super();
    }

    /**
     *@author Jose Antonio Retana
     * @return Número del token
     */
    public int getNumber() {
        return number;
    }

    /**
     * @author Jose Antonio Retana
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
