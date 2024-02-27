import snscrape.modules.twitter as sntwitter

# Spécifiez le hashtag ou l'utilisateur à partir duquel vous voulez extraire les tweets
search_query = "#finance"

# Créez un scraper TwitterSearchScraper
scraper = sntwitter.TwitterSearchScraper(search_query)

# Parcourez les tweets et extrayez le texte et les réactions
for tweet in scraper.get_items():
    tweet_text = tweet.content # Récupère le texte du tweet
    retweets = tweet.retweetCount # Récupère le nombre de retweets
    likes = tweet.likeCount # Récupère le nombre de likes

    # Faites quelque chose avec les données extraites
    print("Texte du tweet :", tweet_text)
    print("Retweets :", retweets)
    print("Likes :", likes)
    print("-----------------------")
