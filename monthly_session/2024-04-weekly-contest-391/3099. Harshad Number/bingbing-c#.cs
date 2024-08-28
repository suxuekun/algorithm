public class Solution {
    public int SumOfTheDigitsOfHarshadNumber(int x) {
        int count = 0;
        int origan = x;
        while(x>0){
            int remindder = x%10;
            x = x/10;
            count+=remindder;
        }

        if(origan % count == 0){
            return count;
        }

        return -1;
    }
}