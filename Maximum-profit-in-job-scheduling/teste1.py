import bisect

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):

        empregos = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        empregos.sort(key=lambda x: x[1])

        fins_ordenados = [emp[1] for emp in empregos]
        dp = [0] * (len(empregos) + 1)

        for i in range(1, len(empregos) + 1):
            inicio, fim, lucro_atual = empregos[i - 1]

            j = bisect.bisect_right(fins_ordenados, inicio)

            lucro_incluindo = lucro_atual + dp[j + 1]
            lucro_nao_incluindo = dp[i - 1]

            dp[i] = max(lucro_incluindo, lucro_nao_incluindo)

        print("Debug - dp final:", dp)
        return dp[-1]

