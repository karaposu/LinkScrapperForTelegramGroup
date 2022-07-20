import configparser



class telegram_connection(object):

  api_id = None
  api_hash = None
  username= None
  phone = None


  def __init__(self):
    self.read_config()


  def read_config(self):
    config = configparser.ConfigParser()
    config.read("config.ini")
    self.api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']

    self.api_hash = str(api_hash)

    self.phone = config['Telegram']['phone']
    self.username = config['Telegram']['username']

  def set_api_id(self, id, hash):
    self.api_id = id
    self.api_hash = hash

  def get_api_id(self):

    return  self.api_id



  def get_api_hash(self):
    return self.api_hash

  def get_username(self):

    return  self.username

  def get_phone(self):

    return  self.phone

  def print_values(self):
    print("------------------------------------")

    print("API_HASH:", self.get_api_hash())
    print("API_ID:", self.get_api_id())
    print("username:", self.get_username())
    print("phone:", self.get_phone())

    print("------------------------------------")





# p1 = Person("John", 36)
#
# print(p1.name)
# print(p1.age)