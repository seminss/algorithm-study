package 백트레킹;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 파이썬으로 푼 문제 자바로 변환
 * */
public class boj16987 {
    private static int answer=-301;
    private static List<int[]> eggs = new ArrayList<>();

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n= Integer.parseInt(br.readLine());
        for(int i=0;i<n;i++){
            StringTokenizer st= new StringTokenizer(br.readLine());
            int s=Integer.parseInt(st.nextToken()); //내구도
            int w=Integer.parseInt(st.nextToken()); //무게
            eggs.add(new int[] {s,w});
        }
        back(0,eggs);
        System.out.println(answer);
    }
    private static int countBrokenEggs(List<int[]> eggs){
        int count=0;
        for(int[] egg : eggs)
            if (egg[0]<=0) count+=1;
        return count;
    }
    private static void back(int depth,List<int[]> eggs){
        int brokenEggs=countBrokenEggs(eggs);
        if (brokenEggs>answer)
            answer=brokenEggs;
        if(depth==eggs.size()||brokenEggs==eggs.size())
            return;
        if(eggs.get(depth)[0]<=0){
            back(depth+1,eggs);
            return;
        }
        boolean allBroken=true;
        for(int i=0;i<eggs.size();i++){
            if(i==depth || eggs.get(i)[0]<=0)
                continue;
            allBroken=false;
            eggs.get(i)[0]-=eggs.get(depth)[1]; //내구도-무게
            eggs.get(depth)[0]-=eggs.get(i)[1];
            back(depth+1,eggs);
            eggs.get(i)[0]+=eggs.get(depth)[1]; //복귀
            eggs.get(depth)[0]+=eggs.get(i)[1];
        }
        if(allBroken)
            return;
    }
}
