package server.Messages;

/**
 * @author Jose Antonio Retana
 * Clase encargada de los mensajes del manejo de tiempo en el juego
 */
public class TimerMessage extends Message{

    int timerNumber;

    String timerType;

    /**
     * @author Jose Antonio Retana
     * Constructor del mensaje del timer
     * @param number
     * @param timerType
     */
    public TimerMessage(int number, String timerType){

        this.timerType = timerType;

        this.timerNumber = number;

    }

    /**
     * @author Jose Antonio Retana
     * @return la cantidad de tiempo necesaria o la finalización del juego
     */
    public int getTimerNumber() {
        return timerNumber;
    }

    /**
     * @author Jose Antonio Retana
     * Set de la cantidad de tiempo necesaria para un reto o la finalización del juego
     * @param number
     */
    public void setTimerNumber(int number) {
        this.timerNumber = number;
    }

    /**
     * @author Jose Antonio Retana
     * @return Tipo de timer que se está enviando
     */
    public String getTimerType() {
        return timerType;
    }

    /**
     * @author Jose Antonio Retana
     * Set del tipo de timer que se va a aenviar
     * @param timerType
     */
    public void setTimerType(String timerType) {
        this.timerType = timerType;
    }
}
