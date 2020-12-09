package server;

import server.Messages.TimerMessage;

import java.io.BufferedReader;
import java.io.PrintWriter;

public class Timer implements Runnable{

    int gameTimer = 0;

    int challengeTimer = 0;

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

        while (!stopTime) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            gameTimer++;
            challengeTimer = (challengeTimer >= 60) ? 0 : challengeTimer + 1;
            if (challengeTimer == 0) {
                challengeSelectionAlgorithm.selectChallenge();
            }
            if (gameTimer == 600) {
                ///SEND END GAME MESSAGE
            }
            out.println(new TimerMessage(gameTimer, "game"));
            out.println(new TimerMessage(challengeTimer, "challenge"));
            System.out.println(gameTimer);
            System.out.println(challengeTimer);
        }
    }
}
