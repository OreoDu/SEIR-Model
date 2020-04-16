# SEIR-Model
Prediction of COVID-19 Epidemic Situation Based on Improved SEIR Model

### Overview
In this project, I mainly use covid-19 data(<u>[data sources](https://www.mhlw.go.jp/stf/newpage_10651.html)</u>) from Japan in April to predict the possible development of epidemic situation in the next 100 days based on SEIR model.

### Model description
The SEIR models the flows of people between four states:
1) Susceptible people (**S(t)**), 
2) Infected people with symptons (**I(t)**), 
3) Infected people but in incubation period (**E(t)**),
4) Recovered people (**R(t)**). 

Based on the coronavirus's infectious characteristics and the current isolation measures, I further improve this model and add more states which is more suitable for the actual situation of the epidemic development: 
1) Isolated and infected people in incubation period (**Eq(t)**), 
2) Isolated and susceptible people and isolated (**Sq(t)**),
3) Isolated and infected people　with symptons (**H(t)**).
4) The people died.(**D(t)**)

Based on those, we can have some assumptions:
1) All the people can be susceptible.
2) The people who infected and was in incubation period can infect others and also they can self-healing in a specific period. And the infectious ability of those people is the same as the people who already have symptons.
3) Once the people being isolated, they cannot get infected or infect others.
4) The people who were recoverd can not be infected again.
5) Only those who get infected and have symptons can be died.
6) All people who have been tested by PCR need to be isolated for 14 days.


The flows between those states canbe showed as follow:
- ![Flows](/Flows.PNG "Flows between the states")

The parameters in the picture:
- The contact rate: c = 2
- The rate of releasing form being isolated: v = 1/14
- The isolation rate of people who didn't have infection symptons: iso = 0.000001
- The isolation rate of people who already have infection symptons:iso_i = 0.13
- The infection rate of COVID-19: b = 0.00000000205
- The cure rate of people who are not isolated: r = 0.014
- The cure rate of people who were isolated already: iso_r = 0.07
- The death rate: d = 0.00027
- The possibility of people geting infection symptoms during incubation period who haven't been isolated:s = 1/7
- The possibility of people geting infection symptoms during incubation period who haven been isolated: iso_s = 0.13

So according to SEIR model, we can have the following formulas:

$$ \frac{dS}{dt} = v·Sq-\left(I+E\right)·S·c·\left(iso·\left(1-b\right)+b\right)$$

$$ \frac{dE}{dt} = b·(I+E)·S·(1-iso)·c -E·s - r·E $$

$$ \frac{dI}{dt} = E·s - I·iso_i - I·r - I·d $$

$$ \frac{dR}{dt} = I·r + r·E + H·iso_r + Eq·iso_r $$

$$ \frac{dSq}{dt} = (I+E)·S·c·iso·(1-b) - v·Sq $$

$$ \frac{dEq}{dt} = (I+E)·b·c·iso·S - Eq·iso_s - Eq·iso_r $$

$$ \frac{dH}{dt} = Eq·iso_s + I·iso_i - H·d - H·iso_r $$

$$ \frac{dD}{dt} = H·d+I·d $$
    

