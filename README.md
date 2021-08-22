### PSAW - Python Scratch API Wrapper

  
Table of contents
<ul>
	<li>How to login</li>
	<li>Commenting</li>
	<li>following</li>
	<li>Loving and Faving projects</li>
	<li>get user data</li>
	<li>get project data</li>
</ul>

**Logging in**
Logging is very basic, to log in, and do everything that requires being logged in, one simply needs to use the code below
```
import psaw

user = PSAWConnect(username, password) #Put your username and password here
```
**Commenting**
    
There are several types of comments in scratch, however, currently in this package, only 1 type is supported (however the others will be added soon). 
<ul>
<li>Profile Comments</li>
</ul>

**Profile Comments**
Profile comments require the user to be logged in, and run using the code:
<pre>
user.profilecomment("message", "user") #Put message in "message" and username where user is.
</pre>
   **Following**
   Following and unfollowing and both very simple commands in PSAW. All you need to do is type
   
<pre>
user.follow("person") #Put the username you want to follow in "person"
user.unfollow("person") #Put the username you want to unfollow in "person"
</pre>
**Loving and Faving projects**

Loving and faving projects is a common task in scratch, and luckily, is included in PSAW!
The code to love and fave, and *un*love and *un*fave is here:

 
<pre>
user.love(project_id) #love a project, put the project id in the parameter
user.unlove(project_id) #unlove a project,put the project id in the parameter
user.fave(project_id) #Favorite a project, put the project id in the parameter
user.unfave(project_id) #Unfavorite a project, put the project id in the parameter
</pre>

**Getting User Data**
There are several current features for getting user data, with more coming in the next update!
<ul>
<li>get followers</li>
<li>get faves</li>
<li>print messages</li>
<li>
</ul>

**get followers**
The get followers command is simply `client.get_followers("username")`, it returns a list with all of the user's followers.

**get faves**
The get faves command is simply  `client.get_user_faves("username")`. It returns a dict with the title of a project with the id of the project. Such as `{"test: "0000"}`

**print messages**
The printmessages command has several parameters. The command is `client.print_messages(all, limit, filter, user)` the all parameter, a boolean, is whether you want or don't want all of the messages, it defaults to True, and you get all messages. The limit param is the limit of messages you want. It is an int, and defaults to 50. If all is set to True, then limit is ignored. Filter is the type of message that you want. You can mainly ignore it however.


### NOTE: THIS MODULE IS A WORK IN PROGRESS, AND IS NOT THE FINISHED ITEM!

    
