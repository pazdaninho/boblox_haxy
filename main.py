import cv2
import pyautogui
import numpy as np

def main():
    screen_width, screen_height = pyautogui.size()
    
    # Tworzenie nowego okna
    cv2.namedWindow("Boblox", cv2.WINDOW_NORMAL)
    win = pyautogui.getWindowsWithTitle("Roblox")[0]
    while True:
        left,top,width,height = win.box.left, win.box.top+20, win.box.width-5, win.box.height-25

        
        # Zrzut ekranu
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        
        # Konwersja zrzutu ekranu do formatu OpenCV
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        # Wyświetlanie zrzutu ekranu w oknie
        cv2.imshow("Boblox", frame)
        
        # Wyjście z pętli po wciśnięciu klawisza 'q'
        if cv2.waitKey(1) == ord('q'):
            break
    
    cv2.destroyAllWindows()

main()
