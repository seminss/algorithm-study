package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj20164 {

    private static int min=100;
    private static int max=0;

    private static void countOdd(String numbers,int cnt) {
        for(char c : numbers.toCharArray()) {
            if (Character.getNumericValue(c)%2==1) {
                cnt++;
            }
        }
        if(numbers.length()==1){
            if(cnt>max) max=cnt;
            if(cnt<min) min=cnt;
            return;
        }
        else if (numbers.length()==2){
            int fstNum= Integer.parseInt(numbers.substring(0,1));
            int secNum= Integer.parseInt(numbers.substring(1,2));
            countOdd(String.valueOf(fstNum+secNum),cnt);
            return;
        }
        for(int i=1;i<numbers.length();i++){
            for(int j=i+1;j<numbers.length();j++){
                int fstNum= Integer.parseInt(numbers.substring(0,i));
                int secNum= Integer.parseInt(numbers.substring(i,j));
                int thdNum= Integer.parseInt(numbers.substring(j,numbers.length()));
                //System.out.printf("%d %d %d = %d", fstNum,secNum,thdNum,fstNum+secNum+thdNum);
                countOdd(String.valueOf(fstNum+secNum+thdNum),cnt);
            }
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String numbers=br.readLine();
        int cnt=0;
        countOdd(numbers,cnt);
        System.out.print(min+" "+max);
    }
}
