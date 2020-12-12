package server.Messages;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;

import javax.sound.midi.Receiver;

@JsonIgnoreProperties(ignoreUnknown = true)
@JsonTypeInfo(use = JsonTypeInfo.Id.NAME, include = JsonTypeInfo.As.PROPERTY)
@JsonSubTypes({
        @JsonSubTypes.Type(value = AVLMessage.class, name = "AVLMessage"),
        @JsonSubTypes.Type(value = BMessage.class, name = "BMessage"),
        @JsonSubTypes.Type(value = BSTMessage.class, name = "BSTMessage"),
        @JsonSubTypes.Type(value = SplayMessage.class, name = "SplayMessage"),
        @JsonSubTypes.Type(value = AVLToken.class, name = "AVLToken"),
        @JsonSubTypes.Type(value = BToken.class, name = "BToken"),
        @JsonSubTypes.Type(value = BSTToken.class, name = "BSTToken"),
        @JsonSubTypes.Type(value = SplayToken.class, name = "SplayToken"),
        @JsonSubTypes.Type(value = TimerMessage.class, name = "TimerMessage"),
        @JsonSubTypes.Type(value = Message.class, name = "Message"),

})
/**
 * @author Jose Antonio Retana
 * Clase encargada del manejo de los mensajes y con JSONS
 */
public abstract class Message { }
