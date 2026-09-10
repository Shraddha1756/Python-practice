''' write the program to detect wheter the comment is a spanm or not. A comment should be treated  as a spam
if it contain any of these paswrd "make a lot of money",now susrcibe this or click this
'''
#solution:

comment = input("Enter your comment: ")

if "make a lot of money" in comment or "now subscribe this" in comment or "click this" in comment:
    print("This comment is spam")
else:
    print("This comment is not spam")
