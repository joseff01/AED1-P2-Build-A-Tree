package server;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import server.Trees.SplayTree;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Main {


    public static void main(String[] args) {

        /*

        SplayTree bTree = new SplayTree();
        bTree.insert(5);
        bTree.insert(6);
        bTree.insert(4);
        bTree.insert(2);
        bTree.insert(1);
        bTree.insert(10);
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            System.out.println(objectMapper.writeValueAsString(bTree));
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        */

        ServerSocket listenSocket = null;

        boolean foundSocketFlag = false;

        boolean startGameFlag = false;

        int ListenSocketNum = 10000;

        while (!foundSocketFlag) {
            try{
                listenSocket = new ServerSocket(ListenSocketNum);
                foundSocketFlag = true;
                System.out.println("ServerSocket: " + ListenSocketNum);
            } catch (IOException e) {
                ListenSocketNum++;
            }
        }

        while (!startGameFlag){
            try{
                Socket EntrySocket = listenSocket.accept();

                BufferedReader in = new BufferedReader(new InputStreamReader(EntrySocket.getInputStream()));

                PrintWriter out = new PrintWriter(EntrySocket.getOutputStream(),true);

                String startGameMessage = in.readLine();
                System.out.println(startGameMessage);
                if (startGameMessage.equals("Start Server Connection")){
                    System.out.println("EntrySocket: " + EntrySocket.getPort());
                    ChallengeSelectionAlgorithm challengeAlgorithm = new ChallengeSelectionAlgorithm(in, out);
                    startGameFlag = true;
                }
            } catch (Exception e) {
                e.printStackTrace();
            }

        }



    }
}
