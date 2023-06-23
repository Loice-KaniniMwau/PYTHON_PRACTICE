class Movies:
    def __init__(self,movie_title,scheduling,budget) :
        self.movie_title=movie_title
        self.scheduling=scheduling
        self.budget=budget
        self.castmembers=[]
        self.movies=[]
       
    def addcast(self,newmembers):
       self.castmembers.append(newmembers)
       return self.castmembers
    def removecast(self,member):
       self.castmembers.remove(member)
       return self.castmembers
    def addmovie(self,moviename):
        self.movies.append(moviename)
        return self.movies
    def removemovie(self,moviename):
       self.movies.remove(moviename)
       return self.movies
    def calculate_budget(self):
        self.amount=0
        self.expenditure={}
        expenditure={"transport":300000,"accomodation":30000,"emergency":20000}
        for expenditur in expenditure.values():
            self.amount+=expenditur
        if self.amount>self.budget:
                return f"${self.amount} exceeds the set budget which is ${self.budget}"
        else:
             return f"${self.amount} fits the set budget which is ${self.budget}"
            
        
       
    
    
movie1=Movies("blacklist",60,400000)
movie1.addcast("macian")
movie1.addcast("loice")
print(movie1.addcast("kanini"))

print(movie1.removecast("loice"))
print(movie1.addmovie("blacklist"))
print(movie1.addmovie("one of us is lying"))
print(movie1.addmovie("the cast"))
# print(movie1.addmovie)
print(movie1.calculate_budget())

# ankara question -where the design of the ankara changes based on the temperature 
# and the mood of the wearer
class Ankara:
   def __init__(self,mood,temp) :
        self.mood=mood
        self.temp=temp
        self.fabric=""
   def fabric_check(self,daily_mood,moment_temp):
       if daily_mood==self.mood:
           if moment_temp==self.temp:
            self.fabric+="Dotted"
           elif moment_temp > self.temp:
               self.fabric+='Stripped'
           else:
               self.fabric+='Floral'
       elif daily_mood > self.mood:
           if moment_temp==self.temp:
            self.fabric+="Dotted"
           elif moment_temp > self.temp:
               self.fabric+='Stripped'
           else:
               self.fabric+='Floral'
       elif daily_mood < self.mood:
           if moment_temp==self.temp:
            self.fabric+="Dotted"
           elif moment_temp > self.temp:
               self.fabric+='Stripped'
           else:
               self.fabric+='Floral'
       else:
           print("please enter mood:")
       return self.fabric
      
wearer1=Ankara("happy",30)
print(wearer1.fabric_check("happy",30))

# movement of wild animals
class Movement:
    def __init__(self,river_levels,predator_location,weather):
        self.river_levels=river_levels
        self.predator_location=predator_location
        self.weather=weather
        self.movement=True
    def migration(self,herd,river,present_location,weather):
        if river==self.river_levels and present_location==self.predator_location and weather==self.weather:
            self.movement=True
            return f"{herd} are moving from {present_location}"
        else:
            return f"{herd} are not moving from {present_location}"
animals=Movement("high","LocationA","sunny")
print(animals.migration("zebra","high","LocationA","sunny"))


# magical baobab
class Baobab:
    def __init__(self):
        # self.seasons=[]
        # self.fruits=[]
        # self.power={}
        self.fruit_seasons={}
    def add_fruit(self,fruit,season):
            self.fruit_seasons[fruit]=season
            print(self.fruit_seasons)
    def predict_next(self,season):
         fruits_for_season = [fruit for fruit, s in self.fruit_seasons.items() if s ==season]
         return fruits_for_season
    def predict_fruit(self,season):
        nextfruit=list(self.fruit_seasons.keys())
        self.season=season
        if not self.fruit_seasons:
            return "No fruits available"
        if self.season=="winter":
          predict_fruit=nextfruit[-1]
          return predict_fruit
        elif self.season=="summer":
            predict_fruit=nextfruit[-2]
            return predict_fruit
        elif self.season=="spring":
            predict_fruit=nextfruit[-3]
            return predict_fruit
        else:
            return "not fruits expected"
# we can also predict the next fruit by accessing the last fruit in fruit_seasons
# keys ..we achieve this by converting the keys of the dictionary(which are the fruits
# into a list)
# then accessing the last element
   
      

season1=Baobab()
season1.add_fruit("mango","winter")
season1.add_fruit("ovacado","winter")
season1.add_fruit("melon","summer")
season1.add_fruit("banana","summer")
season1.add_fruit("kiwi","spring")
season1.add_fruit("grapes","spring")
print(season1.predict_next("winter"))
# different approach for predicting next fruit for the season
print(season1.predict_fruit("winter"))
print(season1.predict_fruit("spring"))
print(season1.predict_fruit("summer"))

# The legendary African drum circle ..different traditional drums each with its own
# unique sound amd rythm.these drums have common attributes like material,sizes
# talking drum--mimics lines of human speech ,djembe-known for wide range of tones
# Bougarabou known for its deep rich bass tones
class Drum:
    def __init__(self, material, size):
        self.material = material
        self.size = size
    def make_sound(self):
        print(f"{self.__class__.__name__} which is {self.size} and is made of {self.material} {self.sound}")
class Djembe(Drum):
    sound = "produces wide range of sound"
class Talking_drum(Drum):
    sound = "can mimic human lines"
class Bougarabou(Drum):
    sound = "produces deep, rich bass tone"
drum1 = Djembe("wood", "medium")
drum1.make_sound()
drum2 = Talking_drum("leather", "large")
drum2.make_sound()
drum3 = Bougarabou("plastic", "small")
drum3.make_sound()

        


        
      
        
    


           
           

   
      

           
           
   
   
        
    

        

        

        

        