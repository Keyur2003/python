'''
20CE122 KEYUR SANGHANI
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.
Input Format: The first line contains. The second line contains an array A[]  of n integers each separated by a space.
Output Format: Print the runner-up score.
Sample Input
5
2 3 6 6 5
Sample Output
5
'''
if __name__ == '__main__':
    n = int(input())
    A = map(int, input().split())
    A = sorted(A,reverse=True)
    for i in range(len(A)):
        if A[i] == A[0]:
            continue
        else:
            print(A[i])  
            break