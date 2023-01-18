point_x1 = float(input())
point_y1 = float(input())
point_x2 = float(input())
point_y2 = float(input())
point_x = float(input())
point_y = float(input())

left_side = ((point_x == point_x1) and (point_y >= point_y1 and point_y <= point_y2))
right_side = ((point_x == point_x2) and (point_y >= point_y1 and point_y <= point_y2))
up_side = ((point_y == point_y1) and (point_x >= point_x1 and point_x <= point_x2))
down_side = ((point_y == point_y2) and (point_x >= point_x1 and point_x <= point_x2))

if left_side or right_side or up_side or down_side:
    print("Border")
else:
    print("Inside / Outside")