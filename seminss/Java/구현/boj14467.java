package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Objects;
import java.util.StringTokenizer;

public class boj14467 {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N= Integer.parseInt(br.readLine());
        HashMap<String, String> cows= new HashMap<String, String>();
        int answer=0;
        for(int i=0;i<N;i++){
            String line=br.readLine();
            String[] parts=line.split(" ");
            String key= parts[0];
            String value=parts[1];
            if (cows.containsKey(key) && !Objects.equals(cows.get(key), value)) {
                answer++;
            }
            cows.put(key,value);
        }
        System.out.println(answer);
    }
}
