#  This Code is just for educational purpose
#  Some of the functions are not soo configured and also might be vulnarable 
#  this code is no where usable for production server 
#  using the same raw code in production might lead to some sql injection attack
#  happy learning (^_^)


import sqlite3

con = sqlite3.connect('database.db')
con.execute("CREATE TABLE IF NOT EXISTS Users (username TEXT PRIMARY KEY, password TEXT, student BOOL)")
con.commit()
con.close()
del con
user_cache = {}

class User:
    def __init__(self, _payload:dict) -> None:
        self.username = _payload.get('username') 
        self.password = _payload.get('password')
        self._student = bool(_payload.get("student"))
        self.name = _payload.get('name') or "Not set"
        self.db:sqlite3.Connection = sqlite3.connect('database.db')
        self.cur:sqlite3.Cursor = self.db.cursor()

    @property
    def is_authorised(self):
        user =  self.db.execute(f"SELECT * FROM Users WHERE username = ? AND password = ?", (self.username,self.password))
        return user.fetchone()
    
    @property
    def student(self):
        return bool(self.is_authorised and self.is_authorised[2])
    
    @property
    def is_registered(self):
        user =  self.db.execute(f"SELECT * FROM Users WHERE username = ?", (self.username,))
        return user.fetchone()
    
    def register(self):
        self.db.execute("INSERT INTO Users (username, password, student) VALUES (?, ?, ?)", (self.username, self.password, self._student))
        self.db.commit()

    def to_dict(self):
        return {"username": self.username, "password": self.password, "student": self._student, "name": self.name}

    

    

ITEMS = {
    "r55600x" : {
        "price" : 16700,
        "company" : "AMD",
        "discount" : 50,  #50% discount
        "info" : {
            "core" : 6,
            "thread" : 12,
            "base_clock" : 3.7,
            "boost_clock" : 4.6,
            "rating" : 4.4
        }
    },
    "i512400f":{
        "price" : 8700,
        "company" : "Intel",
        "discount" : 50,  #50% discount
        "info" : {
            "core" : 6,
            "thread" : 12,
            "base_clock" : 2.9,
            "boost_clock" : 4.3,
            "rating" : 4.5
        }
    },
    "r55600xt" : {
        "price" : 18700,
        "company" : "AMD",
        "discount" : 50,  #50% discount
        "info" : {
            "core" : 6,
            "thread" : 12,
            "base_clock" : 3.8,
            "boost_clock" : 4.7,
            "rating" : 4.5
        }
    },
    "r55600" : {
        "price" : 14700,
        "company" : "AMD",
        "discount" : 50,  #50% discount
        "info" : {
            "core" : 6,
            "thread" : 12,
            "base_clock" : 3.6,
            "boost_clock" : 4.5,
            "rating" : 4.3
        }
    },
    "r55600t" : {
        "price" : 15700,
        "company" : "AMD",
        "discount" : 50,  #50% discount
        "info" : {
            "core" : 6,
            "thread" : 12,
            "base_clock" : 3.6,
            "boost_clock" : 4.5,
            "rating" : 4.3
        }
    },

}
