from extractive import extractive_summary
from abstractive import abstractive_summary

def load_texts(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        texts = f.readlines()
    return [t.strip() for t in texts if len(t.strip()) > 50]

def compare(text):
    print("\n" + "="*60)
    print("📄 Original Text:\n", text)

    ext = extractive_summary(text)
    abs_sum = abstractive_summary(text)

    print("\n🔹 Extractive Summary:\n", ext)
    print("\n🔹 Abstractive Summary:\n", abs_sum)

    print("\n📊 Comparison:")
    print("Extractive → More factual, uses original sentences")
    print("Abstractive → More human-like, may paraphrase")

def menu():
    print("\n💻 TEXT SUMMARIZER")
    print("1. Use Sample Texts")
    print("2. Enter Custom Text")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        texts = load_texts("sample_texts.txt")
        for t in texts[:5]:
            compare(t)

    elif choice == '2':
        text = input("\nEnter your text:\n")
        compare(text)

    elif choice == '3':
        print("Exiting...")
        exit()

    else:
        print("Invalid choice")

if __name__ == "__main__":
    while True:
        menu()