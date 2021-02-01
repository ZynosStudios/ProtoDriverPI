import unittest
import platform
from io import BytesIO
from PIL import Image
from tests.basecase import BaseCase


class MyTestCase(BaseCase):
    def test_ping(self):
        response = self.app.get('/ping')
        self.assertEqual(str, type(response.json['data']))
        self.assertEqual(200, response.status_code)

    def test_uploadimage(self):
        response = self.app.post("uploadimage/test.txt", data="Hello World")
        self.assertEqual(201, response.status_code)
        self.app.delete("deleteimage/test.txt")

    def test_updateimage(self):
        self.app.post("uploadimage/test.txt", data="Hello World")
        response = self.app.put("updateimage/test.txt", data="Hello Again World")
        self.app.delete("deleteimage/test.txt")
        self.assertEqual(200, response.status_code)

    def test_deleteimage(self):
        self.app.post("uploadimage/test.txt", data="Hello World")
        response = self.app.delete("deleteimage/test.txt")
        self.assertEqual(200, response.status_code)

    def test_getimage(self):
        temp = BytesIO()
        img = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
        img.save(temp, format='png')
        self.app.post("uploadimage/test.png", data=temp.getvalue())
        response = self.app.get("getimage/test.png")
        self.app.delete("deleteimage/test.png")
        self.assertEqual(bytes, type(response.data))
        self.assertEqual(200, response.status_code)

    if platform.uname().machine == "armv6l":

        def test_displayimage(self):
            temp = BytesIO()
            img = Image.new('RGB', size=(8, 8), color=(255, 255, 255))
            img.save(temp, format='png')
            self.app.post("uploadimage/test.png", data=temp.getvalue())
            response = self.app.get("displayimage/test.png")
            self.app.delete("deleteimage/test.png")
            self.assertEqual(200, response.status_code)

        def test_cleardisplay(self):
            response = self.app.get("cleardisplay")
            self.assertEqual(200, response.status_code)

    else:
        print("\nskipped PI specific test cases\n")

if __name__ == '__main__':
    unittest.main()
