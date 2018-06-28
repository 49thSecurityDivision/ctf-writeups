### Challenge Description:

I don't like taking baths.

[http://web4.ctf.tamu.edu](http://web4.ctf.tamu.edu/)

### Challenge Solution:

Visiting the link takes us to a simple login page. 

The name of the page is SQLi (which is a pretty big clue). 

If you tinker with the login (try 'admin'/'password' combo, etc.), you get various messages back from the server. But when you start tinkering with SQL injection attacks you get a little bit more back. 

This challenge is designed to be very simple in comparison to a real SQLi attack, but if you DuckDuckGo around for SQLi basics   
(here are the first 3 hits I got back on DuckDuckGo all of which include an explanation of the solution to this challenge:
1) https://www.youtube.com/watch?v=h-9rHTLHJTY

2) https://www.w3schools.com/sql/sql_injection.asp

3) https://www.veracode.com/security/sql-injection ) 

you will come across some suggestions for getting started and a good explanation or two. 

Since I'm no expert, here is a brief explanation and suggestion from a resource I just found on the web:

#### Under normal operation, the user with ID 984 might be logged in, and visit the URL:  
  
  
  
#### https_:_//bankingwebsite/show_balances?user_id=984

#### This means that [the variable] accountBalanceQuery [as a SQL request] would end up being:

```sql
SELECT accountNumber, balance FROM accounts WHERE account_owner_id = 984
```

#### This is passed to the database, and the accounts and balances for user 984 are returned, and rows are added to the page to show them.

#### The attacker could change the parameter “user_id” to be interpreted as:

```sql
0 OR 1=1
```

#### And this results in accountBalanceQuery being:

```sql
SELECT accountNumber, balance FROM accounts WHERE account_owner_id = 0 OR 1=1
```

#### When this query is passed to the database, it will return all the account numbers and balances it has stored, and rows are added to the page to show them. The attacker now knows every user’s account numbers and balances

This explanation is a good one because the suggested attack does ***not*** work on this challenge. It just gives you an idea of what you are looking for. 

Anyway, toying with some SQL attacks you find that you don't even need to enter a username. You can just enter **' or 'a'='a** into the password field (note the single quote that starts the entry). But, this isn't the only entry that works. Try it out and find some more!

Submitting the password returns this:

**gigem{ScRuB7h3InpU7}**
