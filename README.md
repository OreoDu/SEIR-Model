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
2) The people who infected and was in incubation period can infect others and also they can self-healing in a specific period.
3) Once the people being isolated, they cannot get infected or infect others.
4) The people who were recoverd can not be infected again.
5) Only those who get infected and have symptons can be died.
6) All people who have been tested by PCR need to be isolated for 14 days.

The flows between those states canbe showed as follow:
![Flows](URL title)
- c = 2 #contact rate
- v = 1/14  #the rate of releasing from being isolated
- iso = 0.000001 #quarantine rate
- iso_i = 0.13 #quarantine rate of infected people
 -b = 0.00000000205 #infection rate
- r = 0.014  #cure rate
- iso_r = 0.07 #cure rate of quarantined people
- d = 0.00027 #fatality rate
- s = 1/7 #the possibility of infection symptoms during incubation period
- iso_s = 0.13 #the possibility of infection symptoms during incubation period who have been isolated
