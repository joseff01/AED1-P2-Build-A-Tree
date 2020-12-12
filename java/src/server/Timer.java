package server;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import server.Messages.EndGameMessage;
import server.Messages.Message;
import server.Messages.TimerMessage;

import java.io.BufferedReader;
import java.io.PrintWriter;

/**
 * Método de los timers
 * Se encarga de crear y mantener los timers, mand{a}ndole estos como mensajes individuales al cliente
 * @author Jose Retana
 */
public class Timer implements Runnable{

    volatile private int gameTimer = 610;

    volatile private int challengeTimer = 60;

    private BufferedReader in;

    private PrintWriter out;

    private ChallengeSelectionAlgorithm challengeSelectionAlgorithm;

    boolean stopTime = false;

    private ObjectMapper objectMapper;

    /**
     * Constructor de Timer
     * Recibe el BufferedReader, PrintWriter, la instancia del
     * ChallengeSelectionAlgorithm, y el ObjectMapper
     * @param in
     * @param out
     * @param challengeSelectionAlgorithm
     * @param objectMapper
     * @author Jose Retana
     */
    public  Timer(BufferedReader in, PrintWriter out, ChallengeSelectionAlgorithm challengeSelectionAlgorithm, ObjectMapper objectMapper) {
        this.in = in;
        this.out = out;
        this.challengeSelectionAlgorithm = challengeSelectionAlgorithm;
        this.objectMapper = objectMapper;
        out.println(new TimerMessage(gameTimer,"game"));
        out.println(new TimerMessage(challengeTimer,"challenge"));
        System.out.println(gameTimer);
        System.out.println(challengeTimer);
        Thread timerThread = new Thread(this);
        timerThread.start();
    }


    @Override
    /**
     * Método modificado run implementado por Runnable
     * Este se encarga de mantener los timers y que se envíen al cliente
     * Cuando el timer de challenge se acaba, se carga otro challenge distinto
     * Cuando el timer del juego se acaba, el server se finaliza, recibiendo el mensaje apropiado del ciente
     * @author Jose Retana
     */
    public void run() {

        ObjectMapper objectMapper = new ObjectMapper();

        while (!stopTime) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            gameTimer--;
            challengeTimer = (0 >= challengeTimer) ? 60 : challengeTimer - 1;
            if (challengeTimer == 60) {
                challengeSelectionAlgorithm.selectChallenge();
            }
            if (gameTimer <= 0) {
                try {
                    String endMessageJSON = objectMapper.writeValueAsString(new EndGameMessage());
                    out.println(endMessageJSON);
                } catch (JsonProcessingException e) {
                    e.printStackTrace();
                }
            }

            try {
                String timerGameJSON = objectMapper.writeValueAsString(new TimerMessage(gameTimer, "game"));
                String challengeGameJSON = objectMapper.writeValueAsString(new TimerMessage(challengeTimer, "challenge"));
                out.println(timerGameJSON);
                Thread.sleep(10);
                out.println(challengeGameJSON);
                System.out.println(gameTimer);
                System.out.println(challengeTimer);
            } catch (JsonProcessingException | InterruptedException e) {
                e.printStackTrace();
            }

        }
    }

    /**
     * Setter del timer del challenge
     * Utilizado por ChallengeSelectionAlgorithm para resetear el timer del challenge
     * @param challengeTimer
     * @author Jose Retana
     */
    public void setChallengeTimer(int challengeTimer) {
        this.challengeTimer = challengeTimer;
    }

}
