import cv2
import time
  
def play_video(prediction,maximum):  
    cap = cv2.VideoCapture('./video.mp4')
    #length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps= int(cap.get(cv2.CAP_PROP_FPS))
    
    while(cap.isOpened()):
        try: 
        # Capture frames in the video
            ret, frame = cap.read()
            time.sleep(1/fps)
            # describe the type of font
            # to be used.
            font = cv2.FONT_HERSHEY_SIMPLEX
        
            # Use putText() method for
            # inserting text on video
            cv2.putText(frame, 
                        prediction+"   "+ str(maximum), 
                        (50, 50), 
                        font, 1, 
                        (0, 255, 255), 
                        2, 
                        cv2.LINE_4)
        
            # Display the resulting frame
        
            cv2.imshow('video', frame)
            
                
            # creating 'q' as the quit 
            # button for the video
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except Exception as e:
            print(str(e))
    # release the cap object
    cap.release()
    # close all windows
    cv2.destroyAllWindows()