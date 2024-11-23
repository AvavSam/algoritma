# Quiz 1 PAA (Sorting)
Avav Abdillah Sam F55123020

## Merge Sort
- Worst-case (Big O): 𝑂(𝑛 log 𝑛)
- Best-case (Big Θ): Θ(𝑛 log⁡ 𝑛)
- Penjelasan: Merge Sort selalu membagi array menjadi dua bagian dan kemudian menggabungkannya kembali dalam urutan yang terurut. Proses pembagian memakan waktu logaritmik 𝑂(log 𝑛), dan penggabungan membutuhkan waktu linear 𝑂(𝑛). Jadi total kompleksitasnya adalah 𝑂(𝑛 log 𝑛) untuk kasus terbaik maupun terburuk.

## Psudocode Merge Sort
```
MERGE_SORT(array)
If length of array ≤ 1
    Return array
Split array into two halves
   Left = first half of array
   Right = second half of array
Call MERGE_SORT(Left)
Call MERGE_SORT(Right)
Merge Left and Right into sorted array
   Initialize empty result array
   While Left and Right are not empty
      If Left[0] < Right[0]
         Append Left[0] to result
         Remove Left[0] from Left
      Else
         Append Right[0] to result
         Remove Right[0] from Right
   Append remaining elements of Left or Right to result
Return sorted result
```

## Bubble Sort
- Worst-case (Big O): 𝑂(𝑛^2)
- Best-case (Big Θ): Θ(𝑛)
- Penjelasan: Bubble Sort membutuhkan waktu 𝑂(𝑛^2) dalam kasus terburuk karena harus melakukan perbandingan dan pertukaran elemen pada setiap pasangan elemen secara berulang. Dalam kasus terbaik, jika array sudah terurut, hanya dibutuhkan waktu linear Θ(𝑛).

## Psudocode Buble Sort
```
BUBBLE_SORT(array)
For i from 0 to length of array - 1
   For j from 0 to length of array - i - 1
      If array[j] > array[j + 1]
        Swap array[j] and array[j + 1]
Return sorted array
```
