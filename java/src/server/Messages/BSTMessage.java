package server.Messages;

import java.util.Random;

public class BSTMessage extends Message{

    int height;

    Random random = new Random();

    public BSTMessage(){
        this.height = random.nextInt(4) + 2;
    }

    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

}
