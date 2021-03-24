import requests

class TestMubuLogin:
    def test_get_home_page(self):
        url = "https://mubu.com/"
        headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        }
        resp = requests.get(url, headers=headers, verify=False)
        # print("resp---", resp.text)

        assert resp.status_code == 200


    def test_login(self):
        url = "https://mubu.com/login"
        headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        }
        resp = requests.get(url, headers=headers, verify=False)
        # print("resp---", resp.text)

        assert resp.status_code == 200


    def test_login_password(self):
        url = "https://mubu.com/login/password"
        headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        }
        resp = requests.get(url, headers=headers, verify=False)
        # print("resp---", resp.text)

        assert resp.status_code == 200


    def test_login_post(self):
        url = "https://mubu.com/api/login/submit"
        headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "content-type":"application/x-www-form-urlencoded; charset=UTF-8"
        }
        data = "phone=17601007087&password=cyliu836&remember=true"

        # # data = {
        #     "phone": "17601007087",
        #     "password": "cyliu836",
        #     "remember": True
        # }
        resp = requests.post(url, headers=headers, data=data, verify=False)
        print("resp---", resp.text)

        assert resp.status_code == 200
        resp_json = resp.json()
        assert resp_json["code"] == 0


