import requests
import platform



BASE = "http://127.0.0.1:5000/"

def run_tests():
    log = ""
    response = requests.get(BASE + "ping")
    print(response)

    response = requests.post(BASE + "uploadimage/test.txt", data="Hello World")
    print(response)

    response = requests.put(BASE + "updateimage/test.txt", data="Hello Again World")
    print(response)

    response = requests.delete(BASE + "deleteimage/test.txt")
    print(response)

    response = requests.put(BASE + "updateimage/test.txt", data="I Dont Exist")
    print(response)

    response = requests.delete(BASE + "deleteimage/test.txt")
    print(response)

    response = requests.get(BASE + "getimage/test.png")
    print(response)

    if platform.uname().processor == "arm":
        import leddriver
        leddriver.display_image()

if __name__ == "__main__":
    run_tests()
