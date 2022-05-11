import sys
sys.path

sys.path.append("/Users/vinlok/github_personal/vinlok/vinlok.github.io/_posts/algorithms/practical_code")
sys.path

from count_words_new import CountWords


def test_count_words():

    driver=CountWords("words1.txt")
    result=driver.DoIt()    
    assert result == [('vinayak', 1)], "should return"