# --coding:utf-8--

def init():
    set_input(m=3, short=3, long=9)
    set_output("dif", "dea", "macd")


def method():

    def ema(n):
        # 计算ema
        result = []
        for c in close:
            if np.isnan(c):
                c = np.nan_to_num(c)
            if result:
                result.append((2 * c + (n - 1) * result[-1]) / (n + 1))
            else:
                result.append(c)
        return result

    a = ema(short)
    b = ema(long)
    dif = pd.array(a) - pd.array(b)
    dea = []
    for d in dif:
        if dea:
            dea.append((2 * d + (m - 1) * dea[-1]) / (m + 1))
        else:
            dea.append(d)
    dea = pd.array(dea)
    macd = 2 * (dif - dea)
    return {"dif": round(dif[-1], 2), "dea": round(dea[-1], 2), "macd": round(macd[-1], 2)}
