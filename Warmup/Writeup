### JWT Authentication Challenge — Writeup
I found the JWT token stored in a cookie after logging in.

Using jwt_tool, I brute forced the secret key pasosdegigante.

With the secret key, I forged a new JWT token with "role": "admin" and replaced the original cookie with the forged token.

This gave me admin access and revealed the flag on the /login.

The exploit script is provided in [`exploit.py`](exploit.py)
