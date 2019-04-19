/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hangman;

import static java.lang.Character.toLowerCase;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;


public class Hangman {
          
      public String getWord(int index) throws Exception {
          switch (index) {
          case 0: return "BUOY";
          case 1: return "COMPUTER";
          case 2: return "CONNOISSEUR";
          case 3: return "DEHYDRATE";
          case 4: return "FUZZY";
          case 5: return "HUBBUB";
          case 6: return "KEYHOLE";
          case 7: return "QUAGMIRE";
          case 8: return "SLITHER";
          case 9: return "ZIRCON";
          default: throw new Exception("getWord: Illegal index");
}
      }
      Hangman() {
  
        String word;
          try {
              word = getWord(ThreadLocalRandom.current().nextInt(0, 10));
        String temp=word.toLowerCase();
        int count=8;
        HashMap<Character,ArrayList> map=new HashMap<>();
        StringBuilder guess=new StringBuilder();
        for(int i=0;i<temp.length();i++)
            guess.append('-');
        for(int i=0;i<temp.length();i++){
            if(!map.containsKey(temp.charAt(i))){
            map.put(temp.charAt(i),new ArrayList<>());
            map.get(temp.charAt(i)).add(i);
            }else
                map.get(temp.charAt(i)).add(i);
        }
        System.out.println("You Have to Guess a Word"); 
        Scanner reader = new Scanner(System.in);
        while(count!=0&&!guess.toString().equals(temp)){
          // Reading from System.in
        System.out.println("Enter Your Guess: "); 
        Character n = reader.next().charAt(0); // Scans the next token of the input as an int.
        //once finishedc
        if(map.containsKey(n)){
        ArrayList temparr=map.get(n);
        for(int i=0;i<temparr.size();i++){
            guess.setCharAt((int) temparr.get(i), toLowerCase(n));
        }
        System.out.println(guess);
        }else{
            System.out.println("Wrong Guess");
            count--;   
            System.out.println(count+" Guesses Remaining");
        }
        }
        reader.close();
        if(guess.toString().equals(temp)){
            System.out.println("You Won!");
        }else{
            System.out.println("You Loser!");
        }
        } catch (Exception ex) {
              System.out.println(ex);
          }
    }
      
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
       Hangman hm=new Hangman();
    }
    
}

