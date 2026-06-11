Given an arrayof string consisting uppercase english char and a intger k. Integer k is the time we are allowed to replace the char. Calculate the max length of the repeating string after the replacement.

1. 因為英文字母最多只有 26 個，所以我們可以先拿到這個 string 有哪些英文字母再一一去掃，26 是一個可接受的數字不會是 n^2 而是 26(n)。
2. 因為需要關注最長連續重複字母的字串，我們需要知道左邊要從何開始，才能計算，所以使用 sliding window 維護 leftPtr。
3. leftPtr 需要在 replacement 用盡的時候開始往右調整，目標就是調整到目前 window 內第一個 different Char 的下一個 index，這樣 replacement 的扣打就可以加一，rightPtr 也可以繼續走。
4. 在這層邏輯之外就是用 for loop 遍歷我們的 charSet，把每個有出現的 char 都走一遍，最後就會得到 maxLength。

for loop charSet -> c
  for loop s -> rightPtr
    if s[rightPtr] != c:
      k --
    while k < 0 and left <= i:
      if s[left] != c:
        k++
      left++
    maxLength = max(maxLength, i - left + 1)
return maxLength
