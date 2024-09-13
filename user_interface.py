import tkinter
import webview

from maps import create_map_with_weather_layer

FONT = ('arial', 15, "bold")
COLOR = "snow"
html_file_path = '/Users/gauravsingh/pythonProject/pythonlearning/Projects/weather_app/weather_map.html'


class UI:

    def __init__(self):

        self.maps = create_map_with_weather_layer()

        self.window = tkinter.Tk()
        self.window.title("Weather")
        self.window.geometry("1200x1200")

        # Add background image.
        self.canvas = tkinter.Canvas(self.window, height=1200, width=1200, highlightthickness=0)
        self.background_image = tkinter.PhotoImage(file="images/app_background.png")
        self.canvas.create_image(600, 370, image=self.background_image)


        # Draw rectangles for different sections
        self.draw_section()


    def exit_window(self):
        self.window.mainloop()

    def draw_section(self):

        # Draw weather
        self.canvas.create_rectangle(50, 50, 500, 390, fill="", width=3, outline=COLOR)
        self.canvas.create_rectangle(50, 50, 500, 80, fill=COLOR, width=1, outline=COLOR)
        self.canvas.create_text(275, 65, text="WEATHER", font=FONT, width=100, anchor="center", fill= "black")

        # Draw Maps
        self.canvas.create_rectangle(50, 430, 500, 800, fill="", width=3, outline=COLOR)
        self.canvas.create_rectangle(50, 430, 500, 460, fill=COLOR, width=1, outline=COLOR)
        self.canvas.create_text(275, 445, text="Maps", font=FONT, width=100, anchor="center", fill= "black")

        # Draw news
        self.canvas.create_rectangle(550, 50, 1150, 800, fill="", width=3, outline=COLOR)
        self.canvas.create_rectangle(550, 50, 1150, 80, fill=COLOR, width=1, outline=COLOR)
        self.canvas.create_text(850, 65, text="NEWS", font=FONT, width=100, anchor="center", fill= "black")
        self.canvas.place(x=0, y=0)

app = UI()
app.exit_window()

