public class ProductExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        if(nums.length == 1) return nums;
        if(nums.length == 2){
            int temp = nums[0];
            nums[0] = nums[1];
            nums[1] = temp;
            return nums;
        }

        int[] products = new int[nums.length];
        int length = nums.length - 1, right = 1;
        int[] accLeft = new int[length+1], accRight = new int[length+1];

        accRight[length] = accLeft[0] = 1;
        accRight[length-1] = nums[length];
        accLeft[1] = nums[0];

        for(int i = 2;i <= length;i++){
            products[i] = accLeft[i-1] * nums[i - 1];
        }
        for(int i = 0; i <= length;i++){
            products[i] = accLeft[i]*accRight[i];
        }
        return products;
    }
    public int[] better(int[] nums){
        int[] products = new int[nums.length];

        // First pass: calculate left products
        products[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            products[i] = products[i - 1] * nums[i - 1];
        }

        // Second pass: calculate right products on the fly and multiply into products[]
        int suffixProduct = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            products[i] *= suffixProduct;
            suffixProduct *= nums[i];
        }

        return products;
    }
}
