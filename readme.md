# COVID-19 Vaccination Eligibility Checker
### Overview
This command-line interface (CLI) application serves as an eligibility checker for determining when individuals are eligible for the COVID-19 vaccination based on the Australian government's vaccine rollout phases. Users can follow a set of prompts to input their demographic information and receive information on their eligibility phase.

The eligibility phases are organised as follows:

### Groups in each Phase of Vaccine Rollout
| Phase | Group                                                                                                                                                                                                                                                                                                                                                  |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1a    | Quarantine and border workers; Frontline health care workers sub-groups; Aged care and disability staff; Aged care and disability care residents;                                                                                                                                                                                                      |
| 1b    | Elderly adults aged 80 years and over; Elderly adults aged 70-79 years; Other health care workers; Aboriginal and Torres Strait Islander people > 55; Younger adults with an underlying medical condition, including those with a disability; Critical and high-risk workers including defense, police, fire, emergency services, and meat processing; |
| 2a    | Adults aged 60-69 years; Adults aged 50-59 years; Aboriginal and Torres Strait Islander people 18-54; Other critical and high-risk workers;                                                                                                                                                                                                            |
| 2b    | Balance of the adult population; Catch up any unvaccinated Australians from previous phases;                                                                                                                                                                                                                                                           |
| 3     | < 18 if recommended (Pfizer vaccine only)                                                                                                                                                                                                                                                                                                              |

For more information on the COVID-19 vaccine rollout in Australia, you can refer to [When will I get a COVID-19 vaccine?](https://www.health.gov.au/our-work/covid-19-vaccines/who-can-get-vaccinated). Please note that the information on this website is subject to change. *The information provided in the above table was last checked on 02/04/2021.*

----

### Deployment

To run the application, follow these steps:

 1. Open a terminal and navigate to the root folder of the project.
 2. Run the following command:
 
 ```python
 python vaccination_phase.py
```

This will initiate the application, prompting you to enter the required information to determine your eligibility for the COVID-19 vaccination. Please make sure to input accurate details to receive the most relevant information about your eligibility phase.