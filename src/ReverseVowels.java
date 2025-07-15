import java.util.Set;

public class ReverseVowels {
    public String R2(String s){
        Set<Character> vowels = Set.of('a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U');
        char[] letters = s.toCharArray();
        int left = 0, right = letters.length-1;
        char temp;

        while(left < right){
            // Move left pointer to next vowel
            while (left < right && !vowels.contains(letters[left])) {
                left++;
            }

            // Move right pointer to previous vowel
            while (left < right && !vowels.contains(letters[right])) {
                right--;
            }

            temp = letters[left];
            letters[left] = letters[right];
            letters[right] = temp;
            left++;
            right--;
        }
        return new String(letters);
    }
}
