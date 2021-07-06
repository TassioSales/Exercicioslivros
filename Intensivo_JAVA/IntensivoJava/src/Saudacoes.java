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
        for(int i = 0; i < list.size(); i++){
            System.out.println("Ola, tudo bem " + list.get(i));
        }
    } 
}