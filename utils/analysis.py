import numpy as np
from scipy import signal

def correlate_trends(x_main, x_sec):

    corr = signal.correlate(x_main, x_sec)
    corr /= np.max(corr)

    lags = signal.correlation_lags(len(x_main), len(x_sec))

    lag_maxcorr = lags[np.argmax(corr)]

    return lags, corr, lag_maxcorr


def shift_signal(time, signal, delta: int):

    total_len = len(signal)

    if delta <= 0:
        time_adj = time[: total_len+delta]
        signal_adj = signal[-(total_len+delta) :]
    else:
        time_adj = time[delta: ]
        signal_adj = signal[: (total_len-delta)]

    return time_adj, signal_adj
