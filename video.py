import cv2
import time


WINDOW_NAME = "OpenCV Webcam"
HELP = " (Q)uit (I)mage (H)elp"



def run():

    cv2.namedWindow(WINDOW_NAME)

    video_capture = cv2.VideoCapture(0)

    show_help = False
    loop = True
    while loop:
        ret, frame = video_capture.read()
        
        frame2 = frame.copy()

        if show_help :
            cv2.putText(frame2, HELP, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
	    
        cv2.imshow(WINDOW_NAME, frame2)

        key = cv2.waitKey(1)
        if key == ord('q') or key == ord('Q') or key == 27 :
        #if key == 27:
            print("tecla: ", key)
            loop = False
            break
                
        if key == ord('i') or key == ord('I') :
            filename = time.strftime("img_%Y%m%d_%H%M%S.png")
            cv2.imwrite(filename, frame)
    		    
        if key == ord('H') or key == ord('h') :
            show_help = not(show_help)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()

