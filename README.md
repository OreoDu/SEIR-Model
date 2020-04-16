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

![Flows](/Flows.PNG "Flows between the states")

The parameters in the picture:
- The contact rate: c = 2
- The rate of releasing form being isolated: v = 1/14
- The isolation rate of people who didn't have infection symptons: iso = 0.000001
- The isolation rate of people who already have infection symptons:iso_i = 0.037
- The infection rate of COVID-19: b = 0.00000000205
- The cure rate of people who are not isolated: r = 0.014
- The cure rate of people who were isolated already: iso_r = 0.07
- The death rate: d = 0.00027
- The possibility of people geting infection symptoms during incubation period who haven't been isolated:s = 1/7
- The possibility of people geting infection symptoms during incubation period who haven been isolated: iso_s = 0.13
(Some of the value of parameters referenced <u>[this papper](http://www.zjujournals.com/med/CN/10.3785/j.issn.1008-9292.2020.02.05)</u>. I changed a little according to the control measures taken by the government now in Japan. For example,the isolation rate is much lower and also the number of PCR test is much smaller which causes can not be treated in time.)


So according to SEIR model, we can have the following formulas:

dS/dt = v·Sq-(I+E)·S·c·(iso·(1-b)+b)

dE/dt = b·(I+E)·S·(1-iso)·c -E·s - r·E

dI/dt = E·s - I·iso_i - I·r - I·d

dR/dt = I·r + r·E + H·iso_r + Eq·iso_r

dSq/dt = (I+E)·S·c·iso·(1-b) - v·Sq 

dEq/dt = (I+E)·b·c·iso·S - Eq·iso_s - Eq·iso_r

dH/dt = Eq·iso_s + I·iso_i - H·d - H·iso_r

dD/dt = H·d+I·d


Then we have to give the initial value:
(According to the data on April 1st in Japan.)

N0 = 127749000 #The population of Japan

N[0] = N0

E[0] = 1290

S[0] = N[0] - E[0] - I[0] - R[0] - D[0] - Sq[0] -Eq[0]

I[0] = 1594

Eq[0] = 2107

Sq[0] = 29895

R[0] = 456

H[0] = 60

D[0] = 57

### The results of different control measures.
So now we can see the prediction of trends in epidemic in the next 30 days if the government still take the normal control measures. The infected people will reach 100,000 and keep increasing.
![Figure](/Figure_withnormalcontrol.png "If the government take the normal control measures")

#### The impact of contact rate:
Recently, the Japanese government announced a state of emergency and began to take necessary prevention and control measures, such as restricting gatherings, theater performances and other crowd gathering activities. These prevention and control measures are essentially to reduce the contact rate of susceptible people. Under normal control straties, it is assumed that the current contact rate is 2. By increasing the exposure rate to simulate the trend of covid-19.The figure below shows a simulation of the epidemic with a higher and a lower probability of contact.It is found that the strict control has a good inhibitory effect on the large-scale development of current epidemic. If there is no prevention and control isolation, the number of infected people will increase rapidly.

![Figure](/Figure_the%20impact%20of%20control.png "The impact of contact rate")

#### The impact of isolation rate:
In order to control the epidemic situation, strict medical tracing and isolation are needed. This time, the effect of tracking isolation measures was simulated by analyzing the impact of the decrease and increase of tracking isolation ratio. As shown in the figure below, when the isolation ratio drops to 0.5 times, the rising rate and peak value of the number of infected people will increase. When the ratio of isolation increased, the number of infected people gradually decreased. It can be seen that strict medical tracking and isolation is an effective ways to prevent the development of the epidemic.

![Figure](//Figure_the%20impact%20of%20isolation.png "The impact of isolation rate")

    

