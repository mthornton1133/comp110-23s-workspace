class Profile:
     
    handle: str
    followers: int
    is_private: bool

    def __init__(self, handle: str):
          self.handle = handle
          self.followers = 0
          self.is_private = False

    def tweet(self, msg: str) -> None:
          if not self.is_private:
               print(f"@{self.handle} tweets {msg}")
    
    def toggle_privacy(self) -> None:
         self.is_private = not self.is_private

    def __str__(self):
        if self.is_private == False:
            return f"{self.handle}; Followers: {self.followers}; Public"
        if self.is_private == True:
            return f"{self.handle}; Followers: {self.followers}; Private"
         

a: Profile = Profile("alyssa")
b: Profile = Profile("tyler")
b.toggle_privacy()
print(a)
print(b)