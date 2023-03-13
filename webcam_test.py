import cv2
  
  
# define a video capture object
vid = cv2.VideoCapture(0)

width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width, height)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()



# import pandas as pd
# import cv2


# url = "https://en.wikipedia.org/wiki/List_of_common_resolutions"
# table = pd.read_html(url)[0]
# table.columns = table.columns.droplevel()

# cap = cv2.VideoCapture(0)
# resolutions = {}

# for index, row in table[["W", "H"]].iterrows():
#     cap.set(3, row["W"])
#     cap.set(4, row["H"])
#     width = cap.get(3)
#     height = cap.get(4)
#     resolutions[str(width)+"x"+str(height)] = "OK"

# print(resolutions)