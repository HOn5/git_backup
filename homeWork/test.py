class human:
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"{self.age}살 {self.name}입니다.")

    def eat():
        print("밥을 먹습니다.")


man1 = human("hsj", 23)

print(man1.intro())