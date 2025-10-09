import tkinter as tk
from tkinter import filedialog, scrolledtext

def read_fasta_sequence(filepath):
    sequences = []
    current_seq = ""
    with open(filepath, "r") as file:
        for line in file:
            if line.startswith(">"):
                if current_seq:
                    sequences.append(current_seq)
                    current_seq = ""
            else:
                current_seq += line.strip()
        if current_seq:
            sequences.append(current_seq)
    return sequences

def show_sequences_info(S, idx):
    alphabet = set(S)
    length = len(S)
    result = f"Sequence {idx+1}:\n"
    result += f"Alphabet: {alphabet}\n"
    for c in alphabet:
        percent = (S.count(c) / length) * 100
        result += f"{c} percentage: {percent:.2f}%\n"
    result += "\n"
    return result

def analyze_fasta():
    filepath = filedialog.askopenfilename(
        title="Select FASTA file",
        filetypes=[("FASTA files", "*.fasta *.fa")]
    )
    if filepath:
        sequences = read_fasta_sequence(filepath)
        output_text.delete(1.0, tk.END)  # clear previous results
        for idx, seq in enumerate(sequences):
            info = show_sequences_info(seq, idx)
            output_text.insert(tk.END, info)

root = tk.Tk()
root.title("FASTA Sequence Analyzer")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

btn = tk.Button(frame, text="Choose FASTA File", command=analyze_fasta)
btn.pack(pady=5)

output_text = scrolledtext.ScrolledText(frame, width=60, height=20, wrap=tk.WORD)
output_text.pack(pady=5)

root.mainloop()