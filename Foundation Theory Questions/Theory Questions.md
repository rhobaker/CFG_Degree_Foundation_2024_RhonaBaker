## Section One Theory Questions

### 1.1 Explain the difference between a primary key and a foreign key

In a database table, the **primary key** column is the one that uniquely identifies each row held within it.  There can only be one primary key column per table and it is often a sequential ID number, such as the employee number in a table containing all employees.

A **foreign key** column is one that is linked to a column in a different table in the database.  There can be many foreign keys in a table.  It is usually the primary key column in this other table and the link ensures data integrity between the two.  For example if the employee number was a column in a table that recorded employee's holidays, the employee number would be a foreign key, linked to the employee table.  An error would occur if you tried to add a record in the holiday table with an employee number that is not in the employee table.

Reference: https://www.geeksforgeeks.org/difference-between-primary-key-and-foreign-key/

### 1.2 What is the role of the *finally* block in Python exception handling and how would you use it

The **finally** block is part of the **try-except-finally** code block which is used for exception handling within a script in Python.
- First, the try statement executes a block of code and checks for an error in it. 
- If an error is raised the except block of code is executed, to prevent the programme stopping and to give details about the error.  
- The **finally** block of code is then executed regardless of whether or not an exception was found.  It is often used to close connections to a database or to close an external file, regardless of the outcome of the code executed in the blocks above it.  This prevents external resources being left open as the programme continues.

Reference: https://www.w3schools.com/python/ref_keyword_finally.asp

### 1.3 Explain the difference between a commit and push in Git

In Git the **commit** command will record the state of the files in the **local** repository, as they appear in the staging area at the point the command is executed, along with a message describing the changes made.  This point can then be referred back to in the future.

The **push** command will update a **remote** repository, such as GitHub, with any changes that have been committed in the local repository since the last push command was executed.  Only changes that have been committed in the local repository before the push command is executed will be reflected in the remote repository.

Reference: https://www.w3schools.com/git/git_push_to_remote.asp?remote=github

### 1.4 Explain the difference between undefined and null in JavaScript

In JavaScript an **undefined** variable is one that has been declared in the script, but has not yet had a value assigned to it.\
E.g:\
**let myVar;**

The value **null** however, means that a variable has been declared and had the value null, or nothing, deliberately assigned to it.\
E.g:\
**let myVar = null;**

Reference: https://www.geeksforgeeks.org/undefined-vs-null-in-javascript/

### 1.5 Provide examples of two web APIs and describe their functionalities
**X** (Twitter) has the **X Ads API** that offers a set of endpoint APIs that allows advertisers to track the performance of their marketing campaigns.  The API allows analytics to be extracted from X and used in other systems to analyse all aspects of an advertising campaign in order to optimise its impact.

**Google Maps** has the **Map Tiles API** that can be used to embed a map in a third party web page.  These can be two dimensional, three dimensional or provide a street view.  The API allows web site users to interact with Google Maps without having to navigate to it and also allows developers to customise the map to optimise their webpage.

Reference: https://developer.twitter.com/en/docs/twitter-ads-api\
Reference: https://developers.google.com/maps

### 1.6 Describe four tasks in the role of the Product Owner in Agile development

Agile development is focused on software development in small steps, and with continual updates to the requirements of the project as it progresses.  The Product Owner oversees the development team, in a similar way to a project manager.  Their tasks include:
1. Understand the vision of the organisation and turn it into a tangible plan that can be implemented.  This is then communicated to the project's stakeholders, often through a product roadmap, which outlines what development will be done and when.
2. Act as liaison between team members and other stakeholders, such as business managers.  This can include discussions about budgets and what the managers can expect to be delivered and when.
3. Manage which items are prioritised first from any backlog of requirements and requests, based on the company's objectives.  This can continually change as external influences impact on the project and the Project Owner needs to constantly reassess what is a priority.
4. Oversee software development tasks including the design and testing phases.  This includes providing feedback to the team and input into the planning cycle to ensure the quality of the software developed.

Reference: https://www.indeed.com/career-advice/career-development/agile-product-owner

### 1.7 Name two types of SQL joins and provide an example scenario for each.

In SQL a join is used to combine tables together, based on a similar column of data.

When a **left join** is used all the data from the table on the left hand side of the join query is included, whether or not it has matching data in the table on the right.  Where data is not available, null values are included for the missing entries.\
For example if querying an HR database for staff e-mail addresses in order to send out an important communication, you would use a left join between the employee table and the e-mail address table.  This would allow you to see any employees that did not have an e-mail address on the system, so they could be contacted in a different way.

An **inner join** only matches rows where there is data present in both tables.  This means that null values do not need to be inserted.\
For example, if running a query in a HR database for a list of staff with a company car, you would use an inner join between the employee table and the company car table as you would not want to see all the employees that do not have a company car in your query results.

Reference https://www.w3schools.com/mysql/mysql_join.asp

### 1.8 Explain the difference between *mutable* and *immutable* data types in Python, provide an example of each.

**Mutable** data types can be changed after they are created, without creating a new object.  They are therefore easy to manipulate in your code without creating new objects and using extra memory.\
For example, lists are mutable in Python.  Individual elements can be added into them, or removed from them, without having to create a new copy of the list.

**Immutable** data types can't be changed after they are created.  They are quicker to access in your code, but are harder to change, requiring a copy to be made, using extra memory.\
For example, strings are immutable in Python.  Characters can't be changed, added or deleted without creating a copy of the string, leaving the original one unchanged.

Reference: https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/

### 1.9 What is the difference between synchronous and asynchronous functions?

JavaScript can run code asynchronously i.e. continue to execute lines of code in the script while waiting for other code to finish running.  This involves the use of **asynchronous functions** such as **setTimeout**, in which a timer is set before it is executed.  The code following the **setTimeout** function will continue to execute while waiting for the timer to countdown.  The function will then finish its execution later.

**Synchronous** functions are run as they are called and finish running before the next lines of code are executed.

User defined **asynchronous functions** can be created using the **async** keyword.  They return a promise, which represents the final result of the function that hasn't yet finished running.  They are often used with functions that fetch data, such as APIs.

Reference: https://www.sitepoint.com/javascript-async-await/

### 1.10 Describe four differences between agile and waterfall software development methodologies

The **agile** methodology focuses on collaboration and adapting to changes in a project environment.\
The **waterfall** methodology is a more linear approach to project management.  The project is planned in detail at the start, with one project task finished before moving onto the next.

The main differences are:
1. The planning with a waterfall methodology is all done at the beginning of a project and all the requirements set out in detail.  With the agile methodology however, planning carries on throughout the project and adaptions made as needed.
2. The delivery of a product is much quicker with an agile methodology as small, iterative steps are made in development, each producing a product that can be deployed.  However, with the waterfall methodology it can take much longer to deliver a product as all the steps have to be completed first.
3. The agile methodology encourages collaboration and communication between all team members, to keep everyone up to date with the current state of the project.  The waterfall methodology however is based on more formal communication of planning and progress reports.
4. With an agile methodology the testing of the software is done throughout development to find and resolve any problems that are found.  With waterfall methodologies the testing is often done towards the end of the project, after more of the development has been done.

Reference: https://www.float.com/resources/agile-vs-waterfall/
