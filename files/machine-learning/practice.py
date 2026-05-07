import matplotlib.pyplot as plt

# Open the Algerian forest fires data file
infile = open('Algerian_forest_fires_dataset.txt', 'r')


# Initialize lists to store data for Bejaia with fire status
bejaia_data = []  # List of tuples (date, temp, fire_status)
Dates = []
bejaia_temps = []
sidi_bel_abbes_temps = []

for line in infile:
    if 'Bejaia Region Dataset' in line:
        current_region = 'Bejaia'
        continue
    elif 'Sidi-Bel Abbes Region Dataset' in line:
        current_region = 'Sidi-Bel Abbes'
        continue
    
    parts = line.strip().split('\t') #splits the data at '/t' and strips any unnesecerry values
    
    try:
        day = int(parts[0])
        month = int(parts[1])
        temp = float(parts[3])
        fire = parts[13].strip().lower()  # Normalize fire status
        
        if day in [1, 10, 20, 30]:
            date = f'{day}/{month}' # formats the day and month as day/month and gets stored in date
            
            if date not in Dates:
                Dates.append(date)
            
            if current_region == 'Bejaia':
                bejaia_temps.append(temp)
                bejaia_data.append((date, temp, fire == 'fire'))  # Store fire status as boolean
                
            elif current_region == 'Sidi-Bel Abbes':
                sidi_bel_abbes_temps.append(temp)
                
    except (ValueError, IndexError): #just in case there is no value at the index
        continue

infile.close()


def plotNoon():
# Plotting the temperature data
    plt.figure(1)

    plt.plot(Dates, sidi_bel_abbes_temps, color='b', label='Sidi-Bel Abbes')
    plt.plot(Dates, bejaia_temps, color='r', label='Bejaia')
    plt.xlabel('Year 2012')
    plt.ylabel('Celsius Degrees')
    plt.title('Algerian Forest Fires - Temperature Trends')
    #plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    
def plotScatter():
    plt.figure(2)
    
    for date, temp, fire in bejaia_data:
        if fire:
            plt.scatter(date, temp, color='r', label='Fire' if 'Fire' not in plt.gca().get_legend_handles_labels()[1] else "")
        else:
            plt.scatter(date, temp, color='b', label='No Fire' if 'No Fire' not in plt.gca().get_legend_handles_labels()[1] else "")

    plt.xlabel('Date (Month/Day)')
    plt.ylabel('Celsius Degrees')
    plt.title('Algerian Forest Fires - Temperature Scatter Plot')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    
    
def barGraph():
    
    
    
plotNoon()
plotScatter()
