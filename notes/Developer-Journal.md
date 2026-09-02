# AI Engineer Bootcamp Journal

## About Me

Name: Hemant Rai

Goal:
Become an AI Engineer capable of building production-ready AI applications using Machine Learning, Generative AI, RAG, AI Agents, FastAPI, Docker, and AWS.

---

# Day 1

## What I Did

- Created AI-Engineer-Bootcamp folder
- Organized project structure
- Set up VS Code workspace
- Started AI Engineer Bootcamp

---

## Why I Started

I want to become an AI Engineer and build production-ready AI applications instead of just completing tutorials.

---

## Current Skills

Python ⭐⭐⭐☆☆

SQL ⭐⭐⭐☆☆

Machine Learning ⭐⭐☆☆☆

FastAPI ⭐☆☆☆☆

Docker ☆☆☆☆☆

AWS ☆☆☆☆☆

Generative AI ⭐☆☆☆☆

---

## Projects Completed

None

## Date 8/July
## What is Internet?
Internet is a network between computers

## What is Client ?
Any device or sofware which request for some data is a Client

## What is a Server?
A server is a body which recieves the Request by Client

## Why do computers need IP addresses?
To differentiate between others and to communicate among other computers

## Why do we use domain names like google.com instead of IP addresses?
so that we dont have to remember the complex IP Address

## What is DNS, in your own words?
DNS Stands for domain name system which represents a unique IP Address and we dont have to remember complex IP addresses

### What is HTTP?
HTTP Stands for Hypertext Transfer Protocol and it is a language which computers use to communicate between them

## Why do we need HTTP?
we need HTTP to run and use softwares 

## What is an HTTP request?
An HTTP request is a message sent by the client to server which contains information about how and what data user is asking for 

## What is an HTTP response?
An HTTP response is a message sent to the client by server which contains the data which user have asked for

## What are headers?
Headers are used in HTTP which contain metadata

## What is the request body?
request body contains the metadata data or the information about the data which user have asked for

## Why does FastAPI use HTTP?
Fast api uses HTTP To generate the response which has to be given to the user

## Write the request–response journey from your browser to a website.
My IP address --> browser --> HTTP request--> Server of the website --->HTTP response--> My Device

## What is CRUD?
CREATE , READ , UPDATE , DELETE

## Whatsapp API design

1) Create account --    POST
2) message user --      POST
3) Sending file --      POST
4) Editing Messages --  PUT
5) Deleting messages -- DELETE
6) UPLOADING Video --   POST
7) Deleting File --     DELETE
8) Forward Message --   POST 

## Status Codes Meanings
200 --> OK 
201 --> Created new Data
204 --> Deleted Data
400 --> Client Side Error
401 --> No login/Unauthorized
403 --> No Access/Permission
404 --> Not Found
500 --> Server Side Error

## What is JSON
JSON stands for Javascript Object Notation and is a format where data is passed from one system to another

## Why do we use JSON?
We use it for CRUD Operations
 
## Difference between JSON and Python Dictionary.

## Explain every JSON data type.
String,Number,Date,Boolean

## Where is JSON used in AI applications?
for using APIS 

## Date- 09/07/2026

## What is FastAPI?
FastAPI is a modern Python web framework used to build REST APIs. It receives HTTP requests from clients, executes Python code, and returns HTTP responses, usually in JSON format.
It acts as a bridge between applications (such as websites, mobile apps, or AI systems) and Python code.

## Why do we need FastAPI?
FastAPI allows different applications to communicate with each other over the Internet using HTTP.
Without FastAPI, a Python program only runs on your local computer.
With FastAPI, your Python application can be accessed by:
Websites,Mobile applications,Other backend services,AI systems,Machine Learning models
FastAPI makes it easy to expose Python code as web APIs.

## Why can't a Machine Learning model on your laptop be used directly by millions of users?
A Machine Learning model running on a laptop is only accessible on that local machine.
Users on the Internet do not have direct access to your laptop.
FastAPI exposes the model through an HTTP API so that users can send requests over the Internet and receive predictions.

## Why do AI Engineers commonly use FastAPI?
AI Engineers prefer FastAPI because it provides:
High performance,Easy API development,Automatic API documentation (Swagger UI),Automatic request validation
JSON support
Asynchronous programming support
Excellent integration with Python AI libraries such as

## Explain the difference between a Library and a Framework.
Library
A library is a collection of reusable code that your program calls whenever you need it.
You are in control.
Framework
A framework controls the execution of your program.
It decides when to call your code.
Example:
When a browser sends:
FastAPI decides which Python function should execute.
You do not call FastAPI.
FastAPI calls your function.

## What is Uvicorn?
Uvicorn is an ASGI web server that runs FastAPI applications and listens for HTTP requests from clients.

## Why do we need Uvicorn?
We need Uvicorn because it starts the FastAPI application, listens for incoming HTTP requests, and sends responses back to the client.

## What is FastAPI?
FastAPI is a Python web framework used to build REST APIs that allow different applications to communicate over HTTP.

## What happened when you ran uvicorn main:app --reload?
Uvicorn started the FastAPI application, loaded the app object from main.py, and began listening for HTTP requests on http://127.0.0.1:8000.

## What did you see at http://127.0.0.1:8000?
I saw the JSON response returned by my FastAPI application

## What is Swagger UI?
Swagger UI is an automatically generated API documentation provided by FastAPI that allows developers to view, test, and interact with APIs directly from the browser.

## DATE 10/7/26

## What does from fastapi import FastAPI do?
It imports the FastAPI class from the FastAPI package so that we can create a FastAPI application.

## What is FastAPI()?
FastAPI() creates a FastAPI application object that manages routes, requests, responses, and application settings.

## Why do we create app = FastAPI()?
We create an app object because it represents our web application and stores all routes, configurations, and middleware.

## What is a decorator?
A decorator registers a Python function with FastAPI and tells it which function to execute for a specific HTTP request.

## What does @app.get("/") tell FastAPI?
It tells FastAPI to execute the home() function whenever a GET request is made to the "/" route.

## Who calls home()?
FastAPI calls the home() function when a matching HTTP request is received.

## 8. Who converts the Python Dictionary into JSON?
FastAPI automatically converts the Python Dictionary into JSON before sending the HTTP response.

## Explain what happens when a user visits  http://127.0.0.1:8000/about
1) The browser sends a GET request to /about.
2) Uvicorn receives the request.
3) Uvicorn passes the request to FastAPI.
4) FastAPI searches its routing table.
5) FastAPI finds the matching route (@app.get("/about")).
6) FastAPI executes the about() function.
7) The function returns a Python Dictionary.
8) FastAPI converts the dictionary into JSON.
9) Uvicorn sends the HTTP response.
10) The browser displays the JSON response


## Date - 11/07/2026

## What happens if a requested route doesn't exist?
FastAPI searches its routing table. If no matching route is found, it returns 404 Not Found.

## Can two functions have the same HTTP method and route?
No

## ## What is a Path Parameter?
A Path Parameter is a dynamic value in the URL that FastAPI extracts and passes to a function to identify a specific resource.

## Why do we use Path Parameters?
We use Path Parameters to make APIs dynamic and scalable, allowing one endpoint to handle multiple resources instead of creating many endpoints.

## What does `student_id: int` mean?
It is a type hint that tells FastAPI `student_id` must be an integer, and FastAPI automatically validates it.

## What happens when we visit `/students/25`?
FastAPI extracts `25` as `student_id`, executes the matching function, converts the returned Python dictionary into JSON, and sends it back to the browser.

## Why use Path Parameters instead of creating multiple endpoints?
Path Parameters reduce code duplication and allow one endpoint to serve unlimited resources dynamically.

## What is the difference between a Static Route and a Dynamic Route?
A Static Route has a fixed URL (e.g., `/students`), while a Dynamic Route contains variables that change for different requests (e.g., `/students/{student_id}`).

## What is Route Matching?
Route Matching is the process where FastAPI compares the incoming request URL with registered routes and executes the matching function.

## What is a Type Hint?
A Type Hint specifies the expected data type of a variable or parameter and helps FastAPI validate incoming data.

## Does FastAPI automatically convert Path Parameters to the specified type?
Yes. FastAPI automatically converts the path parameter to the specified type (such as `int`) and returns a validation error if the conversion fails.

## What happens if the Path Parameter type is invalid?
FastAPI returns a validation error (HTTP 422 Unprocessable Entity) if the provided value does not match the expected type.

## Can Path Parameters be only integers?
No. Path Parameters can also be strings, floats, UUIDs, and other supported data types.

## Where are Path Parameters commonly used?
They are commonly used to fetch, update, or delete a specific resource such as a student, product, user, order, or employee.

## What is a Query Parameter?
A Query Parameter is a key-value pair added to the URL after the `?` symbol. It is used to filter, search, sort, or customize the data returned by an API.

## Why do we use Query Parameters?
We use Query Parameters to filter, search, sort, or customize the data returned by an API without changing the endpoint.

## What is the difference between Path Parameters and Query Parameters?
Path Parameters identify a specific resource, while Query Parameters are used to filter or customize the returned data. Path Parameters are part of the URL path, whereas Query Parameters appear after the `?` symbol.

## What does `&` do in a URL?
The `&` symbol separates multiple Query Parameters in a URL.

## What is the difference between required and optional Query Parameters?
A required Query Parameter must be provided by the user. An optional Query Parameter has a default value and can be omitted.

## When should we use a Path Parameter?
Use a Path Parameter when identifying a specific resource, such as a user, student, or product.

## When should we use a Query Parameter?
Use Query Parameters when filtering, searching, sorting, or customizing the returned data.

## Date 12/07/2026

## Why do we use a Request Body instead of Path or Query Parameters?
We use a Request Body to send large and structured data to the server. It keeps the URL clean and is mainly used for creating or updating resources.

## Which HTTP methods commonly use a Request Body?
POST, PUT, and PATCH commonly use a Request Body to send data to the server.

## What is Pydantic?
Pydantic is a Python library used for data validation and parsing. It ensures incoming data matches the expected structure and data types.

## What is `BaseModel`?
`BaseModel` is a Pydantic class used to define the structure of incoming data and automatically validate its fields and data types.

## What does `class Account(BaseModel):` do?
It creates a Pydantic model that defines the expected structure of the request body and validates the incoming user data.

## What happens if the client sends invalid data?
FastAPI returns a **422 Unprocessable Entity** error if the incoming data does not match the expected data types or required fields.

## Why is automatic validation useful?
Automatic validation prevents invalid data from entering the application, maintains data consistency, reduces bugs, and improves application reliability.

## What happens if a required field is missing in the Request Body?
FastAPI returns a **422 Unprocessable Entity** error because the request body does not match the required Pydantic model.

## Date 13/07/2026

## What is a Pydantic Model?
A Pydantic Model defines the structure of incoming data and automatically validates it.

## Why do we use Pydantic?
We use Pydantic to validate incoming data, enforce data types, and improve data consistency.

## What is `Optional`?
`Optional` allows a field to be omitted or have a value of `None`.

## What is the difference between an Optional field and a field with a default value?
An Optional field can be omitted and defaults to `None`, while a field with a default value automatically uses the specified value if none is provided.

## What is `EmailStr`?
`EmailStr` is a Pydantic type that validates whether the provided value is a valid email address.

## What is `Field()`?
`Field()` is used to define validation rules such as minimum length, maximum length, and numeric limits for model fields.

## Why do we use validation?
Validation prevents invalid data from entering the application, maintains data consistency, and improves application reliability.

## What is a Nested Model?
A Nested Model is a Pydantic model used as a field inside another Pydantic model.

## Why do we use Nested Models?
Nested Models organize related data, improve code readability, and make complex request bodies easier to manage.

## What is `List[str]`?
`List[str]` represents a list containing multiple string values of the same data type.

## What is a Response Model?
A Response Model defines the structure of the data returned by an API and automatically filters out any fields not included in the model.

## Why do we use Response Models?
We use Response Models to hide sensitive data, maintain security, validate responses, and keep API responses consistent.

## What is the difference between a Request Model and a Response Model?
A Request Model validates incoming data from the client, while a Response Model controls and validates the data sent back to the client.

## What does `response_model=UserResponse` do?
It tells FastAPI to return only the fields defined in the `UserResponse` model, even if the original object contains additional fields.

## Why shouldn't sensitive data be returned by an API?
Sensitive data such as passwords, tokens, and personal information should not be returned to protect user privacy and application security.

## Can the original object contain more fields than the Response Model?
Yes. The original object can contain additional fields, but FastAPI only returns the fields defined in the Response Model.

## What happens if the returned object has extra fields?
FastAPI automatically removes the extra fields and returns only the fields specified in the Response Model.

## DATE -- 16/07/2026

## Why do we use `GET /students/{student_id}`?
We use `GET /students/{student_id}` to retrieve a specific student's information using their unique ID.

## Why do we use a `for` loop?
We use a `for` loop to iterate through the list and find the student whose ID matches the requested ID.

## What does `student.id == student_id` check?
It checks whether the current student's ID matches the ID provided by the user.

## What happens if no student is found?
The API returns a "Student Not Found" message. In production APIs, this is typically returned with a **404 Not Found** status.

## Why is `student_id` an integer?
Student IDs are numeric identifiers, so using `int` allows FastAPI to validate the input and makes comparisons easier.

## What is the time complexity of searching a list using a `for` loop?
The time complexity is **O(n)** because Python may need to check every element in the list in the worst case.

## DATE -- 17/07/2026

## What is the purpose of the PUT method?
The PUT method is used to update or completely replace an existing resource.

## Why do we use `enumerate()`?
`enumerate()` returns both the index and the element while iterating through a list.

## Why can't we simply write `student = updated_student`?
Because it only changes the local variable and does not update the original list. We must update the list using its index.

## What does `students[index] = updated_student` do?
It replaces the existing student object at the specified index with the updated student object.

## What happens if the student ID is not found?
The API returns a "Student Not Found" message. In production APIs, this is usually returned with a **404 Not Found** status.

## What is the difference between PUT and POST?
POST is used to create a new resource, while PUT is used to update or replace an existing resource.

## What is the difference between PUT and PATCH?
PUT replaces the entire resource, while PATCH updates only the specified fields without replacing the whole resource.

## What is the purpose of the DELETE method?
The DELETE method is used to remove an existing resource from the system.

## Why do we use `enumerate()`?
`enumerate()` returns both the index and the element while iterating through a list.

## What does `students.pop(index)` do?
It removes the element at the specified index from the list and returns the removed element.

## Can we use `del students[index]` instead of `pop(index)`?
Yes. Both remove an element from the list. `pop()` returns the removed element, while `del` only removes it.

## Why doesn't a DELETE request usually need a request body?
The resource to delete is identified by the path parameter in the URL, so a request body is usually not required.

## What happens if the student ID doesn't exist?
The API returns a "Student Not Found" message. In production APIs, this is usually returned with a **404 Not Found** status.

## Difference between GET, POST, PUT, and DELETE
- GET retrieves data.
- POST creates a new resource.
- PUT replaces or updates an existing resource.
- DELETE removes an existing resource.

## Why is `students = []` not suitable for production?
A Python list is temporary, not shared across multiple users, and does not scale well for large amounts of data.

## What happens to data in a Python list when the server stops?
The data is stored in RAM, so when the application stops, all data is lost.

## What is a database?
A database is a system that stores, organizes, retrieves, updates, and deletes data permanently.

## Why do companies use PostgreSQL?
Companies use PostgreSQL because it provides permanent storage, supports millions of records, allows multiple users, offers fast searching through indexes, and manages relationships between tables.

## What is SQLAlchemy?
SQLAlchemy is an ORM that allows developers to interact with a database using Python objects instead of writing raw SQL for every operation.

## What does ORM stand for?
ORM stands for **Object Relational Mapper**.

## Which component stores data permanently?
PostgreSQL stores data permanently.

## Explain the request flow.
Client → FastAPI → Pydantic Validation → SQLAlchemy → PostgreSQL → SQLAlchemy → FastAPI → JSON Response → Client



