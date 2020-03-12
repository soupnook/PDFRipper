# PDFRipper

---

Simple program pipeline in order to extract information out of a PDF

Done by splitting PDF into individual page JPGs using pillow and then running tesseract OCR on them. This is then put under either manual classification or NLP to derive meaning.
The following is then structured into a database-worthy format.