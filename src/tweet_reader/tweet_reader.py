def read_tweet_file(file_path):
    with open(file_path) as file:
        content = file.read()
    return content
