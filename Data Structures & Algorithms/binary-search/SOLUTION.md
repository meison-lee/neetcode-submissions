因為已經排好序，所以可以直接用 O(nlogn) binary search。
這裡比較麻煩的是怎麼決定 left, right 相關條件來確保不會 out of index 或是有漏掉的情境。

我們定義的 left, right index 本身都會是有效還沒有比較的值，因此如果最後收斂到 left == right，應該還會再繼續比較下去。
所以 while loop 的條件就是 left < right。
至於 middle 比較完之後我們都是 middle +- 1，因為 middle 本身已經 invalid 了，所以沒有必要重複用它，這樣也確保新生成的 left, right 都是有效還沒有比較的值。
