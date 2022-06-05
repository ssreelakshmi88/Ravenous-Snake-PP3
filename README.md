
# Ravenous Snake

“Ravenous Snake” is a spin-off version of the popular video game genre developed in the late 90’s. The game draws its concept from the original game which is to manoeuvre the snake towards its food. The snake will grow in size proportional to its food consumption and this must be achieved without the snake touching any part of its body or the screen edge. The bigger the snake gets higher will be the user score. This game has been developed predominantly based on Python. 

## UX (User Experience)
 
###   User Stories

  - It is a classic game that helps users to assess their surroundings and thereby gives the users a magnificent chance to learn spatial awareness.
  - Snake game also has some educational uses apart from fun. The game teaches the children patience and also makes them understand that practice makes perfect when it comes to learning new skills.
  
####   First time Visitor Goals

- As first time visitors, they must understand the rules to play the game.

- As the game progresses and ends, the users can see the current and final score.

## Coding Languages Used

1. Python

## Wireframes

1. Wireframe of the welcome page

![Snake game_Welcome Page](https://user-images.githubusercontent.com/97182442/172071973-64d8d25e-276f-432c-9ab1-58816d929ed5.png)


2. Wireframe of the game page


![Snake game_Game Page](https://user-images.githubusercontent.com/97182442/172071975-96ec5d2b-0ab4-4e10-971c-0a889da471b1.png)


## Flowchart

![Flowchart](https://user-images.githubusercontent.com/97182442/172071963-be0aba69-1e37-4abd-ac07-69905b2aa63c.png)



## Features

### Existing features

- The start screen will display the snake and its target at stationary positions. The snake will start moving in the direction as indicated by the user via the arrow keys.

- At any point, the space-bar key can be tapped to toggle between pause and play.

- Game can be exited at any time by tapping the ESC key.

- As the snake hits it first target it will grow in size and a second target randomly pops up in the screen. 

- The game will continue as long as the user manoeuvres the snake without touching any part of its body or when it hits the screen borders. 


## Testing

For this project I have done the following tests:

- Passed the code through a PEP8 liner and confirmed there are no errors.

- Using directional key inputs'.

- Tested in my local terminal and Code Institute Heroku terminal.

#### Validator testing

- PEP8
 No errors were found in PEP8online.com
 
###  Deployment

This project was deployed using Code Insitute's mock terminal for Heroku.

**Steps for deployment**

- Fork or clone the repository.
- Create a new Heroku app.
- Set the buildbacks to Python and NodeJS in that order.
- Link the Heroku app to the repository.
- Click on **Deploy**

## Credits




When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
