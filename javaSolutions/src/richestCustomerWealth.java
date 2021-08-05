public class richestCustomerWealth {

    richestCustomerWealth(){
        int [][] accounts = {{1,2,3},{3,2,1}};
        System.out.println(maximumWealth(accounts));
    }

    public int maximumWealth(int[][] accounts) {
        int richest = 0;
        
        for (int i=0;i<accounts.length;i++){
            int sum = 0;
            for (int j=0;j<accounts[i].length;j++){
                sum += accounts[i][j];
                if (sum > richest){
                    richest = sum;
                }
            }
        }
        return richest;
    }

    public static void main(String[] args) {
        new richestCustomerWealth();
    }
}