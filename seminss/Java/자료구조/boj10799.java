package 자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class boj10799 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String sticks=br.readLine();
        int answer=0;
        Stack<Character> stack = new Stack<>();
        for (int i=0;i<sticks.length();i++){
            char ch= sticks.charAt(i);
            if(ch=='(')
                stack.push(ch);
            else if(ch==')') {
                stack.pop();
            }
            if (i>0){
                if(ch==')' && sticks.charAt(i-1)=='(')
                    answer+=stack.size();
                else if (ch==')' && sticks.charAt(i-1)==')')
                    answer++;
            }
        } //3+3+1+3+1+2+1+1+1+1 =17
        System.out.println(answer);
    }
}

/**
 *  ()(((()())(())()))(())
 *   #((( # #)( #) #))( #)
 **/