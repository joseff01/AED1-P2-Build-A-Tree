package server.Messages;

public class SplayToken extends Message{


    int number;

    int receiver;

    public SplayToken(int number, int receiver){

        this.number = number;
        this.receiver = receiver;

    }
    public SplayToken(){
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
