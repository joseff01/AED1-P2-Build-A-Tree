package server;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import server.Messages.TimerMessage;

import java.io.BufferedReader;
import java.io.PrintWriter;

public class Timer implements Runnable{

    int gameTimer = 610;

    int challengeTimer = 60;

    BufferedReader in;

    PrintWriter out;

    ChallengeSelectionAlgorithm challengeSelectionAlgorithm;

    boolean stopTime = false;

    public  Timer(BufferedReader in, PrintWriter out, ChallengeSelectionAlgorithm challengeSelectionAlgorithm) {
        this.in = in;
        this.out = out;
        this.challengeSelectionAlgorithm = challengeSelectionAlgorithm;
        out.println(new TimerMessage(gameTimer,"game"));
        out.println(new TimerMessage(challengeTimer,"challenge"));
        System.out.println(gameTimer);
        System.out.println(challengeTimer);
        Thread timerThread = new Thread(this);
        timerThread.start();
    }

    public void stopAllTimers(){
        stopTime = true;
    }

    @Override
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
                ///SEND END GAME MESSAGE
            }

            try {
                String timerGameJSON = objectMapper.writeValueAsString(new TimerMessage(gameTimer, "game"));
                String challengeGameJSON = objectMapper.writeValueAsString(new TimerMessage(challengeTimer, "challenge"));
                out.println(timerGameJSON);
                out.println(challengeGameJSON);
                System.out.println(gameTimer);
                System.out.println(challengeTimer);
            } catch (JsonProcessingException e) {
                e.printStackTrace();
            }

        }
    }
}
