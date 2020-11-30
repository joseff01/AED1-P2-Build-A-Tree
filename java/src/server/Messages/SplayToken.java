package server.Messages;

public class SplayToken extends Message{


    int number;

    public SplayToken(int number){

        this.number = number;

    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

}
