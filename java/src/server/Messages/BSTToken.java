package server.Messages;

public class BSTToken extends Message{

    int number;

    public BSTToken(int number){

        this.number = number;

    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

}
