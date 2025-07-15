import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.OptionalInt;

public class MostCandies {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> answers = new ArrayList<>();
        int max = Arrays.stream(candies).max().orElse(candies[0]);

        for(int candy: candies){
            answers.add(candy + extraCandies >= max);
        }

        return answers;
    }
}
