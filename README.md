# SNEAKERFANS

![SNEAKERFANSLogo](static/images/logo-black.png)

This project is based on a database for lovers of sneakers. Around the world sneaker collecting and resale is big business. I created SNEAKERFANS with the aim of drawing this community together and to allow them to create and upload their own favourite sneakers to the website for others to see. I would love to add a posts section in single page layout in the style of facebook and I believe it would unite millions of sneaker lovers around the world. No such site currently exists. This feature could be added on a trial basis for future releases. For now the site is purely a database site that allows users to log in, create data, read data, update data and edit and delete their own data.

There is also the opportunity for businesses to to able to sign up for a fee and access data from a custom dashboard similar to google analytics to see what sneakers are trending and what styles are most popular. This would allow businesses such as store owners to stock up on the most popular brands at the right times of the year and increase their annual sales. For this project time constraints did not allow me to fully explore this option. But it is something I would like to add in the future.

I grew up playing basketball as a teenager in the Michael Air Jordan era of the 1990's. There is no feeling like that of opening a new pair of Air Jordans and to this day decades later I still collect basketball sneakers. 1990s retro releases are my favourites. When I was brainstorming ideas for this milestone project a sneaker database was a no brainer for me. It is a site I would use if it existed and seeing what ideas other users have on sneakers would keep me coming back daily.

I have always loved the simplicity of the Nike website black and white are the main themes and the sneakers do the talking so there are no other distractions or gimmicks. SNEAKERFANS is heavily influenced by the [Nike](https://www.nike.com/ie/) website. 
I did not use any fancy fonts or background colors and opted to use the default sans serif font and white page body with a black navigation bar and footer to see how nice I could make the site while just using the basics. Black and white is the main theme with some dashes of red and orange text. These are prominent themes in some of the most classic sneaker colorways. Such as the holy grail of all retro sneakers The [Air Jordan 3](https://sneakernews.com/wp-content/uploads/2021/05/Air-Jordan-3-Cardinal-2022.jpg)

The website uses HTML and CSS and Javascript in the front end. With my main css framework library being materialize.css and my Javacript framework is jquery cdn. I have also incorporated the use of the font awesome icons cdn for all icons. In the backend flask is used and jinja templating is used to inject data to the HTML. My chosen database is MongoDB.

## [View Live Project](https://ms3-sneakerfans.herokuapp.com/)
![SNEAKERFANS](static/images/responsive.png)

## Wireframes:
My initial wireframes and database schemas were sketched on paper and when I was happy I was going in the correct direction I used [Balsamiq](https://balsamiq.com/wireframes/) to finalise my mockups for the front end. For my database schema I used [db diagram](https://dbdiagram.io/). 
The main inspiration for my website is from the global sneaker giant [nike.com](https://www.nike.com/ie/).  All wireframes can be seen in the links below.

* [Home Not Logged In](wireframes/home1.png)
* [Home Logged In](wireframes/home2.png)
* [Browse Collection](wireframes/browse.png)
* [My Sneakers Profile Page](wireframes/profile.png)
* [Add Sneakers](wireframes/add.png)
* [Full Description Page](wireframes/full.png)
* [Log In Page](wireframes/login.png)
* [Log Out Page](wireframes/logout.png)
* [Sign Up Page](wireframes/signup.png)

* [Database Schema](wireframes/schema.png)


# User Stories:
1. **As a fan of new and retro sneakers I am seeking a website that allows me to search sneakers as well as add my own ideas to the website**

2. **As a sneaker collector I would like to add images and descriptions of my collection for others to see**

3. **As the website owner I would like to create a community of sneaker lovers who can share images and information on popular and extremely rare sneakers. I would also like to create a revenue stream to keep growing the site from advertising from sneaker brands**

4. **As a sneaker retailer I would like to log into a website that allows me to see what sneakers are currently fan favourites so we can stock up on popular items to increase profits**

## Strategy:
### What am I making?
A website/app that offers users to sign up/ Login/ Read data from other users/ Write data to the database/ view, edit and delete their own content on their profile page. The site will create a sneaker community while also allowing businesses to see what styles are most popular to increase revenue.

### Website business goals:
1. Create a community of sneakerfans 
1. Allow businesses to sign up for a monthly fee to collect data and feedback on users sneaker preferences 
1. Increase social media and website traffic with the aim of creating revenue from advertising from the major sneaker brands.

### Website target audience:
1. Sneaker lovers and collectors
1. Sneaker resellers
1. Sneaker retailers

### User value:
1. Sneaker lovers and collectors will gain a positive emotional experience from using the site and they can search the entire database to find retro sneakers they had forgotton about that will bring back memories and also encourage them to upload their own favourite sneakers.
1. Retailers and resellers can see exactly what sneakers are the most popular and at what times of the year they need to stock up on popular items to increase their revenue.

### What users can expect:
1. An easy to navigate no fuss website that is pleasant to use.
1. Easy to sign up quickly and starting browsing and adding data to the website.
1. The ability to edit and delete uploads to their own profile.
1. The ability to read and learn about rare sneakers uploaded to the database by other users.

### What is worth doing:
1. A simple sign up form 
1. A simple log in form 
1. A clean profile page
1. A home page that shows 6 random collections from the database so users can see a fresh content each time they log in.
1. A simple user edit form 
1. Give users the ability to delete their own data
1. A search box to allow users to enter keywords based on database key values so users can browse the entire database efficiently

### What makes it a good experience:
1. Simple outlay. 
1. clean images placed in materilize image cards of the same heights.
1. Familar simple navigation
1. Lots of great information on rare sneakers 

