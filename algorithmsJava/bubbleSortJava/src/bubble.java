import java.util.Arrays;

class sorting {

    public static void bubble(int[] sort_arr, int x) {

        for (int i = 0; i < x - 1; ++i) {
            for (int j = 0; j < x - i - 1; ++j) {
                if (sort_arr[j + 1] < sort_arr[j]) {
                    int swap = sort_arr[j];
                    sort_arr[j] = sort_arr[j + 1];
                    sort_arr[j + 1] = swap;
                }
            }
        }
    }

    public static void main(String args[]) {
        int[] array = { 87, 25, 52, 67, 27, 18, 80, 82, 100 };
        System.out.println(Arrays.toString(array));
        int x = array.length;
        bubble(array, x);
        for (int i = 0; i < x; ++i) {
        }
        System.out.println(Arrays.toString(array));
    }
}