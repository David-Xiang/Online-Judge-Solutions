package java;
import java.util.Arrays;
import java.util.Random;

public class MergeSort {
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
        sort(arr, new int[len], 0, len);
        boolean wrong = false;
        for (int i = 0; i < len; i++) {
            if (sorted[i] != arr[i]) {
                wrong = true;
                break;
            }
        }
        System.out.println(wrong);
    }

    public static void sort(int [] arr, int [] tmp, int begin, int end) {
        if (begin + 1 >= end) {
            return;
        }
        final int mid = (begin + end) / 2;
        sort(arr, tmp, begin, mid);
        sort(arr, tmp, mid, end);
        System.arraycopy(arr, begin, tmp, begin, end - begin);
        int i = begin, j = mid;
        int p = begin;
        while (i < mid && j < end) {
            while (i < mid && tmp[i] <= tmp[j]) arr[p++] = tmp[i++];
            if (i >= mid) break;
            while (j < end && tmp[i] > tmp[j]) arr[p++] = tmp[j++];
        }
        while (i < mid) arr[p++] = tmp[i++];
        while (j < end) arr[p++] = tmp[j++];
    }
}