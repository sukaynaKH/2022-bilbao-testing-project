# import pytest
# import logistic as log
# from math import isclose

# @pytest.mark.parametrize("x,r,expected",[(0.1, 2.2,0.198),(0.2,3.4,0.544),(0.75,1.7,0.31875)])
# def test_log(x,r,expected):

#     output = log.logistic_map(x,r)
#     assert isclose(output,expected)

# @pytest.mark.parametrize("it,x,r,expected",[(1,0.1, 2.2,[0.198]),(4, 0.2, 3.4, [0.544]),(0.75,1.7,0.31875)])
# def test_log(x,r,expected):

#     output = log.logistic_map(x,r)
#     assert isclose(output,expected)