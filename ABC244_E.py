from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="244"
#問題
problem="e"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  mod=998244353
  N,M,K,S,T,X=map(int,input().split())
  G=[[] for _ in range(N)]
  for i in range(M):
    U,V=map(int,input().split())
    U-=1; V-=1
    G[U].append(V)
    G[V].append(U)
  dp=[[[0]*2 for j in range(N)] for _ in range(K+1)]
  dp[0][S-1][0]=1
  for i in range(K):
    for j in range(N):
      for k in range(2):
        for v in G[j]:
          if v==X-1: dp[i+1][v][k^1]=(dp[i+1][v][k^1]+dp[i][j][k])%mod
          else: dp[i+1][v][k]=(dp[i+1][v][k]+dp[i][j][k])%mod
  print(dp[-1][T-1][0])
  """ここから上にコードを記述"""

  print(test_case[__+1])