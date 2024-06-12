import numpy as np
import cv2
import config

def calculate_distance(point, line):
    x, y = point
    A, B, C = line
    distance = abs(A * x + B * y + C) / np.sqrt(A**2 + B**2)
    return distance

def fit_line(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    A = y2 - y1
    B = x1 - x2
    C = -A * x1 - B * y1
    return A, B, C

def ransac(image,num_iterations, threshold_distance, start_point = None):
    height, width = image.shape
    best_line = None
    best_distance = float('inf')

    #
    while_points = []
    for y in range(height):
        for x in range(width):
            if image[y, x] == 255:  # Assuming white is represented by 255
                point = (x, y)
                while_points.append(point)
    #

    for _ in range(num_iterations):
        # Randomly select two white points
        if start_point is None:
            point1 = (np.random.randint(width), height - 1)
        else:
            point1 = start_point
        point2 = (np.random.randint(width), np.random.randint(height))

        # Fit a line to the selected points
        line = fit_line([point1, point2])

        # Calculate total distance from white points to the line
        total_distance = 0

        for point in while_points:
            distance = calculate_distance(point, line)
            total_distance += distance
    
        # Check if the current line is better than the previous best
        if total_distance < best_distance:
            best_line = line
            best_distance = total_distance

    return best_line, best_distance

# def get_two_points_on_line(line):
#     A, B, C = line
#     x1 = 0  # Assume x = 0
#     y1 = -C / B
#     x2 = 100  # Assume x = 100 (or any other value)
#     y2 = (-C - A * x2) / B
#     return (x1, y1), (x2, y2)

def get_decision(img_pred):
    img_pred = cv2.cvtColor(img_pred, cv2.COLOR_BGR2GRAY)

    num_iterations = 30  # Number of RANSAC iterations
    threshold_distance = 2.0  # Distance threshold to consider a point as an inlier
    
    best_line, best_distance = ransac(img_pred, num_iterations, threshold_distance)

    print("Best line:", best_line)
    print("Best distance:", best_distance)

    # Draw the line on the image
    color_image = cv2.cvtColor(img_pred, cv2.COLOR_GRAY2BGR)
    point1 = (0, int((-best_line[2]) / (best_line[1] + 0.01)))
    point2 = (img_pred.shape[1] - 1, int((-best_line[0] * (img_pred.shape[1] - 1) - best_line[2]) / (best_line[1] + 0.01)))
    cv2.line(color_image, point1, point2, (0, 0, 255), 2)

    delta_x = point2[0] - point1[0]
    delta_y = point2[1] - point1[1]
    angle_radians = np.arctan2(delta_y, delta_x)
    angle_degrees = np.degrees(angle_radians)
    if angle_degrees < 0:
        angle_degrees += 180
    print(angle_degrees)

    cv2.imwrite(config.save_path + '1_pred_angle.jpg', color_image)

    return angle_degrees

def get_face_decision(img_pred):
    img_pred = cv2.cvtColor(img_pred, cv2.COLOR_BGR2GRAY)

    num_iterations = 30  # Number of RANSAC iterations
    threshold_distance = 2.0  # Distance threshold to consider a point as an inlier
    
    height, width = img_pred.shape
    start_point = ((width - 1) // 2, height - 1)
    best_line, best_distance = ransac(img_pred, num_iterations, threshold_distance, start_point)

    print("Best line:", best_line)
    print("Best distance:", best_distance)

    # Draw the line on the image
    color_image = cv2.cvtColor(img_pred, cv2.COLOR_GRAY2BGR)
    point1 = (0, int((-best_line[2]) / (best_line[1] + 0.01)))
    point2 = (img_pred.shape[1] - 1, int((-best_line[0] * (img_pred.shape[1] - 1) - best_line[2]) / (best_line[1] + 0.01)))
    cv2.line(color_image, point1, point2, (0, 0, 255), 2)

    delta_x = point2[0] - point1[0]
    delta_y = point2[1] - point1[1]
    angle_radians = np.arctan2(delta_y, delta_x)
    angle_degrees = np.degrees(angle_radians)
    if angle_degrees < 0:
        angle_degrees += 180
    print(angle_degrees)

    cv2.imwrite(config.save_path + '1_pred_angle.jpg', color_image)

    return angle_degrees



def detect_lane_direction(img):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
    contours,hier = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        cnt = contours[0]
    else:
        return None

    # then apply fitline() function
    [vx,vy,x,y] = cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((gray.shape[1]-x)*vy/vx)+y)

    #Finally draw the line

    angle = np.arctan2(vy, vx) * 180 / np.pi

    angle_value = angle[0]
    if angle_value < 0:
        angle_value += 180

    print(angle_value)
    
    cv2.line(img,(gray.shape[1]-1,righty),(0,lefty),255,2)
    cv2.imwrite(config.save_path + '1_pre_angle.jpg', img)

    return angle_value