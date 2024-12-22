from app.services.extraction_service import extract_financial_data

def test_extract_ebit():
    sample_text = "Revenue: 5000 EBIT: 1200 Net Income: 900"
    ocr_data = {"text": sample_text}
    result = extract_financial_data(ocr_data)
    assert "EBIT" in result
    assert result["EBIT"]["value"] == "1200"
    assert result["EBIT"]["confidence"] > 0.9
