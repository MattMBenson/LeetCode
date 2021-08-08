import java.util.*;

public class hackerrank_week1 {
    hackerrank_week1(){
        
    }
    public static void miniMaxSum2(List<Integer> arr) {
        // Write your code here
        int maxSum = -1;
        int minSum = Integer.MAX_VALUE;

        // n^2
        for (int i=0;i<arr.size();i++){
            int tempNum = 0;
            for (int j = 0;j<arr.size();j++){
                if (i != j){
                    tempNum = arr.get(i) + arr.get(j);
                }
            }
            if (tempNum > maxSum){
                maxSum = tempNum;
            }
            else if (tempNum < minSum){
                minSum = tempNum;
            }
        }
        System.out.println(minSum + " " + maxSum);

    }
    public static void plusMinus2(List<Integer> arr) {
        // Write your code here
            int size = arr.size();
            int pos = 0;
            int neg = 0;
            int even = 0;
            for (int i=0;i<size;i++){
                if (arr.get(i)>0){
                    pos++;
                }
                else if (arr.get(i)==0){
                    even++;
                }
                else {
                    neg++;
                }
            }
 
            System.out.println((float)pos/size);
            System.out.println((float)neg/size);
            System.out.println((float)even/size);
        }
    public static void main(String[] args) {
        new hackerrank_week1();
    }
}
