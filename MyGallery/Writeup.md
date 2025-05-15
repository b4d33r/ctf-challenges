# MyGallery Challenge — Writeup

This challenge involved exploiting an insecure cookie to read the flag.

The app sets an `image_data` cookie with a serialized PHP object containing an image path.

I crafted a malicious cookie value pointing the object’s path to `flag.txt` (encoded in base64).

After uploading a dummy image to initialize the session, I set the forged `image_data` cookie in my requests.

Visiting `view.php` with the modified cookie revealed the flag inside a hidden `<pre>` tag.

The exploit script is provided in [`exploit.py`](exploit.py).
