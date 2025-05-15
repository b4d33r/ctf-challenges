# 🕵️ F1ndM1 Challenge — Writeup

### Solution

* Use **[https://www.idcrawl.com/username-search](https://www.idcrawl.com/username-search)** to find linked accounts for **F1ndM1IfYouC4n**.
* On the X account, find a video with Morse code. Decoding it gives `discoed.gg/bio`.
* The word **bio** refers to the X account’s bio text. Replace `bio` in the URL with the actual bio text from the X account to get a Discord invite link.
* Join the Discord server; you find a T9 cipher in a message.
* From decoding the T9 cipher, you understand you need to talk to the bot in the server.
* The bot asks you *"Ajeeya wld fin nta?"*, and you respond with **manik**.
* The bot then guides you to explore **b4d33r**’s connection on the CTF server.
* Find a Spotify profile linked in **b4d33r**’s profile with a public playlist.
* Use numbers from the X account as the order to pick the first letter of each song title in the playlist.
* The collected letters reveal the flag.
