
import java.util.Arrays;

public class Bubblesort {
    public static void main(String[] args) {
        int[] numbers = {7, 2, 9, 4, 1, 12, 14, 8, 3, 18};
        
        System.out.println("Before sorting:");

        System.out.println (Arrays.toString(numbers));

        for (int end = numbers.length - 1; end > 0; end--) {
            for (int i = 0; i < end; i++) {
                if (numbers[i] > numbers[i + 1]) {
                    int temp = numbers[i];
                    numbers[i] = numbers[i + 1];
                    numbers[i + 1] = temp;
                }
            }
        }
        System.out.println("After sorting:");

        System.out.println (Arrays.toString(numbers));
    }
}