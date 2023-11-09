# Marked By Covid (MBC) Web Application Cypress Instructions

# To install Cypress / Run Cypress
1. Ensure that you are using in the project path and in the main markedbycovid directory and then run the following: npm install cypress --save-dev
2. Once it is finished installing address any vulnerabilities by running the following command:  npm audit fix
3. Once this is done you can open cypress by running the following command: npx cypress open
4. If this is your first-time using cypress it will open up with a whats new with cypress screen just click continue.
5. After clicking continue you will be taken to a screen to select either e2e testing or component testing select e2e testing
6. It will then go to a initializing configuration screen. After the configuration initialization it will bring you to a screen to pick the browser to start E2E testing. 
7. In cypress under the specs folder you will find all the test scripts. In the markedbycovid directory the test scripts are located under the cypress folder then the e2e folder. 
8. Pick a test script and double click on it to run the test script. 

# To configure package.json file
```
npm init
```

# Before running test scripts

1. Create a cypress.env.json file and store it in the markedbycovid root directory of the project
2. This cypress.env.json file should include the URLs, usernames and passwords used to access the site.
3. The format of the cypress.env.json file looks like this
```
{

  "BaseUrl": "BaseURL",
  "AdminUrl": "AdminURL",
  "Username": "username",
  "Password": "password",
 
}
```
4. There is a cypress.env.example.json file in the directory that you can use as a template. Just make sure that the cypress.env.json file is in the .gitignore. This file should not be sent to get hub due to the username and password being stored.
Essentially you add the variables in this file that will be used across multiple test scripts.

5. Ensure that data-cy attributes are placed in the vue pages so that they can be used and referenced in test scripts. This is a cypress best practice. These will go where data is inputted or where buttons are clicked. Here is an example of a data-cy attribute on a vue page: 

```
<v-text-field data-cy="first_name" v-model="firstname" :rules="firstNameRules" label="First Name*"
```
These data-cy attributes are important because div, ID, and other CSS elements can change frequently but if your test script targets a data-cy attribute if the CSS/HTML/VUE code is changed then the test script will not need to be updated because it will be able to still select / input data in that field.

There are places such as the django admin pages that cannot be modified to use data-cy attributes so in this case it is ok to use the div, ID, or additional element finding methods in your test scripts. 

6. Create json files for all of the inputs that are needed in the test scripts. These test scripts should be located in following directory: Cypress/e2e/fixtures/

```
import AdminData from "/cypress/fixtures/AddAdmin.json"

```
The word that shows up after import is a name that is customizable and any meaningful name can be used. 

After they are imported then you can you can use the data that is in there in the test scripts like this: 
```
cy.get('input[id="id_username"]').click().type(LoginData.Username)
```
This tells the code to look in the file that is imported with the name LoginData and type the data that is stored for the username in that file.

#Additional Notes: 

Make sure to store all admin scripts in the admin scripts folder. These are the scripts that perform actions on the django admin console. 

Make sure to store all of the frontend scripts in the frontend scripts folder. These are all the scripts that will run against the website itself that everyone is able to access. 

The wagtail URLs are in the WagtailUrls.json file and not in the main cypress.env.json file. Since these are only use in wagtail specific test scripts we moved them to their own .json file. 
Any other wagtail specific URLs that are not in the WagtailUrls.json file are in the respective wagtail test script they are needed in. 


Set your cypress path to the main markedbycovid directory
C:\Users\*yourusername*\PycharmProjects\markedbycovid


