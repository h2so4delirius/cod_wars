def count_change(N, S):
	T = [0] * (N + 1)
	T[0] = 1

	for i in range(len(S)):
		j = S[i]
		while j <= N:
			T[j] += T[j - S[i]]
			j = j + 1

	return T[N]



print(count_change(4, [1,2]),"==",3)
print(count_change(10, [5,2,3]),"==",4)
#test.assert_equals(0, count_change(11, [5,7]))
## https://www.techiedelight.com/coin-change-problem-find-total-number-ways-get-denomination-coins/
## :)))))))))))))))))))))))))))))))))))))))))))))))