# 
import datetime
class AncestralStories:
    def __init__(self, nameof_story, typeof_story, lengthofthe_story, agegroup, moral_lesson, current_language):
        self.nameof_story = nameof_story
        self.typeof_story = typeof_story
        self.lengthofthe_story = lengthofthe_story
        self.agegroup = agegroup
        self.moral_lesson = moral_lesson
        self.current_language = current_language
    def describe_story(self):
        return f"{self.nameof_story} is written in {self.current_language} and is meant for {self.agegroup} and it teaches them about {self.moral_lesson}. It takes {self.lengthofthe_story} hours to narrate."
class Storyteller(AncestralStories):
    def __init__(self, nameof_storyteller, nameof_story, agegroup, moral_lesson):
        super().__init__(nameof_story, "", 0, agegroup, moral_lesson, "")
        self.nameof_storyteller = nameof_storyteller
    def describe_storyteller(self):
        return f"{self.nameof_storyteller} narrates {self.nameof_story} which is a {self.typeof_story} and focuses on {self.agegroup} and teaches us about {self.moral_lesson}"
class Translator(AncestralStories):
    def __init__(self, nameof_story, typeof_story, agegroup, moral_lesson, nameof_translator, current_language, newlanguage):
        super().__init__(nameof_story, typeof_story, 0, agegroup, moral_lesson, current_language)
        self.nameof_translator = nameof_translator
        self.newlanguage = newlanguage
    def describe_translator(self):
        return f"{self.nameof_translator} has translated {self.nameof_story} which is a {self.typeof_story} from {self.current_language} to {self.newlanguage}"


story1 = AncestralStories("bornacrime", "historical", 120, "young boys", "respect", "khosa")
print(story1.describe_story())
story2 = AncestralStories("river and the source", "traditional", 345, "young girls", "upholding dignity", "luo")
print(story2.describe_story())
storyteller = Storyteller("margaret", "river and the source", "young girls", "respect")
print(storyteller.describe_storyteller())

# african cuisines
class AfricanCuisine:
    def __init__(self, originOfCuisine, nameOfCuisine):
        self.nameOfCuisine=nameOfCuisine
        self.originOfCuisine=originOfCuisine
        self.ingredients={}
        self.preparationTime=0
        self.nutritionalvalue=""
    def describeCuisine(self):
        return f"{self.nameOfCuisine} is mostly prepared in {self.originOfCuisine}"
class MoroccanRecipe(AfricanCuisine):
    def __init__(self, originOfCuisine, nameOfCuisine):
        super().__init__(originOfCuisine, nameOfCuisine)
       
    def describeCuisine(self):
        return super().describeCuisine()
    def preparationOfCuisine(self,ingredient,quantity):
        if  ingredient in self.ingredients.keys():
            self.ingredients[ingredient]=quantity
        else:
            self.ingredients[ingredient]=quantity
            return f"{self.nameOfCuisine} is prepared using the folowing ingredients {self.ingredients}"
    def timeofPreparation(self,timetaken):
        timetaken=self.preparationTime+timetaken
        # string format of date into  days hours minutes
        convert=str(datetime.timedelta(seconds=timetaken))
        return f"{self.nameOfCuisine} from {self.originOfCuisine} which is prepared using {self.ingredients} takes {convert} to prepare"
    def nutritionalValue(self):
        if "meat" in self.ingredients.keys():
            self.nutritionalvalue="strengthens the bones"
        elif "lentils" in self.ingredients.keys():
            self.nutritionalvalue="keeps the body hydrated"
        elif "teff flour" in self.ingredients.keys():
            self.nutritionalvalue="rich in fiber, iron, and protein."
        else:
            self.nutritionalvalue="no known nutritional  value"
        return f"The nutritional value for {self.nameOfCuisine} :{self.nutritionalvalue}   "
       

class EthiopianRecipe(MoroccanRecipe):
    def __init__(self, originOfCuisine, nameOfCuisine):
        super().__init__(originOfCuisine, nameOfCuisine)
    def describeCuisine(self):
        return super().describeCuisine()
    def preparationOfCuisine(self, ingredient, quantity):
        return super().preparationOfCuisine(ingredient, quantity)
    def timeofPreparation(self, timetaken):
        return super().timeofPreparation(timetaken)
class NigerianRecipe(MoroccanRecipe):
    def __init__(self, originOfCuisine, nameOfCuisine):
        super().__init__(originOfCuisine, nameOfCuisine)
    def describeCuisine(self):
        return super().describeCuisine()
    def preparationOfCuisine(self, ingredient, quantity):
        return super().preparationOfCuisine(ingredient, quantity)
    def timeofPreparation(self, timetaken):
        return super().timeofPreparation(timetaken)
    

    
 

    

africanCuisine=AfricanCuisine("Kenya","chafua")
print(africanCuisine.describeCuisine())
moroccanRecipe=MoroccanRecipe("morocco","Harira")
print(moroccanRecipe.describeCuisine())
print(moroccanRecipe.preparationOfCuisine("tomatoes","0.5kgs"))
print(moroccanRecipe.preparationOfCuisine("lentilas","10gs"))
print(moroccanRecipe.preparationOfCuisine("lentils","0.5gs"))
print(moroccanRecipe.timeofPreparation(4500))
ethiopianrecipe=EthiopianRecipe("ethiopia","Injera")
print(ethiopianrecipe.describeCuisine())
ethiopianrecipe.preparationOfCuisine("teff flour","3kgs")
print(ethiopianrecipe.preparationOfCuisine("ghee","0.5gs"))
nigerianRecipe=NigerianRecipe("Nigeria","fufu")
nigerianRecipe.describeCuisine()
nigerianRecipe.preparationOfCuisine("cassava","2 cups")
print(nigerianRecipe.preparationOfCuisine("olive oil","1teaspoon"))
print(nigerianRecipe.timeofPreparation(2000))
print(moroccanRecipe.nutritionalValue())
print(ethiopianrecipe.nutritionalValue())


# **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to

# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.

# class Artist:
#     def __init__(self, name, country, musical_style):
#         self.name = name
#         self.country = country
#         self.musical_style = musical_style
#         self.instruments = []
#     def describeArtist(self,instruments):
#         self.instruments.append(instruments)
#         return f"{self.name} is an artist from {self.country} and uses the following musical instruments{self.instruments}"
# class Story:
#     def __init__(self, title, length, moral_lesson, age_group):
#         self.title = title
#         self.length = length
#         self.moral_lesson = moral_lesson
#         self.age_group = age_group

# class StoryTeller:
#     def __init__(self, name, language):
#         self.name = name
#         self.language = language
#         self.stories = []

#     def add_story(self, story):
#         self.stories.append(story)

# class Translator:
#     def __init__(self, source_language, target_language):
#         self.source_language = source_language
#         self.target_language = target_language
#         self.translated_stories = []

#     def translate_story(self, story):
#         if story.age_group == 'children':
           
#             translated_story = translate_for_children(story, self.source_language, self.target_language)
#         else:
         
#             translated_story = translate_for_adults(story, self.source_language, self.target_language)
#         self.translated_stories.append(translated_story)

# class FolkStory(Story):
#     def __init__(self, title, length, moral_lesson, age_group, origin, characters):
#         super().__init__(title, length, moral_lesson, age_group)
#         self.origin = origin
#         self.characters = characters


# class Stage:
#     def __init__(self,stagename,stageCapacity,stagePerfomances):

        
# class Performance:
#     def __init__(self, artist, start_time, end_time):
#         self.artist = artist
#         self.start_time = start_time
#         self.end_time = end_time
# class Stage:
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity
#         self.performances = []
#     def add_performance(self, performance):
#         if len(self.performances) < self.capacity:
#             self.performances.append(performance)
#             print(f"Performance by {performance.artist.name} added to {self.name}")
#         else:
#             print(f"{self.name} is already at full capacity.")
#     def remove_performance(self, performance):
#         if performance in self.performances:
#             self.performances.remove(performance)
#             print(f"Performance by {performance.artist.name} removed from {self.name}")
#         else:
#             print(f"The performance is not scheduled on {self.name}.")
#     def get_performances(self):
#         return self.performances


# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.
class Story:
    def __init__(self):
        self.stories = []
        self.story = {
            "title": "",
            "language": "",
            "genre": "",
            "length_of_story": "",
            "moral_of_story": "",
            "age_group": "",
            "content": ""
        }

    def add_story(self, title, genre, language, length_of_story, moral_of_story, age_group, content):
        if genre and language and length_of_story and moral_of_story and age_group and content and title:
            self.story = {
                "title": title,
                "language": language,
                "genre": genre,
                "length_of_story": length_of_story,
                "moral_of_story": moral_of_story,
                "age_group": age_group,
                "content": content
            }
            self.stories.append(self.story)
            print(f"{title} added successfully.")
        else:
            print("Please add all fields")

    def translate_story(self, expected_language, title):
        for story in self.stories:
            if story["title"] == title:
                if story["language"] != expected_language:
                    story["language"] = expected_language
                    print(f"The story titled {title} has been translated to {expected_language}")
                else:
                    print(f"The story titled {title} is already in {expected_language}")
                return
        print(f"{title} not found")


class StoryTeller(Story):
    def __init__(self):
        super().__init__()
        self.storyteller_details = []

    def add_storyteller_details(self, story, name, age, nationality):
        if story and name and age and nationality:
            storyteller = {
                "story": story,
                "name": name,
                "age": age,
                "nationality": nationality
            }
            self.storyteller_details.append(storyteller)
            print("Storyteller details added successfully.")
        else:
            print("Please provide all details.")

    def view_storyteller_details(self, story):
        for storyteller in self.storyteller_details:
            if story == storyteller["story"]:
                print(storyteller)
                return
        print(f"{story} not found")


story1 = Story()
story1.add_story("born a crime", "family drama", "khosa", 345, "importance of family", "20", "above 18")
story1.translate_story("zulu", "born a crime")

storyteller1 = StoryTeller()
storyteller1.add_storyteller_details("born a crime", "Crime Documentary", 567, "English")
storyteller1.view_storyteller_details("born a crime")


import datetime

class Artist:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def __str__(self):
        return f"{self.name} from {self.country}"

class Performance:
    def __init__(self, artist, start_time, end_time):
        self.artist = artist
        self.start_time = start_time
        self.end_time = end_time
    
    def get_duration(self):
        duration = self.end_time - self.start_time
        duration = str(datetime.timedelta(seconds=duration))
        return duration

class Stage:
    def __init__(self, capacity):
        self.nameofStage = ""
        self.capacity = capacity
        self.schedule = {}
        self.audience_description = {}
        self.artists_songs = {}
    
    def add_performance(self, performance, song):
        self.songs = []
        self.songs.append(song)
        # perfomace is an instance of the perfomance class
        # the perfoamce object is then added to schedule as  a key
        self.schedule[performance] = performance.get_duration()
        # performance.artist accesses the artist attribute of the performance object, which is an instance of the Artist class.
        self.artists_songs[performance.artist.name] = self.songs    
    def determine_performance_stage(self, artist, audience_type, instrument):
        if audience_type == 'young and bubbly' and instrument == 'Guitar':
            self.nameofStage = "stage Youngins"
        elif audience_type == "18 to 35" and instrument == "Piano":
            self.nameofStage = "stage Millennials"
        elif audience_type == "36 to 50" and instrument == "Drums":
            self.nameofStage = "stage Old and Cool"
        else:
            self.nameofStage = "artist not performing in this stage"
        return self.nameofStage
    
    def display_lineup(self):
        sorted_lineup = sorted(self.artists_songs.items(), key=lambda x: x[0])
        for artist, songs in sorted_lineup:
            print(f"{artist}: {', '.join(songs)}")
    
    def __str__(self):
        return f"{self.nameofStage} (Capacity: {self.capacity})"

# Creating instances
artist1 = Artist("Bensoul", "Kenya")
artist2 = Artist("Kidum", "Kenya")
artist3 = Artist("Arya", "Nigeria")
artist4 = Artist("Davido", "Nigeria")

performance1 = Performance(artist1, 70000, 78990)
performance2 = Performance(artist2, 6000, 8000)
performance3=Performance(artist3,6000,8000)
print(performance1.get_duration())


stage1 = Stage(4000)
stage1.add_performance(performance1, "sura yako")
stage1.add_performance(performance2,"too easy")
stage1.add_performance(performance3,"Sability")

print(stage1.artists_songs)

# print(stage1.get_total_duration())
print(stage1.determine_performance_stage("kidum","young and bubbly","Guitar"))
stage2 = Stage(5000)
print(stage2.add_performance(performance2, "Nitafanya"))
print(stage2.determine_performance_stage("Arya","young and bubbly","Piano"))

stage1.display_lineup()
stage2.display_lineup()

# performance is the argument passed to the add_performance() method, 
# which represents an instance of the Performance class.
# performance.artist accesses the artist attribute of the performance object, which is an instance of the Artist class.
# performance.artist.name accesses the name attribute of the artist object, which represents the name of the artist.
# So, performance.artist.name retrieves the name of the artist associated with the performance. It is used as the key in the self.artists_songs dictionary to store the list of songs (self.songs) associated with that artist.

# By using performance.artist.name as the key, the add_performance() method ensures that each artist is associated with their respective songs in the self.artists_songs dictionary.


    
# javascript
# Object.entries(this.artists_songs) converts the artists_songs object into an array of [key, value] pairs. Each key-value pair represents an artist and their associated songs.

# The sort method is called on the resulting array, and a comparison function is provided as an argument. The comparison function (a, b) => a[0].localeCompare(b[0]) determines the sorting order based on the artist names (the first element of each pair).

# Inside the comparison function, a[0] and b[0] represent the artist names of the current pair being compared. The localeCompare method is called on a[0] with b[0] as the argument to perform a string comparison based on the current locale. This method returns a negative number if a[0] comes before b[0] in the sorted order, a positive number if a[0] comes after b[0], or zero if they are considered equal.

# By using localeCompare in the comparison function, the code ensures that the artist names are sorted in a locale-sensitive manner, taking into account language-specific rules for string comparison.

# Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.
from datetime import datetime

class Flight:
    def __init__(self, flight_id, destination):
        self.flight_id = flight_id
        self.destination = destination
        self.travel_dates = datetime.now()
        self.passengers = []

    def __str__(self):
        return f"Flight ID: {self.flight_id}, Destination: {self.destination}, Travel Dates: {self.travel_dates}"

class BookingSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)
        return self.flights

    def search_flights(self, destination, travel_dates):
        available_flights = []
        for flight in self.flights:
            if (
                flight.destination == destination
                and flight.travel_dates.date() == travel_dates.date()
            ):
                available_flights.append(flight)
        return available_flights

    def book_flight(self, flight_id, passenger_name):
        flight = self.find_flight_by_id(flight_id)
        if flight:
            seat_number = self.reserve_seat(flight)
            if seat_number:
                self.add_passenger(flight, passenger_name, seat_number)
                confirmation = self.generate_confirmation(flight, passenger_name, seat_number)
                return confirmation
            else:
                return "No seats available on this flight."
        else:
            return "Flight not found."

    def find_flight_by_id(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
        return None

    def reserve_seat(self, flight):
        max_capacity = 100  
        if len(flight.passengers) < max_capacity:
            seat_number = f"A{len(flight.passengers) + 1}"
            return seat_number
        else:
            return None

    def add_passenger(self, flight, passenger_name, seat_number):
        passenger_info = {
            "name": passenger_name,
            "seat_number": seat_number
        }
        flight.passengers.append(passenger_info)

    def generate_confirmation(self, flight, passenger_name, seat_number):
        confirmation = f"Booking Confirmation:\nFlight ID: {flight.flight_id}\nTravel Dates: {flight.travel_dates}\nPassenger Name: {passenger_name}\nSeat Number: {seat_number}"
        return confirmation

# Testing the code
flight1 = Flight(12, "Nairobi")
flight2 = Flight(13, "Kisumu")
booking1 = BookingSystem()
print(booking1.add_flight(flight1))
print(booking1.add_flight(flight2))


print(booking1.search_flights("Nairobi", datetime(2023, 7, 1)))
print(booking1.book_flight(12, "loice"))



# Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.

class LibraryCatalog:
    def __init__(self, books):
        self.books = books

    def add_book(self, book, author):
        if book in self.books:
            self.books[book] += ', ' + author
        else:
            self.books[book] = author
        print(self.books)

    def available_books(self):
        print(len(self.books))

    def search_book(self, book, author):
        if book in self.books:
            print(f"{book} is available")
        else:
            print(f"{book} is not available")
        if author in self.books.values():
            print(f"Books written by {author} are currently available")
        else:
            print(f"Books written by {author} are currently not available")

    def display_book_details(self):
        for book, author in self.books.items():
            print(f"{book} is written by {author}")


books = {'Born a Crime': 'Trevor Noah', 'River and the source': 'Margaret Ogola'}
catalog = LibraryCatalog(books)

catalog.add_book('Originals', 'Adam Grant')
catalog.available_books()
catalog.search_book('Trevor Noah', 'Margaret Ogola')
catalog.display_book_details()

# student 
class Students:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
    def calculate_averageGrade(self):
        totalSum=sum(self.grades)
        return totalSum/len(self.grades)
    # def highestGrade(self):
    #    highest_grade =max(self.grades)
    # print("highest grade is",highestGrade)
    def student_who_passed(self):
        average_grade=self.calculate_averageGrade()
        if average_grade>=60:
            return "student has passed"
        else:
            return "student failed"

       

student1=Students("ANN",20,[80,70,80,90])
print(student1.calculate_averageGrade())
# print(student1.highestGrade())
print(student1.student_who_passed())

          

    
