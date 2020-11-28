package server.Messages;

import java.util.Random;

public class AVLMessage extends Message{

    int elementAmount;

    Random random = new Random();

    public AVLMessage(){
        this.elementAmount = random.nextInt(8) + 3;
    }

    public int getElementAmount() {
        return elementAmount;
    }

    public void setElementAmount(int elementAmount) {
        this.elementAmount = elementAmount;
    }

}
