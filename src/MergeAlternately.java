public class MergeAlternately {
    public static String mergeAlternating(String word1, String word2) {
        int length = word1.length() + word2.length();

        char[] finalWord = new char[length];
        int finalIndex = 0;

        int minLength = Math.min(word1.length(), word2.length());

        for (int i = 0; i < minLength; i++) {
            finalWord[finalIndex++] = word1.charAt(i);
            finalWord[finalIndex++] = word2.charAt(i);
        }

        if (word1.length() > word2.length()) {
            for (int i = minLength; i < word1.length(); i++) {
                finalWord[finalIndex++] = word1.charAt(i);
            }
        } else {
            for (int i = minLength; i < word2.length(); i++) {
                finalWord[finalIndex++] = word2.charAt(i);
            }
        }

        return new String(finalWord);
    }

}
