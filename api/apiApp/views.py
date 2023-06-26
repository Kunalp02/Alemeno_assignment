from rest_framework.decorators import api_view
from rest_framework.response import Response
import cv2
import numpy as np
from collections import OrderedDict
import json


@api_view(['POST'])
def upload_file(request):
    image = request.FILES.get('image')
    if image:
        # Read the image using OpenCV
        img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
        
        # Perform color analysis on the image
        colors = analyze_colors(img)

        # Define the color names in the specific order
        color_names = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']

        # Create an empty dictionary for color data
        color_data = OrderedDict()

        # Populate the color data dictionary with color names and RGB values
        for index, name in enumerate(color_names):
            color_data[name] = colors[index]

        print(color_data);

        # Prepare the response data
        response_data = {
            'success': 'File uploaded successfully.',
            'body': color_data
        }

        json_data = json.dumps(response_data, sort_keys=False)
        return Response(json_data, status=200)
    else:
        return Response({'error': 'No file provided.'}, status=400)




# def analyze_colors(image):
#     # Convert the image to the appropriate color space if needed
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # Preprocess the image - denoising and contrast enhancement
#     denoised = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

#     # Apply histogram equalization to each channel
#     equalized = cv2.split(denoised)
#     equalized = [cv2.equalizeHist(channel) for channel in equalized]
#     enhanced = cv2.merge(equalized)

#     # Define the regions of interest for each color on the strip
#     color_regions = [
#         (0, 0, 10, 100),    # Region for Color 1
#         (10, 0, 20, 100),   # Region for Color 2
#         (20, 0, 30, 100),   # Region for Color 3
#         (30, 0, 40, 100),   # Region for Color 4
#         (40, 0, 50, 100),   # Region for Color 5
#         (50, 0, 60, 100),   # Region for Color 6
#         (60, 0, 70, 100),   # Region for Color 7
#         (70, 0, 80, 100),   # Region for Color 8
#         (80, 0, 90, 100),   # Region for Color 9
#         (90, 0, 100, 100)   # Region for Color 10
#     ]

#     colors = []

#     for region in color_regions:
#         x, y, w, h = region
#         color_region = enhanced[y:y+h, x:x+w]

#         # Convert the color region to HSV color space
#         hsv = cv2.cvtColor(color_region, cv2.COLOR_RGB2HSV)

#         # Thresholding logic using HSV color space
#         lower_threshold = np.array([0, 0, 0])  # Define the lower threshold for color segmentation
#         upper_threshold = np.array([255, 255, 255])  # Define the upper threshold for color segmentation
#         mask = cv2.inRange(hsv, lower_threshold, upper_threshold)

#         # Apply morphological closing to refine the color region
#         kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
#         closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#         # Find contours of the closed region
#         contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         # Find the largest contour (assuming it represents the color region)
#         if len(contours) > 0:
#             largest_contour = max(contours, key=cv2.contourArea)
#             x, y, w, h = cv2.boundingRect(largest_contour)
#             color_region = color_region[y:y+h, x:x+w]

#         # Compute the mean color of the thresholded region
#         mean_color = np.mean(color_region, axis=(0, 1))

#         # Convert the mean color to integer RGB values
#         rgb = [int(channel) for channel in mean_color]

#         # Append the RGB values to the colors list
#         colors.append(rgb)

#     return colors






def analyze_colors(image):
    # Convert the image to the appropriate color space if needed
    # For example, if the image is in BGR format, convert it to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the regions of interest for each color on the strip
    color_regions = [
        (0, 0, 10, 100),    # Region for Color 1
        (10, 0, 20, 100),   # Region for Color 2
        (20, 0, 30, 100),   # Region for Color 3
        (30, 0, 40, 100),   # Region for Color 4
        (40, 0, 50, 100),   # Region for Color 5
        (50, 0, 60, 100),   # Region for Color 6
        (60, 0, 70, 100),   # Region for Color 7
        (70, 0, 80, 100),   # Region for Color 8
        (80, 0, 90, 100),   # Region for Color 9
        (90, 0, 100, 100)   # Region for Color 10
    ]

    colors = []

    for region in color_regions:
        x, y, w, h = region
        color_region = image[y:y+h, x:x+w]

        # Compute the mean color of the color region
        mean_color = np.mean(color_region, axis=(0, 1))

        # Convert the mean color to integer RGB values
        rgb = [int(channel) for channel in mean_color]

        # Append the RGB values to the colors list
        colors.append(rgb)


    return colors



