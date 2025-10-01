#!/usr/bin/env python3
"""
Command-line interface for pdf-searchable-ocr
"""

import argparse
import sys
from pathlib import Path
from py_ocr import OCRProcessor


def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description="OCR processing with searchable PDF generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  pdf-searchable-ocr image.jpg                          # Basic OCR with default outputs
  pdf-searchable-ocr image.jpg --output invoice         # Custom output prefix
  pdf-searchable-ocr image.jpg --lang ch                # Chinese OCR
  pdf-searchable-ocr image.jpg --gpu                    # Use GPU acceleration
  pdf-searchable-ocr image.jpg --no-pdf                 # Only generate bounding box image
  pdf-searchable-ocr image.jpg --no-boxes               # Only generate searchable PDF
        """
    )
    
    parser.add_argument(
        "image",
        help="Path to the input image file"
    )
    
    parser.add_argument(
        "--output", "-o",
        default="output",
        help="Output prefix for generated files (default: output)"
    )
    
    parser.add_argument(
        "--lang", "-l",
        default="en",
        help="Language for OCR recognition (default: en)"
    )
    
    parser.add_argument(
        "--gpu",
        action="store_true",
        help="Use GPU acceleration (requires CUDA)"
    )
    
    parser.add_argument(
        "--no-pdf",
        action="store_true",
        help="Skip searchable PDF generation"
    )
    
    parser.add_argument(
        "--no-boxes",
        action="store_true",
        help="Skip bounding box image generation"
    )
    
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress verbose output"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="pdf-searchable-ocr 0.1.0"
    )
    
    args = parser.parse_args()
    
    # Validate input file
    image_path = Path(args.image)
    if not image_path.exists():
        print(f"❌ Error: Image file not found: {args.image}")
        return 1
    
    if not image_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif']:
        print(f"❌ Error: Unsupported image format: {image_path.suffix}")
        return 1
    
    try:
        # Initialize OCR processor
        ocr = OCRProcessor(
            lang=args.lang,
            use_gpu=args.gpu,
            verbose=not args.quiet
        )
        
        # Process image
        ocr_result = ocr.process_image(str(image_path))
        if not ocr_result:
            print("❌ Error: OCR processing failed")
            return 1
        
        results = {}
        
        # Generate searchable PDF
        if not args.no_pdf:
            pdf_path = f"{args.output}_searchable.pdf"
            results['pdf'] = ocr.create_searchable_pdf(str(image_path), ocr_result, pdf_path)
        
        # Generate bounding box image
        if not args.no_boxes:
            box_path = f"{args.output}_with_boxes.jpg"
            results['boxes'] = ocr.draw_bounding_boxes(str(image_path), ocr_result, box_path)
        
        # Summary
        if not args.quiet:
            print("\n🎉 Processing completed successfully!")
            print("📁 Generated files:")
            if results.get('pdf'):
                print(f"   📄 {results['pdf']} - Searchable PDF")
            if results.get('boxes'):
                print(f"   🎨 {results['boxes']} - Image with bounding boxes")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n❌ Processing interrupted by user")
        return 1
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())