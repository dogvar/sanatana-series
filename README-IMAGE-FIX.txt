Image display fix (29 October 2026)

Original source illustrations are PORTRAIT 378 x 506 px. Earlier CSS used object-fit: cover in short landscape frames, which cropped off people, Yamraj, crocodile, etc.

Fix: figures now preserve full portrait dimensions using width: 100%, max-width: 520px, height: auto and object-fit: contain. Captions appear BELOW images. Hero displays the entire portrait illustration on the right on desktop, and below the hero text on mobile. Both English and Hindi updated.

Upload the complete package maintaining the images/ directory.
