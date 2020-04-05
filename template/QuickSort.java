import java.util.Arrays;
import java.util.Random;

public class QuickSort {
    public static void main(String [] args){
        int len = 1000;
        Random random = new Random();
        int [] arr = new int [len];
        for (int i = 0; i < len; i++) {
            arr[i] = random.nextInt();
        }
        int [] sorted = new int [len];
        System.arraycopy(arr, 0, sorted, 0, len);
        Arrays.sort(sorted);
        sort(arr, 0, len);
        boolean wrong = false;
        for (int i = 0; i < len; i++) {
            if (sorted[i] != arr[i]) {
                wrong = true;
                break;
            }
        }
        System.out.println(wrong);
    }

    public static void sort(int [] arr, int begin, int end) {
        if (begin + 1 >= end) return;
        int p = arr[begin];
        int i = begin, j = end - 1;
        while (i < j) {
            while (i < j && arr[j] >= p) j--;
            if (i < j) arr[i] = arr[j];
            while (i < j && arr[i] < p) i++;
            if (i < j) arr[j] = arr[i];
        }
        arr[i] = p;
        sort(arr, begin, i);
        sort(arr, i + 1, end);
    }
}