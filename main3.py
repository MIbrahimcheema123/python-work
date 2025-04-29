 # height of trees
tree1 = 90
tree2 = 85
tree3 = 100
tree4 = 50
tree5 = 27
sum = tree1+tree2+tree3+tree4+tree5
print("the sum of all tree height is",sum)
# finding average of trees height
average =sum/5
print("average height of trees is",average)

amount=int(input("enter the amount you want to withdraw"))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10

print("notes of 100",note_1)
print("notes of 50",note_2)
print("notes of 10",note_3)