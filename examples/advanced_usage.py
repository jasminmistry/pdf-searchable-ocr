#!/usr/bin/env python3
"""
Advanced usage example for py-ocr
Demonstrates custom configuration and error handling
"""

from py_ocr import OCRProcessor
import json
from pathlib import Path

def advanced_ocr_example():
    """Demonstrate advanced OCR features"""
    
    print("🚀 Advanced OCR Example")
    print("=" * 50)
    
    # Example 1: Custom configuration
    print("\n1️⃣ Custom OCR Configuration")
    ocr_custom = OCRProcessor(
        lang='en',
        use_gpu=False,  # Set to True if you have CUDA
        verbose=True,
        # Custom PaddleOCR parameters
        use_angle_cls=True,           # Enable angle classification
        use_textline_orientation=True, # Enable text orientation
        det_max_side_len=1280,        # Detection max side length
        rec_batch_num=6,              # Recognition batch size
    )
    
    # Example 2: Process with detailed results
    print("\n2️⃣ Detailed OCR Processing")
    image_path = ocr_custom.download_sample_image()
    
    if image_path:
        # Get detailed OCR results
        ocr_result = ocr_custom.process_image(image_path)
        
        if ocr_result:
            # Analyze results
            texts = ocr_result['rec_texts']
            scores = ocr_result['rec_scores']
            boxes = ocr_result['rec_boxes']
            
            print(f"\n📊 Detailed Analysis:")
            print(f"   📝 Total text blocks: {len(texts)}")
            print(f"   🎯 Confidence range: {min(scores):.3f} - {max(scores):.3f}")
            print(f"   📊 Average confidence: {sum(scores)/len(scores):.3f}")
            
            # High confidence texts
            high_conf_texts = [text for text, score in zip(texts, scores) if score > 0.9]
            print(f"   ✅ High confidence blocks (>0.9): {len(high_conf_texts)}")
            
            # Example 3: Custom output paths
            print("\n3️⃣ Custom Output Generation")
            
            # Create custom output directory
            output_dir = Path("advanced_output")
            output_dir.mkdir(exist_ok=True)
            
            # Generate outputs with custom names
            pdf_path = output_dir / "invoice_searchable.pdf"
            boxes_path = output_dir / "invoice_analysis.jpg"
            
            pdf_result = ocr_custom.create_searchable_pdf(
                image_path, ocr_result, str(pdf_path)
            )
            
            boxes_result = ocr_custom.draw_bounding_boxes(
                image_path, ocr_result, str(boxes_path)
            )
            
            # Example 4: Save OCR results as JSON
            print("\n4️⃣ Export OCR Results")
            
            results_data = {
                'image_path': image_path,
                'total_blocks': len(texts),
                'average_confidence': sum(scores) / len(scores),
                'texts_and_scores': [
                    {
                        'text': text,
                        'confidence': float(score),
                        'bbox': [float(x) for x in box[:4]] if len(box) >= 4 else box
                    }
                    for text, score, box in zip(texts, scores, boxes)
                ],
                'high_confidence_texts': high_conf_texts,
                'extracted_text': ' '.join(texts)
            }
            
            json_path = output_dir / "ocr_results.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(results_data, f, indent=2, ensure_ascii=False)
            
            print(f"   💾 OCR results saved as JSON: {json_path}")
            
            # Example 5: Text filtering and processing
            print("\n5️⃣ Text Analysis")
            
            # Filter by confidence
            reliable_texts = [text for text, score in zip(texts, scores) if score > 0.8]
            print(f"   🔍 Reliable texts (>0.8 confidence): {len(reliable_texts)}")
            
            # Find numeric values
            import re
            numeric_texts = [text for text in texts if re.search(r'\d+', text)]
            print(f"   🔢 Texts containing numbers: {len(numeric_texts)}")
            
            # Find potential currency amounts
            currency_pattern = r'[\$€£¥]\s*\d+(?:\.\d{2})?'
            currency_texts = [text for text in texts if re.search(currency_pattern, text)]
            print(f"   💰 Potential currency amounts: {currency_texts}")
            
            print(f"\n🎉 Advanced processing completed!")
            print(f"📁 All outputs saved to: {output_dir}")

def error_handling_example():
    """Demonstrate error handling"""
    
    print("\n🛡️ Error Handling Example")
    print("=" * 40)
    
    ocr = OCRProcessor(verbose=False)  # Quiet mode for error demo
    
    # Test with non-existent file
    print("Testing with non-existent file...")
    result = ocr.process_image("non_existent_image.jpg")
    if result is None:
        print("✅ Gracefully handled missing file")
    
    # Test with invalid file
    print("Testing with invalid image file...")
    with open("test.txt", "w") as f:
        f.write("This is not an image")
    
    result = ocr.process_image("test.txt")
    if result is None:
        print("✅ Gracefully handled invalid image")
    
    # Clean up
    Path("test.txt").unlink(missing_ok=True)

def main():
    """Main function"""
    try:
        advanced_ocr_example()
        error_handling_example()
        
    except KeyboardInterrupt:
        print("\n❌ Processing interrupted by user")
    except Exception as e:
        print(f"\n❌ Error in advanced example: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()