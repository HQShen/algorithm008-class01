class Solution {
    public void rotate(int[] nums, int k) {
        int count = 0;
        for (int start=0; count < nums.length; start++){
            int current = start;
            int prev = nums[start];
            do{
                current = (current + k)%nums.length;
                int tem = nums[current];
                nums[current] = prev;
                prev = tem;
                count ++;
            }while(start != current);
        }
    }
}