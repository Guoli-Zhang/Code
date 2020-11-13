from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import jieba


def jieba_demo(text):
    """

    :param text:
    :return:
    """
    ret = jieba.cut(text)
    ret = list(ret)
    text = " ".join(ret)
    return text


if __name__  == "__main__":
    pass
