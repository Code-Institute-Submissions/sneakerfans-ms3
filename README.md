# SNEAKERFANS

![SNEAKERFANSLogo](static/images/logo-black.png)

This project is based on a database for lovers of sneakers. Around the world sneaker collecting and resale is big business. I created SNEAKERFANS with the aim of drawing this community together and to allow them to create and upload their own favourite sneakers to the website for others to see. I would love to add a posts section in single page layout in the style of facebook and I believe it would unite millions of sneaker lovers around the world. No such site currently exists. This feature could be added on a trial basis for future releases. For now the site is purely a database site that allows users to log in, create data, read data, update data and edit and delete their own data.

There is also the opportunity for businesses to to able to sign up for a fee and access data from a custom dashboard similar to google analytics to see what sneakers are trending and what styles are most popular. This would allow businesses such as store owners to stock up on the most popular brands at the right times of the year and increase their annual sales. For this project time constraints did not allow me to fully explore this option. But it is something I would like to add in the future.

I grew up playing basketball as a teenager in the Michael Air Jordan era of the 1990's. There is no feeling like that of opening a new pair of Air Jordans and to this day decades later I still collect basketball sneakers. 1990s retro releases are my favourites. When I was brainstorming ideas for this milestone project a sneaker database was a no brainer for me. It is a site I would use if it existed and seeing what ideas other users have on sneakers would keep me coming back daily.

I have always loved the simplicity of the Nike website, black and white are the main themes and the sneakers do the talking so there are no other distractions or gimmicks. SNEAKERFANS is heavily influenced by the [Nike](https://www.nike.com/ie/) website. 
I did not use any fancy fonts or background colors and opted to use the default sans serif font and white page body with a black navigation bar and footer to see how nice I could make the site while just using the basics. Black and white is the main theme with some dashes of red and orange text. These are prominent themes in some of the most classic sneaker colorways. Such as the holy grail of all retro sneakers The [Air Jordan 3](https://sneakernews.com/wp-content/uploads/2021/05/Air-Jordan-3-Cardinal-2022.jpg)

The website uses HTML and CSS and Javascript in the front end. With my main css framework library being materialize.css and my Javacript framework is jquery CDN. I have also incorporated the use of the font awesome icons CDN for all icons. In the backend flask is used and jinja templating is used to inject data to the HTML. My chosen database is MongoDB.

## [View Live Project](https://ms3-sneakerfans.herokuapp.com/)

![SNEAKERFANS](wireframes/responsive.png)

# CONTENT QUICK LINKS
## [UX](#wireframes)
## [FEATURES](#available-features)
## [SITEMAP](#sitemap-layout)
## [DATABASE](#database-schema)
## [SECURITY](#security-features)
## [TECHNOLOGIES](#technologies-used)
## [TESTING](#testing-steps)
## [DEPLOYMENT](#deployment-process)
## [CREDITS](#code-credits)
## [ACKNOWLEDGEMENTS](#my-acknowledgements)
## [DISCLAIMER](#my-disclaimer)

# UX

## Wireframes:
My initial wireframes and database schemas were sketched on paper and when I was happy I was going in the correct direction I used [Balsamiq](https://balsamiq.com/wireframes/) to finalise my mockups for the front end. For my database schema I used [db diagram](https://dbdiagram.io/). 
The main inspiration for my website is from the global sneaker giant [nike.com](https://www.nike.com/ie/).  All wireframes can be seen in the links below.

* [Home Not Logged In](wireframes/home1.png)
* [Home Logged In](wireframes/home2.png)
* [Browse Collection](wireframes/browse.png)
* [My Sneakers Profile Page](wireframes/profile.png)
* [Add/Edit Sneakers](wireframes/add.png)
* [Manage Categories](wireframes/manage_categories.png)
* [Add Categories](wireframes/add_category.png)
* [Full Description Page](wireframes/full.png)
* [Log In Page](wireframes/login.png)
* [Log Out Page](wireframes/logout.png)
* [Sign Up Page](wireframes/signup.png)

* [Database Schema](wireframes/schema.png)


## User Stories:
1. **As a fan of new and retro sneakers I am seeking a website that allows me to search sneakers as well as add my own ideas to the website**

2. **As a sneaker collector I would like to add images and descriptions of my collection for others to see**

3. **As the website owner I would like to create a community of sneaker lovers who can share images and information on popular and extremely rare sneakers**

4. **As the website owner I would also like to create a revenue stream to keep growing the site from advertising from sneaker brands**(Future release)

5. **As a sneaker retailer I would like to log into a website that allows me to see what sneakers are currently fan favourites so we can stock up on popular items to increase profits** (Future release feature)

## Strategy:
### What am I making?
A website/app that offers users to sign up/ Login/ Read data from other users/ Write data to the database/ view, edit and delete their own content on their profile page. The site will create a sneaker community while also allowing businesses to see what styles are most popular to increase revenue.

### Website business goals
1. Create a community of sneakerfans 
1. Allow businesses to sign up for a monthly fee to collect data and feedback on users sneaker preferences 
1. Increase social media and website traffic with the aim of creating revenue from advertising from the major sneaker brands.

### Website target audience
1. Sneaker lovers and collectors
1. Sneaker resellers
1. Sneaker retailers

### User value
1. Sneaker lovers and collectors will gain a positive emotional experience from using the site and they can search the entire database to find retro sneakers they had forgotton about that will bring back memories and also encourage them to upload their own favourite sneakers.
1. Retailers and resellers can see exactly what sneakers are the most popular and at what times of the year they need to stock up on popular items to increase their revenue.

### What users can expect
1. An easy to navigate no fuss website that is pleasant to use.
1. Easy to sign up quickly and begin browsing and adding data to the website.
1. The ability to edit and delete uploads to their own profile.
1. The ability to read and learn about rare sneakers uploaded to the database by other users.

### What is worth doing
1. A simple sign up form 
1. A simple log in form 
1. A clean profile page
1. A home page that shows 6 random collections from the database so users can see fresh content each time they log in.
1. A simple user edit form 
1. Give users the ability to delete their own data
1. A search box to allow users to enter keywords based on database key values so users can browse the entire database efficiently

### What makes it a good experience
1. Simple outlay. 
1. clean images placed in materilize image cards of the same heights.
1. Familar simple navigation
1. Lots of great information on rare sneakers 


## Scope:

### Features for this release
1. Sign up form.
1. Log in form.
1. User edit form. 
1. User delete functionality.
1. Clickable image cards to show full sneaker descriptions
1. Search functionality to browse the entire database.
1. Call to action buttons based on information hierarchy.
1. Social media links.

### User requirements
1. The ability to read and learn about rare sneakers
1. The ability to create content and add to the website database.
1. The ability to edit content belonging to that user.
1. The ability to delete content belonging to that user.
1. The ability to follow the brand on social media. 
1. The ability to view images.

### How we will achieve these requirements
1. By adding collections to the mongodb database that the user can access through forms.
1. By adding attractive image cards and simple styling.
1. By implementing appropriate user forms.
1. By implementing access to parts of the site otherwise hidden for non registered users.
1. Appropriate social links in the footer.
1. Using an attractive hero image and branding on the home page and show a selection of fan favourite sneakers.

## Structure:

### Navigation
I have implemented a multi page site. A user must sign up or log in to access certain pages
of the website.
Non account holders may access:
1. Home
1. Browse Collection
1. Log In
1. Sign Up
1. The header also contains the company logo which has a return to home link.

Account holders will gain additonal access to:
1. My Sneakers - (profile page to show all of user's database entries)
1. Add Sneakers - (form to allow user to write to database)
1. Log Out

Admin will gain access to:
1. Manage Categories - (Admin can add or delete categories)

I have used a fixed navigation bar to allow users to move to any other section from their current section. Navigation has been kept simple and obvious. There are also call to action buttons and text to encourage new visitors to create an account. 

## Skeleton:

### Presentation
1. Simple layout.
1. Hero image on home page.
1. Fixed navigation.
1. Consistent layout and theme.

### User conventional tools
1. Clear headings. 
1. Clickable elements clearly labelled. 
1. Easy to read nav bar. 
1. Social media links in the form of clickable icons in the footer. 

### Progressive disclosure
I have placed the priority content on the home page so the user sees this first.
I have arranged the supporting content in order of priority in additional sections. 
Each section links to the most important items to engage users and encourage a conversion
in the form of a new user registering an account.

### Elements that have priority
1. Navigation menu with fixed scrolling.
1. Clickable logo with return to home link.
1. Image cards of fixed height.
1. Call to action buttons and links to encourage a sign up. 
1. Social media links.

## Surface

### Colors
The website is inspired by [Nike](https://www.nike.com/ie/). I always loved the simplicity of their website. I set out to try and make the website as enticing as possible while using as little styling as possible. I stuck with the basic sans serif font and white body background. My navbar and footer are also black with white text. The image cards text have some orange colors and sign up links are red. These colors are inspired by both the nike website and one the most iconic sneakers of all time
The [Air Jordan 3](https://sneakernews.com/wp-content/uploads/2021/05/Air-Jordan-3-Cardinal-2022.jpg).

### Fonts
For all fonts I kept things simple with the default sans serif. I added some underlines to my page headings and the simplicity seems to suit the style I wanted for the website.

### Images 
The home page uses a hero image of a pair of Air Jordan Sneakers on feet. The image is clean and
emotive and sets the tone for the website. All other images come from database entries from users. I have created neat materialize cards of fixed height to display all images with continuity. When the image cards are clicked the user is brought to the full sneaker description page where they can view a larger image of the sneaker. I used some box shadow to help this image pop a little. 
I used photoshop to design the company logo.
I also used photoshop for the error handler pages and the are you sure you want to delete modal. 
For these pages I used the Air Jordan Jumpman logo and replaced the basketball with an exclamation
circle icon.

![Error Jumpan](static/images/jumpman.png)

### Order and sequence
1. Navigation order Not logged in - Home/ Browse Collection/ Log In/ Sign Up
1. Navigation order logged in - Home/ Browse Collection/ My Sneakers/ Add Sneakers/ Log Out
1. Home page order - Hero image/ Call to action/ Heading/ Materialize image cards/ Sign Up link
1. Browse Collection order - Heading/  Search Box/ Materialize image cards
1. Log In order - Heading/ Form/ Username input/ Password input/ Submit button
1. Sign Up order - Heading/ Form/ Username input/ Password input/ Submit button
1. My Sneakers order - Heading/ Add Sneakers button link/ Materialize image cards
1. Add Sneakers order - Heading/ Form/ Choose Category input/ Shoe Name input/ Release Year input/ Shoe Description input/ Image url input/ Submit button
1. Footer section order - Social links/ copyright.

### Other themes
1. Use of relevant font awesome icons to add a professional touch.
1. Use of subtle shadows to lift some elements off the page.

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #005b96">




# AVAILABLE FEATURES

### Navbar
The nav bar is fixed to enhance user experience.
The nav bar is made responsive using materialize.css sidenav-trigger class with javascript initialization.

### Home
The home page is laid out with an eye catching hero image and call to action button to encourage users
to sign up to the website. I have used the mongodb aggregate method to display 6 random images from the database in materialize image cards. The image cards content is injected using the jinja templating language. At the bottom of the home page another internal link guides the user to the sign up form.

![SNEAKERFANS](wireframes/responsive.png)

### Browse Collection
The browse collection page allows users to view the full sneaker collection whether they are logged in or not. There is the addition of a search bar which allows users to search all documents in the sneakers collection. Allowing non registered users to access this feature will encourage more sign ups to the website as users will be eager to share their sneaker collections and favourites upon seeing what other users have added.


![SNEAKERFANS](wireframes/browse-collection.png)

### Login 
A simple login form of user name and password allows users to quickly log into the site. The styling of this form has been kept similar to other competitor sites such as [nike.com](https://www.nike.com/ie/). I have also used an eye and slash eye font awesome icon which are toggled using a javascript function to show and hide the password. I initially had issues displaying the icon in the input field but eventually I solved this with some css. [Credit](https://codepen.io/Sohail05/pen/yOpeBm)

![SNEAKERFANS](wireframes/log-in.png)

### Sign Up
A simple sign up form of username and password allows users to easily sign up. I have kept this form 
very simple to reduce bounce rates and to encourage new users to sign up without having to verify email links and passwords. As the site's user collection grows I may implement these enhanced security features. I have used the html pattern attribute to ensure certain criteria is met when signing up. I have also used materialize tool tips to clarify all steps of the form to new users.
For added security, when a new user signs up they are directed to the login page to re enter their details instead of being given direct access to the site.

![SNEAKERFANS](wireframes/sign-up.png)

### Profile Page
On successfully signing up and logging in users are directed to their profile page. They are also given a welcome message using the Flask flash() method. I have used javascript to give all flash messages an auto timeout and also the option to manually close. Once users have access to their profile page they can now add their favourite sneakers using a call to action button that is wired to a simple form that writes to the mongodb database. Once a user has added to the database they now have the option to edit and delete everything on their profile page. Users will not have access to edit or delete any other users data.

![SNEAKERFANS](wireframes/my-sneakers.png)

### Add sneakers
When a user clicks on the add sneakers button they are directed to a form which allows them to pick the category/ add the sneaker name/ add the release year/ A description of the sneaker and add an image url. The user name and date it was added to the database with is taken care of in the backend function. I have used jinja templating to inject all of the database information the user adds to attractive image cards. I have also added a backup feature of using the one-error html attribute to add a back up image in case the image url is broken. Sneaker collectors will find the humour in this back up image as I have used an image from a 1980s Air jordan commercial of a pair of sneakers that were banned by the NBA when they were first released. I used photoshop to add the text "No image available".

![SNEAKERFANS](wireframes/add-sneakers.png)

![Image not available](static/images/error-image.png)

### Edit Sneakers
When a user clicks on the edit button on any of their sneaker additons they are directed to the edit sneakers form which is prepopulated using the objectid from mongodb. They now have the option to edit all input fields on the form and resubmit. Once edits are completed this new information is updated in mongodb and now can be seen on their profile page.

![SNEAKERFANS](wireframes/edit-sneakers.png)

### Full info page
When a user clicks on an image card they are taken to the full information of that sneaker. All info from the sneakers collection is injected to the full-info template using jinja and python. If the user clicks on a collection that they added to the database they will be able to edit and delete their own data but not other users. 

![SNEAKERFANS](wireframes/full-info.png)



### Delete sneakers
Users have the option to remove any of their entries to mongodb using the delete button. I have used some defensive programming to prevent accidental deletion. To implement this I have used a materialize modal which is triggered with a javascript function. The delete button calls the modal and from here the user is given the options of "are you sure?" and a yes and no button. The yes button triggers my backend python function to remove the data from mongodb. Since the theme of the site is iconic sneakers I used the well known Air Jordan jumpman logo for all warning and error messages. I doctored the logo in photoshop to replace the basketball with a font awesome circle exclamation icon. 

![Jumpman error image](wireframes/error.png)
![Delete modal image](wireframes/modal.png)

### Mangage Categories
Only admin has access to this page. When admin logs in they are directed to the manage categories page. From here they have the option to add new categories or edit and delete existing categories. I have also used defensive programming to prevent accidental deletion of categories. I have added an if statement in my python functions to check if a category already exists in the database to prevent accidental duplication of categories by user error. Admin also have access to their profile page which allows them to add new sneakers to the database directly from the application. I have kept the admin control to only managing categories for now. As the site grows I would like to implement a full admin dashboard which would allow to monitor inappropriate content and edit or delete user data and profiles if it does not meet the criteria of the website.

![Manage Categories](wireframes/manage-categories.png)

### Footer
I have added social media links and contact details in the footer. All social media icons are clickable and work in external tabs.
I also added copyright details.

## Features to add for future releases:
There are some features that I would love to implement on future releases:

1. #### Add Comments Likes and Views - The end goal for this site is to create a community of sneaker lovers and collectors. I would like to eventually have a social aspect whereby users can comment on and like other users images. I would also like to collect the amount of likes and views on specific sneakers to allow this data to be shared as an analytics tool for sneaker retailers.
2. #### Retailer dashboard - In order to monetize the site. I would like to add an analytics dashboard that sneaker retailers can pay an annual fee to gain access to. Here they can see what sneakers are trending and what sneakers get the most likes and views during different fashion seasons. This data would help retailers stock up on popular brands while not wasting money on stock that does not sell well. This data will also allow retailers to tailor their sneaker marketing campaigns to the demographics they collect in their analytics dashbars. No user information would be shared from this data.
3. #### User profile dashboard - I would like to add a user dashboard which allows users add a profile photo and some information about themselves and edit as necessary. This is certainly a feature I would add soon.
4. #### Restrict Image type - In order to keep the website nice and clean with no broken images I would like to implement a function in the backend which will only allow data to be written to the database if the image url meets the criteria of jpeg or png. If not the user will be given a message that "this image is not a png or jpeg please try again". I had began researching this option towards the end of the project but unfortunatley I just ran out of time to implement it.
5. #### Admin dashboard - Due to time constraints my admin access is limited to just managing categories. For future releases I would like to add a full admin dashboard which allows to monitor all user and retailer accounts. If user content is deemed inappropriate it can be removed from the site or updated as necessary. Retailer accounts and suscriptions can be kept track of from the admin dashbar.

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #005b96">

# Sitemap Layout
The site map was designed using [Lucid Chart](https://www.lucidchart.com/pages/)

![Sitemap](wireframes/sitemap.png)

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #005b96">

# Database Schema

![DB Schema](wireframes/schema.png)

For my database I choose MongoDB for this project. It was a good choice as I had no relational data such as customer Ids, Invoice Ids or Order Ids. My database consists of 3 collections:
1. Categories
2. Sneakers
3. Users 

![Collections](wireframes/collections.png)

## Categories Collection:
This collection consists of category documents. Which can only be managed by admin. Users can select a category from a drop down list when they are logged in and want to add a document to the sneakers collection.

![Categories](wireframes/categories.png)

## Sneakers Collection:
This collection consists of a dictionary containing:
### Category Name:
* Users can write to the database when using the add sneakers form and choose the category from a dropdown list.
### Shoe Name:
* Users Can add the name of the sneaker to the database.
### Release Year:
* Users Can add the year the shoe was first released to the database.
### Shoe Description:
* Users can add a short description of the sneaker to the database.
### Image:
Users can add an image url in jpeg or png to the database. 
### Date Added:
* This is automatically added to the database by importing datetime to my app.py file.
### User:
* This automatically added from the user in session.

![Sneakers](wireframes/sneakers.png)

## Users Collection:
* This collection consists of a dictionary containing:
### Username:
This data is collected when a new user signs up.
### Password: 
* This data is collected when a new user signs up. The password is encrypted by importing generate_password_hash from werkzeug.security.

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #005b96">

# Security Features
## Passwords:
In order to keep a user's password safe I have imported generate_password_hash from werkzeug.security. This ensures user passwords are encrypted when added to the database.
## Secret Keys:
In order to ensure no one gains access to my MongoDB secret key it has been added to the .gitignore file. This means that any sensitive information files I do not want to be commited to my public github profile will be ignored and will not added to the staging area when pushing to github. 
## Check if users are authenticated:
To carry out any of the logged in functionality users must be authenticated. This has been achieved by using the is_authenticated() method. If a user should not have access to a certain feature they will be shown a bad request error and guided back to the home page. 
## Error handlers:
I have imported abort from Flask to deal with user error using appropriate errorhandler() decorators. When a user tries to access a page that they are not authorised to access they will receive an error. I have also implemented is_object_id_valid(id_value) method to check that the database object id is valid. 

![Jumpman error image](wireframes/error.png)

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #005b96">

# TECHNOLOGIES USED

1. [Balsamiq](https://balsamiq.com/wireframes/)
* I found Balsamiq an extremely usefull platform to design mock ups and get a feel of how my website would look before coding.

2. [HTML 5](https://en.wikipedia.org/wiki/HTML)
* HTML is the main mark up language used to design my website.

3. [CSS 3](https://en.wikipedia.org/wiki/CSS)
* All HTML elements were styled to my own personal taste using CSS language.

4. [Javascript](https://www.javascript.com/)
* Javascript was used to auto close flash messages and to validate the select dropdown on all forms.

5. [Jquery](https://jquery.com/)
* Jquery was used to show and hide elements on the document and also trigger modals and mobile navigation drop down.

6. [Materialize 1.0.0](https://materializecss.com/)
* In order to help style my website as well as making the layout responsive I used the materialize CDN.

7. [Font Awesome](https://fontawesome.com/)
* All icons have been sourced and added from the free version of font awesome.

8. [Gitpod](https://www.gitpod.io/)
* I used git pod as my IDE workspace to write and run all code. I used Git as my version control to commit and push all code to my GitHub repository.

9. [Github](https://github.com/)
* I used GitHub to store my Git commits and back up all code.

10. [W3C HTML validator](https://validator.w3.org/)
* I used the W3C validation service to ensure all HTML code passed validation.

11. [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
* I used the W3C validation service to ensure all CSS code passed validation.

12. [Jshint validator](https://jshint.com/)
* Jshint was used to ensure all javascript code passed validation.

13. [PEP8 validator](http://pep8online.com/)
* PEP8 online was used to ensure all python code passed all PEP8 industry standards.

14. [Python extends class validator](https://extendsclass.com/python-tester.html)
* extendsclass was used to ensure all python syntax passed validation.

15. [Lucid Chart](https://www.lucidchart.com/pages/)
* Lucid chart was used to create the sitemap.

16. [db diagram](https://dbdiagram.io/home)
* Db diagram was used to create my database schema.

17. [PIP](https://pip.pypa.io/en/stable/)
* PIP was used to install all packaging tools.

18. [Am I responsive](http://ami.responsivedesign.is/)
* AM I responsive was used to create attractive screenshots from all devices to display on my README file.

19. [Python3](https://www.python.org/download/releases/3.0/)
* Python is the chosen backend programming language.

20. [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* Flask was used as a url based framework for quickly building web pages in conjuction with [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) templating. 
* I also used the [werkzeug toolkit](https://werkzeug.palletsprojects.com/en/2.0.x/) to encrypt user passwords.

21. [MongoDB](https://www.mongodb.com/)
* MongoDB was the chosen NOSQL database for this application.

22. [PyMongo](https://pymongo.readthedocs.io/en/stable/)
* PyMongo was used to query the database using python as the backend language.

23. [Heroku](https://id.heroku.com/login)
* Heroku was used as the hosting platform for this project.

24. [Photoshop](https://www.adobe.com/ie/products/photoshop.html)
* I used Adobe photoshop to create the company logo, error images and favicon.

25. [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
* Throughout the development process I used chrome developer tools for debugging and also to keep checking any changes I was making looked good on all devices.

26. [WAVE web accessibility tool](https://wave.webaim.org/)
* I used WAVE to make check any errors that my site may have which would effect users with hearing or visual disabilities.

27. [a11y](https://color.a11y.com/)
* I used a11y to get my color contrast between background and text as accessible as possible without comprimising my vision for the website design.

28. [CSS Autoprefixer](https://autoprefixer.github.io/)
* I used Autoprefixer to ensure all of my css styles would work on all browsers.

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #005b96">

# Testing Steps

## Click to view [TESTING.md](https://github.com/Joe2308/sneakerfans-ms3/blob/main/TESTING.md)

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #005b96">

# Deployment Process

## Local Deployment
### Required tools:
* [Python3](https://www.python.org/download/releases/3.0/)
* [PIP](https://pip.pypa.io/en/stable/)
* [Gitpod](https://www.gitpod.io/)
* [MongoDB](https://www.mongodb.com/)
* [PyMongo](https://pymongo.readthedocs.io/en/stable/)

### Create a local copy:

### Directions: 
1. On GitHub, navigate to the main page of the repository [https://github.com/Joe2308/sneakerfans-ms3]. 
2. At the top of the repository, select the Code drop down and copy the Clone URL.
![Clone](wireframes/clone.png)
3. In your IDE workspace, open a Terminal window and use the cd command to change the directory to where you want the cloned directory to be made and type git clone and paste in https://github.com/Joe2308/sneakerfans-ms3.git.
4. Click enter and the project will be created and cloned locally.

### Working with the local copy:
1. Install all the project dependencies from the terminal window of your IDE by typing: pip3 install -r requirements.txt.
2. In [MongoDB](https://www.mongodb.com/) create a database. First create a cluster, then a database of the following four collections:
![DB Schema](wireframes/schema.png)
3. Create an env.py file to contain the environment variables, which should include the following:
* Add import os to the top of the file
### Set the environment variables:
* os.environ.setdefault("IP", "0.0.0.0")
* os.environ.setdefault("PORT", "5000")
* os.environ.setdefault("SECRET_KEY", "**secret key goes here**")
* os.environ.setdefault("MONGO_URI", "**mongo uri goes here**")
* os.environ.setdefault("MONGO_DBNAME", "**database name goes here**")

4. In order to prevent sensitive information such as secret keys and database passwords being pushed to your public github repository you need to create a .gitignore file in the root directory of the project and add the env.py file.
5. Type python3 app.py into the terminal to run the app locally. In app.py Set debug to TRUE to work on the application in a live development environment.

## Deployment to Heroku
### Tell Heroku which applications and depencies are needed to run the app:
* Create a requirements.txt file by typing "pip3 freeze --local > requirements.txt in the terminal.
* Creat a Procfile so Heroku knows how to run the app by typing echo web: python app.py > Procfile in the terminal. 
* Push these files to github before deploying. If any new packages or depencies have been added since the last time it was pushed to github the requirements.txt file will need to be updated.

### Deploy from github:
* Next log into [Heroku](https://id.heroku.com/login) and create a new app and choose the location closest to you.

![New App](wireframes/new-app.png)

* For this project I enabled automatic deployment from github for ease of use.
* Choose your github profile and add your repository name.

![Auto deploy](wireframes/auto-deploy.png)

* Press the search button and when it is found click the connect to this app button.

### Tell Heroku variables required to run the app:
* Before enabling automatic deployment we first set up the required variables in Heroku from our env.py file.
* Go to settings in Heroku and select reveal config vars.
* Fill in config vars fields by copying and pasting the data from the env.py file. 

![Config vars](wireframes/config-vars.png)

* We can now enable automatic deployment in Heroku.
* Click deploy main branch in order for Heroku to receive the code from github.
* The app should now be successfully deployed and will auto update each time we push new code to the github repository. 

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #005b96">

# CODE CREDITS

## [Show and hide password](https://codepen.io/Sohail05/pen/yOpeBm)

## [How to use loop index to generate unique ids for modals within for loops](https://code-institute-room.slack.com/archives/C7JQY2RHC/p1619027301419600)

## [MongoDB aggregate method to show 6 random samples on home page](https://stackoverflow.com/questions/2824157/random-record-from-mongodb)

## [Flask error handlers](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)

## [Whenever I got stuck I regularly checked stack overflow for inspiration and ideas](https://stackoverflow.com/)

## [I also used W3C schools for help on html patterns and one-error attributes. And also for inspiration on my javascript function to show and hide passwords](https://www.w3schools.com/)

## [Slack was extremely beneficially for this project. I got excellent feedback here](https://app.slack.com/client/T0L30B202)

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #005b96">

# MY ACKNOWLEDGEMENTS
1. I would like to acknowledge my mentor [Guido Cecilio](https://code-institute-room.slack.com/team/U4ALPK7UG) for his help with keeping the design consistent and also for his guidance on user authentification and handling of errors.
1. I would like to acknowledge [Natasha Clerkin](https://github.com/natashaclerkin/singularartistsMS1) for inspiration from her fantastic README.md file. 
1. I would like to acknowledge [My Cookbook](http://mycookbook-project.herokuapp.com/) for the initial inspiration to get my design off the ground. This site has an amazing high level design and encouraged me to spend some extra time making my site look attractive.
1. I also found the [task manager](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/579bbf01edaf47938e6a860b8f08f275/?child=first) walk through project of great help. I would continously refer back to it to break down and understand the backend end funcitionality for my own project.

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #005b96">

# My Disclaimer 
* This project is for edcational purposes only.

<hr style="height:5px;border-width:0;color:gray;background-color: #005b96">



