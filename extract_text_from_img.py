import boto3
import sys
import os

def extract_text_from_image(image_path, output_path='output.txt'):
    # Initialize Textract client
    textract = boto3.client('textract')

    # Open image file
    with open(image_path, 'rb') as document:
        image_bytes = document.read()

    # Call Amazon Textract
    response = textract.detect_document_text(Document={'Bytes': image_bytes})

    # Extract detected text
    text_lines = []
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            text_lines.append(item["Text"])

    # Save extracted text to a file
    with open(output_path, 'w') as output_file:
        output_file.write('\n'.join(text_lines))

    print(f"Text extracted successfully. Check the file: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_text.py <image-path>")
        sys.exit(1)

    image_path = sys.argv[1]

    if not os.path.isfile(image_path):
        print(f"Error: File '{image_path}' does not exist.")
        sys.exit(1)

    extract_text_from_image(image_path)
