import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connecter

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the number of pages", type=int)
parser.add_argument("--dbname", help="Enter the number of pages", type=int)
args = parser.parse_args()
oyo_url = "https://www.oyorooms.com/hotel-in-bangalore/?page="
page_num_MAX = args.page_num_max
scraped_info_list = []
connecter.connect(args.dbname)

for page_num in range(1, page_num_MAX):
    url = oyo_url + str(page_num)
    print("GET Request for: " + url)
    req = requests.get(oyo_url + str(page_num))
    content = req.content

    soup = BeautifulSoup(content, "html.parser")

    all_hotels = soup.find_all("div", {"class": "hotelCardListing"})

    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription_hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemrop": "streetAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "listingPrice_finalPrice"}).text
        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating_ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"] = None

        parent_amenities_element = hotel.find("div", {"class": "amenityWrapper"})

        amenities_list = []
        for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper_amenity"}):
            amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())

        hotel_dict["amenities"] = ', '.join(amenities_list[:-1])

        scraped_info_list.append(hotel_dict)
        connecter.insert_into_table(args.dbname, tuple(hotel_dict.values()))


dataFrame = pandas.DataFrame(scraped_info_list)
connecter.get_hotel_info(args.dbname)
