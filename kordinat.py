import cv2
  
# function to display the coordinates of
# of the points clicked on the image
def gambar(gambr):
    def cordinate(event, x, y, flags, params):
    
        # checking for left mouse clicks
        if event == cv2.EVENT_LBUTTONDOWN:
    
            # displaying the coordinates
            # on the Shell
            print(x, ' ', y)
    
            # displaying the coordinates
            # on the image window
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(x) + ',' +
                        str(y), (x,y), font,
                        1, (255, 0, 0), 2)
            cv2.imshow(gambr, img)
    
        # checking for right mouse clicks    
        if event==cv2.EVENT_RBUTTONDOWN:
    
            # displaying the coordinates
            # on the Shell
            print(x, ' ', y)
    
            # displaying the coordinates
            # on the image window
            font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
            b = img[y, x, 0]
            g = img[y, x, 1]
            r = img[y, x, 2]
            cv2.putText(img, str(b) + ',' +
                        str(g) + ',' + str(r),
                        (x,y), font, 1,
                        (255, 255, 0), 2)
            cv2.imshow(gambr, img)
    
    
    
        # reading the image
    img = cv2.imread(gambr, 1)
    
        # displaying the image
    cv2.imshow(gambr, img)
    
        # setting mouse handler for the image
        # and calling the click_event() function
    cv2.setMouseCallback(gambr, cordinate)
    
        # wait for a key to be pressed to exit
    cv2.waitKey(0)
    
        # close the window
    cv2.destroyAllWindows()
