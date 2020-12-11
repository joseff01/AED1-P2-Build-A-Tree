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

    Tree[] treeArray = new Tree[4];

    Message currentChallenge;

    public ChallengeSelectionAlgorithm(BufferedReader in, PrintWriter out){

        this.in = in;
        this.out = out;

        timer = new Timer(in,out, this);
        listeningAlgorithm = new ListeningAlgorithm(in,out, this, objectMapper);

        selectChallenge();
        sendToken();

    }

    public void selectChallenge(){
        timer.setChallengeTimer(60);
        int challengeType = random.nextInt(4);

        challengeType = 3; //for testing

        if (challengeType == 0){
            //Challenge BST
            currentChallenge = new BSTMessage();
            player1Tree = new BSTree();
            ((BSTree)player1Tree).setOwner(1);
            player2Tree = new BSTree();
            ((BSTree)player2Tree).setOwner(2);
            player3Tree = new BSTree();
            ((BSTree)player3Tree).setOwner(3);
            player4Tree = new BSTree();
            ((BSTree)player4Tree).setOwner(4);
            treeArray[0] = player1Tree;
            treeArray[1] = player2Tree;
            treeArray[2] = player3Tree;
            treeArray[3] = player4Tree;

        } else if (challengeType == 1){
            //Challenge Type B
            currentChallenge = new BMessage();
            int order = ((BMessage) currentChallenge).getOrder();
            player1Tree = new BTree(order);
            ((BTree)player1Tree).setOwner(1);
            player2Tree = new BTree(order);
            ((BTree)player2Tree).setOwner(2);
            player3Tree = new BTree(order);
            ((BTree)player3Tree).setOwner(3);
            player4Tree = new BTree(order);
            ((BTree)player4Tree).setOwner(4);
            treeArray[0] = player1Tree;
            treeArray[1] = player2Tree;
            treeArray[2] = player3Tree;
            treeArray[3] = player4Tree;

        } else if (challengeType == 2){
            //Challenge AVL
            currentChallenge = new AVLMessage();
            player1Tree = new AVLTree();
            ((AVLTree)player1Tree).setOwner(1);
            player2Tree = new AVLTree();
            ((AVLTree)player2Tree).setOwner(2);
            player3Tree = new AVLTree();
            ((AVLTree)player3Tree).setOwner(3);
            player4Tree = new AVLTree();
            ((AVLTree)player4Tree).setOwner(4);
            treeArray[0] = player1Tree;
            treeArray[1] = player2Tree;
            treeArray[2] = player3Tree;
            treeArray[3] = player4Tree;

        } else {
            //Challenge Splay
            currentChallenge = new SplayMessage();
            player1Tree = new SplayTree();
            ((SplayTree)player1Tree).setOwner(1);
            player2Tree = new SplayTree();
            ((SplayTree)player2Tree).setOwner(2);
            player3Tree = new SplayTree();
            ((SplayTree)player3Tree).setOwner(3);
            player4Tree = new SplayTree();
            ((SplayTree)player4Tree).setOwner(4);
            treeArray[0] = player1Tree;
            treeArray[1] = player2Tree;
            treeArray[2] = player3Tree;
            treeArray[3] = player4Tree;

        }

        String messageJSON = null;
        try {
            messageJSON = objectMapper.writeValueAsString(currentChallenge);
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
            Thread.sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        sendToken();
    }

    public Message getCurrentChallenge() {
        return currentChallenge;
    }

    public Tree[] getTreeArray() {
        return treeArray;
    }

}
