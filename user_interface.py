import tkinter
import re

from datetime import datetime

import pytz

from weather_function import get_location, get_timezone_code, get_datetime, get_weather

FONT = ('arial', 15, "bold")
COLOR = "snow"
WIND_ICON= "↑"

class UI:

    def __init__(self):

        # self.weather_icon_second = None
        # self.weather_icon = None
        # self.icon = None

        # weather parameters
        self.time_now = None
        self.location_latlng = get_location()
        self.timezone = get_timezone_code(latitude= self.location_latlng[0], longitude=self.location_latlng[1])
        self.datetime_now = get_datetime(timezone=self.timezone)
        self.weather_data = get_weather(latitude= self.location_latlng[0], longitude=self.location_latlng[1])

        print(self.weather_data)

        self.window = tkinter.Tk()
        self.window.title("Weather")
        self.window.geometry("1200x1200")

        # Add background image.
        self.canvas = tkinter.Canvas(self.window, height=1200, width=1200, highlightthickness=0)
        self.background_image = tkinter.PhotoImage(file="images/app_background.png")
        self.canvas.create_image(600, 370, image=self.background_image)

        # Draw rectangles for different sections
        self.draw_section()

        # Weather Tile Section.
        self.weather_suburb = self.canvas.create_text(150, 110, text="", font= ('arial', 30, 'bold'), fill= 'snow',
                                                      width= 200, anchor= tkinter.CENTER, justify= tkinter.CENTER)
        self.weather_temperature = self.canvas.create_text(170, 190, text="", font= ('arial', 120, 'bold'), fill= 'gray25',
                                                      width= 250)
        self.weather_feels_like = self.canvas.create_text(160, 270, text="", font=('arial', 20, 'italic'),
                                                          fill='gray15', width=250)
        self.weather_description = self.canvas.create_text(150, 355, text="", font=('arial', 25, 'bold italic'),
                                fill='gray15', width=250, anchor=tkinter.CENTER)
        self.weather_time = self.canvas.create_text(375, 110, text="", font=('arial', 35, 'bold italic'),
                                                           fill='gray15', width=250, anchor=tkinter.CENTER)
        self.weather_date = self.canvas.create_text(375, 175, text="", font=('arial', 20, 'bold italic'),
                                            fill='gray15', width=250, anchor=tkinter.CENTER)
        self.weather_day = self.canvas.create_text(375, 145, text="", font=('arial', 25, 'bold'),
                                            fill='gray15', width=250, anchor=tkinter.CENTER)

        self.weather_wind_degree = self.canvas.create_text(375, 245, text=WIND_ICON, angle=0, font=('arial', 30, 'bold'), fill='gray15',
                                                           width=250, anchor=tkinter.CENTER)
        self.weather_wind_degree_2 = self.canvas.create_text(335, 245, text=WIND_ICON, angle=0, font=('arial', 30, 'bold'),
                                                             fill='gray15',
                                                             width=250, anchor=tkinter.CENTER)
        self.weather_wind_degree_3 = self.canvas.create_text(295, 245, text=WIND_ICON, angle=0, font=('arial', 30, 'bold'),
                                                             fill='gray15',
                                                             width=250, anchor=tkinter.CENTER)
        self.weather_wind_degree_4 = self.canvas.create_text(415, 245, text=WIND_ICON, angle=0, font=('arial', 30, 'bold'),
                                                             fill='gray15',
                                                             width=250, anchor=tkinter.CENTER)
        self.weather_wind_degree_5 = self.canvas.create_text(455, 245, text=WIND_ICON, angle=0, font=('arial', 30, 'bold'),
                                                             fill='gray15', width=250, anchor=tkinter.CENTER)
        self.weather_wind_degree_6 = self.canvas.create_text(375, 270, text=WIND_ICON, angle=0,
                                                             font=('arial', 30, 'bold'), fill='gray15',
                                                             width=250, anchor=tkinter.CENTER)
        self.weather_wind_degree_7 = self.canvas.create_text(335, 270, text=WIND_ICON, angle=0,
                                                             font=('arial', 30, 'bold'),
                                                             fill='gray15', width=250, anchor=tkinter.CENTER)
        self.weather_wind_degree_8 = self.canvas.create_text(295, 270, text=WIND_ICON, angle=0,
                                                             font=('arial', 30, 'bold'),
                                                             fill='gray15', width=250, anchor=tkinter.CENTER)
        self.weather_wind_degree_9 = self.canvas.create_text(415, 270, text=WIND_ICON, angle=0,
                                                             font=('arial', 30, 'bold'),
                                                             fill='gray15',
                                                             width=250, anchor=tkinter.CENTER)
        self.weather_wind_degree_10 = self.canvas.create_text(455, 270, text=WIND_ICON, angle=0,
                                                              font=('arial', 30, 'bold'),
                                                              fill='gray15',
                                                              width=250, anchor=tkinter.CENTER)
        self.weather_wind_speed = self.canvas.create_text(370, 210, text="", angle=0,
                                                              font=('arial', 15, 'bold'),
                                                              fill='gray15',
                                                              width=250, anchor=tkinter.CENTER)

        self.weather_sunrise_icon = self.canvas.create_text(310, 320, text="🌅", angle=0,
                                                              font=('arial', 50, 'bold'),
                                                              fill='gray15',
                                                              width=250, anchor=tkinter.CENTER)
        self.weather_sunset_icon = self.canvas.create_text(440, 320, text="🌄", angle=0,
                                                       font=('arial', 50, 'bold'),
                                                       fill='gray15',
                                                       width=250, anchor=tkinter.CENTER)

        self.sunrise_text = self.canvas.create_text(310, 360, text="", angle=0, font=('arial', 20, 'bold'), fill='gray15',
                                                              width=250, anchor=tkinter.CENTER)
        self.sunset_text = self.canvas.create_text(440, 360, text="", angle=0, font=('arial', 20, 'bold'),
                                                    fill='gray15',
                                                    width=250, anchor=tkinter.CENTER)


        self.update_time()
        self.update_date()
        self.draw_weather()


    def update_date(self):

        # get latest datetime by using get_datetime function.
        self.datetime_now = get_datetime(timezone=self.timezone)

        date = self.datetime_now['date']
        day = self.datetime_now['day']

        self.canvas.itemconfig(self.weather_date, text=date)
        self.canvas.itemconfig(self.weather_day, text=day)

        self.window.after(60000, self.update_date)

    def update_time(self):

        # Get the current date and time in the specified timezone
        self.datetime_now = get_datetime(timezone=self.timezone)
        self.time_now = self.datetime_now['time']

        self.canvas.itemconfig(self.weather_time, text=self.time_now)
        self.window.after(1000, self.update_time)

    def draw_weather(self):
        """
        Draw text and images on the weather tile and update them in every 5 minutes.
        :return: None.
        """

        suburb_name = f"{self.weather_data['name']}"
        temperature = f"{int(self.weather_data['main']['temp'])}{chr(176)}"
        feels_like = f"feels like: {self.weather_data['main']['feels_like']}{chr(176)}C"
        description = self.weather_data['weather'][0]['description'].title()
        wind_angle = self.weather_data['wind']['deg']
        wind_speed = self.weather_data['wind']['speed']
        latitude = self.weather_data['coord']['lat']
        longitude = self.weather_data['coord']['lon']
        time_zone = pytz.timezone(get_timezone_code(latitude, longitude))
        sunrise = datetime.fromtimestamp(self.weather_data['sys']['sunrise']).strftime("%H:%M:%S")
        sunset = datetime.fromtimestamp(self.weather_data['sys']['sunset']).strftime("%H:%M:%S")

        self.icon = tkinter.PhotoImage(file=self.get_icon_link(icon=self.weather_data['weather'][0]['icon']))

        # add country name to the weather tile.
        self.canvas.itemconfig(self.weather_suburb, text=suburb_name)
        self.canvas.itemconfig(self.weather_temperature, text=temperature)
        self.canvas.itemconfig(self.weather_feels_like, text=feels_like)
        self.canvas.itemconfig(self.weather_description, text=description)
        self.canvas.itemconfig(self.weather_wind_degree, angle=wind_angle )
        self.canvas.itemconfig(self.weather_wind_degree_2, angle=wind_angle)
        self.canvas.itemconfig(self.weather_wind_degree_3, angle=wind_angle)
        self.canvas.itemconfig(self.weather_wind_degree_4, angle=wind_angle)
        self.canvas.itemconfig(self.weather_wind_degree_5, angle=wind_angle)
        self.canvas.itemconfig(self.weather_wind_degree_6, angle=wind_angle)
        self.canvas.itemconfig(self.weather_wind_degree_7, angle=wind_angle)
        self.canvas.itemconfig(self.weather_wind_degree_8, angle=wind_angle)
        self.canvas.itemconfig(self.weather_wind_degree_9, angle=wind_angle)
        self.canvas.itemconfig(self.weather_wind_degree_10, angle=wind_angle)
        self.canvas.itemconfig(self.weather_wind_speed, text=f"wind speed : {wind_speed}m/s")
        self.canvas.itemconfig(self.sunrise_text, text= sunrise)
        self.canvas.itemconfig(self.sunset_text, text=sunset)

        # add photo of the icon
        self.weather_icon = self.canvas.create_image(120, 310, image=self.icon)
        self.weather_icon_second = self.canvas.create_image(180, 310, image=self.icon)

        # update the data in every five minutes.
        self.window.after(300000, self.draw_weather)

    def exit_window(self):
        self.window.mainloop()

    def draw_section(self):

        # Draw weather area
        self.canvas.create_rectangle(50, 50, 500, 390, fill="", width=3, outline=COLOR)
        self.canvas.create_rectangle(50, 50, 500, 80, fill=COLOR, width=1, outline=COLOR)
        self.canvas.create_text(275, 65, text="WEATHER", font=FONT, width=100, anchor="center", fill= "black")

        # Draw stocks area
        self.canvas.create_rectangle(50, 430, 500, 800, fill="", width=3, outline=COLOR)
        self.canvas.create_rectangle(50, 430, 500, 460, fill=COLOR, width=1, outline=COLOR)
        self.canvas.create_text(275, 445, text="FORECAST", font=FONT, width=100, anchor="center", fill= "black")
        self.canvas.create_line(275, 450, 275, 800, fill=COLOR, width=2)
        self.canvas.create_line(50, 563, 500, 563, fill=COLOR, width=2)
        self.canvas.create_line(50, 676, 500, 676, fill=COLOR, width=2)

        # Draw news area
        self.canvas.create_rectangle(550, 50, 1150, 800, fill="", width=3, outline=COLOR)
        self.canvas.create_rectangle(550, 50, 1150, 80, fill=COLOR, width=1, outline=COLOR)
        self.canvas.create_text(850, 65, text="NEWS", font=FONT, width=100, anchor="center", fill= "black")
        self.canvas.place(x=0, y=0)

    def get_icon_link(self, icon):

        path = None
        pattern = r'(\d+)(\D+)'
        match = re.match(pattern, icon)
        if match:
            number = int(match.group(1))
            letter = match.group(2)

            if letter == 'n':
                path = f"images/Icons/night/{icon}@2x.png"
            elif letter == 'd':
                path = f"images/Icons/day/{icon}@2x.png"

        return path

app = UI()
app.exit_window()