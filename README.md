
# Football Stadiums Map

This project creates an interactive map of football stadiums with the biggest capacities using the Python `folium` library. The map includes stadiums from around the world and groups them by their respective continents, with markers color-coded based on the stadium's seating capacity.

## Files

- `main.py`: This is the main script that generates the interactive map.
- `markerColor.py`: A utility script that returns a color based on a stadium's capacity to customize marker colors on the map.
- `stadiums.txt`: A CSV file containing the details of the football stadiums, including their name, capacity, region, and geographical coordinates (latitude and longitude).

## Requirements 
To run this project, you need the following Python libraries. You can install them using the `requirements.txt` file. 

### Using`requirements.txt`

1. Clone this repository to your local machine: 
```bash 
git clone https://github.com/yourusername/football-stadiums-map.git
cd football-stadiums-map
``` 
2. Create a virtual environment (optional but recommended): 
```bash 
python -m venv venv
``` 
3. Install the required dependencies: 
```bash
 pip install -r requirements.txt
 ```
## Live Site 
You can view the live map by clicking the link below: 
- [Live Stadium Map](https://folium-app.onrender.com)
