import random
import time
import sys

def console_flip():
    # Animation frames
    spinner = ["|", "/", "-", "\\"]
    
    print("Para atiliyor... ", end="")
    
    # Spin loop
    for _ in range(20):  # Run 20 frames
        for frame in spinner:
            sys.stdout.write(f"\b{frame}") # \b backspaces to overwrite character
            sys.stdout.flush()
            time.sleep(0.05)
            
    # Logic
    random_yazi_tura = random.randint(0, 1)
    result = "Yazi" if random_yazi_tura == 0 else "Tura"
    
    # Final Output
    sys.stdout.write(f"\b \nSonuc: {result}\n")

if __name__ == "__main__":
    console_flip()