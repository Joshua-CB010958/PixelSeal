import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageOps

# Initialize main application
root = tk.Tk()
root.title("Pixel Seal")
root.geometry("500x600")

selected_images = []
watermark_path = None
logo_path = None
logo_scale = 0.1  # Default scale for logo size
watermark_scale = 0.3  # Default scale for watermark size

def select_watermark():
    global watermark_path
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        watermark_path = file_path
        wm_label.config(text=f"Selected: {os.path.basename(file_path)}")

def select_logo():
    global logo_path
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        logo_path = file_path
        logo_label.config(text=f"Selected: {os.path.basename(file_path)}")

def select_images():
    global selected_images
    file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_paths:
        selected_images = list(file_paths)
        img_label.config(text=f"Selected {len(selected_images)} images")

def apply_watermark():
    global logo_scale, watermark_scale
    if not watermark_path and not logo_path:
        messagebox.showerror("Error", "Please select a watermark and/or logo!")
        return

    if not selected_images:
        messagebox.showerror("Error", "No images selected!")
        return

    output_folder = filedialog.askdirectory()
    if not output_folder:
        return

    watermark = Image.open(watermark_path).convert("RGBA") if watermark_path else None
    logo = Image.open(logo_path).convert("RGBA") if logo_path else None

    for img_path in selected_images:
        img = Image.open(img_path).convert("RGBA")
        img = ImageOps.exif_transpose(img)  # Correct the orientation if necessary

        # Apply logo (top-left)
        if logo:
            logo_width = int(img.width * logo_scale)
            logo_height = int(logo.height * (logo_width / logo.width))  # Maintain aspect ratio
            logo_resized = logo.resize((logo_width, logo_height))
            img.paste(logo_resized, (10, 10), logo_resized)

        # Apply watermark (bottom-center)
        if watermark:
            wm_width = int(img.width * watermark_scale)
            wm_ratio = wm_width / watermark.width
            wm_height = int(watermark.height * wm_ratio)
            watermark_resized = watermark.resize((wm_width, wm_height))

            # Calculate bottom-center position
            wm_x = (img.width - wm_width) // 2
            wm_y = img.height - wm_height - 10  # 10px padding from the bottom
            img.paste(watermark_resized, (wm_x, wm_y), watermark_resized)

        # Save output
        output_path = os.path.join(output_folder, os.path.basename(img_path))
        img.convert("RGB").save(output_path)

    messagebox.showinfo("Success", "Watermarking complete!")

# UI Components
tk.Label(root, text="Batch Watermark Tool", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(root, text="Select Watermark", command=select_watermark).pack(pady=5)
wm_label = tk.Label(root, text="No watermark selected", fg="gray")
wm_label.pack()

tk.Button(root, text="Select Logo", command=select_logo).pack(pady=5)
logo_label = tk.Label(root, text="No logo selected", fg="gray")
logo_label.pack()

tk.Button(root, text="Select Images", command=select_images).pack(pady=5)
img_label = tk.Label(root, text="No images selected", fg="gray")
img_label.pack()

# Add sliders for resizing watermark and logo
tk.Label(root, text="Logo Size").pack(pady=5)
logo_slider = tk.Scale(root, from_=0.01, to=0.5, orient="horizontal", resolution=0.01, command=lambda val: update_logo_scale(val))
logo_slider.set(logo_scale)  # Set initial value
logo_slider.pack(pady=5)

tk.Label(root, text="Watermark Size").pack(pady=5)
watermark_slider = tk.Scale(root, from_=0.01, to=0.5, orient="horizontal", resolution=0.01, command=lambda val: update_watermark_scale(val))
watermark_slider.set(watermark_scale)  # Set initial value
watermark_slider.pack(pady=5)

# Apply Watermark button
tk.Button(root, text="Apply Watermark", command=apply_watermark, bg="green", fg="white").pack(pady=10)

# Function to update logo scale
def update_logo_scale(val):
    global logo_scale
    logo_scale = float(val)

# Function to update watermark scale
def update_watermark_scale(val):
    global watermark_scale
    watermark_scale = float(val)

# Run Application
root.mainloop()
