package server;

import com.fasterxml.jackson.databind.ObjectMapper;
import server.Messages.*;
import server.Trees.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.PrintWriter;

public class ListeningAlgorithm implements Runnable {

    ObjectMapper objectMapper;

    ChallengeSelectionAlgorithm challengeSelectionAlgorithm;

    BufferedReader in;
    PrintWriter out;

    public ListeningAlgorithm(BufferedReader in, PrintWriter out, ChallengeSelectionAlgorithm challengeSelectionAlgorithm, ObjectMapper objectMapper) {
        this.in = in;
        this.out = out;
        this.challengeSelectionAlgorithm = challengeSelectionAlgorithm;
        this.objectMapper = objectMapper;

        Thread listenThread = new Thread(this);
        listenThread.start();
    }

    @Override
    public void run() {

        boolean disconnectionFlag = false;

        while (!disconnectionFlag) {
            try {
                String messageJson = in.readLine();
                System.out.println("received: " + messageJson);
                Message receivedMessage = objectMapper.readValue(messageJson, Message.class);
                Message currentChallenge = challengeSelectionAlgorithm.getCurrentChallenge();
                Tree[] treeArray = challengeSelectionAlgorithm.getTreeArray();
                int player;
                Tree tree = null;
                if (currentChallenge instanceof AVLMessage) {
                    if (receivedMessage instanceof AVLToken) {
                        player = ((AVLToken) receivedMessage).getReceiver() - 1;
                        tree = treeArray[player];
                        ((AVLTree)tree).insert(((AVLToken) receivedMessage).getNumber());
                        treeArray[player] = tree;
                        int amount = ((AVLTree)tree).getSize();
                        if (amount == ((AVLMessage) currentChallenge).getElementAmount()){
                            System.out.println("{\"@type\":\"AddPoints\",\"Points\":100,\"player\":" + player + "}");
                            out.println("{\"@type\":\"AddPoints\",\"Points\":100,\"player\":" + player + "}");
                            challengeSelectionAlgorithm.selectChallenge();
                        }
                    } else if (receivedMessage instanceof BSTToken) {
                        player = ((BSTToken) receivedMessage).getReceiver() - 1;
                        tree = new AVLTree();
                        ((AVLTree) tree).setOwner(player+1);
                        treeArray[player] = tree;
                    } else if (receivedMessage instanceof BToken) {
                        player = ((BToken) receivedMessage).getReceiver() - 1;
                        tree = new AVLTree();
                        ((AVLTree) tree).setOwner(player+1);
                        treeArray[player] = tree;
                    } else if (receivedMessage instanceof SplayToken) {
                        player = ((SplayToken) receivedMessage).getReceiver() - 1;
                        tree = new AVLTree();
                        ((AVLTree) tree).setOwner(player+1);
                        treeArray[player] = tree;
                    }
                    System.out.println(objectMapper.writeValueAsString(tree));
                    out.println(objectMapper.writeValueAsString(tree));
                } else if (currentChallenge instanceof BSTMessage) {
                    if (receivedMessage instanceof AVLToken) {
                        player = ((AVLToken) receivedMessage).getReceiver() - 1;
                        tree = new BSTree();
                        ((BSTree) tree).setOwner(player+1);
                        treeArray[player] = tree;
                    } else if (receivedMessage instanceof BSTToken) {
                        player = ((BSTToken) receivedMessage).getReceiver() - 1;
                        tree = treeArray[player];
                        ((BSTree)tree).insert(((BSTToken) receivedMessage).getNumber());
                        treeArray[player] = tree;
                        int height = ((BSTree)tree).getHeight();
                        if (height == ((BSTMessage) currentChallenge).getHeight()){
                            System.out.println("{\"@type\":\"AddPoints\",\"Points\":100,\"player\":" + player + "}");
                            out.println("{\"@type\":\"AddPoints\",\"Points\":100,\"player\":" + player + "}");
                            challengeSelectionAlgorithm.selectChallenge();
                        }
                    } else if (receivedMessage instanceof BToken) {
                        player = ((BToken) receivedMessage).getReceiver() - 1;
                        tree = new BSTree();
                        ((BSTree) tree).setOwner(player+1);
                        treeArray[player] = tree;
                    } else if (receivedMessage instanceof SplayToken) {
                        player = ((SplayToken) receivedMessage).getReceiver() - 1;
                        tree = new BSTree();
                        ((BSTree) tree).setOwner(player+1);
                        treeArray[player] = tree;
                    }
                    System.out.println(objectMapper.writeValueAsString(tree));
                    out.println(objectMapper.writeValueAsString(tree));
                } else if (currentChallenge instanceof BMessage) {
                    int order = ((BMessage) currentChallenge).getOrder();
                    if (receivedMessage instanceof AVLToken) {
                        player = ((AVLToken) receivedMessage).getReceiver() - 1;
                        tree = new BTree(order);
                        ((BTree) tree).setOwner(player+1);
                        treeArray[player] = tree;
                    } else if (receivedMessage instanceof BSTToken) {
                        player = ((BSTToken) receivedMessage).getReceiver() - 1;
                        tree = new BTree(order);
                        ((BTree) tree).setOwner(player+1);
                        treeArray[player] = tree;
                    } else if (receivedMessage instanceof BToken) {
                        player = ((BToken) receivedMessage).getReceiver() - 1;
                        tree = treeArray[player];
                        ((BTree)tree).insert(((BToken) receivedMessage).getNumber());
                        treeArray[player] = tree;
                        int height = ((BTree)tree).getHeight();
                        if (height == ((BMessage) currentChallenge).getLevel()){
                            System.out.println("{\"@type\":\"AddPoints\",\"Points\":100,\"player\":" + player + "}");
                            out.println("{\"@type\":\"AddPoints\",\"Points\":100,\"player\":" + player + "}");
                            challengeSelectionAlgorithm.selectChallenge();
                        }
                    } else if (receivedMessage instanceof SplayToken) {
                        player = ((SplayToken) receivedMessage).getReceiver() - 1;
                        tree = new BTree(order);
                        ((BTree) tree).setOwner(player+1);
                        treeArray[player] = tree;
                    }
                    System.out.println(objectMapper.writeValueAsString(tree));
                    out.println(objectMapper.writeValueAsString(tree));
                } else if (currentChallenge instanceof SplayMessage) {
                    if (receivedMessage instanceof AVLToken) {
                        player = ((AVLToken) receivedMessage).getReceiver() - 1;
                        tree = new SplayTree();
                        ((SplayTree) tree).setOwner(player+1);
                        treeArray[player] = tree;
                    } else if (receivedMessage instanceof BSTToken) {
                        player = ((BSTToken) receivedMessage).getReceiver() - 1;
                        tree = new SplayTree();
                        ((SplayTree) tree).setOwner(player+1);
                        treeArray[player] = tree;
                    } else if (receivedMessage instanceof BToken) {
                        player = ((BToken) receivedMessage).getReceiver() - 1;
                        tree = new SplayTree();
                        ((SplayTree) tree).setOwner(player+1);
                        treeArray[player] = tree;
                    } else if (receivedMessage instanceof SplayToken) {
                        player = ((SplayToken) receivedMessage).getReceiver() - 1;
                        tree = treeArray[player];
                        ((SplayTree)tree).insert(((SplayToken) receivedMessage).getNumber());
                        treeArray[player] = tree;
                        int height = ((SplayTree)tree).getSize();
                        if (height == ((SplayMessage) currentChallenge).getElementAmount()){
                            System.out.println("{\"@type\":\"AddPoints\",\"Points\":100,\"player\":" + player + "}");
                            out.println("{\"@type\":\"AddPoints\",\"Points\":100,\"player\":" + player + "}");
                            challengeSelectionAlgorithm.selectChallenge();
                        }
                    }
                    System.out.println(objectMapper.writeValueAsString(tree));
                    out.println(objectMapper.writeValueAsString(tree));
                } else {
                    System.out.println("THIS SHOULD NOT BE HAPPENING. LOOK INTO THIS");
                }


            } catch (IOException e) {
                e.printStackTrace();
                disconnectionFlag = true;
            }
        }
    }
}
