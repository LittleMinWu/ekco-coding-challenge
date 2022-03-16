------------------This is for coding challenge in Ekco, written by Min.-----------------------

Ekco Coding Challenge

Summary
Your challenge is to fetch and display temperature data for named locations. The details of the APIs to use will be given below. Remember that this challenge is to allow us to evaluate your ability as an engineer; think about what engineer means to you and what if anything distinguishes an engineer from a developer or coder and use your work to demonstrate that difference.

Rules
1.	The code making the calls to the APIs and handling input, output and exceptions must be in Python. 
2.	It is up to you how to display the returned data but you should use either HTML and JavaScript / TypeScript or Python or a mix. Do not use any other language. 
3.	It is your decision whether to develop as a web page or a CLI, both are equally acceptable.
4.	Provide at least basic unit tests with your code
5.	Your code should work with place names such as London, Dublin, Amsterdam, as well as any arbitrary place name.
6.	Your code does not need to work with addresses, post codes, wild cards or search terms
7.	You only need accept one place name at a time; you do not need to handle multiple place names in one call.
8.	Do not worry about retrieving the latitude and longitude for the centre of the given place name: any reasonable values returned from the geocode API are acceptable.

APIs
Use this API from open-meteo.com to retrieve the temperature data. The API can be called as follows: https://api.open-meteo.com/v1/forecast?latitude=[latt]&longitude=[long]&hourly=temperature_2m  
[latt] and [long] variables should be replaced with the correct latitude and longitude for the given place name. 

Use the following API to retrieve the latitude and longitude from a place name: https://geocode.xyz/[place]?json=1

Eg: 
https://geocode.xyz/London?json=1 returns a JSON object from which the latitude and longitude for London, UK can be extracted. These values can then be used in the open-meteo API:

https://api.open-meteo.com/v1/forecast?latitude=51.52&longitude=-0.11&hourly=temperature_2m  
 
Challenge
Write an application that accepts text input of a place name and then retrieves and displays the temperature data for that place. Place names can be arbitrary but examples include: London, Amsterdam, Dublin.

The data can be input via a CLI, a web text box or another method as long as the user can try to retrieve the temperature data for an arbitrary place name. You do not need to handle lists of place names: the program should only handle one place name at a time. You do not need to handle wild card characters or search terms. You do not need to handle addresses.

Use the geocode.xyz API to get the latitude and longitude for the given place name and then use those values to call the open-meteo API as shown above.

You should then display any data set returned from the open-meteo API. You can display the data any way you see fit (graph, table, etc.) but the temperature data should be clearly linked to the time it refers to. Make sure that whatever display method you choose would make sense to a user. 

Users must be able to make multiple consecutive requests and for arbitrary place names.

Make sure to handle your input and data correctly and any exception conditions, including misspelt or non-existent place names. The application should not break nor show non-user-friendly messages or exceptions.

Use any third party libraries you think appropriate.

Output
1.	All code you have written to perform this task. API calls, data and exception handling must be written in Python. Display may be written in HTML and JavaScript / TypeScript OR Python OR both
2.	A set of at least basic unit tests
3.	Screenshots of your output display for a selection of scenarios. The idea is to show your code working and how it handles various scenarios and conditions so have a think about what you should include here.
