#!/usr/bin/env python3
"""
Basic usage example for py-ocr
"""

from py_ocr import OCRProcessor

def main():
    # Initialize the OCR processor
    print("🔧 Initializing OCR processor...")
    ocr = OCRProcessor(lang='en', verbose=True)
    
    # Download a sample image for testing
    print("\n📥 Downloading sample image...")
    image_path = ocr.download_sample_image()
    
    if not image_path:
        print("❌ Failed to get sample image")
        return
    
    # Process the image and generate all outputs
    print(f"\n🔍 Processing image: {image_path}")
    results = ocr.process_and_generate_all(image_path, output_prefix="basic_example")
    
    # Print results
    print("\n🎉 Processing completed!")
    print("📁 Generated files:")
    
    if results['searchable_pdf']:
        print(f"   📄 {results['searchable_pdf']} - Searchable PDF")
    
    if results['boxed_image']:
        print(f"   🎨 {results['boxed_image']} - Image with bounding boxes")
    
    # Extract some text information
    ocr_result = results['ocr_result']
    if ocr_result:
        texts = ocr_result['rec_texts']
        scores = ocr_result['rec_scores']
        
        print(f"\n📊 OCR Summary:")
        print(f"   📝 Total text blocks: {len(texts)}")
        print(f"   🎯 Average confidence: {sum(scores)/len(scores):.3f}")
        print(f"   📄 Full text preview: {' '.join(texts[:5])}{'...' if len(texts) > 5 else ''}")

if __name__ == "__main__":
    main()