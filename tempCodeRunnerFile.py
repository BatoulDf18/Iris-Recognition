import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from correspondance import lancer
from extraction import extractions
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from PIL import Image, ImageTk
import time
from PIL import Image, ImageDraw, ImageTk
from tkinter import font
import threading
# Create the default root window


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./pictures")

# Global variables
url = ''
window4 = None

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def return_to_main_window():
  global window3
  window3.destroy()
  create_main_window()

def return_to_main_window4():
  global window4
  window4.destroy()
  create_main_window()

upld = None
def create_main_window():
    
    global url
    global window
    window = tk.Tk()
    window.geometry("1010x616")
    window.configure(bg="#FFF5F5")

    canvas = tk.Canvas(
        window,
        bg="#FFF5F5",
        height=616,
        width=1010,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    image_image_151 = PhotoImage(
    file=relative_to_assets("image_151.png"))
    image_151 = canvas.create_image(
    506.0,
    344.0,
    image=image_image_151
)
    canvas.create_text(
    250.0,
    55.0,
    anchor="nw",
    text="Biometric identificaion system",
    fill="#000000",
    font=("Poppins", 40 * -1)
)
    image_image_1 = tk.PhotoImage(file=relative_to_assets("image_1.png"))
    image_image_2 = tk.PhotoImage(file=relative_to_assets("image_2.png"))
    image_image_3 = tk.PhotoImage(file=relative_to_assets("image_3.png"))
    

    canvas.create_image(505.0, 375.0, image=image_image_1)
    canvas.create_image(505.0, 322.0, image=image_image_2)
    canvas.create_text(412.0, 365.0, anchor="nw", text="Select a file or drag and drop here", fill="#000000", font=("Helvetica", 13 * -1))
    canvas.create_text(386.0, 396.0, anchor="nw", text="PNG picture, file size no more than 10MB", fill="#000000", font=("Poppins Regular", 12 * -1))
    canvas.create_image(497.0, 384.0, image=image_image_3)
    

    
    button_image_2 = tk.PhotoImage(file=relative_to_assets("SELECT FILE.png"))
    button_image_3 = tk.PhotoImage(file=relative_to_assets("VEREFICATION.png"))

   

    btn = tk.Button(window, image=button_image_2, borderwidth=0, highlightthickness=0, relief='flat', command=load)
    btn.pack(side=tk.LEFT)
    btn.place(x=462.0, y=425.0, width=86.0, height=39.0)

    upld = tk.Button(window, image=button_image_3, borderwidth=0, highlightthickness=0, relief='flat', command=verif)
    upld.pack(side=tk.LEFT, expand=True, pady=30)
    upld.place(x=872.0, y=562.0, width=119.0, height=39.0)

    window.resizable(False, False)
    window.mainloop()






#function to load picture
def load():
    global url
    url = filedialog.askopenfilename(title="veuillez selectionner une image",filetypes=(('Image Files', '*.png'),))
    print(url)

    loading_window = Tk()
    loading_window.geometry("200x100")
    loading_window.title("Uploading...")

    canvas = Canvas(loading_window, width=200, height=100, bg="#FFFFFF", highlightthickness=0)
    canvas.pack()

    loading_text = canvas.create_text(100, 30, text="Uploading...", fill="#000000", font=("Helvetica", 12))

    progress_bar = canvas.create_rectangle(50, 50, 150, 60, fill="#CCCCCC", outline="")

    for i in range(1, 101):
        canvas.delete(progress_bar)
        progress_bar = canvas.create_rectangle(50, 50, 50 + i, 60, fill="#0F91D2", outline="")
        loading_window.update()
        time.sleep(0.05)  # Simulate delay
    loading_window.destroy()



#function to verify the picture 
def verif():
    global url, upld, window
    if url == None or url == '':
        return  
    else:
        x, y, matching_res = lancer(url=url)
        if x:
            resultat(y, matching_res)
        else:
            not_in_bdd()



            
#function to show window3 if picture arent in the database
def not_in_bdd():
    global window, window3
    if window:
        window.destroy()
    window3 = Tk()
    window3.geometry("1010x616")
    window3.configure(bg="#FFFFFF")
    # Load and display the image on window3
    canvas = Canvas(
        window3,
        bg="#FFFFFF",
        height=616,
        width=1010,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    image_image_111 = tk.PhotoImage(file=relative_to_assets("image_111.png"))
    image_111 = canvas.create_image(504.0, 274.0, image=image_image_111)

    
    button_image_111 = tk.PhotoImage(file=relative_to_assets("button_111.png"))
    button_111 = tk.Button(
        window3,
        image=button_image_111,
        borderwidth=0,
        highlightthickness=0,
        command=return_to_main_window,
        relief="flat"
    )
    button_111.place(x=435.0, y=341.0, width=139.0, height=45.0)

    window3.resizable(False, False)
    window3.mainloop()



# function to show window 4 after the matching
def show_window4():
    global window4
    window2.destroy()
        
    window4 =Tk()
    window4.geometry("1010x616")
    window4.configure(bg="#FFFFFF")

    # Create canvas
    canvas = Canvas(
        window4,
        bg="#FFFFFF",
        height=616,
        width=1010,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    
    image_image_1111 = PhotoImage(file=relative_to_assets("image_1111.png"))
    image_1111 = canvas.create_image(
        512.0,
        279.0,
        image=image_image_1111
    )

    
    button_image_1111 = PhotoImage(file=relative_to_assets("button_1111.png"))
    button_1111 = Button(
        window4,
        image=button_image_1111,
        highlightthickness=0,
        command=return_to_main_window4,
        relief="flat"
    )
    button_1111.place(
        x=442.0,
        y=342.0,
        width=139.0,
        height=45.0
    )

    # Make window4 non-resizable
    window4.resizable(False, False)
    window4.mainloop()
  




#function to show the result if picture exist
def resultat(y, matching_res):
    global window2, window
    if window:
        window.destroy()
    window2 =Tk()  
    window2.geometry("1010x616")
    window2.configure(bg="#FFF5F5")

    canvas = tk.Canvas(
        window2,
        bg="#FFF5F5",
        height=616,
        width=1010,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)



    image_image_11 = tk.PhotoImage(file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(802.0, 333.0, image=image_image_11)

    image_image_22 = tk.PhotoImage(file=relative_to_assets("image_22.png"))
    image_22 = canvas.create_image(529.0, 576.0, image=image_image_22)

    canvas.create_rectangle(30.0, 251.0, 214.0, 410.0, fill="#FFFFFF", outline="")
    canvas.create_rectangle(309.0, 251.0, 493.0, 410.0, fill="#FFFFFF", outline="")

    canvas.create_text(76.0, 432.0, anchor="nw", text="Original Picture", fill="#000000", font=("Poppins Medium", 15))
    canvas.create_text(763.0, 428.0, anchor="nw", text="Matching", fill="#000000", font=("Poppins Medium", 15))
    canvas.create_text(334.0, 432.0, anchor="nw", text="Processed Picture", fill="#000000", font=("Poppins Medium", 15))

    image_image_33 = tk.PhotoImage(file=relative_to_assets("image_33.png"))
    image_33 = canvas.create_image(260.0, 333.0, image=image_image_33)

    image_image_44 = tk.PhotoImage(file=relative_to_assets("image_44.png"))
    image_44 = canvas.create_image(553.0, 333.0, image=image_image_44)

    canvas.create_rectangle(614.0, 251.0, 980.0, 410.0, fill="#FFFFFF", outline="")

    image_image_55 = tk.PhotoImage(file=relative_to_assets("image_5.png"))
    image_55 = canvas.create_image(505.0, 140.0, image=image_image_55)

    image_image_66 = tk.PhotoImage(file=relative_to_assets("image_6.png"))
    image_66 = canvas.create_image(487.0, 576.0, image=image_image_66)

    

        # Load images
    img1 = Image.open("./results/bdd.png")
    img2 = Image.open("./results/real.png")
    img3 = Image.open("./results/matching.png")

    # Resize images
    img1 = img1.resize((int(214.0 - 30.0), int(410.0 - 251.0)))
    img2 = img2.resize((int(493.0 - 309.0), int(410.0 - 251.0)))
    img3 = img3.resize((int(980.0 - 614.0), int(410.0 - 251.0)))

    # Add rounded corners to images
    img1 = add_rounded_corners(img1, 15)
    img2 = add_rounded_corners(img2, 15)
    img3 = add_rounded_corners(img3, 15)

    # Convert images to Tkinter PhotoImage objects
    img1_tk = ImageTk.PhotoImage(img1)
    img2_tk = ImageTk.PhotoImage(img2)
    img3_tk = ImageTk.PhotoImage(img3)

    # Display images on the canvas
    canvas.create_image(30.0, 251.0, anchor=NW, image=img1_tk)
    canvas.create_image(309.0, 251.0, anchor=NW, image=img2_tk)
    canvas.create_image(614.0, 251.0, anchor=NW, image=img3_tk)

    person_id = tk.Label(
        window2,
        text="code :" + str(y) + "\n similarité :" + str(matching_res) + "%",
        font=("DyyIN Alternate", 18)
        ).place(x=1190, y=70)
    window2.after(5000, show_window4)
    window2.mainloop()



def add_rounded_corners(img, border_radius):
    # Create a mask for the border radius
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)

    # Draw a rounded rectangle on the mask
    draw.rounded_rectangle((0, 0, img.width, img.height), radius=border_radius, fill=255)

    # Apply the mask to the image
    img.putalpha(mask)

    return img
if __name__ == "__main__":
    # Create a thread for extraction and start it
    extraction_thread = threading.Thread(target=extractions)
    extraction_thread.start()

    # Continue with creating the main window
    create_main_window()
