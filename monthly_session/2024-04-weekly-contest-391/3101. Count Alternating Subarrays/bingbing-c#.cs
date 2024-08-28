public class Solution {
     public long CountAlternatingSubarrays(int[] nums) {
        long num = 1;
        long count = 0;
        for(var i = 0; i<nums.Length;i++){
            if(i+1<nums.Length){
                if(nums[i] == nums[i+1]){
                    count+=ReturnCount(num);
                    num = 0;
                }
                num++;
            }else{
                count+=ReturnCount(num);
            }
        }

        return count;
    }

    public long ReturnCount(long num){
        if(num%2 == 0){
            return (num+1)*(num/2);
        }else{
            return (num+1)*(num/2)+ (num+1)/2;
        }
    }
}


