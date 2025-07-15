public class MoveZeroes {
    public void moveZeroes(int[] nums) {
        int first, second;
        for(int i = 0; i < nums.length;i++)
        {
            if(nums[i] == 0)
            {
                first = i;
                second = first;
                while(second < nums.length-1 && nums[second] == 0)
                {
                    second++;
                }
                nums[first] = nums[second];
                nums[second] = 0;
            }
        }

        for(int num: nums)
            System.out.println(num);
    }
}
