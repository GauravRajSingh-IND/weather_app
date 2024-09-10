import io
import tkinter
import urllib.request
from PIL import Image, ImageTk

from news_api_function import get_current_article_data, get_news_data

FONT = ('arial', 15, "bold")
COLOR = "snow"


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

        self.photo = None

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

    def write_article_data(self):

            # Title update
        title = self.article_data['title'].title()
        self.canvas.itemconfig(self.title, text=title)

        # background rectangle of title update.
        bbox = self.canvas.bbox(self.title)
        padding = 10
        self.canvas.coords(self.title_bg, bbox[0] - padding, bbox[1] - padding, bbox[2] + padding, bbox[3] + padding)

        # Author Name update
        author = self.article_data['author'].title()
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

app = UI()
app.exit_window()
