
import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join('../')))

from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor

_, tweet_list = read_json("C:/Users/samrit/Desktop/10 accadamay/week0/Twitter-Data-Analysis/data/Economic_Twitter_Data.json")


columns = ['created_at', 'source', 'original_text', 'clean_text', 'sentiment', 'polarity', 'subjectivity', 'lang', 'favorite_count', 'retweet_count',
           'original_author', 'screen_count', 'followers_count', 'friends_count', 'possibly_sensitive', 'hashtags', 'user_mentions', 'place', 'place_coord_boundaries']


class TestTweetDfExtractor(unittest.TestCase):
    """
                A class for unit-testing function in the fix_clean_tweets_dataframe.py file

                Args:
        -----
                        unittest.TestCase this allows the new class to inherit
                        from the unittest module
        """

    def setUp(self) -> pd.DataFrame:
        self.df = TweetDfExtractor(tweet_list[:5])

   # def test_find_statuses_count(self):
    #    self.assertEqual(self.df.find_statuses_count(), [
      #                   204051, 3462, 6727, 45477, 277957])

    def test_find_full_text(self):
        text = ['RT @nikitheblogger: Irre: Annalena Baerbock sagt, es bricht[654 chars]sc…', 
                'RT @sagt_mit Merkel sch[524 chars] sc',
                'RT @Kryptonoun @WRi007 Pharma in Lebensmitteln, Trinkwasser, in der Luft oder in der Zahnpasta irgendwo muss ein Beruhigungsmittel bzw Be',
                'RT @WRi007 Die #Deutschen sind ein braves Volk Mit #Spritpreisen von 2 Euro abgefunden Mit #inflation abgefunden Mit hheren #Abgaben',
                'RT @RolandTichy Baerbock verkndet mal so nebenhin in Riga das Ende der Energieimporte aus Russland Habeck rudert schon zurck, Scholz sc']

        self.assertEqual(self.df.find_full_text(), text)

   # def test_find_sentiments(self):
      #  self.assertEqual(self.df.find_sentiments(self.df.find_full_text()), ([0.16666666666666666, 0.13333333333333333, 0.3166666666666667, 0.08611111111111111, 0.27999999999999997], [
          #               0.18888888888888888, 0.45555555555555555, 0.48333333333333334, 0.19722222222222224, 0.6199999999999999]))

    def test_find_created_time(self):
        created_at = ['Fri Apr 22 22:20:18 +0000 2022', 'Fri Apr 22 22:19:16 +0000 2022', 'Fri Apr 22 22:17:28 +0000 2022',
                      'Fri Apr 22 22:17:20 +0000 2022', 'Fri Apr 22 22:13:15 +0000 2022']

        self.assertEqual(self.df.find_created_time(), created_at)

    def test_find_source(self):
        source = ['<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', 
                  '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
                  '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', 
                  '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
                  '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>']

        self.assertEqual(self.df.find_source(), source)

    def test_find_screen_name(self):
       name = ['McMc74078966', 'McMc74078966',
                'McMc74078966', 'McMc74078966', 'McMc74078966']
       self.assertEqual(self.df.find_screen_name(), name)

    def test_find_followers_count(self):
        f_count = [3, 3, 3, 3, 3]
        self.assertEqual(self.df.find_followers_count(), f_count)

    def test_find_friends_count(self):
        friends_count = [12, 12, 12, 12, 12]
        self.assertEqual(self.df.find_friends_count(), friends_count)

    def test_find_is_sensitive(self):
        self.assertEqual(self.df.is_sensitive(), [
                         None, None, None, None, None])

    def test_find_favourite_count(self):
        self.assertEqual(self.df.find_favourite_count(),
                         [12, 12, 12, 12, 12])

    def test_find_retweet_count(self):
        self.assertEqual(self.df.find_retweet_count(), [355, 505, 4, 332, 386])

    def test_find_hashtags(self):
        self.assertEqual(self.df.find_hashtags(), [
                         [], [], [],[{'text': 'Deutschen', 'indices': [16, 26]}, {'text': 'Spritpreisen', 'indices': [54, 67]}, {'text': 'inflation', 'indices': [95, 105]}, {'text': 'Abgaben', 'indices': [130, 138]}], []])

    def test_find_mentions(self):
        self.assertEqual(self.df.find_mentions(), [[{'screen_name': 'nikitheblogger', 'name': 'Neverforgetniki', 'id': 809188392089092097, 'id_str': '809188392089092097', 'indices': [3, 18]}],
                      [{'screen_name': 'sagt_mit', 'name': 'Sie sagt es mit Bildern', 'id': 1511959918777184256, 'id_str': '1511959918777184256', 'indices': [3, 12]}],
                       [{'screen_name': 'Kryptonoun', 'name': 'Kryptoguru', 'id': 951051508321345536, 'id_str': '951051508321345536', 'indices': [3, 14]}, {'screen_name': 'WRi007', 'name': 'Wolfgang Berger', 'id': 1214543251283357696, 'id_str': '1214543251283357696', 'indices': [16, 23]}],
                      [{'screen_name': 'WRi007', 'name': 'Wolfgang Berger', 'id': 1214543251283357696, 'id_str': '1214543251283357696', 'indices': [3, 10]}], 
                       [{'screen_name': 'RolandTichy', 'name': 'Roland Tichy', 'id': 19962363, 'id_str': '19962363', 'indices': [3, 15]}]])

   # def test_find_location(self):
    #    self.assertEqual(self.df.find_location(), [
      #                   'Mass', 'Edinburgh, Scotland', None, None, 'United Kingdom'])


if __name__ == '__main__':
    unittest.main()