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
    video = r"C:\Users\eperr\Anaconda3\Scripts3\Edge\handling_input_streams\test_video.mp4"
    # video = r"C:\Users\eperr\Anaconda3\Scripts3\Edge\handling_input_streams\blue-car.jpg"
    ### TODO: Handle image, video or webcam
    # Create a flag for single images
    image_flag = False
    # Check if the input is a webcam
    if args.i == 'CAM':
        args.i = 0
    elif args.i.endswith('.jpg') or args.i.endswith('.bmp'):
        print('True')
        image_flag = True

    ### TODO: Get and open video capture
    cap = cv2.VideoCapture(args.i)
    cap.open(args.i)
    if cap == True:
        print("LLKJ")
    # Create a video writer for the output video
    if not image_flag:
        # The second argument should be `cv2.VideoWriter_fourcc('M','J','P','G')`
        # on Mac, and `0x00000021` on Linux
        # 100x100 to match desired resizing
        out = cv2.VideoWriter(r"C:\Users\eperr\Anaconda3\Scripts3\Edge\handling_input_streams\out.mp4", 0x00000021, 30, (100,100))
    else:
        print("doublecheck")
        out = None
    print(image_flag, "OOOOOO")
    # Process frames until the video ends, or process is exited
    while cap.isOpened():
        # Read the next frame
        flag, frame = cap.read()
        if not flag:
            print('break')
            break
        key_pressed = cv2.waitKey(60)
        if flag == True:
            cv2.imshow('frame', frame)
            
        ### TODO: Re-size the frame to 100x100
        frame = cv2.resize(frame, (100,100))

        ### TODO: Add Canny Edge Detection to the frame, 
        ###       with min & max values of 100 and 200
        ###       Make sure to use np.dstack after to make a 3-channel image
        frame = cv2.Canny(frame, 100, 200)
        frame = np.dstack((frame, frame, frame))
        print(image_flag)
        ### TODO: Write out the frame, depending on image or video
        print('Truerertet')
        if image_flag:
            print('test')
            cv2.imshow('frame', frame)
            cv2.imwrite(r"C:\Users\eperr\Anaconda3\Scripts3\Edge\handling_input_streams\output_image.jpg", frame)
        else:
            print('test 1')
            out.write(frame)
        # Break if escape key pressed
        if key_pressed == 27:
            break
    print('True True')
    ### TODO: Close the stream and any windows at the end of the application
    if not image_flag:
        out.release()
    cap.release()
    cv2.destroyAllWindows()


def main():
    args = get_args()
    capture_stream(args)


if __name__ == "__main__":
    main()
