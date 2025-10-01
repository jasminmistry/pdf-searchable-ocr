#!/usr/bin/env python3
"""
Test the new OCRProcessor class
"""

from py_ocr import OCRProcessor

def test_class_functionality():
    """Test the OCRProcessor class"""
    
    print("🧪 Testing OCRProcessor class...")
    
    # Initialize processor
    ocr = OCRProcessor(lang='en', verbose=True)
    
    # Download sample image
    image_path = ocr.download_sample_image()
    
    if image_path:
        # Test complete workflow
        results = ocr.process_and_generate_all(image_path, "class_test")
        
        if results['searchable_pdf']:
            print("✅ Class-based approach working perfectly!")
            return True
        else:
            print("❌ Class-based approach failed")
            return False
    else:
        print("❌ Could not download sample image")
        return False

if __name__ == "__main__":
    success = test_class_functionality()
    if success:
        print("\n🎉 Package is ready for publishing!")
    else:
        print("\n❌ Package needs debugging before publishing")