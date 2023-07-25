import pyfiglet

def generate_ascii_art(text):
    # 使用"slant"字体样式来创建字符艺术字
    ascii_art = pyfiglet.figlet_format(text, font='slant')
    return ascii_art

def convert_to_c_array(ascii_art):
    # 将字符艺术字转换为C语言的char型数组字符串
    lines = ascii_art.split('\n')
    # 去除末尾的空行
    lines = [line.rstrip() for line in lines if line.strip()]
    max_length = max(len(line) for line in lines)
    c_array_str = ""

    for line in lines:
        line += ' ' * (max_length - len(line))  # 补齐每行的长度
        c_array_str += '"' + line + '\\n"\n'

    return c_array_str

if __name__ == "__main__":
    text = "testcode"
    ascii_art = generate_ascii_art(text)
    print(ascii_art)

    # 将字符艺术字转换为C语言的char型数组字符串并输出
    c_array_str = convert_to_c_array(ascii_art)
    print("const char* ascii_art = {")
    print(c_array_str)
    print("};")
