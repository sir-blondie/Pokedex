from tkinter import * 
from PIL import Image, ImageTk
import Pokemon

class Pokedex:
    
    name_dict = {'1': 'bulbasaur', '2': 'ivysaur', '3': 'venusaur', '4':'charmander', '5':'charmeleon', '6':'charizard', '7':'squirtle'}

    def __init__(self):
        self.pokedex = Tk()
        self.pokedex.geometry("500x750")
        self.pokedex.title("Pokedex")
        

        self.label = Label(self.pokedex, text="Pokemon", font=('Arial', 16))
        self.label.pack()

        self.myentry = Entry(self.pokedex, font=('Arial', 16))
        self.myentry.pack()

        self.button = Button(self.pokedex, text="Confirm", bg="GREEN", command=self.pokemon_info)
        self.button.pack()

        image = Image.open("pokemon_logo.png")
        image = image.resize((300, 150), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        self.image_label = Label(self.pokedex, relief="raised", image=image)
        self.image_label.pack()

        self.text1 = Text(self.pokedex, height=8)
        self.text1.pack()

        self.pokedex.mainloop()

    def display_details(self, pokemon):     
        '''if pokemon.is_caught:
            self.text1.insert(END, f"Entry Number: {pokemon.entry}\n")
            self.text1.insert(END, f"Name: {pokemon.name}\n")
            self.text1.insert(END, f"Type: {pokemon.types}\n")
            self.text1.insert(END, f"Description: {pokemon.description}\n")
            self.text1.insert(END, f"{pokemon.name} has already been caught!")
        else:
            self.text1.insert(END, f"Entry Number: {pokemon.entry}\n")
            self.text1.insert(END, f"Name: {pokemon.name}\n")
            self.text1.insert(END, f"Type: {pokemon.types}\n")
            self.text1.insert(END, f"Description: {pokemon.description}\n")
            self.text1.insert(END, f"{pokemon.name} has not been caught!")'''

    def pokemon_info(self):
        self.text1.delete("1.0", END)
        for key in Pokedex.name_dict:
            if self.myentry.get() == key:
                temp_name = Pokedex.name_dict[key]
                self.text1.insert(END, f"Entry Number: {temp_name.entry}\n")
                self.text1.insert(END, f"Name: {temp_name.name}\n")
                self.text1.insert(END, f"Type: {temp_name.types}\n")
                self.text1.insert(END, f"Description: {temp_name.description}\n")
                self.text1.insert(END, f"{temp_name.name} has already been caught!")
                #self.display_details(temp_name)
                image = Image.open("squirtle.png")
                image = image.resize((200, 200), Image.LANCZOS)
                image = ImageTk.PhotoImage(image)
                self.image_label.config(image=image)
                self.image_label.img=image
                
        else:
            self.text1.insert(INSERT, "Invalid!")
        
        '''if self.myentry.get() == "1":
            self.display_details(Pokemon.squirtle)
            image = Image.open("squirtle.png")
            image = image.resize((200, 200), Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            self.image_label.config(image=image)
            self.image_label.img=image
        elif self.myentry.get() == "2":
            self.display_details(Pokemon.charmander)
            image = Image.open("charmander.png")
            image = image.resize((200, 200), Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            self.image_label.config(image=image)
            self.image_label.img=image
        elif self.myentry.get() == "3":
            self.display_details(Pokemon.bulbasaur)
            image = Image.open("bulbasaur.png")
            image = image.resize((200, 200), Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            self.image_label.config(image=image)
            self.image_label.img=image'''
            

Pokedex()