---
author: pushtaev
id: 19
published: 2018-03-23
sequence: http-redirect
---

# HTTP redirect

Imagine you are moving your web-API from HTTP to HTTPS.
How do you handle all requests from clients who are not aware they should use HTTPS?
You set up redirection rules.

What HTTP status code should you use?
The choice is usually between **301 Moved Permanently** and **302 Found**.
The first one is permanent (as the status name states)
and the second one is one-off and never cached.
Moving to HTTPS is usually permanent, so the choice is obvious,
it's **301 Moved Permanently**.

The problem with both **301** and **302** is that they work properly only
for HEAD and GET requests.
Though all other methods (such as POST) should work as well according to RFC,
they don't.
A lot of modern HTTP-clients (your favorite browser probably included)
make GET requests after the redirection despite the original request method.
That became so usual that RFC now explicitly says,
that you couldn't rely on the client persisting the method.

To fight that problem two other codes were introduced:
**303 See Other** and **307 Temporary Redirect**.
**303** says *use GET for the new request*
and **307** means *use the same method for the new request*.
So basically most of the client s do **303** instead of **302** while they should do **307**.

Sadly, both **303** and **307** are temporary.
To make a redirect that both method-persisting and permanent
one can use **308 Permanent Redirect**, but that code is still experimental.

So the correct solution for our HTTP to HTTPS migration is to use
**307 Temporary Redirect**.
**308** is even better, but can't be relied on.
Mind that human users usually start an interaction by sending GET request,
so the problem with **301** only applies to robots.
