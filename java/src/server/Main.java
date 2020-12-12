package server;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import server.Trees.BSTree;
import server.Trees.BTree;
import server.Trees.SplayTree;
import server.Trees.Tree;

import java.io.*;
import java.net.ServerSocket; 
import java.net.Socket;

public class Main {


    public static void main(String[] args) {

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
