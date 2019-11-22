"# Twitter-Project" 

This project is a basic implementation of Twitter using Python and NoSQL databases. Google App Engine alongside the Atom text editor is used to develop this project. Please refer the following description for further understanding of the project.

1.	Main Page :

The get method:

A user login /logout shell is written in the get method of the main page. A NoSQL database is used to store all the user information.  When a user logs in, the entire database is searched to check if the email address of the user exists, if yes then the user is directed to his home page of the application.
If the user does not exist, the he is directed to a new page to enter his basic information which is then stored in the database. 
For an existing user, all the tweets of the users in his following list are fetched and displayed in an order with the newest tweet first including the user’s own tweets(50 tweets only).

The post  method:
This method is used to store the values in the NoSQl datastore. The user has the option to type in a tweet and post it. The user is fetched depending on his unique key and then the value is stored in his tweet list.

2.	Profile Page :

The get method:
This page displays the user’s own Username, Full Name and description as stored in the database. All the above values are fetched from the database using the unique key of the user. Also, the user’s own tweets are displayed in an order from newest to oldest 50 tweets.

The post method:

Beside every tweet, two buttons namely ‘Edit’ and ‘Delete’ are provided. Every tweet has a specific index in the user’s tweet list. When the user chooses to edit, he is redirected to a new page where in an input box his original tweet is displayed. The user can now edit his tweet. The previous tweet is removed from the database and the edited tweet is stored as the new and the latest one.
If the user chooses to delete the tweet, the index of the tweet is fetched and then the tweet is removed from the database.

3.	Edit Information:

The get method:

The user has the option to edit his personal information as stored in the system. The user is directed to a form, where the input fields already have the values as the user has stored them in the database. However , the username remains fixed and cannot be changed( declared as a read-only property in html). The values are fetched using the user’s unique key and displayed using the Jinja Library.

The post method:
This method is triggered by the ‘Submit’ option on the page. All the values that are entered by the user, are updated in the database by fetching the user by using his unique key.

4.	 Search Users:

The get method:

An input box is provided, where the user can enter usernames of other users in the application and search them. This method is triggered when the user clicks the search button. The value that the user entered is fetched from the database, if the value exists, then the user is redirected to a new page that is the view of the searched user’s profile. The values on the page are displayed using the Jinja library . There is an follow/unfollow button. If the user is in the current user’s following list , then the button is set to Unfollow else the button is set to follow.

The post method:

If the user chooses to follow, then the user will be added to the current user’s following list and tweets of this user will also be displayed to the current user.
If the user chooses to unfollow, then the value will be fetched and removed from the user’s following list and the user will not be able to view this user’s tweet on his home page. 

5.	Search Content in Tweets

The get method:
This method is triggered when the user clicks on Search Content in the navigation bar. An input box is provided where the user can type in phrases or words that he wants to search in tweets. If a phrase is entered , the phrase is searched as whole . Only the tweets with the complete phrase will be displayed to the user. The ‘if in tweet’ conditional statement is used for this purpose.

The post method:
This method is triggered when the user clicks on the back button . He will be redirected to the main page.


Models and Databases:
1.	MyUser :
This data model is designed using the ndb model of the Google App Engine. The data model has the following values :
a.	Email Address: String Property
b.	Username : String Property
c.	Full Name : String Property
d.	Following : String Property (repeated = true, reason being many values can be stored by appending them to the existing values)
e.	Tweet : String property (Tweet list of the user, repeated = true, reason being many values can be stored by appending them to the existing values)
Every user is stored as a separate entity in the datastore, and is uniquely identified by using the key id which is a set of digits.
2.	Tweet :
This data model is designed using the ndb model of the Google App Engine. The data model has the following values :
a.	Username : String Property
b.	Tweet : String Property 
c.	Tweet time : DateTime Property (System time when the tweet was posted by the user)
Every tweet is stored as a separate entity in the database. This helps is displaying the tweets time wise.  


User Interface Design
1.	Background colour:
A faint blue background colour is used for every page of the application. The reason being that the content of the page which is in black appears clear in contrast to the blue colour. The appearance of the webpage is not stressful to the eyes due to the above color combination.

2.	Navigation Bar
The  navigation bar is a filled bar with various options available to the user. This makes the page look concise and it becomes easier for the user to navigate through the application as all possible options are provided on the same line of the page.
When the user hovers over the options, the options get highlighted and in a darker colour than the navigation bar colour. This helps the user notice , what button he is on.
3.	Back buttons
Every page of the application has a back button , which redirects the user to the main page. Due to this, the user does not need to click the back button the browser a number of times. 
4.	Appearance of webpages
In most of the web pages, the content of the page is displayed in the centre of the page. Due to this the user does not have to specifically search for something . Headings are of bigger fonts as compared to the rest. Usernames are displayed in different colours as compared to tweets so that the user can easily 

