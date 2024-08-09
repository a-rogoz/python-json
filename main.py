import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def encode_who(w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            raise TypeError(w.__class__.__name__ + "is not JSON serializable")
    
    @staticmethod
    def decode_who(w):
        return Who(w["name"], w["age"])


class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, z)
        

class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)


some_man = Who('John Doe', 42)
print(json.dumps(some_man, cls=MyEncoder))

jstr = '"\\"The Meaning of Life\\" by Monty Python\'s Flying Circus"'
comics = json.loads(jstr)
print(type(comics))
print(comics)

old_man = Who("Jane Doe", 23)
json_str = json.dumps(old_man, default=Who.encode_who)
new_man = json.loads(json_str, object_hook=Who.decode_who)
print(type(new_man))
print(new_man.__dict__)

json_str2 = json.dumps(some_man, cls=MyEncoder)
new_man2 = json.loads(json_str2, cls=MyDecoder)

print(type(new_man2))
print(new_man2.__dict__)