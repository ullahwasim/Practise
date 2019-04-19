/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ai;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

/**
 *
 * @author k164018
 */
class Edge{
    int weight;
    String node;
    Edge(){
        weight=0;
        node="";
    }
    public Edge(String n, int w){
            this.node = n;
            this.weight = w;
        }
        public String getNode(){
            return node;
        }      
        public int getWieght(){
            return weight;
        }
}
class Graph{
    HashMap<String,LinkedList> arr;
    HashMap<String,Integer> heuristics=new HashMap<>();
    HashMap<String,String> map=new HashMap<>();
    Graph(){
        arr = new HashMap<>();
    }
    void addEdge(String Node,String ConnectedNode,int weight){
        Edge e=new Edge(ConnectedNode,weight);
        LinkedList<Edge> list;
        if(!arr.containsKey(Node)){
        list = new LinkedList<>();
        list.add(e);
        arr.put(Node,list);
        }else{
        list=arr.get(Node);
        list.add(e);
        }
        
        //Edge q=(Edge) arr.get("a").get(0);
        //System.out.println(q.getNode());
    }

    
    boolean DFS(String source,String des){
        boolean flag=true;
        String temp=source,temp1;
        ArrayList<String> Visited;
        Visited = new ArrayList<>();
        ArrayList<String> Path;
        Path = new ArrayList<>();
        Stack<String> stack;
        stack = new Stack<>();
        stack.add(source);
        System.out.println(source);
        map.put(source, null);
        while(!stack.isEmpty()){
            
          //  Edge q=(Edge) arr.get(temp).get(0);
            if(arr.containsKey(temp)){
            if(!arr.get(temp).isEmpty()){
            Iterator edge=arr.get(temp).iterator();
            while(edge.hasNext()){
                Edge q=(Edge) edge.next();
                temp1=q.getNode();
                if(!Visited.contains(temp1)){
                stack.add(temp1);
                map.put(temp1, temp);
                System.out.println(temp1);
                Visited.add(temp1);
                flag=false;
                break;
                }
            }
            if(flag){
                stack.pop();
            }
            flag=true;
              if(stack.isEmpty()){
                  System.out.println("Destination Not Found");
            return false;
        }
            temp=stack.peek();
            }
            }else{
                stack.pop(); 
                 flag=true;
            temp=stack.peek();
            }
      
       // temp=stack.pop();
        
        if(temp.equals(des)){
            System.out.println("Destination Found");
            break;
        }
     }
        return true;
    }
   
    int PrintPath(String des){
        int cost=0;
        String s,temp="";
        while(des != null){
        if(map.containsKey(des)){
            s=map.get(des);
            if(arr.containsKey(s)){
            if(!arr.get(s).isEmpty()){
            Iterator edge=arr.get(s).iterator();
            Edge q;
            do{
                
                q=(Edge) edge.next();
                temp=q.getNode();
                if(temp.equals(des))
                    break;
                }while(edge.hasNext());
            temp="";
                cost=cost+q.getWieght();
                System.out.print(des+" --> ");
            }
        
        }
            des=s;
        }
        }
        return cost;
        }
    
}
class AI {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
      
      
              BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        Scanner in = new Scanner(System.in);
        Graph graph=new Graph();
	String s,d,a;
        String str = null; 
	Integer c;
	while(true){
	System.out.println("Enter Edge Source");	
	s = reader.readLine();
	System.out.println("Enter Edge Destination");
	d = reader.readLine();
	System.out.println("Enter Edge Cost");
	c = Integer.parseInt(reader.readLine());
	graph.addEdge(s, d, c);
	System.out.println("Enter exit if you are done else enter anything");
  
	a = reader.readLine();
        System.out.println(a);
	if(a.equals("exit"))
		break;
	}
        //graph.addEdge("oralea", "zerlind", 71);
        //String source="oralea",des="neamt";
	System.out.println("Enter Edge Source for Start Edge");	
	s = reader.readLine();
	System.out.println("Enter Edge Destination");
	d = reader.readLine();
       // String source="arad",des="bucharesh";
        System.out.println("-----------------DFS---------------------");
        boolean tem=graph.DFS(s, d);
        if(tem)
        System.out.println(s+" Cost is "+graph.PrintPath(d));
     
    }
    
}

