
def convert(s, numRows):
    out = [""]* numRows
    direct = 1
    index = 0
    for i in range(0, len(s)):            
        out[index] += (s[i])

        if index == numRows-1:
            direct = -1
        elif index == 0:
            direct = 1

        index += direct
    print(out)
    out = "".join(str(x) for x in out)
    return out

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    num_rows = 3
    print(convert(s, num_rows))