# Project 3

Web Programming with Python and JavaScript
youtube video: https://youtu.be/gBGk2o56jiE

This is Project 3 for CS50W. The goal is to create a Pizza delivery website using Django. The website should replicate the menu of Pinocchio pizza (Cambridge, MA). The website should allow admins to modify menus and staff members to see orders.

This code comes with an Admin user pre created with the following credentials:
Login: Admin
Pwd: SuperSecret

The files architectures follows the normal Django framework. The app is contained in the orderrs folders.

-views.py contains all the different python application to run server side. It manipulates databases and pushes pages to be rendered.

-urls maps all the different pages urls

-models.py is where all the models are defined, these models are then migrated to create SQL databases

-admin.py contains the link to the models that admins should be able to edit in the admin section of the website

-templates/orders contains all the html pages and layouts to be rendered by the app

-static/orders contains all the CSS and Javascript code to control the website design and animate it. Some JS files also contain Ajax requests to the server.

