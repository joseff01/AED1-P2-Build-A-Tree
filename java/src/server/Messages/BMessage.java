package server.Messages;

import java.util.Random;

public class BMessage extends Message{

    int order;

    int level;

    Random random = new Random();

    public BMessage(){
        this.order = random.nextInt(3) + 3;
        this.level = random.nextInt(3) + 2;
    }

    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }

    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

}
