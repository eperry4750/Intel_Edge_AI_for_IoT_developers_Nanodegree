import argparse
import cv2
import numpy as np

def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Handle an input stream")
    # -- Create the descriptions for the commands
    i_desc = "The location of the input file"

    # -- Create the arguments
    parser.add_argument("-i", help=i_desc)
    args = parser.parse_args()

    return args


def capture_stream(args):
    ### TODO: Handle image, video or webcam
    # Create a flag for single images
    image_flag = False
    # Check if the input is a webcam
    if args.i == 'CAM':
        args.i = 0
    elif args.i.endswith('.jpg') or args.i.endswith('.bmp'):
        image_flag = True

    # Process frames until the video ends, or process is exited
    if image_flag:
        out = None
        frame = cv2.imread(args.i)
        key_pressed = cv2.waitKey(60)

        ### TODO: Re-size the frame to 100x100
        frame = cv2.resize(frame, (100,100))

        ### TODO: Add Canny Edge Detection to the frame, 
        ###       with min & max values of 100 and 200
        ###       Make sure to use np.dstack after to make a 3-channel image
        frame = cv2.Canny(frame, 100, 200)
        frame = np.dstack((frame, frame, frame))        
        cv2.imwrite('output_image.jpg', frame)
    else:
        out = cv2.VideoWriter('out.mp4', 0x00000021, 30, (100,100))
        ### TODO: Get and open video capture    
        cap = cv2.VideoCapture(args.i)
        cap.open(args.i)
        while cap.isOpened():
            # Read the next frame
            flag, frame = cap.read()
            if not flag:
                break
            key_pressed = cv2.waitKey(60)
    
            ### TODO: Re-size the frame to 100x100
            frame = cv2.resize(frame, (100,100))
    
            ### TODO: Add Canny Edge Detection to the frame, 
            ###       with min & max values of 100 and 200
            ###       Make sure to use np.dstack after to make a 3-channel image
            frame = cv2.Canny(frame, 100, 200)
            frame = np.dstack((frame, frame, frame))

            out.write(frame)
            # Break if escape key pressed
            if key_pressed == 27:
                break

        ### TODO: Close the stream and any windows at the end of the application
        out.release()
        cap.release()
    cv2.destroyAllWindows()


def main():
    args = get_args()
    capture_stream(args)


if __name__ == "__main__":
    main()
