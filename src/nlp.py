import json
import difflib

# Load QA pairs from JSON file
def load_qa(path="../data/qa_pairs.json"):
    with open(path, "r", encoding="utf-8") as f:
        qa_pairs = json.load(f)
    return qa_pairs

# Find the closest question match
def find_best_match(text, qa_pairs):
    questions = list(qa_pairs.keys())
    best_match = difflib.get_close_matches(text.lower(), questions, n=1, cutoff=0.5)
    if best_match:
        return qa_pairs[best_match[0]]
    else:
        return "Munyihanganire ntago ndi ku byumva neza mwasubiramo ?"

# Main function for response logic
def get_response(text):
    qa_pairs = load_qa()
    return find_best_match(text, qa_pairs)
