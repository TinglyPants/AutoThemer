import sys

if __name__ == "__main__":
    hex = sys.argv[1][1:]
    
    red = hex[0:2].lower()
    green = hex[2:4].lower()
    blue = hex[4:6].lower()
    
    print(f"rgb({red}{green}{blue})")