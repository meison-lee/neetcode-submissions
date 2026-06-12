就是用兩個 binary searc 下去解，就是先照著 matrix[i][0] 的值去判斷，
這裡要注意到的是第一次的 binary search 並不是用來確認是否存在的（除非剛好有撞到 target）是用來判斷範圍的，我們想要從第一次的 search 找到應該在哪一個 row 才能進行第二次 binary search 找資料。

所以第一次 search 完之後還要再做一些條件判斷，不然會出現該 target 其實應該在前一個 row 的情形，最後找到是哪一個 row 的範圍之後就再做一個 search 就可以“判斷”是否存在了。
