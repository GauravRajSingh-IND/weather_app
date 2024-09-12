import io
import tkinter
import urllib.request
from PIL import Image, ImageTk

from news_api_function import get_current_article_data, get_news_data
import re

from datetime import datetime

import pytz

from weather_function import get_location, get_timezone_code, get_datetime, get_weather

FONT = ('arial', 15, "bold")
COLOR = "snow"
WIND_ICON= "↑"


def get_image_url(url):
    # Create a request with a User-Agent header
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    # Open the URL and read the image data
    with urllib.request.urlopen(req) as response:
        image_data = response.read()
    # Convert the image data to a format Pillow can work with
    image = Image.open(io.BytesIO(image_data))

    # Optionally resize the image
    image = image.resize((590, 400))

    return image

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

        self.window = tkinter.Tk()
        self.window.title("Weather")
        self.window.geometry("1200x1200")

        # Add background image.
        self.canvas = tkinter.Canvas(self.window, height=1200, width=1200, highlightthickness=0)
        self.background_image = tkinter.PhotoImage(file="images/app_background.png")
        self.canvas.create_image(600, 370, image=self.background_image)

        # Draw rectangles for different sections
        self.draw_section()

        # news data of current article
        self.article_number = 0
        self.articles_data_fetch = get_news_data()

        # list of articles which have image url.
        self.articles = [article for article in self.articles_data_fetch if article['urlToImage'] is not None]
        self.article_data = get_current_article_data(articles=self.articles, article_no=self.article_number)

        # display current article data.
        self.title = self.canvas.create_text(850, 400, text="", font=('arial', 30, 'bold italic'), fill= "snow",
                                             justify=tkinter.CENTER, width=500, tags='news')
        self.title_bg = self.canvas.create_rectangle(self.canvas.bbox(self.title), fill="SkyBlue4", outline= "")

        self.author = self.canvas.create_text(725, 500, text="", font=('arial', 15, 'bold italic'),
                                              justify=tkinter.CENTER, width=550, tags='news')
        self.published = self.canvas.create_text(1070, 500, text="", font=('arial', 15, 'bold italic'),
                                             justify=tkinter.CENTER, width=550, tags='news')
        self.description = self.canvas.create_text(850, 625, text="", font=('arial', 25, 'bold italic'), fill= "blanched almond",
                                             justify=tkinter.CENTER, width=550, tags='news')

        self.draw_button()
        self.write_article_data()
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

    def write_article_data(self):

        # Title update

        title = self.article_data['title'].title()
        self.canvas.itemconfig(self.title, text=title)

        # background rectangle of title update.
        bbox = self.canvas.bbox(self.title)
        padding = 10
        self.canvas.coords(self.title_bg, bbox[0] - padding, bbox[1] - padding, bbox[2] + padding, bbox[3] + padding)

        # Author Name update
        try:
            author = self.article_data['author'].title()
        except AttributeError:
            author = "Unknown"
        self.canvas.itemconfig(self.author, text=author)

        # published text update.
        published = self.article_data['published'].split('T')[0]
        self.canvas.itemconfig(self.published, text=published)

        # description of the article.
        description = self.article_data['description'].title()
        self.canvas.itemconfig(self.description, text=description)

        # Image of the article.
        image_url = self.article_data['image']
        image = get_image_url(image_url)
        # Convert the image to a PhotoImage object for Tkinter
        self.photo = ImageTk.PhotoImage(image)
        # Display the image on the canvas
        self.canvas.create_image(850, 285, image=self.photo)


        self.canvas.tag_raise(self.title_bg)
        self.canvas.tag_raise(self.title)
        self.canvas.tag_raise(self.author)

        self.window.after(1000000, self.write_article_data)

    def draw_button(self):

        self.next_button = tkinter.Button(self.window, bg= "snow", fg= "black", height= 1, highlightthickness= 0,
                                          text= "NEXT", font= ('arial', 15, 'bold'), command= self.next_command)
        self.next_button.place(x=900, y=750)

        self.previous_button = tkinter.Button(self.window, bg="snow", fg="black", height=1, highlightthickness=0,
                                          text="PREV", font= ('arial', 15, 'bold'), command= self.previous_command)
        self.previous_button.place(x=750, y=750)

        self.refresh_button = tkinter.Button(self.window, bg="snow", fg="black", height=1, highlightthickness=0,
                                              text="🔄", font=('arial', 25, 'bold'), command=self.refresh_news)
        self.refresh_button.place(x=1080, y=5)

    def next_command(self):

        if  len(self.articles) >= self.article_number:
            self.article_number += 1

        self.article_data = get_current_article_data(articles=self.articles, article_no=self.article_number)
        self.write_article_data()

    def previous_command(self):

        if  self.article_number == 0:
            pass
        else:
            self.article_number -= 1
            self.article_data = get_current_article_data(articles=self.articles, article_no=self.article_number)
            self.write_article_data()

    def refresh_news(self):
        self.article_number = 0
        self.articles_data_fetch = get_news_data()

        # list of articles which have image url.
        self.articles = [article for article in self.articles_data_fetch if article['urlToImage'] is not None]
        self.article_data = get_current_article_data(articles=self.articles, article_no=self.article_number)
        self.write_article_data()

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
