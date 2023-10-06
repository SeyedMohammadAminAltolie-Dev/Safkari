# Safkari
This project is for chain repair shops on the Python Django framework.

here is the ERD of this project

<img width="905" alt="Screenshot 2023-10-06 at 1 15 09 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/fca95a79-1fa0-4d76-bf0d-393f4a956dce">

backend implementation:
In this project, we used the Django framework under the Python language for the dedicated part.
Django Rest Framework (DRF) is a compelling and practical framework for creating web APIs. Suppose you have a website and now you want to create a mobile application for your website. Launch it. Here you can act in two ways. First, design a database for your application exactly like the website, and for every change in the website, apply the changes manually in the application as well. The second way is this Connect the application to the website using the API. With this method, for every change in the website's database, the information in the application will also be updated.
In general, API is a tool that extracts information from the website according to our needs. Therefore, APIs are very important in programming. Django Rest Framework is one of them
Robust tools for implementing Web APIs are developed with Python programming language.

Application Design in DRF
Safkari application is our main application, it contains the main project information, settings file, and project management file.
Company application Our application is for entering the information of the company and its branches, as well as the information of the employees of those branches.
The db.sqlite3 file is our database. At the moment, because we are in the development phase, we use it as Django's default mode.
The Operation application is related to operators' information and how to register them. The car_information application is related to the information of cars and their owners.
The repair_request application is related to smoothing and painting request information and other information including payments and photo albums, additional accessories, and repair items.
<img width="205" alt="Screenshot 2023-10-06 at 1 36 43 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/4a7d95d5-2c52-4a49-9850-7d00f054555a">

Types of requests in the project
In this section, we examine the types of requests and how to create them. In this section, we send all the information to the server in JSON format

• Request to create a company To create a new company
we must apply to the address below and provide the necessary information for registration
api/company/new_company/
<img width="479" alt="Screenshot 2023-10-06 at 1 39 49 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/94a84404-46ac-41ba-bf31-e5bdb21de478">
In response, the server returns the following information.
<img width="394" alt="Screenshot 2023-10-06 at 1 40 15 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/76f35ed4-e95f-4285-8791-d6ea81a0907f">
• Company branch registration request
To register the company branch, we send the information in the following format to the address /api/company/new_branch, please note that instead of the company value, we must put the registered company ID.
<img width="477" alt="Screenshot 2023-10-06 at 1 41 39 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/9f67a7c3-2e80-4de9-ad39-2915df72da6a">
The server returns the following values in response.
<img width="347" alt="Screenshot 2023-10-06 at 1 42 10 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/5940d2dc-fe32-4d66-9ec8-acb32e058f55">
• New worker registration request
To request the registration of a new worker, we must send the worker's information to the /api/company/new_worker/ address, as shown in the images below. The value of branch is the ID of the branch where the worker works.
<img width="410" alt="Screenshot 2023-10-06 at 1 47 08 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/9c48a764-da18-4613-ae1f-961217feb7dd">
The server returns the following values in response
<img width="303" alt="Screenshot 2023-10-06 at 1 47 39 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/ea2b9d89-5223-4ff1-a8d2-2ca7c261a028">
• Operator registration request
To register a new operator, we must first send the operator information to the /api/operation/new_user/ address as shown in the picture below.
<img width="366" alt="Screenshot 2023-10-06 at 1 48 21 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/2e24d9a3-71cc-4535-b1d8-af8fe3f1589e">
The server also includes the following values in the response.
<img width="360" alt="Screenshot 2023-10-06 at 1 48 59 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/a1cef754-6fde-40d7-b2dc-9f0c3f9c614e">
• Operator login
So far we have looked at requests that anyone can create, (registration), but from here on requests are only for logged-in users. To login and authenticate the user, we use Djano oauth 2.0 We did it, it is currently used for Instagram, Facebook, etc.
The first step is to log in as an administrator, and for that we must have a super user, and we must be in the project terminal.
Enter the following command
<img width="514" alt="Screenshot 2023-10-06 at 1 50 54 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/e975cb63-7583-4b19-8395-2b6bbe2af7ae">
Note: Since I set up Python3 in my virtual environment, I entered this command model. Note: In the database, I consider the first company and the first branch as the main management branch and company, which has a higher level of access and is available only to the system owner. After entering this command, enter the necessary information to create our super user. In the second step, we enter the admin panel from the address http://127.0.0.1:8000/admin with the superuser information.

<img width="599" alt="Screenshot 2023-10-06 at 1 51 40 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/21da8c25-408c-4af2-b587-8545efe3404d">

After entering, we are faced with the following page, we have nothing to do with it.

<img width="429" alt="Screenshot 2023-10-06 at 1 52 09 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/4acb71fe-677c-4acd-9adb-c4aa42d21629">

In the next step, we enter the /oauth/applications/ address and create an application on that page.


<img width="644" alt="Screenshot 2023-10-06 at 1 52 34 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/b687e5f5-905f-42b7-8caa-2b12e4452ba5">

On the application creation page, we proceed as shown in the picture below.
<img width="511" alt="Screenshot 2023-10-06 at 1 53 05 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/6a317629-8132-4276-91c2-0906d35c06e4">

Then we click save and we will be transferred to the next page as we can see in the image below.
<img width="446" alt="Screenshot 2023-10-06 at 1 53 34 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/5b3acac8-dad4-4d84-834a-c34025a8a3fc">

We save the values of client id and client secret, and we pay close attention to the security points when storing them, because they are very sensitive values of this project.
In the next step, we send the following values to the /oauth/token/ address for user login.

In Django OAuth 2.0, client ID and client secret are important components used for implementing OAuth 2.0 authentication and authorization. They are typically associated with applications or clients that want to access protected resources on behalf of a user. Here's a brief description of each:

1. **Client ID**:
   - The client ID, also known as the "client identifier" or "client key," is a unique identifier assigned to each OAuth 2.0 client application by the authorization server (OAuth provider). 
   - It is a public piece of information, meaning it is not meant to be kept secret. The client ID is used by the authorization server to identify and verify the client application requesting access to protected resources.
   - When a user initiates the OAuth 2.0 flow by trying to log in or grant permissions to an application, they will often be asked to provide the client ID for the application they are authorizing.
   - It is included in the OAuth 2.0 authorization request and serves as a way for the authorization server to track and validate the client making the request.

2. **Client Secret**:
   - The client secret is a confidential piece of information, known only to the client application and the authorization server. It is used to authenticate the client application to the authorization server during the OAuth 2.0 flow.
   - The client secret should be kept secure and should never be exposed to or shared with the public or end-users. It's used to prove the authenticity of the client application to the authorization server.
   - Typically, it is used in the "client credentials" or "token exchange" grant types of OAuth 2.0, where the client application can directly request an access token from the authorization server by presenting its client ID and client secret.
   - In some cases, the client secret may also be used for refreshing access tokens, depending on the OAuth 2.0 flow being used.

In a Django application implementing OAuth 2.0, you would typically configure the client ID and client secret when you register your application with the OAuth provider (e.g., Google, Facebook, GitHub, etc.). The specific steps for configuring these credentials may vary depending on the OAuth provider you are using.

It's crucial to handle client secrets securely in your Django application, such as storing them in environment variables, and never exposing them in client-side code or public repositories to prevent unauthorized access to your application's resources.

In the next step, we send the following values to the /oauth/token/ address for user login.

<img width="533" alt="Screenshot 2023-10-06 at 1 55 47 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/7dbcc392-3062-41a7-9667-df223ceba992">

The server returns the following values to us.
<img width="478" alt="Screenshot 2023-10-06 at 1 56 20 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/2f239ca4-1840-4c6c-838b-36335255c669">
We store the values of access_token and refresh token. We use the value of access_token for authentication in requests, it is valid for 360,000 seconds. If our token expires, we make another request as shown below

<img width="497" alt="Screenshot 2023-10-06 at 1 57 13 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/f8abedd0-f69a-4999-9131-2c2f954a5569">
In fact, in this method, we don't need to use the password anymore, we send the password only once. In the next step, to use it in places where we need to authenticate, we just need to put the value of access_token in the header (I put the image of Postman software).

<img width="699" alt="Screenshot 2023-10-06 at 1 57 55 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/31932571-e271-466b-a774-c16338d4ee9f">

• List of registered companies
  To get the list of registered companies, you can go to /api/company/companies_list/127.0.0.1:8000
Make a request with the GET method. After sending the request, the server returns the following result.
<img width="403" alt="Screenshot 2023-10-06 at 1 58 38 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/43d0b756-34b2-4822-9469-c4162a13dd24">
• Edit company information
  To edit the information of a company, we must send the value of the company id with the changed field to the address /api/company/Company_edit with the PATCH method.
For example, we want to change the value of the name of the owner of the following company
<img width="506" alt="Screenshot 2023-10-06 at 1 59 17 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/d2ef1240-141d-4cdf-87ac-86b9b3b7100c">

We send it like this.
<img width="357" alt="Screenshot 2023-10-06 at 1 59 57 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/3166f85c-d41b-4f20-b3cd-21a3a71d0063">

The server also returns the following response.


<img width="426" alt="Screenshot 2023-10-06 at 2 00 28 PM" src="https://github.com/SeyedMohammadAminAltolie-Dev/Safkari/assets/33419682/ce766588-a546-4987-b641-2830816ab5a1">

Note: All the edits for the said items are like this. I will mention their address below.
• api/company/ Company_edit/ [name='Company_edit']
• api/company/ branch_edit/ [name='Branch_edit']
• api/company/ worker_edit/ [name='Worker_edit']
• api/operation/ user_edit/ [name='User_Edit']
So far, we have checked all the required methods and fields, and the rest of the requests work the same way (I only put their addresses below).
• api/operation/users_list/[name='Users_list']
• api/company/branches_lists/
• api/company/workers_lists/[name='Workers_list']
• api/car_information/Cars_list/[name='Cars_list']
• api/car_information/CarEdit/[name='Car_edit']
• api/car_information/ Car_owner_list/ [name='Car_owner_list']
• api/car_information/ Car_owner_edit/ ['name='Car_owner_edit]
• api/repair_request/repair_request_list/  ['name='Repair_requests_list]
• api/repair_request/repair_request_edit/  [name='Repair_requests_edit']
• api/repair_request/repair_item_list/ [name='Repair_item_list']
• api/repair_request/repair_item_edit/ [name='Repair_item_edit']
• api/repair_request/album_list/ [name='Repair_item_edit']
• api/repair_request/new_Image/[name='new_Image']
• api/repair_request/image_edit/[name='Image_edit']
• api/repair_request/image_list/ [name='Image_list']
• api/repair_request/new_payment/ [name='New_payment']
• api/repair_request/payment_edit/ [name='payment_edit']
• api/repair_request/payment_liest/ [name='payment_list']

How to implement the project
After extracting the project file, you have created it in the virtual environment, pip install -r /requirements.txt command to install the required libraries. After that, enter the python manage.py makemigrations command, and in the next step of the command, enter the python manage.py migrate command to create the tables and database of the project.
To start the project server, enter the python manage.py runserver command to run the server.
