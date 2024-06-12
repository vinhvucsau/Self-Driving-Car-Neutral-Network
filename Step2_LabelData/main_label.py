import cv2
import numpy as np
import matplotlib.pyplot as plt

# Biến toàn cục để lưu trữ các điểm đã được vẽ


def label_lanes(filename, filename_new):
    img_height = 128
    img_width = 256
    scale_size = 2

    points = []
    points2 = []
    is_line_1 = True

    # Hàm callback được gọi khi chuột được nhấp vào ảnh
    def mouse_callback(event, x, y, flags, param):
        # global points
        # global points2
        # global is_line_1

        if event == cv2.EVENT_LBUTTONDOWN:
            # Lưu tọa độ của điểm được vẽ
            #chỉnh
            if is_line_1:
                points.append((x, y))
            else:
                points2.append((x, y))

    # Tạo cửa sổ và gắn hàm callback chuột
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', mouse_callback)

    # Đọc ảnh gốc
    image = cv2.imread(filename)

    image = cv2.resize(image, (img_width*scale_size, img_height*scale_size))

    # Tạo một bản sao của ảnh để vẽ lên
    drawing_image = image.copy()

    while True:
        # Hiển thị ảnh và đường đã vẽ
        cv2.imshow('Image', drawing_image)
        
        # Chờ phím bấm
        key = cv2.waitKey(1) & 0xFF

        if key == ord('1'):
            is_line_1 = True
        
        if key == ord('2'):
            is_line_1 = False
        
        # Thoát khỏi vòng lặp nếu nhấn phím 'q'
        if key == 27:
            # Tạo một ma trận trắng có kích thước bằng ảnh gốc
            mask = np.zeros(image.shape[:2], dtype=np.uint8)
            
            # Vẽ các đường trắng trên ma trận trắng
            for i in range(len(points) - 1):
                cv2.line(mask, points[i], points[i+1], 255, thickness=2)

            for i in range(len(points2) - 1):
                cv2.line(mask, points2[i], points2[i+1], 255, thickness=2)

            # Tạo một ảnh trắng
            white_image = np.ones_like(image) * 255
            
            # Áp dụng mask vào ảnh trắng
            result = cv2.bitwise_and(white_image, white_image, mask=mask)
            
            # Áp dụng ảnh kết quả vào ảnh gốc

            black_image = np.zeros_like(image)

            final_result = cv2.bitwise_or(black_image, result)

            final_result = cv2.resize(final_result, (img_width, img_height))
            
            # Hiển thị ảnh kết quả
            cv2.imshow('Result Image', final_result)
            
            # Lưu ảnh kết quả
            cv2.imwrite(filename_new, final_result)
            
            break
        
        if key == ord('x'):
            points = []
            points2 = []
            
        # Lưu ảnh nếu nhấn phím 's'
        if key == ord('s'):
            # Tạo một ma trận trắng có kích thước bằng ảnh gốc
            mask = np.zeros(image.shape[:2], dtype=np.uint8)
            
            # Vẽ các đường trắng trên ma trận trắng
            for i in range(len(points) - 1):
                cv2.line(mask, points[i], points[i+1], 255, thickness=2)

            for i in range(len(points2) - 1):
                cv2.line(mask, points2[i], points2[i+1], 255, thickness=2)

            # Tạo một ảnh trắng
            white_image = np.ones_like(image) * 255
            
            # Áp dụng mask vào ảnh trắng
            result = cv2.bitwise_and(white_image, white_image, mask=mask)
            
            # Áp dụng ảnh kết quả vào ảnh gốc

            black_image = np.zeros_like(image)

            final_result = cv2.bitwise_or(black_image, result)

            final_result = cv2.resize(final_result, (img_width, img_height))
            
            # Hiển thị ảnh kết quả
            cv2.imshow('Result Image', final_result)
            
            # Lưu ảnh kết quả
            cv2.imwrite(filename_new, final_result)
        

        # Cập nhật ảnh vẽ
        drawing_image = image.copy()
        
        # Vẽ các đường đã lưu
        for i in range(len(points) - 1):
            cv2.line(drawing_image, points[i], points[i+1], (255, 255, 255), thickness=2)

        for i in range(len(points2) - 1):
            cv2.line(drawing_image, points2[i], points2[i+1], (255, 255, 255), thickness=2)

        
    # Giải phóng cửa sổ và kết thúc chương trình
    cv2.destroyAllWindows()