import sys
input=sys.stdin.readline
n=int(input())
arr=list(map((int,input().split())))
m=int(input())
xarr=list(map(int,input().split()))
arr.sort()
for a in xarr: