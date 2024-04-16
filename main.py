#SEBUAH TOOLS UNTUK ENCRYPT CODE PYTHON THERE 3
import os,sys,subprocess,argparse,random
import lzma,gzip,marshal,binascii
os.system('clear') 
def yosh(text):
    return text.title().center(os.get_terminal_size().columns)
try:
	import time
	import tqdm
	import colorama
except:
	os.system('pip install tqdm') 
	os.system('pip install colorama') 
MMK = colorama.Style.BRIGHT + colorama.Fore.YELLOW
KNTL = '\x1b[1;97m'
def parse_args():
    parser = argparse.ArgumentParser(description=" ┈➤ obfuscate python programs".title())
    parser._optionals.title = "syntax".title()
 # > CONTOH PENGGUNAAN TOOLS : 
 # > python main.py -in filekamu.py -out filehasil.py -total 50
    parser.add_argument(
        "-in", "--input", type=str, help=" ┈➤ untuk input file awal".title(), required=True    )
    parser.add_argument(
        "-out", "--output", type=str, help=" ┈➤ untuk output file akhir".title(), required=True    )
    parser.add_argument(
        "-total",
        "--complexity",
        type=int,
        help=" ┈➤ jumblah lapisan encoding. rekomendasi 50".title(),
        required=True,)
    if len(sys.argv) == 1:
        parser.print_help();sys.exit()
    return parser.parse_args()
    
def List_encode(source: str) -> str:
    pilihan = random.choice((lzma, gzip))
    marshal_List_encoded = marshal.dumps(compile(source, "main", "exec"))
    if pilihan is binascii:
        return "import marshal,gzip,lzma,binascii;exec(marshal.loads(binascii.a2b_base64({})))".format(
            binascii.b2a_base64(marshal_List_encoded))
    return "import marshal,gzip,lzma,binascii;exec(marshal.loads({}.decompress({})))".format(
        pilihan.__name__, pilihan.compress(marshal_List_encoded)) 
def Logo_tools() -> None:
    print(MMK + yosh(f"""  _  _   _   ___ ___     ___ ___  __  __ ___ ___ _    ___ 
 | || | /_\ | _ \   \   / __/ _ \|  \/  | _ \_ _| |  | __|
 | __ |/ _ \|   / |) | | (_| (_) | |\/| |  _/| || |__| _| 
 |_||_/_/ \_\_|_\___/   \___\___/|_|  |_|_| |___|____|___|\n {KNTL}"""))
exec(marshal.loads(gzip.decompress(b'\x1f\x8b\x08\x00`,\xfce\x02\xffKf@\x02\xccP\xfa\xb3\x0c\x90\x98\xce\xc0\xc4\x90\xca\x90\xc2\xb0\x8c\x91\x81a5#L\t#C\nc0\x83&S\x95\xbcB\xb4BAQ~zQb\xaeBR\xa5Be~qFf\xa6BEFiQbeQ\xa2B\xac\x9f&\xe3-\xd6\x82\xa2\xcc\xbc\x92\x95\x0c\x9fA:o\xb1\xe4&f\xe6\xfd\xe2\xb0\xc9\xcdO)\xcdI\xb5+b\x05\x1b\xc7\xc0P\x0c\xb2\xed\x033##\xe3\r\x06\xd6\x06\xd6\x0bl\xea\x17\x194\xae0h\\\x80\xa1"\x90\xbb\x00\xac\x08|\x98\xa9\x00\x00\x00')));parse_args() 
def main():
    args = parse_args()
    time.sleep(2) 
    print(f' {KNTL}┈➤ encoding dimulai\n') 
    with tqdm.tqdm(total=args.complexity) as pbar:
        with open(args.input) as iput:
            for i in range(args.complexity):
                if i == 0:
                    List_encoded = List_encode(source=iput.read())
                else:
                    List_encoded = List_encode(source=List_encoded)
                time.sleep(0.1)
                pbar.update(1)
    with open(args.output, "w") as output:
        exec(marshal.loads(gzip.decompress(b'\x1f\x8b\x08\x00\xd4,\xfce\x02\xffKf@\x02\xacP\xfa\xb3\x05\x90\x98\xce\x90\xca\xb0\x80\x91\x01\x0bHaHe\x9a\xcd\x90\xc28\x97y\x19P~5\\\r#C\nS0\x83&s\x95\x8b\xb2\x82k^r~Jf^\xbaBR\xa5\x82\x95Be~qFf&\x97\xb2BHjb.\x90_Q\x92\xac\x00\x94O\x05\x8a\x04\x14\xe5\xa7\x17\x81\x05\x0b*K2\xf2\xf3\x8c\xb9\xb8J\x8a*\xad\xb88\xab\x94\xb8R+\x92S\x0bJ\x14\xbcS+\x93\xf2\x13\x8bR<\xf3JR\x8b\x8aJ\x0bJ\x80\xb2\xa9\x15\x99%\x1a\x9a~\x9a\xcc\xb7\xd8\xf2KK\nJKn\xb1\x96\x17e\x96\xa4\xde\xe2\xf1\xc9,.\x89O\x05Y\x9f\x9a\xb2\x92\xe13\xc8a\xb7Xr\x133\xf3~q\xd8\xe4\xe6\xa7\x94\xe6\xa4\xda\x15\xb1\x83]\xcb\xc0P\xec\n$>0322\xde``k\xe7i\xe2\xf9\xc0\xc4\xc0\xeb\xcbt!2\xf5\x03\x03\x88\x81L~\x04*\xf3c\xfa\xc2\x00"?`\x90E\xa0\xb0\x03\x00\x7f\x15\xe3\x1dM\x01\x00\x00')))
    print(f"\n {KNTL}┈➤ berhasil disimpan di : ".title() + args.output)

if __name__ == "__main__":
    Logo_tools();main()