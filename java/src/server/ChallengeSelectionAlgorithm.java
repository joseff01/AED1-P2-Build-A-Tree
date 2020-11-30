package server;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import server.Messages.*;

import java.io.BufferedReader;
import java.io.PrintWriter;
import java.util.Random;

public class ChallengeSelectionAlgorithm{

    BufferedReader in;
    PrintWriter out;

    Random random = new Random();

    ObjectMapper objectMapper = new ObjectMapper();

    boolean newChallengeFlag = false;

    public ChallengeSelectionAlgorithm(BufferedReader in, PrintWriter out){

        this.in = in;
        this.out = out;

        SelectChallenge();
    }

    private void SelectChallenge(){
        int challengeType = random.nextInt(4);

        Message message;

        if (challengeType == 0){
            //Challenge BST
            message = new BSTMessage();
        } else if (challengeType == 1){
            //Challenge Type B
            message = new BMessage();
        } else if (challengeType == 2){
            //Challenge AVL
            message = new AVLMessage();
        } else {
            //Challenge Splay
            message = new SplayMessage();
        }

        String messageJSON = null;
        try {
            messageJSON = objectMapper.writeValueAsString(message);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
        System.out.println("sent: " + messageJSON);
        out.println(messageJSON);

        sendToken();
    }

    public void sendToken(){

        int tokenType = random.nextInt(4);

        int randomNumber = random.nextInt(100);

        Message message;

        if (tokenType == 0){
            //Token BTS (Rhombus)
            message = new BSTToken(randomNumber);
        } else if (tokenType == 1){
            //Token Type B (Square)
            message = new BToken(randomNumber);
        } else if (tokenType == 2){
            //Token AVL (Circle)
            message = new AVLToken(randomNumber);
        } else {
            //Token Splay (Triangle)
            message = new SplayToken(randomNumber);
        }

        String messageJSON = null;

        try {
            messageJSON = objectMapper.writeValueAsString(message);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        System.out.println("sent: " + messageJSON);
        out.println(messageJSON);

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        sendToken();
    }
}
