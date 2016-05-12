[![Build Status](https://travis-ci.org/jreiher2003/Composite.svg?branch=master)](https://travis-ci.org/jreiher2003/Composite)
# Composite 
___


### Tech Stack 
* python 
* flask 
* basic cache
* sqlalchemy
* postgres 
* bootstrap 
* heroku


### This site emphasizes CRUD functionality, AJAX requests, and using API's
_______

#### Page 1 Home or /
**Front page** has a submission form to collect title and ascii art. The app also collects IP addresses and converts them to geoPts of lat, lon which is represented on the map with a marker when you make a post.
**Crud functionality** - this app can create read update and delete

#### Page 2 /ajax
This page uses **ajax requests and api's**.
The api's used are **NY Times, Wikipedia, and Google street maps**
A user puts in an address and a street view picture shows up along with NYT articles about the city and any Wikipedia links about the city or state.

#### Page 3 /api 
This page uses my own **api** that I created from this [site](http://adopt-puppy.herokuapp.com/api ) and this [repo](https://github.com/jreiher2003/Puppy-Adoption).  It is a simple example of how to create and use an api in this type of tech stack.  