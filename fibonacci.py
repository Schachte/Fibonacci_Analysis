'''
Fibonacci Practice
@Author: Ryan Schachte
@Description: Analyzing Methods of Computing the N-th Term in Fib. Sequence.
'''

import time

def dynApprTimeSpace(seqNum):
    '''O(N) Method, fast and takes minimal space'''
    seqNum = int(seqNum)
    a = 1
    b = 1
    for x in range(2, seqNum):
        c = a + b
        a = b
        b = c
    return b
    
def dynApprTime(seqNum):
    '''O(N) Method, fast, but takes up a lot of space'''
    seqNum = int(seqNum)
    fibArr = [0] * seqNum
    fibArr[0] = 1
    fibArr[1] = 1

    for fib in range(2, len(fibArr)):
        fibArr[fib] = fibArr[fib-1] + fibArr[fib-2]
    
    return fibArr[seqNum-1]

def fibAppr(seqNum):
    '''Very slow method, takes a lot of space and time'''
    seqNum = int(seqNum)
    if (seqNum == 0):
        return 0
    elif (seqNum == 1):
        return 1
    else:
        return fibAppr(seqNum - 1) + fibAppr(seqNum - 2)

def approach(type):
    
    sequence=raw_input('Enter Sequence Number: ')
    if (type == 'a'):
        current = time.time()
        print(fibAppr(str(sequence)))
        end = time.time()
        print("This took %.10f seconds to complete" %(end - current))
    elif (type == 'b'):
        current = time.time()
        print(dynApprTime(str(sequence)))
        end = time.time()
        print("This took %.10f seconds to complete" %(end - current))
    elif (type == 'c'):
        current = time.time()
        print(dynApprTimeSpace(str(sequence)))
        end = time.time()
        print("This took %.10f seconds to complete" %(end - current))
        
def main(): 
    
    choice = 'a'
    
    while (choice == 'a' or choice == 'b' or choice == 'c'):
        print('''
                A) Recursive Approach
                B) Dynamic Programming Approach (Improving Time Complexity)
                C) Dynamic Programming Approach (Improving Time & Space Complexity)
        ''')
        
        choice = raw_input("Which Fibonacci Method Would You Like To Analyze? ")
        choice = choice.lower()
        
        if (choice == 'a'):
            approach(choice)
        elif (choice == 'b'):
            approach(choice)
        elif (choice == 'c'):
            approach(choice)
        else:
            print('invalid')
    
main()
