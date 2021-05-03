class Country:
  def __init__(self, name, capital, population, continent):
    self._name = name
    self._capital = capital
    self._population = population
    self._continent = continent
    
    
my_country = Country('France', 'Paris', 67081000, 'Europe')
print(my_country._name)
print(my_country._capital)
print(my_country._population)
print(my_country._continent)


#----------------------------------------------------------------------------

class Artist:
  def __init__(self, name, medium, style, famous_artwork):
    self.__name = name
    self.__medium = medium
    self.__style = style
    self.__famous_artwork = famous_artwork
    

my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')
#print(my_artist.__name)
#print(my_artist.__medium)
#print(my_artist.__style)
#print(my_artist.__famous_artwork)

print(my_artist._Artist__name)
print(my_artist._Artist__medium)
print(my_artist._Artist__style)
print(my_artist._Artist__famous_artwork)


#----------------------------------------------------------------------------

class BankAccount:
  def __init__(self):
    self._checking = 0
    self._savings = 0
    
  def get_checking(self):
    return self._checking
  
  
  def set_checking(self, checking):
    self._checking = checking
    
    
  def get_savings(self):
    return self._savings
  
  
  def set_savings(self, savings):
    self._savings = savings
    
    
    
    
my_account = BankAccount()
my_account.set_checking(523.48)
print(my_account.get_checking())
my_account.set_savings(386.15)
print(my_account.get_savings())


#----------------------------------------------------------------------------

class Dancer:
  def __init__(self, name, nationality, style):
    self._name = name
    self._nationality = nationality
    self._style = style
    
  
  def get_name(self):
    return self._name
  
  
  def set_name(self, name):
    self._name = name


  def get_nationality(self):
    return self._nationality
  
  
  def set_nationality(self, nationality):
    self._nationality = nationality
    

  def get_style(self):
    return self._style
  

  def set_style(self, style):
    self._style = style
    
    
  name = property(get_name, set_name)
  nationality = property(get_nationality, set_nationality)
  style = property(get_style, set_style)



    
my_dancer = Dancer("Savion Glover", "American", "tap")
print(my_dancer.name)
print(my_dancer.nationality)
print(my_dancer.style)
my_dancer.name = 'Anna Pavlova'
my_dancer.nationality = 'Russian'
my_dancer.style = 'ballet'
print(my_dancer.name)
print(my_dancer.nationality)
print(my_dancer.style)


#----------------------------------------------------------------------------

class Cyclist:
    def __init__(self, name, nationality, nickname):
        self._name = name
        self._nationality = nationality
        self._nickname = nickname
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        self._nationality = nationality

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        self._nickname = nickname

my_cyclist = Cyclist("Greg LeMond", "American", "Le Montstre")
print(my_cyclist.name)
print(my_cyclist.nationality)
print(my_cyclist.nickname)
my_cyclist.name = "Eddy Merckx"
my_cyclist.nationality = "Belgian"
my_cyclist.nickname = "The Cannibal"
print(my_cyclist.name)
print(my_cyclist.nationality)
print(my_cyclist.nickname)