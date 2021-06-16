import geocoder
import reverse_geocoder as rg

def location():
  latitude, longitude = geocoder.ipinfo("me").latlng
  city = rg.search((latitude, longitude), verbose=False)
  return city[0]["name"]

if __name__ == '__main__':
  print(f'Your current location: {location()}')