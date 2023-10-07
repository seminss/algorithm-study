package 자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class boj2504 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputs=br.readLine();
        Stack<Object> stack= new Stack<>();
        int i;
        for(i=0;i<inputs.length();i++){
            Character ch=inputs.charAt(i);
            if(ch.equals('(') ||ch.equals('['))
                stack.push(ch);
            else if(ch.equals(')')&&!stack.isEmpty()){
                if(stack.peek().equals('(')){
                    stack.pop();
                    stack.push(2);
                }
                else if (stack.peek() instanceof Integer){
                    int num=0;
                    while(!stack.isEmpty()&&stack.peek() instanceof Integer) //스택에 정수, 캐릭터를 모두 넣었기 때문에 Integer 인지 체크
                        num+=(Integer)stack.pop();
                    if(!stack.isEmpty()&&stack.peek().equals('(')){ // 내부 값들 더할 때도 숫자인지 체크해줘야 함, ClassCastException 터짐
                        stack.pop();
                        stack.push(num*2);
                    }else break;
                }
            }
            else if(ch.equals(']')&&!stack.isEmpty()){
                if(stack.peek().equals('[')){
                    stack.pop();
                    stack.push(3);
                }
                else if (stack.peek() instanceof Integer){
                    int num=0;
                    while(!stack.isEmpty()&&stack.peek() instanceof Integer)
                        num+=(Integer)stack.pop();
                    if(!stack.isEmpty()&&stack.peek().equals('[')){
                        stack.pop();
                        stack.push(num*3);
                    }else break;
                }
            }
            else //잘못된 입력 예외처리
                break;
        }

        int result=0;
        while(!stack.isEmpty()){
            if(stack.peek() instanceof Integer)
                result+=(Integer)stack.pop();
            else
                break;
        }
        System.out.println(stack.isEmpty()||i<inputs.length()-1?result:0);
    }
}
