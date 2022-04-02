Python Basic Web Project: Phonebook

Problems for exercises for the "Programming Fundamentals" course @ SoftUni

Problem

You have been tasked to create a simple Phonebook application. The application should hold contacts, which are the main app model.

The functionality of the application should support:

Listing contacts



Adding Contacts





Overview

Requirements

Django framework

SQLite database

Data Model

The Contact model holds 2 properties:

name - Character field with a max length of 30 characters

number - Integer field

Project Skeletons

You will be given the applications' skeletons, which hold most of the logic. You'll need to write some code for the application to function properly.

The application's templates will be given to you fully implemented. You only need to include them in your business logic.

Everything that has been given to you inside the skeleton is correctly implemented, and if you write your code correctly, the application should work just fine. You are free to change anything in the skeleton on your account.

Setting Up PyCharm Configuration

Start PyCharm and import the skeleton. From the File menu click Open, choose the directory you've downloaded your skeleton and click OK.



In the project skeleton, you have a requirements.txt file. It is used for specifying what python packages are required to run the project you are looking at. PyCharm will ask you to create a virtual environment and install the packages using the requirements.txt file immediately after opening the project. Click OK:

. 

You can start working on your code!

Landing Page View

In the phonebook app, you can see the files that define our app:

 

Open the views.py file and create a view for our landing page. A view is a Python function that takes a Web request and returns a Web response. In this case, our view function will return a Web response - the HTML contents of our Web page. For the example, we will name the function landing_page:



Next, let's design our URL pattern that will retrieve the created view in the browser. To call the view, we need to map it to a URL - and for this, we need a URLconf. In the phonebook app directory, open a file called urls.py:



We want to see the page as we open the localhost, so in this case, the route will be an empty string (""), and the view will be the landing_page. Open the urls.py file and add the following code:



One more step, we need to point it to the root URLconf. To do that, in djangoproject/urls.py include the djangoproject.phonebook.urls module, so the file looks like this:



You can now run the created project so far. Open the Terminal and write the command:

																py manage.py runserver

You'll see the following output on the command line:



Now that the server's running. Visit http://127.0.0.1:8000/ with your Web browser. You can see the landing page:



Contact Model

It's time to create our first model. Open the models.py file. The file should look like this:



We need to define our contact model. Create a new python class called Contact with its attributes:



Our Contact model is ready. The only thing left to do is to migrate the created model to the database. For this project, we are using SQLite. Run the Django command-line utilities to create the database tables automatically:

py manage.py makemigrations

py manage.py migrate

You can see the migrations in the automatically created .py file in the phonebook/migrations directory: 



Creating New Contact

We have reached the point where we can develop our business logic for creating contact with a name and a number. Open the views.py file and create a second view. For the example, we will name it create_contact:



This function will save contacts and store them in the database. In the end, it redirects the user back to the landing page as a response. Although we do not have an HTML template for this view, we need to create an URL path. Open the phonebook/urls.py file and add a second path:



Thanks to the form, we can process POST requests:



In the templates/phonebook/index.html file, we see the <form> … </form> that allows a visitor to enter text, select options, manipulate objects or controls, and so on, and then send that information back to the server. Each form must define two things:

The HTTP method is used to send the data using the method attribute

The destination of the data on the server using the action attribute

In our template, we have already implemented the method. The only thing left to do is to add an action parameter.



To connect the form with our create_contact view. We use the name of the created in the urls.py path: "new-contact".

So far, we have implemented the business logic for creating a contact and sending the user data to the database. Each time a user clicks on the "Add" button, a name with a number will be saved in the database.

Adding the Created Contact

Finally, we need to add the contact to our list and give a response to the user.

In the views.py file, in our landing_page view, we need to implement the following code:



The render() function takes the request object as its first argument, a template name as its second argument, and a dictionary with the context we want to return as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context. In our case, the context needs to be all created contacts (objects). 

The key name "contacts" is used as a variable name in the template index.html:



The code above implements logic for iterating over the collection of contacts and taking each name and number. Thus, they can be visualized in the contacts table on our localhost server.

With that, we finished our Python Phonebook. Feel free to build on your project even further. 