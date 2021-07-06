import java.util.*;   
  
public class Saudacoes { 
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
        for (String s : list) {
            System.out.println("Ola, tudo bem " + s);
        }
    } 
}