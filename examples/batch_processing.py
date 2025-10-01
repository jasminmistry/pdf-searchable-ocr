#!/usr/bin/env python3
"""
Batch processing example for py-ocr
Process multiple images in a folder
"""

import os
from pathlib import Path
from py_ocr import OCRProcessor

def process_folder(input_folder: str, output_folder: str = "batch_output"):
    """
    Process all images in a folder
    
    Args:
        input_folder (str): Path to folder containing images
        output_folder (str): Path to output folder
    """
    
    # Create output directory
    output_path = Path(output_folder)
    output_path.mkdir(exist_ok=True)
    
    # Initialize OCR processor
    print("🔧 Initializing OCR processor...")
    ocr = OCRProcessor(lang='en', verbose=False)  # Quiet mode for batch processing
    
    # Supported image extensions
    supported_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif'}
    
    # Find all image files
    input_path = Path(input_folder)
    if not input_path.exists():
        print(f"❌ Error: Input folder not found: {input_folder}")
        return
    
    image_files = [
        f for f in input_path.iterdir() 
        if f.is_file() and f.suffix.lower() in supported_extensions
    ]
    
    if not image_files:
        print(f"❌ No supported image files found in: {input_folder}")
        return
    
    print(f"📁 Found {len(image_files)} image files to process")
    
    # Process each image
    successful = 0
    failed = 0
    
    for i, image_file in enumerate(image_files, 1):
        print(f"\n🔍 Processing {i}/{len(image_files)}: {image_file.name}")
        
        try:
            # Generate output prefix
            output_prefix = output_path / image_file.stem
            
            # Process image
            results = ocr.process_and_generate_all(
                str(image_file), 
                output_prefix=str(output_prefix)
            )
            
            if results['searchable_pdf'] and results['boxed_image']:
                print(f"   ✅ Success: {image_file.name}")
                successful += 1
            else:
                print(f"   ⚠️  Partial success: {image_file.name}")
                successful += 1
                
        except Exception as e:
            print(f"   ❌ Failed: {image_file.name} - {e}")
            failed += 1
    
    # Summary
    print(f"\n🎉 Batch processing completed!")
    print(f"📊 Results:")
    print(f"   ✅ Successful: {successful}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📁 Output folder: {output_folder}")

def main():
    """Main function with example usage"""
    
    # Example 1: Process a specific folder
    input_folder = input("📁 Enter path to image folder (or press Enter for current directory): ").strip()
    if not input_folder:
        input_folder = "."
    
    output_folder = input("📁 Enter output folder (or press Enter for 'batch_output'): ").strip()
    if not output_folder:
        output_folder = "batch_output"
    
    process_folder(input_folder, output_folder)

if __name__ == "__main__":
    main()