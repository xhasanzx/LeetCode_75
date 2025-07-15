public class IncreasingTriplet {
    public boolean increasingTriplet(int[] nums) {
        if(nums.length < 3) return false;
        int first = nums[0], second = nums[1];
        for(int i = 2;i < nums.length;i++){
            if(first >= second) {
                first = second;
                second = nums[i];
                continue;
            }
            if(nums[i] < first) first = nums[i];
            if(nums[i] > first && nums[i] < second) second = nums[i];
            if(nums[i] > second) return true;
        }
        return false;
    }
}
