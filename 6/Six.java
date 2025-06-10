import java.util.*;

public class Six {
    public static void main(String[] args) {
        int sumOfSquares = 0;
        int squareOfSum = 0;
        int max = 100;
        for (int i = 1; i <= max; i++) {
            sumOfSquares += i * i;
            squareOfSum += i;
        }
        squareOfSum *= squareOfSum;
        System.out.println(squareOfSum - sumOfSquares);        

    }
}