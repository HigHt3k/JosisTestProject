from src.math.calculator import add, substract
from src.tweet_reader.tweet_reader import read_tweet_file

def test_function():
    print("hi")


if __name__ == "__main__":
    test_function()

    a = add(5, 10)
    b = substract(10, 5)

    print("a: ", a)
    print("b: ", b)

    print(read_tweet_file("../res/tweets/tweets.txt"))