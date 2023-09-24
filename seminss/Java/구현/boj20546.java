package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class boj20546 {

    public static int junhyon(int seed, List<Integer> prices){
        int num=0;
        for( int p:prices){
            if (p>seed)
                continue;
            num+=seed/p;
            seed%=p;
        }
        return seed+num*prices.get(prices.size()-1);
    }

    public static int seongmin(int seed, List<Integer> prices){
        int num=0;
        for(int i=3;i<prices.size();i++){
            int p3=prices.get(i);
            int p2=prices.get(i-1);
            int p1=prices.get(i-2);
            int p0=prices.get(i-3);
            if (p0>p1 && p1>p2 && p2>p3 && p3<=seed){
                num+=seed/p3;
                seed%=p3;
            }
            else if (p0<p1 && p1<p2 && p2<p3 ){
                seed+=num*p3;
                num=0;
            }
        }
        return seed+num*prices.get(prices.size()-1);
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int money= Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> prices= new ArrayList<>();
        while(st.hasMoreTokens()){
            prices.add(Integer.parseInt(st.nextToken()));
        }

        var j=junhyon(money, prices);
        var s=seongmin(money,prices);

        var answer = switch(Integer.compare(j,s)){
            case 0 -> "SAMESAME";
            case 1 -> "BNP";
            default -> "TIMING";
        };

        System.out.print(answer);
    }
}
