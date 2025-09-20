import jetson.utils
import cv2

cams = []

def create_camera(csi_port): 
    cams.append(jetson.utils.videoSource("csi://" + str(csi_port)))

def create_usb_camera(device="/dev/video1"):
    cams.append(jetson.utils.videoSource("v4l2://" + device))

def get_image_size(camera_id):
    return cams[camera_id].GetWidth(), cams[camera_id].GetHeight()

def get_video(camera_id):
    return cv2.cvtColor(jetson.utils.cudaToNumpy(cams[camera_id].Capture()), cv2.COLOR_RGB2BGR)

def close_cameras():
    for cam in cams:
        cam.Close()    

if __name__ == "__main__":
    create_camera(0)                 # Kamera CSI
    create_usb_camera("/dev/video1") # Kamera USB

    while True:
        img_csi = get_video(0)
        img_usb = get_video(1)

        cv2.imshow("CSI Camera", img_csi)
        cv2.imshow("USB Camera", img_usb)

        if cv2.waitKey(1) == 27:  # ESC untuk keluar
            break

    close_cameras()
    cv2.destroyAllWindows()
