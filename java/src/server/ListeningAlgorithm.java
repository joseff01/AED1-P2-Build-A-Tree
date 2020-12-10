package server;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.PrintWriter;

public class ListeningAlgorithm implements Runnable {

    ChallengeSelectionAlgorithm challengeSelectionAlgorithm;

    BufferedReader in;
    PrintWriter out;

    public ListeningAlgorithm(BufferedReader in, PrintWriter out, ChallengeSelectionAlgorithm challengeSelectionAlgorithm) {
        this.in = in;
        this.out = out;
        this.challengeSelectionAlgorithm = challengeSelectionAlgorithm;

        Thread listenThread = new Thread(this);
        listenThread.start();
    }

    @Override
    public void run() {

        boolean disconnectionFlag = false;

        while (!disconnectionFlag) {
            try {
                String messageJson = in.readLine();
                System.out.println(messageJson);
            } catch (IOException e) {
                e.printStackTrace();
                disconnectionFlag = true;
            }
        }
    }
}
