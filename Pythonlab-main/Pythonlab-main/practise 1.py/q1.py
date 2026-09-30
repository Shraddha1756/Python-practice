''' Write  a pp to input to student marks in m cosecutive test and store them in a list.find the longest
 cosecutive seq in which each mark is strictly graetor than the previous mark.

 display the seq ,its list , and uts starting and ending test numbers are as tuples. if multiple seq 
 have the same max length,display and the first one

 marks: [55,60,68,70,78,74]
 longest improving  seq;[62,65,70,78]
 numbersof item: 4
 test range;(4,7)

 condition: 
 accept at leat one text
 equal marks bareak the improving seq
 test number begin at 1
 donot sort the list bec the original test order matters.

'''

#solution:

n = int(input("Enter no. of test:"))
marks = []
for i in range(n):
    marks.append(int(input("enter marks:")))
    start = 0
    best_length = i

    length = i - start + 1
    if length > best_length:
        best_start = start
        best_length = length

        sequence = marks[best_start:best_start+ best_length]
        test_range = (best_start + 1, best_start + best_length)

        print("Longest improving sequence:", sequence)
        print("test range:" , test_range )
