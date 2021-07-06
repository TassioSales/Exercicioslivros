import java.util.ArrayList;
import java.util.List;

// Armazene os nomes de alguns de seus amigos em uma lista
// chamada names. Exiba o nome de cada pessoa acessando cada elemento da
// lista, um de cada vez.

import java.util.*;   
  
public class Nomes { 
    public static void main(String args[]) 
    { 
        List<String> list = new ArrayList<String>(){
          {
           add("João");
           add("Maria");
           add("Jose");
           add("Madalena");
          }
        };
        for(int i = 0; i < list.size(); i++){
            System.out.println(list.get(i));
        }
    } 
}

