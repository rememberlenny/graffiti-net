# Graffiti Net

A way to document all unique street art in the world and create a genealogy of all publicly visual media (using machine learning).

## What

These are a few scripts that were used to show 5,623 photos cluster the similar artists based on 25,088 dimensions. [1]

![-- working](https://user-images.githubusercontent.com/1332366/45318320-96da7600-b50a-11e8-88c7-f57835c819e7.gif)

The mouse in this link [2] shows two artists, Banksy and Blek le Rat - who has similar styles.

![-- banksy](https://user-images.githubusercontent.com/1332366/45318319-95a94900-b50a-11e8-9439-efad44c4f4b3.gif)

I can share the dataset of images for anyone who is interested. There are 15 artists and ~5300 photos. Shoot me a message on Twitter [5].

The encoded features (using VGG16) are in a hdf5 file that I can also share for anyone interested.

The clustering is done using the Annoy (Approximate Nearest Neighbors OY) [6] from @SpotifyEng - I tried to use FAISS [7], but struggled with the instructions. Apparently its significantly faster, but the documentation wasn't great.

[^1] https://twitter.com/rememberlenny/status/1038992069094780928
[^2] https://twitter.com/rememberlenny/status/1038994489896042497
[^5] https://twitter.com/rememberlenny
[^6] https://github.com/spotify/annoy
[^7] https://github.com/facebookresearch/faiss
