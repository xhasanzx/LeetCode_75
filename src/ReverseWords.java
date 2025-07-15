import java.util.NoSuchElementException;

public class ReverseWords {
    public String reverse(String s) {
        char[] str = s.toCharArray();
        StringBuilder sb = new StringBuilder();
        int left, right = str.length - 1;

        while (right >= 0) {
            while (right >= 0 && str[right] == ' ') right--;
            if (right < 0) break;

            left = right;
            while (left >= 0 && str[left] != ' ') left--;

            for (int i = left + 1; i <= right; i++) sb.append(str[i]);
            sb.append(' ');

            right = left - 1;
        }
        return sb.toString().trim();
    }
}
