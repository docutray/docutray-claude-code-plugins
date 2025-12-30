"""Document Loader - Extract text from various file formats."""

import os
import base64
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


class DocumentLoader:
    """Load and extract text from various document formats."""

    SUPPORTED_EXTENSIONS = {".pdf", ".md", ".txt", ".markdown", ".rst", ".json"}

    def __init__(self, use_mistral_ocr: bool = True):
        """
        Initialize document loader.

        Args:
            use_mistral_ocr: Whether to use Mistral API for PDF OCR
        """
        self.use_mistral_ocr = use_mistral_ocr
        self._mistral_client = None

    @property
    def mistral_client(self):
        """Lazy initialization of Mistral client."""
        if self._mistral_client is None and self.use_mistral_ocr:
            api_key = os.getenv("MISTRAL_API_KEY")
            if api_key:
                from mistralai import Mistral
                self._mistral_client = Mistral(api_key=api_key)
        return self._mistral_client

    def load(self, file_path: str) -> tuple[str, str]:
        """
        Load document and extract text.

        Args:
            file_path: Path to document file

        Returns:
            Tuple of (extracted_text, file_type)

        Raises:
            ValueError: If file type is not supported
            FileNotFoundError: If file doesn't exist
        """
        path = Path(file_path).resolve()

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        ext = path.suffix.lower()

        if ext not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {ext}. "
                f"Supported: {', '.join(self.SUPPORTED_EXTENSIONS)}"
            )

        if ext == ".pdf":
            text = self._load_pdf(path)
        elif ext in {".md", ".markdown", ".txt", ".rst"}:
            text = self._load_text(path)
        elif ext == ".json":
            text = self._load_json(path)
        else:
            text = self._load_text(path)

        return text, ext.lstrip(".")

    def _load_text(self, path: Path) -> str:
        """Load plain text file."""
        return path.read_text(encoding="utf-8", errors="ignore")

    def _load_json(self, path: Path) -> str:
        """Load JSON file as formatted text."""
        import json
        data = json.loads(path.read_text(encoding="utf-8"))
        return json.dumps(data, indent=2)

    def _load_pdf(self, path: Path) -> str:
        """
        Load PDF file using Mistral OCR or pypdf fallback.

        Mistral OCR is preferred for scanned documents and complex layouts.
        pypdf is used as fallback for text-based PDFs.
        """
        # Try Mistral OCR first if available
        if self.use_mistral_ocr and self.mistral_client:
            try:
                return self._load_pdf_mistral(path)
            except Exception as e:
                print(f"Mistral OCR failed, falling back to pypdf: {e}")

        # Fallback to pypdf
        return self._load_pdf_pypdf(path)

    def _load_pdf_mistral(self, path: Path) -> str:
        """Load PDF using Mistral AI OCR API."""
        # Read and encode PDF
        pdf_bytes = path.read_bytes()
        base64_pdf = base64.standard_b64encode(pdf_bytes).decode("utf-8")

        # Call Mistral OCR
        response = self.mistral_client.ocr.process(
            model="mistral-ocr-latest",
            document={
                "type": "document_url",
                "document_url": f"data:application/pdf;base64,{base64_pdf}",
            },
        )

        # Extract text from all pages
        pages_text = []
        for page in response.pages:
            pages_text.append(page.markdown)

        return "\n\n---\n\n".join(pages_text)

    def _load_pdf_pypdf(self, path: Path) -> str:
        """Load PDF using pypdf library."""
        from pypdf import PdfReader

        reader = PdfReader(path)
        pages_text = []

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                pages_text.append(f"[Page {i + 1}]\n{text}")

        return "\n\n".join(pages_text)

    def get_title_from_file(self, file_path: str) -> str:
        """Extract a title from filename."""
        path = Path(file_path)
        # Remove extension and clean up
        name = path.stem
        # Replace common separators with spaces
        name = name.replace("_", " ").replace("-", " ")
        # Title case
        return name.title()

    @classmethod
    def is_supported(cls, file_path: str) -> bool:
        """Check if file type is supported."""
        ext = Path(file_path).suffix.lower()
        return ext in cls.SUPPORTED_EXTENSIONS
