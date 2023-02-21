import spacy
nlp = spacy.load('en_core_web_md')

# Read movies.txt and store each movie as an item in movie_list
movie_list = []
with open('movies.txt', 'r') as movies:
    for line in movies:
        movie_list.append(line.replace('\n', ''))

# Function that compares a given movie description to the movie descriptions in movies.txt
def recommend(description):
    recommendations = []
    for i in movie_list:
        token = nlp(i)
        recommendations.append(float(nlp(description).similarity(token)))
    location = recommendations.index(max(recommendations))
    print('The most similar movie is ' + ' '.join(movie_list[location].split()[0:2]))

planet_hulk_description = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the lluminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator'''

recommend(planet_hulk_description)