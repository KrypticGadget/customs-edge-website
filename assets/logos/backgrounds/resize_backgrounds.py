#!/usr/bin/env python3
"""
Background Image Resizer for Customs Edge
Resizes square background images to proper desktop and mobile dimensions
"""

from PIL import Image
import os

def resize_background(input_path, output_path, target_width, target_height, description=""):
    """
    Resize and crop an image to target dimensions while maintaining quality
    """
    try:
        # Open the image
        img = Image.open(input_path)
        original_width, original_height = img.size
        
        print(f"\n{description}")
        print(f"  Original: {original_width}x{original_height}")
        print(f"  Target: {target_width}x{target_height}")
        
        # Calculate scaling to cover the target area
        scale_x = target_width / original_width
        scale_y = target_height / original_height
        scale = max(scale_x, scale_y)  # Use max to ensure full coverage
        
        # Calculate new dimensions
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
        
        # Resize image
        img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Calculate crop box to center the image
        left = (new_width - target_width) // 2
        top = (new_height - target_height) // 2
        right = left + target_width
        bottom = top + target_height
        
        # Crop to target dimensions
        img_cropped = img_resized.crop((left, top, right, bottom))
        
        # Save the result
        img_cropped.save(output_path, 'PNG', optimize=True, quality=95)
        print(f"  [OK] Saved: {output_path}")
        
        # Return file size
        file_size = os.path.getsize(output_path) / 1024  # KB
        print(f"  File size: {file_size:.1f} KB")
        
        return True
        
    except Exception as e:
        print(f"  [ERROR] Error: {str(e)}")
        return False

def main():
    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("=" * 60)
    print("CUSTOMS EDGE - Background Image Resizer")
    print("=" * 60)
    
    # First, backup originals
    print("\n1. Creating backups...")
    try:
        desktop_img = Image.open(os.path.join(current_dir, "hero-bg-desktop.png"))
        desktop_img.save(os.path.join(current_dir, "hero-bg-desktop-original.png"))
        print("  [OK] Backed up desktop image")
        
        mobile_img = Image.open(os.path.join(current_dir, "hero-bg-mobile.png"))
        mobile_img.save(os.path.join(current_dir, "hero-bg-mobile-original.png"))
        print("  [OK] Backed up mobile image")
    except Exception as e:
        print(f"  [ERROR] Backup error: {str(e)}")
    
    # Resize desktop background
    print("\n2. Resizing desktop background...")
    desktop_sizes = [
        # (width, height, suffix, description)
        (1920, 1080, "", "Desktop HD (1920x1080)"),
        (2560, 1440, "-2k", "Desktop 2K (2560x1440)"),
        (1366, 768, "-laptop", "Laptop (1366x768)")
    ]
    
    for width, height, suffix, desc in desktop_sizes:
        input_file = os.path.join(current_dir, "hero-bg-desktop-original.png")
        output_file = os.path.join(current_dir, f"hero-bg-desktop{suffix}.png")
        resize_background(input_file, output_file, width, height, desc)
    
    # Resize mobile background
    print("\n3. Resizing mobile background...")
    mobile_sizes = [
        # (width, height, suffix, description)
        (414, 896, "", "Mobile Portrait (414x896)"),
        (390, 844, "-iphone", "iPhone (390x844)"),
        (896, 414, "-landscape", "Mobile Landscape (896x414)"),
        (768, 1024, "-tablet", "Tablet (768x1024)")
    ]
    
    for width, height, suffix, desc in mobile_sizes:
        input_file = os.path.join(current_dir, "hero-bg-mobile-original.png")
        output_file = os.path.join(current_dir, f"hero-bg-mobile{suffix}.png")
        resize_background(input_file, output_file, width, height, desc)
    
    print("\n" + "=" * 60)
    print("RESIZING COMPLETE!")
    print("=" * 60)
    print("\nRecommended usage:")
    print("  Desktop: hero-bg-desktop.png (1920x1080)")
    print("  Mobile: hero-bg-mobile.png (414x896)")
    print("  Originals saved as: *-original.png")

if __name__ == "__main__":
    main()