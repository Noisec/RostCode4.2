#pytoun
import cryptocode
import os


def compress_text(text, mapping):
    for pair in mapping:
        text = text.replace(pair[0], pair[1])
    return text
def decompress_text(text, mapping):
    for pair in mapping:
        text = text.replace(pair[1], pair[0])
    return text

import random
import string


map=[]
def generate_mapping(seed=None):
    random.seed(seed)

    letters = string.ascii_letters
    numbers = string.digits
    senoritas=["à","è","ì","ò","ù","À","È","Ì","Ò","Ù","á","é","í","ó","ú","ý","Á","É","Í","Ó","Ú","Ý","â","ê","î","ô","û","Â","Ê","Î","Ô","Û","ã","ñ","õ","Ã","Ñ","Õ","ä","ë","ï","ö","ü","ÿ","Ä","Ë","Ï","Ö","Ü","Ÿ","å","Å","æ","Æ","œ","Œ","ç","Ç","ð","Ð","ø","Ø","ß","ก","ข","ฃ","ค","ฅ","ฆ","ง","จ","ฉ","ช","ซ","ฌ","ญ","ฏ","ฐ","ฑ","ฒ","ณ","ด","ต","ถ","ท","ธ","น","บ","ป","ผ","ฝ","พ","ฟ","ภ","ม","ย","ร","ฤ","ล","ฦ","ว","ศ","ษ","ส","ห","ฬ","อ","ฮ","ฯ","ะ","า","เ","แ","โ","ใ","ไ","ๅ","ๆ","Գ","Դ","Ե","Զ","Է","Ը","Թ","Ժ","Ի","Լ","Խ","Ծ","Ձ","Ղ","Ճ","ճ","ղ","ձ","կ","ծ","լ","ի","ժ","թ","ը","է","զ","ե","դ","գ","բ","ա","Յ","Ն","Շ","Ո","Չ","Պ","Ռ","Ս","Վ","Տ","Ր","Ց","Ւ","Փ","Ք","Օ","Ֆ","և","ֆ","օ","ք","փ","ւ","ց","տ","վ","ս","ռ","ջ","պ","չ","ո","շ","յ","մ","က","ခ","ဂ","ဃ","င","ည","ဉ","ဈ","ဇ","ဆ","စ","ဋ","ဌ","ဍ","ဎ","ဏ","န","ဓ","ဒ","ထ","ပ","ဖ","ဗ","ဘ","မ","ယ","ရ","လ","ဠ","ဝ","ဟ","သ","ဿ","အ","ဣ","ဤ","ဥ","ဦ","ဪ","ဩ","ぁ","あ","ぃ","い","ぅ","う","ぇ","え","ぉ","お","か","が","き","ぎ","く","ぐ","け","げ","こ","ご","さ","ざ","し","じ","す","ず","せ","ぜ","そ","ぞ","た","だ","ち","ぢ","っ","つ","づ","て","で","と","ど","な","に","ぬ","ね","の","は","ば","ぱ","ひ","び","ぴ","ふ","ぶ","ぷ","へ","べ","ぺ","ほ","ぼ","ぽ","ま","み","む","め","も","ゃ","や","ゅ","ゆ","ょ","よ","ら","り","る","れ","ろ","ゎ","わ","ゐ","ゑ","を","ん","ゔ","ゕ","ゖ","ゝ","ゞ","ゟ","ァ","ア","ィ","イ","ゥ","ウ","ェ","エ","ォ","オ","カ","ガ","キ","ギ","ク","グ","ケ","ゲ","コ","ゴ","サ","ザ","シ","ジ","ス","ズ","セ","ゼ","ソ","ゾ","タ","ダ","チ","ヂ","ッ","ツ","ヅ","テ","デ","ト","ド","ナ","ニ","ヌ","ネ","ノ","ハ","バ","パ","ヒ","ビ","ピ","フ","ブ","プ","ヘ","ベ","ペ","ホ","ボ","ポ","マ","ミ","ム","メ","モ","ャ","ヤ","ュ","ユ","ョ","ヨ","ラ","リ","ル","レ","ロ","ヮ","ワ","ヰ","ヱ","ヲ","ン","ヴ","ヵ","ヶ","ヷ","ヸ","ヹ","ł","€","]","@","&",">","<","đ","Ł","|","~","^","°"]
    
    mapping = {}

    for symbol in senoritas:
        is_number = random.choice([True, False, False])  
        if is_number:
            random_key = random.sample(numbers, 2)
        else:
            random_key = random.sample(letters, 2)

        mapping[''.join(random_key)] = symbol

    return mapping
def ycompmap(user_seed,txt):
    if user_seed=="!":
        user_seed = str(random.randint(1,9999)).zfill(4)
    generated_mapping = generate_mapping(seed=user_seed)
    for key, value in generated_mapping.items():
       map.append([key,value])
    return str(compress_text(txt,map))+user_seed

def ncompmap(user_seed,txt):
    if user_seed=="!":
        user_seed = str(random.randint(1,9999)).zfill(4)
    generated_mapping = generate_mapping(seed=user_seed)
    for key, value in generated_mapping.items():
       map.append([key,value])
    return str(decompress_text(txt,map))+user_seed



def tag(txt):
    return(f'{etag}:{utag} | {txt}')

def enrichteous(text):
    number = 0
    for i in range(min(len(text), 4)):
        number += ord(text[i]) * (256 ** i)
    return number

def encode_text(text, key):
    encoded_parts = []
    innumero = enrichteous(key)
    for part in text.split("."):
        locvarlist = ""
        for i in part:
            locvarlist += str(ord(i) * innumero) + "_"
        encoded_part = cryptocode.encrypt(str(locvarlist), str(key))
        encoded_parts.append(encoded_part)
    return "`".join(encoded_parts)

def decode_text(encoded_text, key):
    decoded_parts = []
    innumero = enrichteous(key)
    for encoded_part in encoded_text.split("`"):
        decoded_part = ""
        inkod = str(cryptocode.decrypt(encoded_part, str(key))).split("_")
        inkod = inkod[:-1]
        for i in range(len(inkod)):
            inkod[i] = int(inkod[i])
        for i in inkod:
            decoded_part += chr(int(int(i) / innumero))
        decoded_parts.append(decoded_part)
    return ".".join(decoded_parts)











def encode_file(filename, key):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    encoded_text = encode_text(text, key)
    output_filename = os.path.splitext(filename)[0] + "_enc" + os.path.splitext(filename)[1]
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(ycompmap("!",encoded_text))
    print(f"Encoded file saved as {output_filename}")

def decode_file(filename, key):
    with open(filename, "r", encoding="utf-8") as f:
        encoded_text = f.read()
    dd=ncompmap(encoded_text[-4:],encoded_text[:-4])
    decoded_text = decode_text(dd, key)
    output_filename = os.path.splitext(filename)[0] + "_dec" + os.path.splitext(filename)[1]
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(decoded_text)
    print(f"Decoded file saved as {output_filename}")













while True:
    etag="-"
    utag="-"
    action = input(tag("File or Text? (f,t): "))
    if action == "f" or action == "F":
        etag="F"
        filename = input(tag("Filename: "))
        
        if input(tag("Encode or Decode (e,d): ")) == "e":
            utag="E"
            key = input(tag("Key: "))
            encode_file(filename, key)
        else:
            utag="D"
            key = input(tag("Key: "))
            decode_file(filename, key)
    else:
        etag="T"
        if input(tag("Encode or Decode (e,d): ")) == "e":
            utag="E"
            key = input(tag("Key: "))
            text = input(tag("Text: "))
            encoded_text = encode_text(text, key)
            print()
            print(ycompmap("!",encoded_text))
        else:
            utag="D"
            key = input(tag("Key: "))
            encoded_text = input(tag("Text: "))
            dd=ncompmap(encoded_text[-4:],encoded_text[:-4])
            decoded_text = decode_text(dd, key)
            print()
            print(decoded_text)
    print()
    print(".."*30)
    print()