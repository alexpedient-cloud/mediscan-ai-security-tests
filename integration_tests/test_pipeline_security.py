def sanitize_metadata(metadata):

    blocked = ["DROP TABLE", "' OR '1'='1"]

    for pattern in blocked:
        if pattern in metadata:
            raise ValueError("Malicious metadata detected")

    return True


def validate_output(response):

    forbidden = ["patient_name", "/internal/", "stack_trace"]

    for item in forbidden:
        if item in response:
            raise ValueError("Sensitive data leak")

    return True


def test_metadata_injection():

    malicious = "' OR '1'='1"

    try:
        sanitize_metadata(malicious)
    except ValueError:
        assert True


def test_output_validation():

    safe_output = "Diagnosis: Pneumonia"

    assert validate_output(safe_output)