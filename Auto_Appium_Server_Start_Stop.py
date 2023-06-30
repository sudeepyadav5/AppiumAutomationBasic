import subprocess
import time


def start_appium_server():
    # Start the Appium server using CLI command
    subprocess.Popen("appium", shell=True)

    # Wait for the server to start
    time.sleep(10)
    print("Appium server started.")


def stop_appium_server():
    # Stop the Appium server using CLI command
    subprocess.Popen("pkill -f appium", shell=True)

    # Wait for the server to stop
    time.sleep(5)
    print("Appium server stopped.")


# Example usage
start_appium_server()

# Your test code here...

stop_appium_server()
