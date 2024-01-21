package SWEA.D4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class solution5432 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            sb.append("#").append(tc).append(" ");
            Stack<Character> stack = new Stack<>();
            String sticks = br.readLine();
            int result = 0;
            for (int i = 0; i < sticks.length(); i++) {
                char current = sticks.charAt(i);
                if (current == '(') {
                    stack.push(current);
                    continue;
                }
                stack.pop();
                if (sticks.charAt(i - 1) == ')') {
                    result++; //이미 이전에 통으로 잘랐음, 이후로는 -> 하나씩 증가
                    continue;
                }
                result += stack.size(); //통으로 자름
            }
            sb.append(result).append("\n");
        }
        System.out.println(sb);
    }
}
