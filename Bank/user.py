# User class
class User:
  """This class will hold user information.
  """
  def __init__(self):
    self.password = ""
    self.first_name = ""
    self.last_name = ""
    self.email = ""
    self.phone_number = ""
    self.sin = ""

  def view_user(self, user_id):
    return user_id

  def log_in(self, user_id, user_password):
    
  
  def register(self,):
    pass

  def log_out(self):
    pass
  
  def set_password(self,old_pass,new_pass): 
    if(old_pass == self.password):
      self.password = new_pass

  def set_first_name(self,name):
    self.first_name = name

  def set_last_name(self,name):
    self.last_name = name

  def set_email(self,email):
    self.email = email

  def set_phone_number(self,number):
    self.phone_number = number
  
  def set_sin(self,sin):
    self.sin = sin

  def get_password(self):
    return self.password

  def get_first_name(self):
    return self.first_name

  def get_last_name(self):
    return self.last_name

  def get_email(self):
    return self.email

  def get_phone_number(self):
    return self.phone_number
    
  def get_sin(self):
    return self.sin
