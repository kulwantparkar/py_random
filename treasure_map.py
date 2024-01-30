line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
position_list = []
for char in position:
    position_list.append(char)

num1 = 0
if position_list[0] == "A":
    num1 = 0
elif position_list[0] == "B":
    num1 = 1
elif position_list[0] == "C":
    num1 = 2

num2 = int(position_list[1]) - 1

map[num1][num2] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")