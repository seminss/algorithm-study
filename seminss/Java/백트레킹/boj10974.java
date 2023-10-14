package 백트레킹;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class boj10974 {
    private static int n;
    static List<String> answer = new ArrayList<>();

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n= Integer.parseInt(br.readLine());
        for(int i=1;i<=n;i++)
            back(new ArrayList<>(Arrays.asList(i)));
        Collections.sort(answer);
        answer.stream().forEach(System.out::println);
    }

    private static void back(List<Integer> list) {
        if(list.size()==n){
            StringBuilder sb = new StringBuilder();
            list.stream().forEach(num->sb.append(num).append(" "));
            answer.add(String.valueOf(sb));
            return;
        }
        for(int i=1;i<=n;i++){
            if(list.contains(i))
                continue;
            list.add(i);
            back(new ArrayList<>(list)); //매번 새로 할당해줘야 함, 안그러면 인덱스 에러
            list.remove(list.size()-1); //지울 때는 인덱스
        }
    }
}
