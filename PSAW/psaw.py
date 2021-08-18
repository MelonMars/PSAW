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
        global _client
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
        _client = f"https://api.scratch.mit/users/{self.username}/"
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

    def getmessages(self, all:bool=True, limit:int=10, filter:str="all"):
        res = requests.get(f"https://api.scratch.mit.edu/users/{self.username}/messages?x-token={self.token}&filter={filter}&limit={limit}")
        res = res.json()
        if all:
            for dict in res:
                if dict["type"] == "addcomment":
                    _actor = dict["actor_username"]
                    _comment_frag = dict["comment_fragment"]
                    _comment_src = dict["comment_obj_title"]
                    print(f"{_actor} sent you a message: {_comment_frag} in {_comment_src}".replace('&#39;', '\''))
                elif dict["type"] == "studioactivity":
                    _studio = dict["title"]
                    print(f"new activity in: {_studio}".replace('&#39;', '\''))
                elif dict["type"] == "curatorinvite":
                    _actor = dict["actor_username"]
                    _studio = dict["title"]
                    print(f"{_actor} has invited you to {_studio}".replace('&#39;', '\''))
                elif dict["type"] == "followuser":
                    _actor = dict["actor_username"]
                    print(f"{_actor} is now following you!".replace('&#39;', '\''))
                print("\n")
        else:
            for dict in res in range(limit):
                if dict["type"] == "addcomment":
                    _actor = dict["actor_username"]
                    _comment_frag = dict["comment_fragment"]
                    _comment_src = dict["comment_obj_title"]
                    print(f"{_actor} sent you a message: {_comment_frag} in {_comment_src}".replace('&#39;', '\''))
                elif dict["type"] == "studioactivity":
                    _studio = dict["title"]
                    print(f"new activity in: {_studio}".replace('&#39;', '\''))
                elif dict["type"] == "curatorinvite":
                    _actor = dict["actor_username"]
                    _studio = dict["title"]
                    print(f"{_actor} has invited you to {_studio}".replace('&#39;', '\''))
                elif dict["type"] == "followuser":
                    _actor = dict["actor_username"]
                    print(f"{_actor} is now following you!".replace('&#39;', '\''))
                print("\n")


e = PSAWConnect("MelonMars", "benny1113!")
e.getmessages()