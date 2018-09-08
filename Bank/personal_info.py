class Personal_info:
  def __init__(self,name,lname,pwd,age,joined,gender):
    self.name = name,
    self.lname = lname,
    self.pwd = pwd,
    self.age = age,
    self.joined = joined,
    self.gender = gender,
    self.attrs = ["name","lname","pwd","age","joined","gender"]
    
  def edit(self,to_edit,new_val):
    if(to_edit in self.attrs):
       a = "self."+to_edit+"="+new_val
    else:
      print("Sorry but the input was invalad")
  
    
