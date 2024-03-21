class hoare {
    static int leftright(int[] arr, int low, int high) {
        int pivot = arr[low];
        int i = low - 1, j = high + 1;

        while (true) {
            do {
                i++;
            } while (arr[i] < pivot);
            do {
                j--;
            } while (arr[j] > pivot);
            if (i >= j)
                return j;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    static void Sort(int[] arr, int low, int high) {
        if (low < high) {

            int p = leftright(arr, low, high);

            Sort(arr, low, p);
            Sort(arr, p + 1, high);
        }
    }

    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    static public void main(String[] args) {
        int[] arr = { 63, 9, 65, 21, 8, 34, 9, 8, 30, 36 };
        printArray(arr);
        int n = arr.length;
        Sort(arr, 0, n - 1);
        printArray(arr);
    }
}