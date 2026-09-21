import os
import sys
from PIL import Image
from pyzbar.pyzbar import decode

def clear_screen():
    """Clears the terminal screen for a cleaner menu."""
    os.system('cls' if os.name == 'nt' else 'clear')

def scan_basic():
    """Scans an image and quickly prints just the data."""
    print("\n--- Basic Quick Scan ---")
    image_path = input("Enter the image filename (e.g., my_qr.png): ").strip()
    
    try:
        img = Image.open(image_path)
        decoded_objects = decode(img)
        
        if not decoded_objects:
            print("\n❌ No QR codes or barcodes found in this image.")
            return

        print(f"\n✅ Found {len(decoded_objects)} code(s):")
        for i, obj in enumerate(decoded_objects, 1):
            data = obj.data.decode("utf-8")
            print(f"  [{i}] Type: {obj.type} | Data: {data}")
            
    except FileNotFoundError:
        print(f"\n❌ Error: Could not find the file '{image_path}'. Make sure it is in the same folder.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

def scan_detailed():
    """Scans an image, prints spatial data, and offers to save the output."""
    print("\n--- Detailed Scan & Save ---")
    image_path = input("Enter the image filename (e.g., custom_qr.png): ").strip()
    
    try:
        img = Image.open(image_path)
        decoded_objects = decode(img)
        
        if not decoded_objects:
            print("\n❌ No QR codes or barcodes found in this image.")
            return

        print(f"\n✅ Successfully decoded {len(decoded_objects)} item(s).")
        
        # Prepare the output text
        output_lines = [f"--- Scan Results for {image_path} ---"]
        
        for i, obj in enumerate(decoded_objects, 1):
            data = obj.data.decode("utf-8")
            output_lines.append(f"\nCode #{i}:")
            output_lines.append(f"  Type:          {obj.type}")
            output_lines.append(f"  Data:          {data}")
            output_lines.append(f"  Bounding Box:  {obj.rect}")
            output_lines.append(f"  Polygon Array: {obj.polygon}")

        # Print to console
        print("\n".join(output_lines))
        
        # Offer to save to a file
        save_choice = input("\nWould you like to save this data to a text file? (y/n): ").strip().lower()
        if save_choice == 'y':
            txt_filename = image_path.split('.')[0] + "_results.txt"
            with open(txt_filename, "w") as f:
                f.write("\n".join(output_lines))
            print(f"💾 Results saved successfully to '{txt_filename}'.")

    except FileNotFoundError:
        print(f"\n❌ Error: Could not find the file '{image_path}'.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

def main():
    """Main menu loop for the reader."""
    clear_screen()
    while True:
        print("\n" + "="*35)
        print("   🔍 ADVANCED QR CODE READER 🔍")
        print("="*35)
        print("1. Quick Scan (View data only)")
        print("2. Detailed Scan (View bounding boxes & Save to .txt)")
        print("3. Clear Screen")
        print("4. Exit")
        print("="*35)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            scan_basic()
        elif choice == '2':
            scan_detailed()
        elif choice == '3':
            clear_screen()
        elif choice == '4':
            print("\nExiting scanner. Have a great day!")
            sys.exit()
        else:
            print("\n❌ Invalid choice. Please type a number between 1 and 4.")

if __name__ == "__main__":
    main()
