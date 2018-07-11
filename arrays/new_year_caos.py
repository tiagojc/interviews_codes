# Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up,
# and each person wears a sticker indicating their initial position in the queue. Initial positions increment by from
# at the front of the line to  at the back.
# Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap
# positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two
# others. For example, if and  bribes , the queue will look like this: .
# Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the
# queue into its current state!
#
# Function Description
# Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of
# bribes necessary, or Too chaotic if the line configuration is not possible.
# minimumBribes has the following parameter(s):
# q: an array of integers
#
# Input Format
# The first line contains an integer , the number of test cases.
# Each of the next  pairs of lines are as follows:
# - The first line contains an integer , the number of people in the queue
# - The second line has  space-separated integers describing the final state of the queue.
#
# Output Format
# Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print Too
# chaotic if the state is invalid, i.e. it requires a person to have bribed more than  people.


# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases = int(input())

queues_processed = 0
people = list()
queues = list()
while queues_processed < test_cases:
    tmp = int(input())
    people.append(tmp)
    tmp = input().split()
    queues.append(tmp)
    queues_processed += 1

for idx, person in enumerate(people):
    start_q = queues[idx]
    start_q = list(map(int, start_q))
    final_q = list()
    chaotic = False
    for i in range(1, person + 1):
        final_q.append(i)
    total_bribes = 0
    cont = 0
    total_bribes = 0
    while cont < 2:
        for i in range(person - 1, 0, -1):
            if start_q[i] < start_q[i - 1]:
                start_q[i], start_q[i - 1] = start_q[i - 1], start_q[i]
                total_bribes += 1
        cont += 1

    if start_q == final_q:
        print(total_bribes)
    else:
        print("Too chaotic")