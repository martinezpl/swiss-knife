import cv2

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    
    # FOR RECORDING
    #width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    #height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    #size = (width, height)
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('video.avi', fourcc, 20.0, size)
    
    cv2.namedWindow("preview")
    #cv2.moveWindow("preview", 2000, 100)
    

    if cap.isOpened():  # try to get the first frame
        rval, frame = cap.read()
    else:
        rval = False
    
    while rval:
        frame_f = frame
        cv2.imshow("preview", frame_f)
        rval, frame = cap.read()
        #out.write(frame_f)
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break

    cap.release()
    #out.release()
    cv2.destroyWindow("preview")
