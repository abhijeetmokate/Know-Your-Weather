from tkinter import *
import tkinter.messagebox
from fetchWeatherData import *

main_window = Tk()
main_window.title('Know Your Weather')
main_window.geometry('600x400+450+200')
main_window.resizable(False, False)
font = ('garamond', 17, 'bold')
font2 = ('sansserif', 10, 'bold')
font3 = ('sansserif', 10)
buttonfont = ('sansserif', 15, 'bold')

city_label = Label(main_window, text='City Name', font=font)
city_label.place(x='20', y='20')

textbox = Entry(main_window, text='enter name', font=font)
textbox.place(x='200', y='20')

name = Label(main_window, text='City', font=font2).place(x='50', y='150')
name_value = Label(main_window, text='', font=font3)
name_value.place(x='150', y='150')

temperature = Label(main_window, text='Temperature', font=font2).place(x='50', y='200')
temperature_value = Label(main_window, text='', font=font3)
temperature_value.place(x='150', y='200')

weather = Label(main_window, text='Weather', font=font2).place(x='50', y='250')
weather_value = Label(main_window, text='', font=font3)
weather_value.place(x='150', y='250')

pressure = Label(main_window, text='Pressure', font=font2).place(x='50', y='300')
pressure_value = Label(main_window, text='', font=font3)
pressure_value.place(x='150', y='300')

humidity = Label(main_window, text='Humidity', font=font2).place(x='320', y='150')
humidity_value = Label(main_window, text='', font=font3)
humidity_value.place(x='420', y='150')

wind_speed = Label(main_window, text='Wind Speed', font=font2).place(x='320', y='200')
wind_speed_value = Label(main_window, text='', font=font3)
wind_speed_value.place(x='420', y='200')


def fetch_data():
    city = textbox.get()
    city_weather = get_weather(city)
    if city_weather.get_city_name() == 'ERROR':
        pop_up()

    name_value.config(text=city_weather.get_city_name() + ', ' + city_weather.get_country())
    temperature_value.config(text=str(city_weather.get_temperature()) + ' °C')
    pressure_value.config(text=str(city_weather.get_pressure()) + ' pa')
    weather_value.config(text=city_weather.get_weather_condition())
    humidity_value.config(text=str(city_weather.get_humidity()) + '%')
    wind_speed_value.config(text=str(city_weather.get_wind_speed()) + ' knot')


def pop_up():
    tkinter.messagebox.showerror("Error", "Please Enter Correct City Name")


search_button = Button(main_window, text='Search', font=buttonfont, command=fetch_data)
search_button.place(x='450', y='20')

main_window.configure()

main_window.mainloop()
