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

### CLI Usage

The package also provides a command-line tool:

```bash
# Basic usage - creates searchable PDF only
pdf-searchable-ocr input.jpg

# Specify custom output PDF name
pdf-searchable-ocr input.jpg --output-pdf my_document.pdf

# Enable bounding box visualization
pdf-searchable-ocr input.jpg --bounding-boxes

# Full options with custom names
pdf-searchable-ocr invoice.jpg \
    --output-pdf invoice_searchable.pdf \
    --output-prefix invoice_processed \
    --bounding-boxes \
    --lang en
```

### Complete Workflow

```python
from py_ocr import OCRProcessor

# Initialize processor
ocr = OCRProcessor(lang='en', use_gpu=False, verbose=True)

# Process image with custom PDF name and bounding boxes enabled
results = ocr.process_and_generate_all(
    'invoice.jpg', 
    output_pdf='invoice_searchable.pdf',
    output_prefix='invoice_processed',
    bounding_boxes=True
)

if results['searchable_pdf']:
    print(f"✅ Searchable PDF: {results['searchable_pdf']}")
if results['boxed_image']:
    print(f"✅ Visualization: {results['boxed_image']}")

# Or use defaults (no bounding boxes)
results = ocr.process_and_generate_all('document.jpg')
```

### Using Sample Images

```python
from py_ocr import OCRProcessor

# Initialize processor
ocr = OCRProcessor()

# Download a sample image for testing
image_path = ocr.download_sample_image()

# Process with custom settings
results = ocr.process_and_generate_all(
    image_path,
    output_pdf='sample_searchable.pdf',
    output_prefix='sample',
    bounding_boxes=True  # Enable visualization
)
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

#### `process_and_generate_all(image_path: str, output_pdf: str, output_prefix: str, bounding_boxes: bool) -> dict`

Complete workflow: OCR + Searchable PDF + Optional Bounding Box Image.

**Parameters:**
- `image_path` (str): Path to the input image
- `output_pdf` (str): Output PDF filename (default: "searchable_output.pdf")
- `output_prefix` (str): Prefix for output files (default: "output")
- `bounding_boxes` (bool): Whether to generate bounding box visualization (default: False)

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

### Output Control

```python
# Control output files and features
ocr = OCRProcessor(lang='en')

# Minimal processing - only searchable PDF
results = ocr.process_and_generate_all(
    'document.jpg',
    output_pdf='my_document.pdf',
    bounding_boxes=False  # Skip visualization
)

# Full processing with custom names
results = ocr.process_and_generate_all(
    'invoice.jpg',
    output_pdf='invoice_searchable.pdf',
    output_prefix='invoice_analysis',
    bounding_boxes=True  # Include visualization
)

# Generated files:
# - invoice_searchable.pdf (searchable PDF)
# - invoice_analysis_with_boxes.jpg (visualization)
```

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
        base_name = os.path.splitext(filename)[0]
        
        # Process with custom output names
        results = ocr.process_and_generate_all(
            image_path, 
            output_pdf=f"searchable_{base_name}.pdf",
            output_prefix=f"processed_{base_name}",
            bounding_boxes=True  # Generate visualizations
        )
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
✅ Searchable PDF saved as: my_document.pdf
🎨 Drawing 48 bounding boxes on image...
✅ Image with bounding boxes saved as: output_with_boxes.jpg
```

### Generated Files
When using `bounding_boxes=True`:
- `my_document.pdf` - Searchable PDF with invisible text layers
- `output_with_boxes.jpg` - Original image with colored bounding boxes

When using `bounding_boxes=False` (default):
- `my_document.pdf` - Searchable PDF only (faster processing)

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