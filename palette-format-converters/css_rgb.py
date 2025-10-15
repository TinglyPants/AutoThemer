import sys

if __name__ == "__main__":
    hex = sys.argv[1][1:]
    
    red = int(hex[0:2], 16)
    green = int(hex[2:4], 16)
    blue = int(hex[4:6], 16)
    
    print(f"rgb({red}, {green}, {blue})")