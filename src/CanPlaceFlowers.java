import java.lang.foreign.StructLayout;

public class CanPlaceFlowers {

    // {1,0,0,0,0,1}, 2
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int availableBeds = 0;
        Boolean emptyLeft, emptyRight;
        int len = flowerbed.length;

        for(int i = 0;i < len;i++){
            if(flowerbed[i] == 0){
                emptyLeft = (i == 0) || (flowerbed[i-1] == 0);
                emptyRight = (i == len-1) || (flowerbed[i+1] == 0);

                if(emptyRight && emptyLeft){
                    availableBeds++;
                    flowerbed[i] = 1;
                    i++;
                }
            }
        }
        return (availableBeds >= n);
    }
}
