package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Integer.parseInt;

public class boj8979 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());

        int n = parseInt(st.nextToken());
        int k = parseInt(st.nextToken());
        Country[] countries = new Country[n+1];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int name = Integer.parseInt(st.nextToken());
            int gold = Integer.parseInt(st.nextToken());
            int silver = Integer.parseInt(st.nextToken());
            int bronze = Integer.parseInt(st.nextToken());
            Country country = new Country(gold, silver, bronze);
            countries[name] = country;
        }
        int rank = 1;
        for (int i = 1; i <= n; i++) {
            if (countries[k].compareTo(countries[i]) < 0) {
                rank++;
            }
        }
        System.out.println(rank);
    }

    static class Country implements Comparable<Country> {
        int gold;
        int silver;
        int bronze;

        public Country(int gold, int silver, int bronze) {
            this.gold = gold;
            this.silver = silver;
            this.bronze = bronze;
        }

        @Override
        public int compareTo(Country o) {
            if (this.gold > o.gold) {
                return 1;
            }
            if (this.gold == o.gold && this.silver > o.silver) {
                return 1;
            }
            if (this.gold == o.gold && this.silver == o.silver && this.bronze > o.bronze) {
                return 1;
            }
            if (this.gold == o.gold && this.silver == o.silver && this.bronze == o.bronze) {
                return 0;
            }
            return -1;
        }
    }
}
