import json

class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def add_user(self,name,age):
        user = {"id":self.next_id,"name":name,"age":age}
        self.user.append(user)
        self.next_id = self.next_id + 1
        return user

    def get_user(self,user_id):
        for u in self.users:
            if u["id"] == user_id:
             return u
        return None

    def update_age(self,user_id,new_age):
        user = self.get_user(user_id)
        if user is None:
            return False
        user["age"] = new_age
        return True

    def remove_user(self,user_id):
        user = self.get_user(user_id)
        if user is None:
            return False
        self.users.remove(user)
        return True

    def list_users(self):
        return self.users

    def save_to_json(self,filepath):
        with open(filepath,"w",encoding="utf_8") as f:
            json.dump(self.users,f,ensure_ascii=False)

    def load_from_json(self,filepath):
        try:
            f = open(filepath,"r",encoding =  "utf_8")
        except FileNotFoundError:
            return

        with f:
            self.users = json.load(f)

        if self.users:
            max -id = 0
            for u in self.users:
                if u["id"] > max_id:
                    max_id = u["id"]
            self.next_id = max_id + 1
        else:
            self.next_id = 1