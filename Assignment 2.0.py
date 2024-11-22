import java.util.Scanner;

public class AverageCalculator {

    public static void main(String[] args) {
        // Initialize variables
        int sum = 0;
        int count = 0;

        // Create a Scanner object for input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user for instructions
        System.out.println("Enter numbers one by one. Enter -1 to finish.");

        while (true) {
            System.out.print("Enter a number: ");
            String input = scanner.nextLine();

            try {
                int number = Integer.parseInt(input);

                if (number == -1) {
                    // Exit condition
                    break;
                }

                // Update sum and count
                sum += number;
                count++;
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid number.");
            }
        }

        // Calculate and display the average
        if (count == 0) {
            System.out.println("No numbers entered. Cannot compute average.");
        } else {
            double average = (double) sum / count;
            System.out.printf("The average is: %.2f\n", average);
        }

        scanner.close();
    }
}
