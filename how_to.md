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


