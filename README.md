# PaddleOCR Python Project

# pdf-searchable-ocr

A simple and powerful Python package for Optical Character Recognition (OCR) with searchable PDF generation using PaddleOCR.

## Features

- 🔍 **High-accuracy OCR** using PaddleOCR
- 📄 **Searchable PDF generation** with invisible text layers
- 🎨 **Bounding box visualization** for OCR results
- 🌍 **Multi-language support** (80+ languages)
- ⚡ **GPU acceleration** support
- 🔧 **Simple class-based API**
- 📦 **Easy installation and usage**

## Installation

### Using pip (recommended)

```bash
pip install pdf-searchable-ocr
```

### Using uv (for development)

```bash
git clone <repository-url>
cd pdf-searchable-ocr
uv sync
```

## Quick Start

### Basic Usage

```python
from py_ocr import OCRProcessor

# Initialize the OCR processor
ocr = OCRProcessor(lang='en', verbose=True)

# Process an image
ocr_result = ocr.process_image('path/to/your/image.jpg')

# Create a searchable PDF
pdf_path = ocr.create_searchable_pdf('path/to/your/image.jpg', ocr_result)

# Draw bounding boxes for visualization
boxed_image = ocr.draw_bounding_boxes('path/to/your/image.jpg', ocr_result)

print(f"Searchable PDF created: {pdf_path}")
print(f"Image with bounding boxes: {boxed_image}")
```

### Complete Workflow

```python
from py_ocr import OCRProcessor

# Initialize processor
ocr = OCRProcessor(lang='en', use_gpu=False, verbose=True)

# Process image and generate all outputs
results = ocr.process_and_generate_all('invoice.jpg', output_prefix='invoice_processed')

if results['searchable_pdf']:
    print(f"✅ Searchable PDF: {results['searchable_pdf']}")
if results['boxed_image']:
    print(f"✅ Visualization: {results['boxed_image']}")
```

### Using Sample Images

```python
from py_ocr import OCRProcessor

# Initialize processor
ocr = OCRProcessor()

# Download a sample image for testing
image_path = ocr.download_sample_image()

# Process the sample image
results = ocr.process_and_generate_all(image_path)
```

## API Reference

### OCRProcessor Class

#### `__init__(lang='en', use_gpu=False, verbose=True, **kwargs)`

Initialize the OCR processor.

**Parameters:**
- `lang` (str): Language for OCR recognition (default: 'en')
- `use_gpu` (bool): Whether to use GPU acceleration (default: False)
- `verbose` (bool): Whether to print verbose output (default: True)
- `**kwargs`: Additional arguments passed to PaddleOCR

#### `process_image(image_path: str) -> Dict[str, Any]`

Perform OCR on an image.

**Parameters:**
- `image_path` (str): Path to the image file

**Returns:**
- `dict`: OCR results containing texts, scores, and bounding boxes
- `None`: If OCR failed

#### `create_searchable_pdf(image_path: str, ocr_result: dict, output_pdf: str) -> str`

Create a searchable PDF with invisible text layers.

**Parameters:**
- `image_path` (str): Path to the source image
- `ocr_result` (dict): OCR results from `process_image()`
- `output_pdf` (str): Output PDF filename (default: "searchable_output.pdf")

**Returns:**
- `str`: Path to the created PDF
- `None`: If creation failed

#### `draw_bounding_boxes(image_path: str, ocr_result: dict, output_image: str) -> str`

Draw bounding boxes on the image to visualize OCR detection.

**Parameters:**
- `image_path` (str): Path to the source image
- `ocr_result` (dict): OCR results from `process_image()`
- `output_image` (str): Output image filename (default: "image_with_boxes.jpg")

**Returns:**
- `str`: Path to the image with bounding boxes
- `None`: If creation failed

#### `process_and_generate_all(image_path: str, output_prefix: str) -> dict`

Complete workflow: OCR + Searchable PDF + Bounding Box Image.

**Parameters:**
- `image_path` (str): Path to the input image
- `output_prefix` (str): Prefix for output files (default: "output")

**Returns:**
- `dict`: Dictionary containing paths to all generated files

## Supported Languages

pdf-searchable-ocr supports 80+ languages through PaddleOCR. Some popular ones include:

- `en` - English
- `ch` - Chinese (Simplified)
- `french` - French
- `german` - German
- `korean` - Korean
- `japan` - Japanese
- `it` - Italian
- `xi` - Spanish
- `ru` - Russian
- `ar` - Arabic

For the complete list, see [PaddleOCR documentation](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_en/multi_languages_en.md).

## Advanced Configuration

### GPU Acceleration

```python
# Enable GPU acceleration (requires CUDA)
ocr = OCRProcessor(lang='en', use_gpu=True)
```

### Custom PaddleOCR Settings

```python
# Pass additional PaddleOCR parameters
ocr = OCRProcessor(
    lang='en',
    use_angle_cls=True,              # Enable angle classification
    use_textline_orientation=True,   # Enable text line orientation
    det_model_dir='custom/det/path', # Custom detection model
    rec_model_dir='custom/rec/path'  # Custom recognition model
)
```

### Batch Processing

```python
from py_ocr import OCRProcessor
import os

ocr = OCRProcessor(lang='en')

# Process multiple images
image_folder = 'path/to/images'
for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        image_path = os.path.join(image_folder, filename)
        results = ocr.process_and_generate_all(image_path, f"output_{filename}")
        print(f"Processed: {filename}")
```

## Output Examples

### Console Output
```
🔧 Initializing OCR engine with language: en
✅ OCR engine initialized successfully
📁 Using existing sample image: sample_image.jpg
🔍 Processing image: sample_image.jpg
📊 Text blocks detected: 48 | Average confidence: 0.984
✅ Searchable PDF saved as: output_searchable.pdf
🎨 Drawing 48 bounding boxes on image...
✅ Image with bounding boxes saved as: output_with_boxes.jpg
```

### Generated Files
- `output_searchable.pdf` - Searchable PDF with invisible text layers
- `output_with_boxes.jpg` - Original image with colored bounding boxes

## Requirements

- Python >= 3.8
- PaddleOCR >= 2.7.0
- OpenCV >= 4.0
- ReportLab >= 4.0
- Pillow >= 8.0

## Installation from Source

```bash
# Clone the repository
git clone <repository-url>
cd pdf-searchable-ocr

# Install with uv (recommended for development)
uv sync

# Or install with pip
pip install -e .
```

## Development

### Running Tests
```bash
uv run python -m pytest tests/
```

### Code Formatting
```bash
uv run black py_ocr/
uv run isort py_ocr/
```

### Type Checking
```bash
uv run mypy py_ocr/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) for the excellent OCR engine
- [ReportLab](https://www.reportlab.com/) for PDF generation capabilities
- [OpenCV](https://opencv.org/) for image processing

## Changelog

### v0.1.0
- Initial release
- Basic OCR functionality
- Searchable PDF generation
- Bounding box visualization
- Multi-language support

## Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

## Roadmap

- [ ] Web interface for easy usage
- [ ] Batch processing CLI tool
- [ ] Docker container
- [ ] Additional output formats (Excel, Word)
- [ ] OCR result caching
- [ ] Performance optimizations

## Features

- Text detection and recognition using PaddleOCR
- Support for multiple languages (English by default)
- Automatic sample image download for testing
- Confidence scoring for OCR results
- Clean output formatting

## Prerequisites

- Python 3.12 or higher
- uv package manager

## Installation

1. Clone or navigate to the project directory:
```bash
cd py-ocr
```

2. Install dependencies using uv:
```bash
uv sync
```

## Usage

### Basic Demo
Run the main OCR demonstration:
```bash
uv run python main.py
```
This downloads a sample image and demonstrates OCR capabilities.

### Quick OCR for Any Image
Process your own images:
```bash
uv run python quick_ocr.py path/to/your/image.jpg
uv run python quick_ocr.py document.png en
```

### Command-line OCR Tool
For more detailed results:
```bash
uv run python ocr_custom.py image.jpg
uv run python ocr_custom.py image.jpg en output.txt
```

### Batch Processing
Process multiple images at once:
```bash
uv run python batch_ocr.py ./images_folder
uv run python batch_ocr.py ./images ./results
```

## Project Structure

```
pdf-searchable-ocr/
├── main.py           # Main OCR demonstration with sample image
├── quick_ocr.py      # Simple script to OCR any image file
├── ocr_custom.py     # Command-line OCR tool for single images
├── batch_ocr.py      # Batch processing script for multiple images
├── pyproject.toml    # Project configuration and dependencies
├── README.md         # This file
├── sample_image.jpg  # Downloaded sample image (created on first run)
└── .venv/           # Virtual environment (created by uv)
```

## Dependencies

- `paddlepaddle`: Deep learning framework
- `paddleocr`: OCR toolkit based on PaddlePaddle
- `pillow`: Python Imaging Library

## Customization

You can modify the `main.py` file to:
- Use different languages (change `lang='en'` parameter)
- Process your own images (replace the image path)
- Adjust OCR parameters for better accuracy
- Add image preprocessing steps

## Supported Languages

PaddleOCR supports many languages. Some common ones:
- `en`: English
- `ch`: Chinese
- `fr`: French
- `de`: German
- `ko`: Korean
- `ja`: Japanese

For a full list, check the [PaddleOCR documentation](https://github.com/PaddlePaddle/PaddleOCR).