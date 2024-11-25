from azure.storage.blob import BlobServiceClient
import subprocess
from gpiozero import MotionSensor
from datetime import datetime
import sys

# Configurations
connection_string = "<connection_string>"
container_name = "<container_name>"
image_path = "tmp/"
pir = MotionSensor(4)


def take_pic(blob_name):
    output = image_path + blob_name
    try:
        subprocess.run(["sudo rpicam-still --nopreview -o " + output], check=True, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' returned with error (code {}): {}".format(e.cmd, e.returncode, e.output))


def upload_pic(blob_name):
    src = image_path + blob_name
    try:
        client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = client.get_blob_client(container=container_name, blob=blob_name)

        with open(src, "rb") as image_file:
            blob_client.upload_blob(image_file)

        print(f"Image uploaded successfully to {container_name}/{blob_name}")
    except Exception as e:
        print("Error uploading file: ", e)


def exit_gracefully():
    print("Interrupt encountered. Exiting...")
    sys.exit(0)


def main():
    blob_name = ""
    while True:
        pir.wait_for_motion()
        blob_name = "img_" + datetime.now().strftime("%H:%M:%S") + ".jpg"
        take_pic(blob_name)
        upload_pic(blob_name)
        pir.wait_for_no_motion()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        pass
    finally:
        exit_gracefully()