# TESTING STEPS

## User story testing:
1. **As a fan of new and retro sneakers** I am looking for a website where I can share my interest in sneakers with other sneaker fans. Having found the SNEAKERFANS website this allows me to do just that. I can use the browse collection search bar to check for all types of sneakers and to give me great ideas for my next purchase.

2. **As a sneaker collector** I am looking for a website where I can find ideas to add my exstensive collection of sneakers. The SNEAKERFANS website allows me to see sneakers I did not realise were realeased. Everything from vintage to signature and retro releases are available to view on SNEAKERFANS. I especially enjoy photographing my own collection and adding them to the database.

3. **As the website owner** I would like to create a community of sneaker lovers who can share images and information on popular and extremely rare sneakers. The website does exactly what it says on the tin. New users are signing up each day and sharing their passion for sneakers. It is easy to sign up and add your sneakers in a matter of minutes

4. **As a sneaker retailer** I created an account with the SNEAKERFANS website. It allows me to see what sneakers people enjoy and it also gives me great ideas for rare releases I can add to my store to stand out from my competitors. I would love if I had a way of seeing what sneakers are trending on the site based on how many views a sneaker has or how many likes it has. I have spoken to the website owner and they have assured me this is a feature they will soon be adding. I would definately pay a suscription for this type of information. It would help me boost sales and stay ahead of the curve.

## Code Validation:

### **Html**:

![Html validation](wireframes/html-validate.png)
I checked all Html pages using the url from my Heroku application to avoid errors due to jinja templating. I had one error in the html validator which was using the type attribute on an anchor link. Having removed this my Html code passed all validation. The above image is showing a heading error because of flash messaging added to my base.html to extend to all other relevant pages. All Html code was validated using the [W3C HTML validator](https://validator.w3.org/).

### **CSS**:

![CSS validation](wireframes/css-validate.png)
All CSS code passed using the [W3C CSS validator](https://jigsaw.w3.org/css-validator/).

### **PEP8 Compliance**:

![PEP8 validation](wireframes/pep8.png)
All code was checked for valid indentation, whitespace, blank line space and line length using 
the [PEP8 validator](http://pep8online.com/).

### **Python Syntax**:

![Python syntax validation](wireframes/extends-class.png)
All python syntax was validated using the [Python extends class validator](https://extendsclass.com/python-tester.html).

### **Javascript Validation**:

![Javascript validation](wireframes/jshint.png)
All Javascript code was validated using [Jshint validator](https://jshint.com/). My code passed with no major errors.

## Manual Testing:

### Responsive Design: 
For this project I decided to use [Materialize 1.0.0](https://materializecss.com/). Initially I thought of changing back to bootsrap. But the more I used it the more I like the simplicity of Materialize. Its grid system allows for excellent responsive designs. I used [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) to check how my application was looking on all screen sizes and adjusted as necessary. I had to used minimal media queries in my css code.

### Call to action buttons:
I checked and rechecked all buttons were working on all devices and were leading to the correct sections of the website. It was also important that I laid out 
my CTA choices in order of priorty to my user stories with a button to encourage new visitors to sign up being the most important.

### External links:
I made sure to check that all links and social media links were directed to the correct URLS and also that my target="_blank" attribute was working. 
All external links open in a new browser tab.

### Lighthouse performance test:
![Lighhouse test](wireframes/lighthouse.png)

I used Lighthouse in Chrome devtools to test my website's performance.
I increased my SEO scores by adding meta content for seo description.
I also increased my best practises score by adding rel="noreferrer" to all external links.
I found that testing with lighthouse generated higher scores in incognito mode due to browser caching.

### Accessibility:

![Accessiblity test](wireframes/wave.png)

I used [WAVE web accessibility tool](https://wave.webaim.org/) to make sure the site was accessable to the visually impaired. I also used [a11y](https://color.a11y.com/) to make sure my color contrasts between fonts and backgrounds was acceptable without excessively comprising my vision of the website final design. There were no major errors but some contrast issues. I decided not to change my origional concept as a google lighthouse test gave an accessibility score over 95%.
