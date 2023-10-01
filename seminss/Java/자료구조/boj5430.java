package 자료구조;
//12:54~1:10, 1:55~2:30
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.stream.Collectors;

public class boj5430 {
    public static StringBuilder sb = new StringBuilder();
    private static void AC(String p, LinkedList<Integer> arr){
        boolean isReversed=false;
        for(char c: p.toCharArray()){
            if (c=='R')
                isReversed=!isReversed;
            else if (arr.isEmpty()) { //c=='D'
                sb.append("error\n");
                return;
            }
            else if (isReversed) //c=='D'
                arr.removeLast();
            else //c=='D'
                arr.removeFirst();
        }

        makeOutput(arr, isReversed);
    }

    private static void makeOutput(LinkedList<Integer> arr, boolean isReversed) {
        sb.append('[');
        if(arr.isEmpty()){
            sb.append("]\n");
            return;
        }
        if(isReversed)
            Collections.reverse(arr);
        sb.append(arr.removeFirst());
        while(!arr.isEmpty())
            sb.append(',').append(arr.removeFirst());
        sb.append("]\n");
    }

    private static LinkedList<Integer> makeLinkedList(String input) {
        LinkedList<Integer> arr;
        if (input.equals("[]")) {
            arr = new LinkedList<>();
        } else {
            arr = Arrays.stream(input.replaceAll("[\\[\\]]", "").split(","))
                    .map(Integer::parseInt)
                    .collect(Collectors.toCollection(LinkedList::new));
        }
        return arr;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T= Integer.parseInt(br.readLine());
        for (int i=0;i<T;i++){
            String p=br.readLine().strip();
            Integer.parseInt(br.readLine()); //input 길이
            String input=br.readLine().strip();
            LinkedList<Integer> arr;
            arr = makeLinkedList(input);
            AC(p, arr);
        }
        System.out.print(sb);
    }
}

//StringBuilder로 모든 결과를 묶어서 출력해야한다;;;;;;; 로직 똑같아도 각각 출력하면 틀린다ㅏ..