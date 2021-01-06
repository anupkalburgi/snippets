from visualiser.visualiser import Visualiser as vs


@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def lcs_sum_memo(lst, prev, curr, acc_sum, dp):   
    if curr == len(lst):
        return acc_sum
    else:
        if dp[prev][curr] == -1:
            c1 = acc_sum
            if prev == -1 or lst[prev] < lst[curr]:
                c1 = lcs_sum_memo(lst, curr, curr+1, acc_sum+lst[curr], dp)
            c2 = lcs_sum_memo(lst, prev, curr+1, acc_sum, dp)
            dp[prev][curr] = max(c1, c2)
            return dp[prev][curr]
        else:
            return dp[prev][curr]




def main():
    # Call function
    dp = [[-1 for _ in range(5)] for _ in range(5)] 
    print(lcs_sum_memo([-4, 10, 3, 7, 15], -1, 0, 0, dp))
    # Save recursion tree to a file
    vs.make_animation("lis_sum.gif", delay=2)


if __name__ == "__main__":
    main()