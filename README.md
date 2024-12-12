# BOOTCHAMP  

###### THE TRIALS AND TRIBULATIONS OF JR SOFTWARE DEVELOPERS

BOOTCHAMP is a forum for jr software developers to share projects, inspirational stories, cautionary tales, and candid advice. Though BOOTCHAMP reflects UX norms established by social media it takes more after blogs and forums. It took a three week sprint to establish scope, devise and prioritise user stories, and deliver the MVP.   
  
Said MVP is a web application where users can share experiences starting out in software development by way of putting posts to a forum. A user can view a list of posts on the home page, and can click on each post to view more detail. Signed in users can create, edit and delete posts. Signed in users can comment on posts, and edit and delete those comments. Each registered user gets a profile with their post and comment history which they can update, but not delete.  Bootstrap toasts notify users of changes made and Django all-auth handles user registration securely. 

### TECH STACK  

###### LANGUAGES

- HTML
- CSS
- JS
- PYTHON

###### SERVICES

- HEROKU - web application hosting service
- NEONDB - database service
- CLOUDINARY - image hosting service
- GOOGLEFONTS - Jockey One and Open Sans fonts 
- FONTAWESOME - Used for icons
 
###### LIBRARIES AND FRAMEWORKS

- BOOTSTRAP - A library of CSS class for quick styling
- DJANGO - Python framework for full stack applications
- DJANGO CRISPY FORMS - Bootstrap compatible form layouts
- WHITENOISE - serving static files dynamically
- DJANGO ALLAUTH - authorisation and secure site access

###### TOOLS

- GITHUB PROJECTS - information radiators
- BALSAMIQ - tool for creating wireframes
- LUCIDCHART - tool for creating entity relationship diagrams
  
### DESIGN  

The user stories establish the CRUD functionality of the website. Posts, Comments, Profiles and Likes each have a data model that relates to a built in User model. The entity relationships laid out below includes some features that were not implemented in sprint 1.  

![ERD document](static/images/readme/erd.png/)  

BOOTCHAMP was intended to share a layout with contemporary social media

![wireframes](static/images/readme/home(loggedOut).png)  

![mobile wireframes](static/images/readme/mobilePostView.png)    

###### MUST HAVE USER STORIES  

You can visit the [Project board](https://github.com/users/Sjwilhelms/projects/6) here. 
  
Manually tested and passed

1. as a site user I can view a list of posts so that I can survey the sites content at a glance
1. as a site user I can view each post in detail so that I can engage with the content
1. as a site user I can view the author of each posts profile so that I can see more about them, including their post and commments
1. as a site user I can register an account so that I can have my own profile and contribute to the forum 
1. as a signed in site user I can create, edit, and/or delete a post so that I can contribute to the forum
1. as a signed in site user I can comment on a post and edit/delete said comment so that I can interact with other users
1. as a signed in site user I can update my profile biography
1. as a signed in site user I can get feedback whenever I makea contribution or a change so that I can use the website confidently  

###### SHOULD HAVE USER STORIES  

Not implemented

1. as a site user I can click on an image for full screen so that I can see it in detail
1. as a site user I can scroll through a dynamically paginated 'endless' list of posts so that my load times are kept short
1. as a site user I can search the site from the navbar so I can search as opposed to browse
1. as a signed in site user I can leave a like on a comment or post so that I can interact with other users
1. as a signed in site user I can review/moderate user content so as to filter for inappropriate content
1. as a signed in site user I can categorise posts so that I can engage with a particular theme
1. as a signed in site user I can create categories to assign posts so that I can 

###### THE SECOND ITERATION
  
BOOTCHAMP will have dynamic pagination using AJAX logic; a like button that totals on the recipients profile; full screen viewer for images; and a search bar. 

BOOTCHAMP's test posts dilute the stated goal of the project. Better targeted test users and more semantic forms would help to correct this lilt.

It will also have another iteration of styling to give the project more flavour and to fully eliminate mobile scrolling from all forms throughout the project. . 

### DEPLOYMENT

### TESTING

###### VALIDATION

HTML and CSS Validated with W3Schools. All views passed validation except 2 detailed below:  

accounts/signup 

![sign up page error message](static/images/readme/w3%20validation%20auth%20--%20register.png)

post_detail/

![post detail error message](static/images/readme/post%20detail%20error%20message.png)

I used page speed to validate my page for accessibility and performance on mobile and desktop.  

Mobile:

![Mobile performance](static/images/readme/mobile%20performance.png)  
  
Desktop:  

![Desktop performance](static/images/readme/desktop%20performance.png)  

###### USER TESTING

The project has had a raft of manual testing from the developer and from other users.

###### AUTOMATIC TESTING

The next iteration of BOOTCHAMP will feature automatic testing.

### REFERENCES

