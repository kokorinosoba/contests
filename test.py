import time
import collections
times = []
# x = "hehe"
# A = collections.deque([i for i in range(1000000)])
# a = 1
#A = [i for i in range(100000)]
"""
def test(B):
    B[10] = 12345
    return B
"""
for i in range(10000):

    # A = list(i for i in range(1000000))

    start = time.time()
    # del A[0]         0.0074714446067810055
    # A.pop(0)         0.007406091690063477
    # A.popleft()      1.2159347534179688e-05
    # A = A[1:]        0.013241753578186036
    # A.insert(100, x) 0.004876136779785156
    # A.insert(100, x) 1.5020370483398438e-05
    # A = A[100:] + [x] + A[101:] 0.05580425262451172

    # A = [int(n) for n in input().split()] 0.014417171478271484
    # A = list(map(int, input().split()))   0.013602972030639648

    # print([0, 1][a == 1]) 5.099773406982422e-06
    """ 5.085468292236328e-06
    if a == 1:
        print(1)
    else:
        print(0)
    """
    # print(1 if a == 1 else 0) 4.365444183349609e-06

    # for _ in range(100000): 0.003777163028717041
    # for _ in [0]*100000:    0.002701156139373779

    # A = test(A) 3.1894922256469724e-07
    # test(A) 3.023958206176758e-07

    # evalはめっちゃ遅い
    # sum(map(int,a)) 0.001547907018661499
    # eval("+".join(a)) 0.0116243084192276
    # "+".join(a) 0.0001213904619216919n

    times.append(time.time() - start)

print(sum(times) / len(times))
