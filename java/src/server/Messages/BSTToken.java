package server.Messages;

public class BSTToken extends Message{

    int number;

    int receiver;
    public BSTToken(int number, int receiver){

        this.number = number;
        this.receiver = receiver;

    }
    public BSTToken(){
        super();
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
