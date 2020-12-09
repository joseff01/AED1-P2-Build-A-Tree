package server.Messages;

public class TimerMessage {

    int timerNumber;

    String timerType;

    public TimerMessage(int number, String timerType){

        this.timerType = timerType;

        this.timerNumber = number;

    }

    public int getTimerNumber() {
        return timerNumber;
    }

    public void setTimerNumber(int number) {
        this.timerNumber = number;
    }

    public String getTimerType() {
        return timerType;
    }

    public void setTimerType(String timerType) {
        this.timerType = timerType;
    }
}
