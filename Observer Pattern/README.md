### IMPLEMENTATION AND DOCUMENTATION.

>**Note: Explanation is made in my own understanding and hence open to corrections.**

>So what is Observer Pattern?? In my own words, i see it as an approach taken when we want to deal with **Event Driven and State Managed Situations**.

> e.g For example creating a inventory system. we might want to update the total amount of products in say our database and also send emails to our stock keepers about the available stocks left. This is sought of an event driven system and you actually could build this without this approach but i feel it cleaner and better (my opinion tho)

### SINCE WE HAVE A WORKING EXAMPLE, LET'S MOVE ON

>core.py holds what i like to call the dispatcher. It implements the interface for subscribing for an event (attach function) and also dispatching of event. Once an event of a product quantity change it calls the dispatcher(_update_obeservers) and notifiers them of the change.

### We create an instance [called **inventory**] of the Inventory class in core.py and use in all other files.

>observers.py and send_email.py are essentially functions that just calls the dispatch fucntion of the instance [inventory] so as to add it to the list of observers waiting for an action

>main.py file is used to alter the state of the **inventory system** or **trigger the events**

>There you have it ;) **Observer Pattern**