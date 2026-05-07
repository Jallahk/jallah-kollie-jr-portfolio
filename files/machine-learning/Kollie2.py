"""Jallah Kollie, Algerian Fire data"""
import matplotlib.pyplot as plt
import calendar

# Open the Algerian forest fires data file
infile = open('Algerian_forest_fires_dataset.txt', 'r')


# Initialize lists to store data for Bejaia with fire status,dates, and temps
bejaia_data = []  # List for (date, temp, fire_status)
Dates = []
bejaia_temps = []
sidi_bel_abbes_temps = []
bejaia_monthly_temps = {}
sidi_bel_abbes_monthly_temps = {}

for line in infile:
    #looks for the region name
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
                if month not in bejaia_monthly_temps:
                    bejaia_monthly_temps[month] = []
                bejaia_monthly_temps[month].append(temp)
                
                
            elif current_region == 'Sidi-Bel Abbes':
                sidi_bel_abbes_temps.append(temp)
                if month not in sidi_bel_abbes_monthly_temps:
                    sidi_bel_abbes_monthly_temps[month] = []
                sidi_bel_abbes_monthly_temps[month].append(temp)
            
                
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
    plt.title('Noon Temperatures')
    plt.legend()
    plt.show()
    
    
def plotScatter():
    plt.figure(2)
    
    for date, temp, fire in bejaia_data:
        if fire:
            plt.scatter(date, temp, color='r', label='Fire' if 'Fire' not in plt.gca().get_legend_handles_labels()[1] else "")
        else:
            plt.scatter(date, temp, color='b', label='No Fire' if 'No Fire' not in plt.gca().get_legend_handles_labels()[1] else "")

    plt.xlabel('Year 2012')
    plt.ylabel('Temperature')
    plt.title('Fires in Bejaia Region')
    plt.legend()
    plt.show()
    
    
    
    
def barGraph():
       # Function to calculate average temperatures
    def calculate_monthly_averages(region_data):
        monthly_averages = {}
        for month, temps in region_data.items():
            avg_temp = sum(temps) / len(temps)
            monthly_averages[month] = avg_temp
        return monthly_averages

    # Calculate averages for both regions
    bejaia_avg_temps = calculate_monthly_averages(bejaia_monthly_temps)
    sidi_bel_abbes_avg_temps = calculate_monthly_averages(sidi_bel_abbes_monthly_temps)

    # Prepare data for plotting
    months = range(6, 10)
    bejaia_vals = [bejaia_avg_temps.get(month, 0) for month in months]
    sidi_vals = [sidi_bel_abbes_avg_temps.get(month, 0) for month in months]

    # Get month names using calendar module
    month_names = [calendar.month_name[m] for m in months]

    # Plotting the bar chart
    bar_width = 0.25
    x_positions = list(range(len(months)))  # Positions for the bars

    plt.figure(3)
    bejaia_positions = [x - bar_width/1 for x in x_positions]
    sidi_positions = [x + bar_width/1 for x in x_positions]
    
    # Plot Bejaia and Sidi-Bel Abbes bars side by side
    plt.bar(bejaia_positions, bejaia_vals, width=bar_width, color='r', label='Bejaia')
    plt.bar(sidi_positions, sidi_vals, width=bar_width, color='b', label='Sidi-Bel Abbes')

    # Duplicating month names for both bars
    # Place month labels directly under each bar
    combined_positions = bejaia_positions + sidi_positions
    combined_month_names = month_names * 2  # Duplicate month names for both bars
    

    # Setting the x-axis labels under both bars
    plt.xticks(combined_positions, combined_month_names)

    plt.xlabel('2012')
    plt.ylabel('Temperature')
    plt.title('Average Monthly Temperatures')
    plt.legend(loc ='upper left')
    plt.tight_layout()
    plt.show()
    
    
    
plotNoon()
plotScatter()
barGraph()
