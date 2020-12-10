package server;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import server.Messages.*;
import server.Trees.*;

import java.io.BufferedReader;
import java.io.PrintWriter;
import java.util.Random;

public class ChallengeSelectionAlgorithm{

    Timer timer;

    BufferedReader in;
    PrintWriter out;

    Random random = new Random();

    ObjectMapper objectMapper = new ObjectMapper();

    boolean newChallengeFlag = false;

    ListeningAlgorithm listeningAlgorithm;

    Tree player1Tree = null;
    Tree player2Tree = null;
    Tree player3Tree = null;
    Tree player4Tree = null;

    public ChallengeSelectionAlgorithm(BufferedReader in, PrintWriter out){

        this.in = in;
        this.out = out;

        timer = new Timer(in,out, this);
        listeningAlgorithm = new ListeningAlgorithm(in,out, this);

        selectChallenge();
        sendToken();

    }

    public void selectChallenge(){
        int challengeType = random.nextInt(4);

        Message message;

        if (challengeType == 0){
            //Challenge BST
            message = new BSTMessage();
            player1Tree = new BSTree();
            player2Tree = new BSTree();
            player3Tree = new BSTree();
            player4Tree = new BSTree();
        } else if (challengeType == 1){
            //Challenge Type B
            message = new BMessage();
            int order = ((BMessage) message).getOrder();
            player1Tree = new BTree(order);
            player2Tree = new BTree(order);
            player3Tree = new BTree(order);
            player4Tree = new BTree(order);
        } else if (challengeType == 2){
            //Challenge AVL
            message = new AVLMessage();
            player1Tree = new AVLTree();
            player2Tree = new AVLTree();
            player3Tree = new AVLTree();
            player4Tree = new AVLTree();
        } else {
            //Challenge Splay
            message = new SplayMessage();
            player1Tree = new SplayTree();
            player2Tree = new SplayTree();
            player3Tree = new SplayTree();
            player4Tree = new SplayTree();
        }

        String messageJSON = null;
        try {
            messageJSON = objectMapper.writeValueAsString(message);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
        System.out.println("sent: " + messageJSON);
        out.println(messageJSON);

    }

    public void sendToken(){

        int tokenType = random.nextInt(4);

        int randomNumber = random.nextInt(100);

        Message message;

        if (tokenType == 0){
            //Token BTS (Rhombus)
            message = new BSTToken(randomNumber,0);
        } else if (tokenType == 1){
            //Token Type B (Square)
            message = new BToken(randomNumber,0);
        } else if (tokenType == 2){
            //Token AVL (Circle)
            message = new AVLToken(randomNumber,0);
        } else {
            //Token Splay (Triangle)
            message = new SplayToken(randomNumber,0);
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
