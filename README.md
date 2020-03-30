# recommendation-engine

## What work's and what doesn't?

1. <strike>The project only runs without any issues on PyCharm.</strike> 
    It can be run simply from a command prompt.
2. <strike>The first file, that you must run is createConfig.py to set up the paths.</strike>
    No need of running this file seperately.
3. <strike>This does not yet produce any recommendations, needs a lot of fixing.</strike>
    It does generate recommendations based on the genre(s) for which the user has seen the **maximum** number of movies, and the
    recommendations are movies from that genre(s) which the user has **not** seen.

## How to generate recommendations?

Generating recommendations is as simple as running the generateRecommendations.py file, and providing it a user id as input. 

<code>python generateRecommendations.py</code>

**Note** that recommendations are displayed in an instant if the user ids are between 1 and 32, as they have already been generated, where as generating recommendations for other users takes about 20 - 30 minutes.

