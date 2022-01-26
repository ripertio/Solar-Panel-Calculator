# Solar Panel Calculator

Author: Richard Kempert
Semester: 21W

## Motivation
The task is related to solar panels, how much energy can be generated with which area at which investment costs.
Friends of mine are currently thinking about installing solar panels on their roof. My goal was to help them in their decision if they should install solar panels or not.

## Reflexion on implementation
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
