

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():

    valid_shape=["square","triangle","pyramid","heart","rectangle","inverted triangle"]

    while True :
        select_shape =input('Shape?: ').lower()
        if select_shape == "":continue
        if select_shape not in  valid_shape: 
            return None

        else:
            return select_shape
    


# TODO: Step 1 - get height (it must be int!)
def get_height():

        while True :
            try:
                height = int(input('Height?: '))
            except ValueError:
                continue
            if height > 80:
                continue
            if height < 0:
                continue
            else:
                break
            

        return height

        


# TODO: Step 2
def draw_pyramid(height, outline):

    #displays solid pyramid
    if outline == False:
        for rows in range(height):
            for space in range(height-rows -1):
                print(" ", end="")
            for columns in range(2*rows+1):
                print("*", end="")
            print()

    #diplays outline of pyramid        
    else:
        for rows in range(height):
            for space in range(height-rows -1):
                print(" ", end="")
            for columns in range(2*rows+1):
                if rows == 0 or rows ==height-1 or columns== 0 or columns == 2*rows:
                    print("*", end="")
                else:
                    print(" ",end=(""))
            print()


# TODO: Step 3
def draw_square(height, outline):

    #displays solid shape of square
    if outline == False:
        for rows in range (height):
            for columns in range (height):
                print("*",end=(""))
            print()

    #displays outline of square        
    else:
        for rows in range (height):
            for columns in range (height):
                if rows== 0 or columns==0 or rows==height-1 or columns==height-1:
                    print("*",end=(""))
                else:
                    print(" ",end=(""))
            print()


# TODO: Step 4
def draw_triangle(height, outline):

    #displays solid shape of triangle
    if outline == False:
        for rows in range(height):
            for space in range(height-rows -1):
                print("", end="")
            for columns in range(rows+1):
                print("*", end="")
            print()

    #displays outline of triangle
    else:
        for rows in range(height):
            for space in range(height-rows -1):
                print("", end="")
            for columns in range(rows+1):
                if columns== 0 or columns==rows or columns == height-1 or rows== height-1:
                    print("*", end="")

                else:
                    print(" ",end=(""))
            print()
 
 #additional shape 1
def draw_heart(height, outline):

    #display solid shape heart
    half_height = height//2
    if outline == False:
        for i in range(1,half_height):
            for j in range(half_height-i-1):
                print(" ",end="")
            for j in range(i + 1):
                print("* ",end=(""))
            for j in range (2*(half_height-i-1)):
                print(" ",end=(""))
            for j in range(i+1):
                print("* ",end=(""))

            print()

        for i in range(height,0,-1):
            for j in range(height-i):
                print(" ",end=(""))
            for j in range(i,0,-1):
                print("* ",end=(""))
            print()
#display the outline of a heart
    else:
        for row in range(height):
            for colin in range (height+1):
                if (row == 0 and colin %3 != 0 ) or (row == 1 and colin % 3 == 0 ) or (row - colin == 2) or (row + colin == 8):
                    print("*",end=(" "))

                else:
                    print(" ",end=(" "))

            print()

#additional shape 2
def draw_rectangle(height, outline):

    #display the solid shape of a rectangle
    half_height = height//2
    if outline == False:
        for row in range(half_height):
            for col in range(height):
                print("*",end=(" "))

            print()

#display the outline of a rectangle
    else:
        for row in range(half_height):
            for col in range(height):
                if row== 0 or col ==0 or row==3-1 or col==6-1:
                    print("*",end=(" "))

                else:
                    print(" ",end=(" "))
            print()


#additional shape 3
def draw_inverted_triangle(height, outline):

    #display solid shape of inverted right angle triangle
    if outline == False:
        for row in range(height):
            for col in range(height-row):
                print("*",end=(" "))
            print()

#display outline of a inverted right angle triangle
    else:
        for i in range(height, 0, -1):
            for j in range(i, 0, -1):
                if i == 1 or i == height or j == 1 or j == i:
                    print('*', end = ' ')
                else:
                    print(' ', end = ' ')
            print()




# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):

    #determines what shape to print based of user input
    if shape == "pyramid":
        draw_pyramid(height, outline)
    
    elif shape == "square":
        draw_square(height,outline)

    elif shape == "heart":
        draw_heart(height,outline)

    elif shape == "rectangle":
        draw_rectangle(height,outline)

    elif shape == "inverted triangle":
        draw_inverted_triangle(height,outline)

    else:
        draw_triangle(height,outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    the_outline=input('Outline only? (y/N):')

    if the_outline =="" or the_outline == "n".lower():
        return False
    else:
        return True


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

