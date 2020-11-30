package server.Messages;

public class BToken extends Message{

    int number;

    public BToken(int number){

        this.number = number;

    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

}
