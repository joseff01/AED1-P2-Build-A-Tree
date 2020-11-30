package server.Messages;

import java.util.Random;

public class AVLToken extends Message{

    int number;

    public AVLToken(int number){

        this.number = number;

    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


}
