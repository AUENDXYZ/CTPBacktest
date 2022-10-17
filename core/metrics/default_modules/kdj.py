# --coding:utf-8--

def init():
    set_input(fastk_period=9, slowk_period=3, slowd_period=3)
    set_output("k", "d", "j")


def method():
    """
    此处填写具体的计算方法
    ---
    pandas包自动导入为pd, numpy包自动导入为np, talib已导入, 需要打开文件请使用alias_open
    ---
    datetime为日期列表, open为开盘价列表, close为收盘价列表, high为最高价列表, low为最低价列表, volume为成交量列表
    或使用df, df是一个dataframe, 有[datetime, open, close, high, low, volume列],其中datetime列为索引
    数据的使用长度为200
    ---
    输出变量必须为:
    1. 字典类型, 字典中的值必须为列表形式(list, array)
    2. dataframe格式, 必须包含datetime列, 所有输出参数列
    """

    def cal_rsv(n):
        l_low = talib.MIN(np.array(low), n)
        h_high = talib.MAX(np.array(high), n)
        rsv = (np.array(close) - l_low) / (h_high - l_low) * 100.
        return rsv

    def SMA_CN(arr, n, m):
        n = int(n)
        m = int(m)
        y = 0
        result = []
        for x in arr:
            if np.isnan(x):
                x = np.nan_to_num(x)
            y = (m * x + (n - m) * y) / n
            result.append(y)

        return np.array(result)

    rsv = cal_rsv(fastk_period)
    k = SMA_CN(rsv, slowk_period, 1)
    d = SMA_CN(k, slowd_period, 1)
    j = 3 * k - 2 * d
    return {"k": round(k[-1], 2), "d": round(d[-1], 2), "j": round(j[-1], 2)}

