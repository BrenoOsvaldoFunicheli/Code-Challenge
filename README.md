# Code-Challenge
Code Challenge

This repository is a code challenge with the purpose of evaluating knowledge of python development.

### Challenge Requirements

* bring weather forecast information
* Evaluate based on a humidity rule which days of the week a person needs to take the umbrella
* Python Code
* Use Rest API

### Applied Knowledge

* Rest API consumption
* Clean Code
* Pandas Processing
* OOP
* 12-factor

### Using

 The application was built for use in a module, so it can be used both iteratively and as a library.
 
#### Basic Use

``` python

from main import run


run()

```

#### Module Use 

The script below demonstrates the use of classes created that abstract system objects. 

``` python


p = ParamAuth(app_id='api_key', url='base_url',
                  city='id_city')
a = Authentication(param_obj=p)
ap = APIConsumer(a)
f = Forecaster(ap)
lst_umbrella = f.get_umbrella_day()
days = ", ".join(lst_umbrella)

```

As the API is based on authentication by a specific key, two ways were considered for its consumption, one that takes 12-factor into account and centralizes the information in an .env file and another that values the OOP demonstrated in the previous code.
It should be noted that the first code is executed automatically as long as the .env is properly configured.
 
