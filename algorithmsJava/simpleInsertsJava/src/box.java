import java.util.Arrays;

public class box {
    public static void main(String[] args) throws Exception {
        int[] array = { 87, 25, 52, 67, 27, 18, 80, 82, 100 };
        System.out.println(Arrays.toString(array));
        for (int left = 0; left < array.length; left++) {

            int value = array[left];

            int i = left - 1;
            for (; i >= 0; i--) {
                if (value < array[i]) {
                    array[i + 1] = array[i];
                } else {
                    break;
                }
            }
            array[i + 1] = value;
        }
        System.out.println(Arrays.toString(array));
    }
}
