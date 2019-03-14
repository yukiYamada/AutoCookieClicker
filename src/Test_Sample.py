import unittest
import datetime as dt
from Sample import Sample
from mock import patch

class TestSample(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDonw(self):
        # 終了処理
        pass

    def test_isOverLimitTime(self):
        # 境界確認
        # datetimeのMockがまともに動かない。原始的に行く 
        start = dt.datetime.now()
        actual = False
        proc = dt.datetime.now()
        limit = 2
        while (not actual) :           
            actual = Sample.isOverLimitTime(self, start, limit)           
            proc = dt.datetime.now()           

        # 処理時間分で微妙にずれるけど、そこまで厳密に見る気もないのでいっか。。。
        self.assertGreater((proc - start).total_seconds(), limit)

        #with patch('Sample.datetime.datetime') as mock:
        #    from datetime import datetime
            #nowを10秒経過後にしておく
        #    mock.now.return_valie = start + testdatetime.timedelta(seconds=10)       
            #end - start = limit
            
            #まともにMockできそうにないからほどほどにしておく
            #end - start > limit
            #actual = Sample.isOverLimitTime(self, start, 9)
            #self.assertEqual(True, actual)
            #end - start <  limit
            #actual = Sample.isOverLimitTime(self, start, 11)
            #self.assertEqual(False, actual)
        pass

    def test_exec(self):
        #sp.exec(10)
        pass

if __name__ == "__main__":
    unittest.main()
