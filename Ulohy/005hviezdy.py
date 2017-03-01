n = int(input())
medzery = n - 1  
hviezdy = "*"

while (medzery >= 0):  # < n
    print(" " * medzery, end="")
    print(hviezdy)
    hviezdy += "**"
    medzery -= 1   
