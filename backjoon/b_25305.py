n, m = map(int, input().split())
members = list(map(int, input().split()))
members.sort(reverse=True)

print(members[m-1])