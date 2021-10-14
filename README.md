![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome USER_NAME,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

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

----------------------------------------------------------------------
# Four in a row

The game four in a row is played on a standing board with seven columns of six rows where two players alternate dropping
a tile into a column of their choice. The tile ends up at the bottom free row of the chosen column. The goal of the game 
is to get four of your own tiles in a row either vertically, horizontally or diagonally.

This is a command-line version of the game, suitable to learn how to play or to entertain.

## Features 

A digital representation of the game.
A visual representation of the game.
Two users can play the game.
One user can play against the computer.
Any number of users can watch two computer players play eachother.
Games can be saved and watched again.
Moves can be undone.

### Existing Features



- __A digital representation of the game.__

  Each game is simply stored as a Python list consisting of player1, player2, column nr for move#1, column nr for move#2, ...

- __A visual representation of the game.__

  The game is represented as a ASCII-graphic in the command window, as follows:

 
                  O
            @  O  @
      1  2  3  4  5  6  7    8) 9) 0)

1-7 represents the columns 8) - 0) non-move commands that can be given, like undo last move, save game, return to start menu.


- __User playing the game__

A human player gives input through entering single digit integers into the command line.



- __Computer playing the game__ 

There is a computer player able to process the digital game representation and make a move. By selecting both player1 & player2
as computers you can watch the computer play itself.


### Features Left to Implement

- Replay saved games

- Different computer players


## Testing 

- By methodically going through the games menus I have managed to run through every option 
  without the program crashing.
  
- By having the computer player play itself 100's of times I am reasonably confident that no
  moves in the game cause any problems.


### Validator Testing 

- Python PEP8 - http://pep8online.com/
- Pylance - https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance

### Unfixed Bugs

- Pylance claims parts of the code in "view_replay()" is unreachable (probably due to me not
  using any kind of type annotation), but running the program shows it indeed is.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits 

In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 