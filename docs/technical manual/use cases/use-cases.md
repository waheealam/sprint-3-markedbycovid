# MarkedByCovid (MBC) Use Case Documentation
This documentation shows the relationships among the actors and uses cases within the Marked By Covid (MBC) system. Overall, this document provides an overview of the usage requirements of the MBC system in the form of an essential model or business model and communicates the scope of the development project. And finally, model the analysis of the usage requirements in the state of a system use case model.

The MBC use case documentation comprises one or more use case diagrams and supporting documentation such as use case specifications and actor definitions. Further, the use case models are developed from the perspective of MBC stakeholders.

The following sections provide relevant information about the use case of MBC:

1. Actors
2. Relationships
3. Use Cases
4. System Boundary Boxes

## Actors
There are two generalized categories of actors for the MBC application:

1. **Community user**
2. **Administrator**

Each of the generalized categories of the actors with the MBC application. Several types of specific actors include **administrators**, **community users**, and **community activists**. 
However, each of the particular actors can interchangeably take the role of user or Administrator with the expectation of a Bridge Engineer, whose role will be limited to the user. 

### Administrator
The Administrator's primary role is to moderate, monitor, and maintain the application. The Administrator is responsible for maintaining the proper functioning of the application and data pipeline. Further, this includes maintaining a relation database, which provides for adding, updating, and deleting existing application databases and its pipeline. 

## Administrator
The following is a use case diagram for administrator:
![Use-case of administrator](images/admin-usecase.png)

### System management
- *Integrate applications*
- *Update applications*
- *Manage server*

### Data Management
- *Check data integrity*
    * Capability to maintain the data quality in compliance with [NBI coding guide](https://www.fhwa.dot.gov/bridge/mtguide.pdf).
- *Load data*
    * Timely addition of the NBI and NBE datasets into a relational database.
- *Delete data*
    * Capability to delete erroneous or redundant data.
- *Backup data*
    * Timely backup of the existing database. 
- *Restore data*
    * Capability to restore the database from backup. 

### Profile Management
- *Registration*
- *Login*, includes *Restore password*
- *Logout*
- *Create user*
- *Change user*
- *Restore user*
- *Remove user*

## Community-User 
The primary role of the user is to interact with the existing application. The user will be able to search and select the existing data applications. Further, the users will interact with the application by adjusting data and model parameters. 

### Use cases of Community user
The following is a use case diagram for administrator:
![Use-case of Community User](images/community-user-case.png)


