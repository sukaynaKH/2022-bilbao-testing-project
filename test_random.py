import pytest
import numpy as np
import logistic as log
from numpy.testing import assert_allclose

#set the random seed for once here
SEED = np.random.randint(0, 2**31)

@pytest.fixture
def random_state():
    print(f'Using seed {SEED}')
    random_state = np.random.RandomState(SEED)
    return random_state

def test_converge(random_state):
    x = random_state.rand()
    result = log.iterate_f(100, x, 1.5)
    print(result)
    assert_allclose(result[-1], 1/3)

# def test_bounded(random_state):
#     x = random_state.rand()
#     result = log.iterate_f(100000, x, 3.8)
#     assert np.all(result < 1) & np.all(result > 0)

# def test_aperiodic(random_state):
#     x = random_state.rand()
#     result = log.iterate_f(100000, x, 3.8)
#     print(result)
#     assert np.unique(result[-1000])
    

