
#     0 1 2 3
# 0   a * * *
# 1   * n * *
# 2   * * k *
# 3   * * * i

# [index no of rows][index no of cols]
# a --> [0][0]
# n --> [1][1]
# k --> [2][2]
# i --> [3][3]


name = input("Enter your name : ")
# name = "anki"

iteration = len(name)

for i in range(0,iteration):
    for j in range(0,iteration):
      
      if(i==j):
        print(name[j],sep=" ",end=" ")
      else:
        print("*",sep=" ",end=" ")
    print()



