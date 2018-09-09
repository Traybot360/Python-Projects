class Personal_info:
  def __init__(self,name,lname,pwd,age,joined,gender):
    self.name = name
    self.lname = lname
    self.pwd = pwd
    self.age = age
    self.joined = joined
    self.gender = gender
    self.attributes = ["name","lname","pwd","age","joined","gender"]
    
  def edit(self,attribute,value):
    if(attribute in self.attributes):
       exec("self."+attribute+"=value")
    else:
      print("Sorry but the input was invalid")
  
    
