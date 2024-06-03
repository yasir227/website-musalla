def countingBits(n):
    ans = [0] * (n+1)
    for i in range (1, n+1):
        ans[i] = ans[i//2] + (i % 2)
    return ans
#n = 15
print(countingBits(n))


############## Reverse String #############

txt = "I am Yasir"[::-1]
print(txt)


