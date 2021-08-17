import requests, json, re


class PSAWConnect:
    def __init__(self, uname, pword):
        self.username = uname
        self.password = pword
        self._userlogin()

    def _userlogin(self):
        """
        Function to login(don't use this)
        """
        global _user_link
        headers = {
            "x-csrftoken": "a",
            "x-requested-with": "XMLHttpRequest",
            "Cookie": "scratchcsrftoken=a;scratchlanguage=en;",
            "referer": "https://scratch.mit.edu",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
        }
        data = json.dumps({"username": self.username, "password": self.password})
        request = requests.post(f"https://scratch.mit.edu/login/", data=data, headers=headers)
        try:
            self.session_id = re.search('"(.*)"', request.headers["Set-Cookie"]).group()
            self.token = request.json()[0]["token"]
        except AttributeError:
            raise Exception('Invalid Username or Password!')
        headers = {
            "x-requested-with": "XMLHttpRequest",
            "Cookie": "scratchlanguage=en;permissions=%7B%7D;",
            "referer": "https://scratch.mit.edu",
        }
        request = requests.get("https://scratch.mit.edu/csrf_token/", headers=headers)
        self.csrf_token = re.search("scratchcsrftoken=(.*?);", request.headers["Set-Cookie"]).group(1)
        _user_link = f"https://api.scratch.mit/users/{self.username}/"
        self.headers = {
            "x-csrftoken": self.csrf_token,
            "X-Token": self.token,
            "x-requested-with": "XMLHttpRequest",
            "Cookie": "scratchcsrftoken="
                      + self.csrf_token
                      + ";scratchlanguage=en;scratchsessionsid="
                      + self.session_id
                      + ";",
            "referer": "https://scratch.mit.edu",
        }



e = PSAWConnect("MelonMars", "benny1113!")