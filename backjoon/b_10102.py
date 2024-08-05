"""
두개의 문자의 수를 비교해서 많은 문자 출력, 같다면 tie 출력 
"""

N = int(input())
audition = input()


if audition.count("A") == audition.count("B"):
    print("Tie")
elif audition.count("A") > audition.count("B"):
    print("A")
else:
    print("B")
