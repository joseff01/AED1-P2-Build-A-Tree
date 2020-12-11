package server.Messages;

public class BToken extends Message{

    int number;

    int receiver;
    public BToken(int number, int receiver){

        this.number = number;
        this.receiver = receiver;

    }
    public BToken(){
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
