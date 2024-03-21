import java.util.Arrays;

class Main {
    static void choise_sort(int Array[]) {
        int n = Array.length;

        for (int i = 0; i < n - 1; i++) {
            int min_idx = i;
            for (int j = i + 1; j < n; j++)
                if (Array[j] < Array[min_idx])
                    min_idx = j;

            int temp = Array[min_idx];
            Array[min_idx] = Array[i];
            Array[i] = temp;
        }
    }

    public static void main(String args[]) {
        int numArray[] = { 87, 25, 52, 67, 27, 18, 80, 82, 100 };
        System.out.println(Arrays.toString(numArray));
        choise_sort(numArray);
        System.out.println(Arrays.toString(numArray));
    }
}