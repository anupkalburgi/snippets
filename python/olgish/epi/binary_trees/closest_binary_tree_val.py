# there are three possible situation here
# 1. left < root < right - then root is the answer as going doing either direction is going to increase the diff
# 2. target < root.val go left
# 3. target > right.val go right
# here we cannot use zero as  the base condition as we will have to check of both left and right are none and return accordingly