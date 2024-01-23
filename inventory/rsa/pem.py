import base64


def encode_to_pem(data, pem_type):
    """
    Encode binary data to PEM format.

    Parameters:
    - data: Bytes-like object to be encoded.
    - pem_type: A string specifying the type of PEM block (e.g., "CERTIFICATE", "RSA PRIVATE KEY").

    Returns:
    - PEM-encoded string.
    """
    b64_data = base64.b64encode(data).decode('ascii')
    pem_block = f"-----BEGIN {pem_type}-----\n{insert_newlines(b64_data, 64)}\n-----END {pem_type}-----\n"
    return pem_block


def decode_from_pem(pem_data, pem_type):
    """
    Decode PEM-encoded data.

    Parameters:
    - pem_data: PEM-encoded string.
    - pem_type: A string specifying the type of PEM block (e.g., "CERTIFICATE", "RSA PRIVATE KEY").

    Returns:
    - Decoded bytes.
    """
    pem_data = pem_data.strip()
    start_marker = f"-----BEGIN {pem_type}-----"
    end_marker = f"-----END {pem_type}-----"

    start_idx = pem_data.find(start_marker)
    end_idx = pem_data.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        raise ValueError(f"Invalid PEM data. Could not find start or end marker for {pem_type}.")

    b64_data = pem_data[start_idx + len(start_marker):end_idx].replace('\n', '')
    decoded_data = base64.b64decode(b64_data)
    return decoded_data


def insert_newlines(s, line_length):
    """Insert newline characters into a string at specified intervals."""
    return '\n'.join(s[i:i + line_length] for i in range(0, len(s), line_length))


# Example usage:
data_to_encode = b"200@13"
pem_type = "PUBLIC KEY"
print(data_to_encode)
pem_encoded = encode_to_pem(data_to_encode, pem_type)
print("PEM Encoded:")
print(pem_encoded)

decoded_data = decode_from_pem(pem_encoded, pem_type)
print("\nDecoded Data:")
print(decoded_data.decode('utf-8'))
