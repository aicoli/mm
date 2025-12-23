import time
from math import gcd as math_gcd


def extended_gcd(a, b):
    """扩展欧几里得算法计算模逆"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):
    """计算模逆 a^(-1) mod m"""
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("模逆不存在")
    return x % m


def generate_keypair():
    """生成小型RSA密钥（用于演示）"""
    p, q = 61, 53  # 固定小素数便于演示
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    while math_gcd(e, phi) != 1:
        e += 1
    d = mod_inverse(e, phi)
    return (e, n), d


def main():
    # 生成密钥
    public, private = generate_keypair()
    e, n = public
    d = private

    # 验证过程
    m = 207
    c = pow(m, e, n)
    m_dec = pow(c, d, n)

    # 性能测试 - 增加测试次数避免除零错误
    test_count = 10000  # 增加到10000次
    start = time.time()
    for _ in range(test_count):
        pow(m, e, n)
    total = time.time() - start
    avg = total / test_count

    # 中文简洁输出
    print(f"公钥: e={e}, n={n}")
    print(f"私钥: d={d}")
    print(f"验证: {m} → {c} → {m_dec} {'✓' if m_dec == m else '✗'}")

    # 避免除零错误
    if total > 0:
        print(f"性能: 总耗时{total:.4f}s | 平均{avg:.6f}s | 速率{test_count / total:.0f}/s")
    else:
        print("性能: 耗时过短无法测量")


if __name__ == "__main__":
    main()