import os
import sys
from PIL import Image
from pyzbar.pyzbar import decode

def scan_basic():
    image_path = input("Enter image filename: ").strip()
    
    try:
        img = Image.open(image_path)
        decoded_objects = decode(img)
        
        if not decoded_objects:
            print("No QR codes or barcodes found.")
            return

        print(f"\nFound {len(decoded_objects)} code(s):")
        for i, obj in enumerate(decoded_objects, 1):
            data = obj.data.decode("utf-8", errors="replace")
            print(f"[{i}] Type: {obj.type} | Data: {data}")
            
    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def scan_detailed():
    image_path = input("Enter image filename: ").strip()
    
    try:
        img = Image.open(image_path)
        decoded_objects = decode(img)
        
        if not decoded_objects:
            print("No QR codes or barcodes found.")
            return

        output_lines = [f"Scan Results for {image_path}"]
        
        for i, obj in enumerate(decoded_objects, 1):
            data = obj.data.decode("utf-8", errors="replace")
            output_lines.append(f"\nCode #{i}:")
            output_lines.append(f"  Type: {obj.type}")
            output_lines.append(f"  Data: {data}")
            output_lines.append(f"  Rect: {obj.rect}")
            output_lines.append(f"  Polygon: {obj.polygon}")

        print("\n".join(output_lines))
        
        save_choice = input("\nSave results to text file? (y/n): ").strip().lower()
        if save_choice == 'y':
            base_name, _ = os.path.splitext(image_path)
            txt_filename = f"{base_name}_results.txt"
            with open(txt_filename, "w") as f:
                f.write("\n".join(output_lines))
            print(f"Saved to '{txt_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\n--- QR Code Reader ---")
        print("1. Quick Scan")
        print("2. Detailed Scan")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            scan_basic()
        elif choice == '2':
            scan_detailed()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()