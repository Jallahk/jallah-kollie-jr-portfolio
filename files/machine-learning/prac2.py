"""Jallah Kollie, Algerian forest fires data"""
import matplotlib.pyplot as plt

# Open the Algerian forest fires data file
infile = open('Algerian_forest_fires_dataset.txt', 'r')

# Initialize lists to store data for each region
dates = []
bejaia_temps = []
sidi_bel_abbes_temps = []
red=[]
blue=[]

# Track the current region
current_region = None

# Read the file line by line
for line in infile:
   # line = line.strip()
    
    # Detect and update current region
    if 'Bejaia Region Dataset' in line:
        current_region = 'Bejaia'
        continue
    elif 'Sidi-Bel Abbes Region Dataset' in line:
        current_region = 'Sidi-Bel Abbes'
        continue
    
    # Skip empty lines and headers
    #if not line or line.startswith('day,month'):
        #continue
    
    parts = line.split('\t')
    
    try:
        day = int(parts[0])
        month = int(parts[1])
        temp = float(parts[3])  # parts[8] is Temperature
        fire = str(parts[13]).strip()
        # Filter for 1st, 10th, 20th, and 30th day of the month
        if day in [1, 10, 20, 30]:
            date = f'{month}/{day}'
            
            # Add date only once to avoid duplicates
            if date not in dates:
                dates.append(date)
            
            # Append temperature based on the current region
            if current_region == 'Bejaia':
                bejaia_temps.append(temp)
                if fire == 'fire':
                    red.append(temp)
                else:
                    blue.append(temp)
                
                    
                
            elif current_region == 'Sidi-Bel Abbes':
                sidi_bel_abbes_temps.append(temp)
            #print(red)
            #print(blue)
            print(parts)
            
    except ValueError:
        # Skip lines that can't be converted to integers/floats
        continue


# Close the file
infile.close()
#print(temp)
def plotNoon():
# Plotting the temperature data
    plt.figure()

    plt.plot(dates, sidi_bel_abbes_temps, color='b', label='Sidi-Bel Abbes')
    plt.plot(dates, bejaia_temps, color='r', label='Bejaia')
    plt.xlabel('Year 2012')
    plt.ylabel('Celsius Degrees')
    plt.title('Algerian Forest Fires - Temperature Trends')
    #plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    

def plotScatter():
    
    fire_dates = []
    noFire_dates = []
    fire_temps = []
    noFire_temps = []
    plt.figure(2)

    # Iterate through Bejaia temperatures with index
    for idx, temp in enumerate(bejaia_temps):
        if temp in red:
            fire_dates.append(dates[idx])
            fire_temps.append(temp)
            plt.scatter(fire_dates, fire_temps, color='r',marker='o')
        elif temp in blue:
            noFire_dates.append(dates[idx])
            noFire_temps.append(temp)
            plt.scatter(noFire_dates, noFire_temps, color='b',marker='o')

    # Iterate through Sidi-Bel Abbes temperatures with index
    

    # Plotting the scatter plot
    

    #plt.scatter(fire_dates, fire_temps, color='b', label='Fire', marker='o')
    #plt.scatter(noFire_dates, noFire_temps, color='r', label='No Fire', marker='o')


    

    plt.xlabel('Date (Month/Day)')
    plt.ylabel('Celsius Degrees')
    plt.title('Algerian Forest Fires - Temperature Scatter Plot')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show() 
    


#def BarGraph():
    








#plotNoon()
plotScatter()

