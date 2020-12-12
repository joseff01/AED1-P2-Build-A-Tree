package server;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import server.Messages.*;
import server.Trees.*;

import java.io.BufferedReader;
import java.io.PrintWriter;
import java.util.Random;

/**
 * Clase principal del servidor.
 * Manda los nodos, mantiene los árboles de los jugadores
 *
 * @Author Jose Retana
 */
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

    /**
     * Constructor
     * Recibe el BufferedReader y PrintWriter creados en el main
     *
     * @param in
     * @param out
     * @author Jose Retana
     */
    public ChallengeSelectionAlgorithm(BufferedReader in, PrintWriter out){

        this.in = in;
        this.out = out;

        timer = new Timer(in,out, this, objectMapper);
        listeningAlgorithm = new ListeningAlgorithm(in,out, this, objectMapper);

        selectChallenge();
        sendToken();

    }

    /**
     * Método de selección, creación y envío del challenge al cliente
     * Resetea los árboles actuales y cambia el timer del challenge
     *
     * @author Jose Retana
     */
    public void selectChallenge(){
        timer.setChallengeTimer(60);
        int challengeType = random.nextInt(4);
        
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
        try {
            Thread.sleep(10);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        out.println(messageJSON);

    }

    /**
     * Método de selección y envío de tokes al cliente
     *
     * @author Jose Retana
     */
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

    /**
     * Getter del challenge activo
     * @return currentChallenge
     */
    public Message getCurrentChallenge() {
        return currentChallenge;
    }

    /**
     * Getter del array con los árboles de los jugadores
     * @return treeArray
     */
    public Tree[] getTreeArray() {
        return treeArray;
    }

}
