這裡我的解法是用 hashmap(python Dict) 紀錄兩個 string 在 s1 這個 window 下的 hashmap 是不是長一樣。
1. 我先使用 defaultdict 來初始化兩個 dict，因為這會可以讓還沒出現過的 key 有 int 初始值（0）
2. 之後就先塞好 s1Dict 和 s2 從 index = 0 len(s1) 算出來的 s2Dict
3. 再來就是 loop over s2，並且我們會遍歷到 index == len(s2) -len(s1)，每次就會把上一個 index char 減一（等於零的時候移除）並且把下一個新加進來的 char 加一

-----
做完之後看網路上的解答，他還用了 matches 來做，可以做到 O(n)，我這個做法應該只是 O(26n)，因為每次的兩個 Dict compare 都需要便利整個 Dict，最糟的情況是 Dict 有 26 個字母需要比較，這樣就會是 26*n 了。
我看他是用 array 做 init 蠻酷的，因為是英文字母全小寫，所以長度只需要 26，拿 ord(char) - ord('a') 就可以表示英文字母。
如果這裡是可能出現大小寫就會是兩倍的長度（但感覺沒那麼好 init 因為大小寫英文字母的 ascii 是不連續的）

他的 matches flag 就是在 init 好兩個 array 之後先便利兩個 array 的每個 index 看看有幾個值是相同的，最多就是 26 個，然後之後再做上述的第三步驟時我們會有兩個步驟，每做一個步驟就更新 matches 的值，這樣就不是做便利兩個 dictionary 做比較
進而做到 O(N)。
