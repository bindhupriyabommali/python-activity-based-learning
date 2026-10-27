def compress_text(text):
    if not text:
        return ""

    compressed = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1

    compressed += text[-1] + str(count)

    print("Original Text:", text)
    print("Original Length:", len(text))

    if len(compressed) < len(text):
        print("Compressed Text:", compressed)
        print("Compressed Length:", len(compressed))
    else:
        print("Compressed Text:", text)
        print("Compressed Length:", len(text))
        print("Compression is not beneficial.")

# Input
text = input("Enter a string: ")
compress_text(text)
