# In order to Run this file you need to install the module suntime (pip3 install suntime) and datetime
# Importing required models
from solar_panel_calculator_functions import *
import matplotlib.pyplot as plt  # needed if you want to plot the comparison of costs

#########################################################################################
# Reading input file and creating a dictionary with the required input values ###########
#########################################################################################
name = "Solar-Panel-Calculator/input.txt"
value_inputs = open(name)
list_input_values = {}
for line in value_inputs:
    if line[0] == "#":  # ignoring Comments from file
        continue
    words = line.split()
    if len(words) < 1:  # ignoring empty lines
        continue
    input_variable = words[0]
    input_value = words[1]
    list_input_values[input_variable] = input_value

#########################################################################################
# Converting required input values of the dictionary into floating points ###############
# and assign them to variables #########################################################
#########################################################################################

latitude_val = convert_to_float(list_input_values["location_lat:"])
longitude_val = convert_to_float(list_input_values["location_lon:"])
sun_hour_average = convert_to_float(list_input_values["sun_hours:"])
roof_area = convert_to_float(list_input_values["roof_area:"])
efficiency = convert_to_float(list_input_values["efficiency:"])
offset_pv_production = convert_to_float(list_input_values["offset_pv_production:"])
yearly_energy_consumption = convert_to_float(list_input_values["energy_consumption_year:"])
output_per_m2 = convert_to_float(list_input_values["output_kwp_per_m2:"])
energy_costs = convert_to_float(list_input_values["energy_cost_kwH:"])
eco_energy = convert_to_bool(list_input_values["eco_electricity:"])
available_capital = convert_to_float(list_input_values["available_capital:"])
credit_interest_rate = convert_to_float(list_input_values["credit_interest_rate:"])

co2_per_kwH_in_KG = 0.401  # source https://www.co2online.de/energie-sparen/strom-sparen/strom-sparen-stromspartipps/was-ist-echter-oekostrom/
oeko_co2_per_kwH_proportion = 0.1  # source: https://www.co2online.de/energie-sparen/strom-sparen/strom-sparen-stromspartipps/was-ist-echter-oekostrom/
co2_per_kwH_SOLAR_in_KG = 0.05
invest_1kWp_solar = 1350  # Euro source: https://www.rechnerphotovoltaik.de/rechner/amortisationszeit

##################################################################################
# Creating a list based on the location and the average daily sun hours (year) ###
##################################################################################
LST__date_sun_hours_clear_sky = daily_sun_hours_clear_sky_lst_one_year(2020, latitude_val, longitude_val)
LST_sun_hours = correcting_sun_hour_clear_sky__observed_average(sun_hour_average, LST__date_sun_hours_clear_sky)

##################################################################################
# Calculating wanted key figures #################################################
##################################################################################


output_PV_needed_in_KWh = max_kwh_needed_output(yearly_energy_consumption, LST_sun_hours, offset_pv_production,
                                                efficiency)
needed_pv_area = needed_solar_area_size(output_PV_needed_in_KWh, output_per_m2)
enough_roof_area_available = enough_roof_area(roof_area, needed_pv_area)
investment_pv_area = needed_pv_area * invest_1kWp_solar
if investment_pv_area > available_capital:
    credit_need = investment_pv_area - available_capital
else:
    credit_need = 0.0

energy_savings = energy_savings_kw_h(yearly_energy_consumption, LST_sun_hours, output_PV_needed_in_KWh, efficiency)
costs_without_solar = yearly_energy_consumption * energy_costs
co2_production = co2_production_no_solar(yearly_energy_consumption, co2_per_kwH_in_KG, eco_energy)
co2_savings_with_solar = co2_savings_sol(co2_production, yearly_energy_consumption, energy_savings, co2_per_kwH_SOLAR_in_KG)
costs_savings = energy_savings * energy_costs
pay_back_years_credit = years_to_credit_free(credit_need, credit_interest_rate, costs_savings)
armortization_years, sum_interest_credit, LST_compare_NO_solar_costs, LST_compare_solar_costs = years_to_armortization(
    investment_pv_area, credit_need, credit_interest_rate, costs_without_solar, costs_savings)

##################################################################################
# Printing the key figures #######################################################
##################################################################################

print(
    f"\nYou consumed last year {yearly_energy_consumption:.0f} kwH, with the price of {energy_costs:.3f}EURO per kwH. \nYou paid {costs_without_solar:.0f} EURO.")
print(f"Thus you produced {co2_production:.0f} kg co2.")
print(f"\nYou want to produce {offset_pv_production * 100:.0f}% of energy consumption even on regular winter days.")
if not enough_roof_area_available:
    print("To do so you do not have enough roof area.\n")
if enough_roof_area_available:
    print("To do so you have enough roof area: NICE!")
    print(f"You need to install {needed_pv_area:.2f}m^2 and you need to invest {investment_pv_area:.0f} Euro in order to achieve your solar production goal.")
    print(f"With the {needed_pv_area:.2f} m2 area of solar panels you can produce {energy_savings:.1f} kwH, \nand save yearly {costs_savings:.0f} EURO and  {co2_savings_with_solar:.0f} kg CO2. \nAfter {armortization_years} years you save money compared to not having solar panels.")
    if credit_need > 0:
        print(
            f"You need to borrow {credit_need:.0f} EURO, based on your interest rate of {credit_interest_rate * 100:.1f} % you need to pay {sum_interest_credit:.0f} EUROS interest, "
            f"\nand if you pay back the yearly cost savings of installing solar panels you can pay back the credit in {pay_back_years_credit} years ")
    print("\n")
##################################################################################
# Plotting the costs of solar energy vs no solar energy ##########################
##################################################################################

plt.figure(figsize=(5, 3), constrained_layout=True)
plt.plot(LST_compare_solar_costs, label="Solar_costs")
plt.plot(LST_compare_NO_solar_costs, label="NO_Solar_costs")
plt.xlabel('Years')
plt.ylabel('Costs in EURO')
plt.title("Comparison Solar Costs vs. No Solar Costs")
plt.legend()
plt.savefig('plot_solarcosts_vs_nosolarcosts.svg', dpi=350)

