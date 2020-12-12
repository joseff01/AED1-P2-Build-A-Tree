package server.Trees;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import server.Trees.*;

/**
 * @author Jose Antonio Retana
 * Manejo de los árboles para un archivo JSON
 */
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonTypeInfo(use = JsonTypeInfo.Id.NAME, include = JsonTypeInfo.As.PROPERTY)
@JsonSubTypes({
        @JsonSubTypes.Type(value = AVLTree.class, name = "AVLTree"),
        @JsonSubTypes.Type(value = BSTree.class, name = "BSTree"),
        @JsonSubTypes.Type(value = BTree.class, name = "BTree"),
        @JsonSubTypes.Type(value = SplayTree.class, name = "SplayTree"),
})
public abstract class Tree {}
