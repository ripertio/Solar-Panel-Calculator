# Solar Panel Calculator
Author: Richard Kempert
Semester: 21W

## General Information:
The file `solar_panel_calcuation.py` processes the input data and returns key figures that should help you to estimate whether an installing solar panel might be profitable and possible and how much you may reduce your carbon footprint. 
The file `solar_panel_calculator_functions.py` contains the required functions to compute the key figures. I got the idea from https://www.omnicalculator.com/ecology/solar-panel
Based on the input factors provided in `input.txt` file the program calculates:
- your investment costs
- the required roof area
- potential yearly savings of CO2
- potential yearly cost reductions
- if a credit is needed in how many years you can pay off the credit if you return the yearly cost savings due to the solar panels 
- how many years till the investment of solar panels is equal to the total costs that would be occurred without solar panels; this is also plotted using matplotlib

The input factors that are required to compute these calculations are:

| Input Faktor | Name in `input.txt` file |
|---|---|
| energy consumption per year | `energy_consumption_year:  3000` in kwH |
| location | ` location_lat: 47.26667  location_lon: 11.38333 ` |
| the average sun hours per day | `sun_hours: 6 `|
| available roof area | `roof_area: 20` in m^2|
| efficiency of the solar modules |  `efficiency: 0.6 `    For further information see https://www.photovoltaik-web.de/photovoltaik/dacheignung/dachausrichtung` |
| how much proportion you want to cover with the solar panel | `offset_pv_production: 0.8 ` use zero-dot notation|
| available capital | `available_capital: 2000`in EURO |
| possible loan interest rate | `credit_interest_rate: 0.0  ` use zero-dot notation | 
| renewable electricity mix purchased to date (eco: True/False) | `eco_electricity: False` If your energy mix is based on renewable energy enter `True`|
| your electricity costs per kwH | `energy_cost_kwH: 0.27 ` in Euro|

## Tutorial
This program requires the modules `datetime` `suntime` and `matplotlib`
To compute the wanted information at first you must provide the listed input values listed above in the `input.txt` file. 
**Important: ** only edit the values of the lines NOT starting with `#`.
for example do not change these two lines:
```
# The solar panel calculator provides detailed information, helping to find the perfect solar panel size for your house
# Input Values required to calculate
```
and in the lines that does not start whit `#` only edit or insert a value after the `:`
for example in these two lines:
```
sun_hours: 3.4                  # average daily sun hours of the location
roof_area: 50                   # Available roof area, in m^2 
```
only edit the numbers `3.4` and `50`. Everything that cam after a `#`is an explanation for you what input is asked from you.
Then run the file `main.py` to computed to calculations, in case of invalided input values the program should prompt a respective assertion, and you can correct your input values in the `input.txt`file NOT in the `main.py`file!
Have fun calculating the benefits you might gain by installing a (surprisingly) small area of solar panels!

## Example calculation
the following example `input.txt` cofiguration:
```
# The solar panel calculator provides detailed information, helping to find the perfect solar panel size for your house
# Input Values required to calculate
location_lat: 47.26667          #   location (latitude)
location_lon: 11.38333          #   location (longitute)
sun_hours: 6                    #   average daily sun hours of the location
roof_area: 20                   #   Available roof area, in m^2
efficiency: 0.9                 #   For further information see https://www.photovoltaik-web.de/photovoltaik/dacheignung/dachausrichtung
offset_pv_production: 0.8       #   The proportion of how much energy you want to produce even on days with few hours of sunshine e.g. in the winter
output_kwp_per_m2: 0.34         #   Peak performance of the (kilo watt peak) of the solar panels
eco_electricity: False          #   Electricity mix purchased to date (eco True/False),
energy_consumption_year:  3000  #   energy consumption per year, in kwH
energy_cost_kwH: 0.27           #   electricity costs per kwH
available_capital: 2000         #   available capital ,
credit_interest_rate: 0.1       #   possible loan interest rate.
```

returns the following computation:
```

You consumed last year 3000 kwH, with the price of 0.270EURO per kwH 
You paid 810 EURO
Thus you produced 1203 kg co2

You want to produce 80% of energy consumption even on regular winter days.
To do so you have enough roof area: NICE!
You need to install 5.17m^2 and you need to invest 6981 Euro in order to achieve your solar production goal.
With the 5.17 m2 area of solar panels you can produce 2879.7 kwH, 
and save yearly 778 EURO and  1011 kg CO2.
After 6 years you save money compared to not having solar panels.
You need to borrow 4981 EURO, based on your interest rate of 10.0 % you need to pay 1854 EUROS interest, 
and if you pay back the yearly cost savings of installing solar panels you can pay back the credit in 11 years 

```
Additionally, the program plots a comparison of costs with and without solar panels installed:

![](example_plot_solarcosts_vs_nosolarcosts.svg)


## Reflection:

### Motivation
The task is related to solar panels, how much energy can be generated with which area at which investment costs.
Friends of mine are currently thinking about installing solar panels on their roof. My goal was to help them in their decision if they should install solar panels or not.

### Reflexion on implementation
To implement the program was for me more difficult than I assumed. Especially the implementation of the daily sun hours was quite demanding. 
My original take was to return a random number of sun hours based on the max. possible sun hours that day due to location and the average daily sun hours. But I was not able to.
Furthermore. the calculation of the return of investment and the comparison of when the solar panels is "cheaper" than not installing them.
Additionally, to come up with useful test before the implementation was difficult because often I "found" a way to implement the wanted calculation in the process of writing the code.
I think I should have spent more time with the identification of the specific problem that I want so solve with each particular function before starting to implement the solution.
But this was exactly what I tried, but maybe it would work out better to do it more iteratively. 

### Programming
The implementation of all functions in sums seems quite "clumsy" and "bulky" for sure with more experience one could have implemented it in a smarter and slimmer way.
Nevertheless, I am quite satisfied with generic calculation especially the definitions of function. In my opinion, thus the code is readable.

### Testing
I am not happy with testing. In my workflow I thought about the implementation, designing test cases and implementing the computation the process of testing does not feel "smooth".
Often the test cases was added during the implementation or after the function worked as I thought it should because only then I knew how it should work. 
But I could not come up with a better workflow. Nevertheless, defining tests made me think about possible issues that could come up which is nice.
For example what the minimal set of input variables are in oder to perform each calculation.

### Plans
I plan to extend this program to calculate the efficiency of the solar panels based on the orientation and the slope of the roof.
Further it would be interesting to not take the average sun hours per day but include more variation on each day to be more realistic 
and plot the result to illustrate in which and how many months of the year the solar penal area does deliver how much energy.
