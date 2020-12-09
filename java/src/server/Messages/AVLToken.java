package server.Messages;

import java.util.Random;

public class AVLToken extends Message{

    int number;

    int receiver;

    public AVLToken(int number, int receiver){

        this.number = number;
        this.receiver = receiver;

    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public int getReceiver() {
        return receiver;
    }

    public void setReceiver(int receiver) {
        this.receiver = receiver;
    }

}
