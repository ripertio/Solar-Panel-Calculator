import datetime


####################################################
# function definition: #############################
####################################################
def convert_to_float(a_value):
    """
    A function that converts a value into a floating point, if it does not work the user is asked to change the value within the input.txt file
    :param a_value: The value that is to be converted into a float
    :type a_value: any
    :return: the same value converted into a float
    :rtype: float

    >>> convert_to_float("True")
    Traceback (most recent call last):
        ...
    TypeError: Return to the input.txt file and enter a  number
    >>> convert_to_float(1)
    1.0
    >>> convert_to_float(1.0)
    1.0
    >>> convert_to_float("1")
    1.0
    >>> convert_to_float("1.0")
    1.0

    >>> convert_to_float("s")
    Traceback (most recent call last):
        ...
    TypeError: Return to the input.txt file and enter a  number

    """
    if a_value == "False" or a_value == "True":
        raise TypeError("Return to the input.txt file and enter a  number")
    try:
        a_value = float(a_value)
    except ValueError:
        pass
    if type(a_value) != float:
        raise TypeError("Return to the input.txt file and enter a  number")
    else:
        return a_value


def float_check(n):
    """
    Checks if the argument type is float and returns it
    otherwise raises an exception,
    :param n (any)


    >>> float_check(1.0)
    1.0

    >>> float_check(True)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> float_check(1)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> float_check("1.0")
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    """
    if type(n) != float:
        raise TypeError("Use a float as an argument")
    else:
        return n


def convert_to_bool(a_value):
    """
    A function that converts a value into a bool point, if it does not work the user is asked to change the value within the input.txt file
    :param a_value: The value that is to be converted into a bool
    :type a_value: any
    :return: True or False
    :rtype: bool
    >>> convert_to_bool("True")
    True
    >>> convert_to_bool("False")
    False
    >>> convert_to_bool("true")
    Traceback (most recent call last):
        ...
    TypeError: Either use the exact spelling !True! or !False! in the input.txt file to express weather you use eco_electricity
    >>> convert_to_bool(1)
    Traceback (most recent call last):
        ...
    TypeError: Either use the exact spelling !True! or !False! in the input.txt file to express weather you use eco_electricity
    >>> convert_to_bool(None)
    Traceback (most recent call last):
        ...
    TypeError: Either use the exact spelling !True! or !False! in the input.txt file to express weather you use eco_electricity
    >>> convert_to_bool(0.0)
    Traceback (most recent call last):
        ...
    TypeError: Either use the exact spelling !True! or !False! in the input.txt file to express weather you use eco_electricity

    """
    if a_value == "True":
        n = True
    elif a_value == "False":
        n = False
    else:
        raise TypeError(
            "Either use the exact spelling !True! or !False! in the input.txt file to express weather you use eco_electricity")
    return n


def bool_check(a_value):
    """
    Checks if the argument type is bool, if not it raises and TypeError
    >>> bool_check(1)
    Traceback (most recent call last):
        ...
    TypeError: Use a bool as argument!
    >>> bool_check(1.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a bool as argument!
    >>> bool_check("1")
    Traceback (most recent call last):
        ...
    TypeError: Use a bool as argument!
    >>> bool_check(None)
    Traceback (most recent call last):
        ...
    TypeError: Use a bool as argument!
    >>> bool_check([None, ])
    Traceback (most recent call last):
        ...
    TypeError: Use a bool as argument!
    >>> bool_check(False)

    >>> bool_check(True)
     
    """
    if type(a_value) != bool:
        raise TypeError("Use a bool as argument!")


def datetime_date_check(n):
    """
    Checks if the argument type is float it not it raises an exception.

    >>> datetime_date_check(datetime.date(2020,1,1))

    >>> datetime_date_check(datetime.datetime(2020,1,1))

    >>> datetime_date_check(True)
    Traceback (most recent call last):
        ...
    TypeError: Use a datetime.date object as an argument
    >>> datetime_date_check(1)
    Traceback (most recent call last):
        ...
    TypeError: Use a datetime.date object as an argument
    >>> datetime_date_check("1.0")
    Traceback (most recent call last):
        ...
    TypeError: Use a datetime.date object as an argument
    """

    if not isinstance(n, datetime.date):
        raise TypeError("Use a datetime.date object as an argument")


def list_check(a_list):
    """
    Checks if the argument type is a list if not it raises an exception
    >>> list_check([1, ])

    >>> list_check(1.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a list as an argument
    >>> list_check({1:0})
    Traceback (most recent call last):
        ...
    TypeError: Use a list as an argument
    >>> list_check(True)
    Traceback (most recent call last):
        ...
    TypeError: Use a list as an argument
    >>> list_check((1,2))
    Traceback (most recent call last):
        ...
    TypeError: Use a list as an argument
    >>> list_check("1.0")
    Traceback (most recent call last):
        ...
    TypeError: Use a list as an argument

    """
    if type(a_list) != list:
        raise TypeError("Use a list as an argument")


def daily_sun_hours_clear_sky(value_lat, value_lon, date):
    """
    This function calculates the sun hours on a specified date at a spefied location. It assumes that there are no clouds or other radiation "blocking" circumstances.
    This function requires the modul datetime and suntime

    :param value_lat: Geographical latitude
    :type value_lat: float
    :param value_lon: Geographical lontitude
    :type value_lon: float
    :param date: Date
    :type date: datetime.date
    :return: sun hours at specified date, at specified location
    :rtype: float


    >>> daily_sun_hours_clear_sky("47.2667", 11.38333, datetime.date(2020,1,1))
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> daily_sun_hours_clear_sky( 47.2667, 0, datetime.date(2020,1,1))
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> daily_sun_hours_clear_sky(47.2667, 11.38333, "2020,1,1")
    Traceback (most recent call last):
        ...
    TypeError: Use a datetime.date object as an argument
    >>> daily_sun_hours_clear_sky(-90.00001, 11.38333, datetime.date(2020,1,1))
    Traceback (most recent call last):
        ...
    ValueError: the latitude must be a number between -66.56 and 66.56
    >>> daily_sun_hours_clear_sky(90.000001, 11.38333, datetime.date(2020,1,1))
    Traceback (most recent call last):
        ...
    ValueError: the latitude must be a number between -66.56 and 66.56
    >>> daily_sun_hours_clear_sky(47.26667, 180.00001, datetime.date(2020,1,1))
    Traceback (most recent call last):
        ...
    ValueError: the longitude must be a number between -180 and 180
    >>> daily_sun_hours_clear_sky(47.26667, -180.00001, datetime.date(2020,1,1))
    Traceback (most recent call last):
        ...
    ValueError: the longitude must be a number between -180 and 180
    >>> daily_sun_hours_clear_sky(47.268, 11.393, datetime.date(2020,1,1)) # checked with https://www.timeanddate.com/sun/austria/innsbruck
    8.533333333333333
    >>> daily_sun_hours_clear_sky(0.0, 0.0, datetime.date(2000,1,1)) # checked with https://www.timeanddate.com/sun/@0.032,0.052?month=1&year=2020
    12.116666666666667

    """
    import datetime
    from suntime import Sun
    float_check(value_lat)
    if value_lat < -66.56 or value_lat > 66.56:
        raise ValueError("the latitude must be a number between -66.56 and 66.56")
    float_check(value_lon)
    if value_lon < -180 or value_lon > 180:
        raise ValueError("the longitude must be a number between -180 and 180")
    datetime_date_check(date)

    sun = Sun(value_lat, value_lon)
    d_sunrise = sun.get_local_sunrise_time(date)
    d_sunset = sun.get_local_sunset_time(date)
    d_sunhours = d_sunset - d_sunrise
    d_sunhours_in_hours = d_sunhours / datetime.timedelta(hours=1)
    return d_sunhours_in_hours


def daily_sun_hours_clear_sky_lst_one_year(year, value_lat, value_lon, month_start=1, day_start=1, month_end=12,
                                           day_end=31):
    """
    This function creates a list containing all dates of a specified year as first element of a tuple and the second element is the respectife sun hourse on this date.
    It requires the module datetime and the function `daily_sun_hours_clear_sky()`
    The function can create any sequence of dates within one year, but the purpose is to return a list of all dates of one year and the respective sun hours
    :param year:
    :type year: int
    :param value_lat:
    :type value_lat: float
    :param value_lon:
    :type value_lon: float
    :param month_start: starting month of the wanted list
    :type month_start: int
    :param day_start: startin day of the wanted list of the month
    :type day_start: int
    :param month_end: ending month of the wanted list
    :type month_end: int
    :param day_end: ending day of the wanted list of the month
    :type day_end: int
    :return: List of tupes (Date, respective sun_hours without radiation blockers) containing as many elements as dates of the year
    :rtype: list

    >>> daily_sun_hours_clear_sky_lst_one_year("2000", 0.0, 0.0) #the parameters value_lat and value_lon are checked in the function daily_sun_hours_clear_sky()
    Traceback (most recent call last):
        ...
    TypeError: Use a int as an argument
    >>> daily_sun_hours_clear_sky_lst_one_year(2020, 47.268, 11.393, 1, 1, 1,4) # checked with https://www.timeanddate.com/sun/@0.032,0.052?month=1&year=2020
    [(datetime.date(2020, 1, 1), 8.533333333333333), (datetime.date(2020, 1, 2), 8.55), (datetime.date(2020, 1, 3), 8.566666666666666), (datetime.date(2020, 1, 4), 8.583333333333334)]
    >>> daily_sun_hours_clear_sky_lst_one_year(2000, 0.0, 0.0, 1, 1, 1,4) # checked with https://www.timeanddate.com/sun/@0.032,0.052?month=1&year=2020
    [(datetime.date(2000, 1, 1), 12.116666666666667), (datetime.date(2000, 1, 2), 12.133333333333333), (datetime.date(2000, 1, 3), 12.116666666666667), (datetime.date(2000, 1, 4), 12.133333333333333)]

    """
    import datetime
    if type(year) != int or type(month_start) != int or type(month_end) != int or type(day_start) != int or type(
            day_end) != int:
        raise TypeError("Use a int as an argument")
    date_list = list()
    start_date = datetime.date(year, month_start, day_start)
    end_date = datetime.date(year, month_end, day_end)
    diff = (end_date - start_date).days + 1

    counter = 0
    sum_sun_hours = 0
    for d in range(diff):
        date = start_date + datetime.timedelta(d)
        sun_hours = daily_sun_hours_clear_sky(value_lat, value_lon, date)
        sum_sun_hours += sun_hours
        counter += 1
        date_list.append((date, sun_hours))
    return date_list


def correcting_sun_hour_clear_sky__observed_average(average_sun_hours_observed, lst_sun_hours_clear_sky):
    """
    This function creates a new list containing tuples with (dates, and respective sun_hours on this day) By using the previous created list of sun hours on each date (sequence specified) and the average sun hours on the respective location
    It devides the average sun hours observed of an location by the  means of the sun hours of the sequence (without rediation blocking)
    NOTE!! this makes only sense if List of sun_hours contains all dates!! But um die function to test I use a shorter and artificial list to see if the calculations work
    :param average_sun_hours_observed:
    :type average_sun_hours_observed: float
    :param lst_sun_hours_clear_sky:
    :type lst_sun_hours_clear_sky: list
    :return: List of average sun hours on each date year, containing as many elements as dates of the year
    :rtype: list

    >>> correcting_sun_hour_clear_sky__observed_average(5.0, ((1,15),(2,15),(3,15),(4,15)))
    Traceback (most recent call last):
        ...
    TypeError: Use a list as an argument
    >>> correcting_sun_hour_clear_sky__observed_average(5, ((1,15),(2,15),(3,15),(4,15)))
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> correcting_sun_hour_clear_sky__observed_average(5.0, [(1,7.5),(2,10),(3,15),(4,7.5)])
    [3.75, 5.0, 7.5, 3.75]
    >>> correcting_sun_hour_clear_sky__observed_average(5.0, [(1,15),(2,15),(3,15),(4,15)])
    [5.0, 5.0, 5.0, 5.0]

    """
    float_check(average_sun_hours_observed)
    list_check(lst_sun_hours_clear_sky)

    lst_sun_hour_modeled = list()
    sum_sun_hours = 0
    len_lst = 0
    for e in lst_sun_hours_clear_sky:
        sum_sun_hours += e[1]
        len_lst += 1
    average_sun_hours_clear_sky = sum_sun_hours / len_lst
    proportion_sun_hours_clear_sky_observed = average_sun_hours_observed / average_sun_hours_clear_sky
    for e in lst_sun_hours_clear_sky:
        e = e[1] * proportion_sun_hours_clear_sky_observed
        lst_sun_hour_modeled.append(e)
    return lst_sun_hour_modeled


def max_kwh_needed_output(energy_consumption_year, solar_hours_daily, proportion_own_energy_production, efficiency):
    """
    This function calcualtes the estimated max_needed output based on the avarage sun_hours of each day of the year and location
    and the offset of energyconsumption that is to be covered on every day

    :param energy_consumption_year:
    :type energy_consumption_year: float
    :param solar_hours_daily: list of daily hours based on location -> 365 entries
    :type solar_hours_daily: list
    :param proportion_own_energy_production:
    :type proportion_own_energy_production: float
    :param efficiency:
    :type efficiency: float
    :return: the amount of kwH that the solar panel must produce in order to meet the requirments specified
    :rtype: float

    >>> max_kwh_needed_output(365.0, [10,9,8,7,6,5,4,3,2,1], 1, 1.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> max_kwh_needed_output(365, [10,9,8,7,6,5,4,3,2,1], 1.0, 1.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> max_kwh_needed_output(365.0, [10,9,8,7,6,5,4,3,2,1], 1.0, "1.0")
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> max_kwh_needed_output(365.0, (10,9,8,7,6,5,4,3,2,1), 1.0, 1.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a list as an argument
    >>> max_kwh_needed_output(365.0, [9,8,7,6,5,4,3,2,1], 1.0, 1.0)
    1.0
    >>> max_kwh_needed_output(365.0, [10,9,8,7,6,5,4,3,2,1], 1.0, 0.5)
    2.0

    """
    float_check(energy_consumption_year)
    float_check(proportion_own_energy_production)
    float_check(efficiency)
    list_check(solar_hours_daily)

    daily_energy_consumption = energy_consumption_year / 365
    max_kwh_needed_output = 0
    for i in solar_hours_daily:
        daily_solar_output = daily_energy_consumption / i
        if daily_solar_output > max_kwh_needed_output:
            max_kwh_needed_output = daily_solar_output
    max_kwh_needed_output = max_kwh_needed_output * (proportion_own_energy_production / efficiency)
    return max_kwh_needed_output


def needed_solar_area_size(max_output, output_kwp_per_m2):
    """
    This function calcualtes the estimated solar_panel_area that is needed to cover specified perceptage of the energy concumption

    :param max_output
    :type max_output: float
    :param output_kwp_per_m2:
    :type output_kwp_per_m2: float
    :return: area needed to cover specified proportion of energy consumption in m^2
    :rtype: float

    >>> needed_solar_area_size(1, 0.1)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> needed_solar_area_size(1.0, True)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument

    >>> needed_solar_area_size(1.0, 0.1)
    10.0
    >>> needed_solar_area_size(10.0, 2.0)
    5.0

    """
    float_check(max_output)
    float_check(output_kwp_per_m2)
    solar_penal_area = max_output / output_kwp_per_m2
    return solar_penal_area


def enough_roof_area(available_roof_area, needed_roof_area):
    """
    This function calculates if enough roof area is available

    :param available_roof_area:
    :type available_roof_area: float
    :param needed_roof_area:
    :type needed_roof_area: float
    :return: is enough area avaliable to cover the required energy production YES/NO
    :rtype: bool
    >>> enough_roof_area(1, 1.5)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> enough_roof_area(1.0, "1.5")
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> enough_roof_area(10.0, 5.0)
    True
    >>> enough_roof_area(2.0, 2.001)
    False
    >>> enough_roof_area(2.0, 2.0)
    True

    """
    float_check(available_roof_area)
    float_check(needed_roof_area)
    if available_roof_area >= needed_roof_area:
        enough_area = True
    else:
        enough_area = False
    return enough_area


def energy_savings_kw_h(energy_consumption_year, solar_hours_daily, output_solar, efficiency):
    """
    This function calcualtes the energy savings of using Solar_energy. It assumes that the energy consumption is equally distributed among each day and during the time the sun is shining
    and that the solar output cannot be  fed into the power grid thus cannot be  greater than the the daily consumed energy
    :param energy_consumption_year: in kwH
    :type energy_consumption_year: float
    :param solar_hours_daily: as list avarage daily hours depending on locotation and date
    :type solar_hours_daily: list
    :param output_solar: in kwH
    :type output_solar: float
    :param efficiency: of the solar panals
    :type efficiency: float
    :return: number of how much kwH per year are saved thorugh using the solar energy
    :rtype: float

    >>> energy_savings_kw_h(365, [1 for i in range(365)], 1.0, 1.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> energy_savings_kw_h(365.0, [1 for i in range(365)], None, 1.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> energy_savings_kw_h(365.0, (1 for i in range(365)), 2.0, 1.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a list as an argument
    >>> energy_savings_kw_h(365.0, (1 for i in range(365)), 2.0, "a")
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> energy_savings_kw_h(365.0, [1 for i in range(365)], 1.0, 1.0)
    365.0
    >>> energy_savings_kw_h(1000.0, [1 for i in range(365)], 1.0, 1.0)
    365.0
    >>> energy_savings_kw_h(365*5.0, [i for i in range(365)], 1.0, 1.0) == 365*5-15
    True

    """
    float_check(energy_consumption_year)
    float_check(output_solar)
    float_check(efficiency)
    list_check(solar_hours_daily)

    savings = 0
    daily_energy_consumption = energy_consumption_year / 365
    for e in solar_hours_daily:
        daily_save = e * output_solar * efficiency
        if daily_save > daily_energy_consumption:
            savings += daily_energy_consumption
        else:
            savings += daily_save
    return savings


def co2_production_no_solar(energy_consumption_year, co2_per_kwh_kg, eco_energy_bool):
    """
    TZhis function calculates the co2 production due to the energy consumption of an hole year
    :param energy_consumption_year:
    :type energy_consumption_year: float
    :param co2_per_kwh_kg:
    :type co2_per_kwh_kg: float
    :param eco_energy_bool:
    :type eco_energy_bool: bool
    :return: the amount of CO2 produced through energy consumtion in kg
    :rtype: float

    >>> co2_production_no_solar(100, 1.0, False)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> co2_production_no_solar(100.0, 1, False)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> co2_production_no_solar(100.0, 1.0, "False")
    Traceback (most recent call last):
        ...
    TypeError: Use a bool as argument!
    >>> co2_production_no_solar(100.0, 1.0, False)
    100.0
    >>> co2_production_no_solar(50.0, 2.0, True)
    10.0

    """
    float_check(energy_consumption_year)
    float_check(co2_per_kwh_kg)
    bool_check(eco_energy_bool)

    oeko_co2_per_kw_h_proportion = 0.1  # source: https://www.co2online.de/energie-sparen/strom-sparen/strom-sparen-stromspartipps/was-ist-echter-oekostrom/
    if eco_energy_bool:
        co2_production_no_solar = energy_consumption_year * co2_per_kwh_kg * oeko_co2_per_kw_h_proportion
    else:
        co2_production_no_solar = energy_consumption_year * co2_per_kwh_kg
    return co2_production_no_solar


def co2_savings_sol(co2_production_no_solar, energy_consumption_year, energy_savings_solar, co2_solar_per_kwh):
    """
    This function calculates the amount of saved CO2 due to using solar energy
    :param co2_production_no_solar:
    :type co2_production_no_solar: float
    :param energy_consumption_year:
    :type energy_consumption_year: float
    :param energy_savings_solar:
    :type energy_savings_solar: float
    :param co2_solar_per_kwh:
    :type co2_solar_per_kwh: float
    :return: Amount of KG saved by using solar panels
    :rtype: float

    >>> co2_savings_sol(100.0, 100.0, 50., 5)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> co2_savings_sol(100, 100, 50.0, 5.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> co2_savings_sol(100.0, 100.0, 50, 5.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> co2_savings_sol(100.0, 100.0, 50.0, 5)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> co2_savings_sol(100.0, 100.0, 50.0, 0.5)
    25.0
    >>> co2_savings_sol(50.0, 200.0, 200.0, 0.1)
    30.0

    """
    float_check(co2_production_no_solar)
    float_check(energy_consumption_year)
    float_check(energy_savings_solar)
    float_check(co2_solar_per_kwh)

    co2_per_kwh = co2_production_no_solar / energy_consumption_year
    co2_savings_sol = -energy_savings_solar * co2_solar_per_kwh + energy_savings_solar * co2_per_kwh
    return co2_savings_sol


def years_to_credit_free(credit_volume, interest_rate, pay_back_rate):
    """
    This function calculates the time needed in years to pay back a credit, interest rates and pay back rates are yearly
    :param credit_volume:
    :type credit_volume: float
    :param interest_rate:
    :type interest_rate: float
    :param pay_back_rate:
    :type pay_back_rate: float
    :return: years
    :rtype: int

    >>> years_to_credit_free(100, 0.2, 13.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> years_to_credit_free(100.0, 2, 13.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> years_to_credit_free(100.0, 0.2, 13)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument

    >>> years_to_credit_free(100.0, 2.0, 13.1)
    Traceback (most recent call last):
        ...
    AssertionError: You cannot afford this credit with this Pay Back Rate
    >>> years_to_credit_free(200.0, 0.01, 202.00)
    1
    >>> years_to_credit_free(200.0, 0.01, 201.99)
    2

    """
    float_check(credit_volume)
    float_check(interest_rate)
    float_check(pay_back_rate)

    new_volume = credit_volume
    years = 0
    if new_volume * interest_rate >= pay_back_rate:
        raise AssertionError("You cannot afford this credit with this Pay Back Rate")
    else:
        while new_volume > 0:
            new_volume = new_volume * (1 + interest_rate) - pay_back_rate
            years += 1
        return years


def years_to_armortization(investment_pv, credit, interest_rate, yearly_costs, cost_savings_solar):
    """
    THis function retures the number of years after the solar panales are profitable compared to not having them
    :param investment_pv:
    :type investment_pv: float
    :param credit:
    :type credit: float
    :param interest_rate:
    :type interest_rate: float
    :param yearly_costs:
    :type yearly_costs: float
    :param cost_savings_solar:
    :type cost_savings_solar: float
    :return: a Tuple with the (Armortization years, sum of interest, List of costs without solar energy, List of costs with solar energy)
    :rtype: tuple (float, float, list, list)
    >>> years_to_armortization(10, 10.0, 10.0, 10.0, 10.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> years_to_armortization(10.0, 10, 10.0, 10.0, 10.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> years_to_armortization(10.0, 10.0, 10, 10.0, 10.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> years_to_armortization(10.0, 10.0, 10.0, 10, 10.0)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> years_to_armortization(10.0, 10.0, 10.0, 10.0, 10)
    Traceback (most recent call last):
        ...
    TypeError: Use a float as an argument
    >>> years_to_armortization(1000.0, 0.0, 0.05, 100.0, 100.0)
    (5, 0, [0.0, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0], [1000.0, 900.0, 800.0, 700.0, 600.0, 500.0, 400.0, 300.0])
    >>> years_to_armortization(1000.0, 500.0, 0.05, 200.0, 200.0)
    (3, 45.0, [0.0, 200.0, 400.0, 600.0, 800.0], [1000.0, 825.0, 640.0, 445.0, 245.0])

    """
    float_check(investment_pv)
    float_check(credit)
    float_check(interest_rate)
    float_check(yearly_costs)
    float_check(cost_savings_solar)

    yearly_sum_solar_costs = investment_pv
    yearly_sum_energy_cons = 0.0
    amortization_years = 0
    interest_sum = 0
    lst_compare_solar_costs = [yearly_sum_solar_costs]
    lst_compare_no_solar_costs = [yearly_sum_energy_cons]
    while yearly_sum_energy_cons < 2 * yearly_sum_solar_costs:
        if yearly_sum_energy_cons < yearly_sum_solar_costs:
            amortization_years += 1
        yearly_sum_energy_cons += yearly_costs
        if credit <= 0:
            credit = 0
        else:
            yearly_sum_solar_costs += credit * interest_rate
            interest_sum += credit * interest_rate
            credit -= cost_savings_solar
        yearly_sum_solar_costs -= cost_savings_solar
        lst_compare_no_solar_costs.append(yearly_sum_energy_cons)
        lst_compare_solar_costs.append(yearly_sum_solar_costs)
        # print("DEBUG: ", yearly_sum_energy_cons,yearly_sum_solar_costs
    return amortization_years, interest_sum, lst_compare_no_solar_costs, lst_compare_solar_costs


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
