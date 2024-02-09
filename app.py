from flask import Flask, render_template, request, jsonify
from Brain import search
from traning_set import get_response
def load_qa_data(file_path):
    qa_dict = {}
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            if len(parts) != 2:
                continue
            q, a = parts
            qa_dict[q] = a
    return qa_dict

qa_file_path = r"F:\J.A.R.V.I.S\DATA\BRAIN_DATA\QNQ_DATA\qna.txt"
qa_dict = load_qa_data(qa_file_path)

keywords = ["what is", "who is", "tell me", "teach me", "who are",
            "where is", "how to", "explain", "define", "describe",
            "show", "demonstrate", "educate", "enlighten", "clarify",
            "elaborate", "illustrate", "inform", "reveal", "uncover",
            "introduce", "discuss", "expound", "unveil", "present",
            "outline", "interpret", "instruct", "guide", "advise",
            "inform", "educate", "narrate", "depict", "portray",
            "detail", "mention", "enumerate", "elucidate", "enumerate",
            "brief", "communicate", "convey", "disclose", "decipher",
            "unravel", "unmask", "unfold", "shed light on", "throw light on",
            "shed insight on", "throw insight on", "shed clarity on", "throw clarity on",
            "shed knowledge on", "throw knowledge on", "shed information on", "throw information on",
            "shed understanding on", "throw understanding on", "shed perspective on", "throw perspective on",
            "shed awareness on", "throw awareness on", "shed light upon", "throw light upon",
            "shed insight upon", "throw insight upon", "shed clarity upon", "throw clarity upon",
            "shed knowledge upon", "throw knowledge upon", "shed information upon", "throw information upon",
            "shed understanding upon", "throw understanding upon", "shed perspective upon", "throw perspective upon",
            "shed awareness upon", "throw awareness upon", "shed light", "throw light",
            "shed insight", "throw insight", "shed clarity", "throw clarity",
            "shed knowledge", "throw knowledge", "shed information", "throw information",
            "shed understanding", "throw understanding", "shed perspective", "throw perspective",
            "shed awareness", "throw awareness", "explain to me", "teach me about",
            "define for me", "clarify for me", "elaborate on", "illustrate for me",
            "inform me about", "reveal to me", "uncover for me", "introduce to me",
            "discuss with me", "expound on", "unveil for me", "present to me",
            "outline for me", "interpret for me", "instruct me on", "guide me through",
            "advise me on", "narrate to me", "depict for me", "portray for me",
            "detail for me", "mention to me", "enumerate for me", "elucidate for me",
            "enumerate for me", "brief me on", "communicate to me", "convey to me",
            "disclose to me", "decipher for me", "unravel for me", "unmask for me",
            "unfold for me", "explain to me", "teach me about", "define for me",
            "clarify for me", "elaborate on", "illustrate for me", "inform me about",
            "reveal to me", "uncover for me", "introduce to me", "discuss with me",
            "expound on", "unveil for me", "present to me", "outline for me",
            "interpret for me", "instruct me on", "guide me through", "advise me on",
            "inform me about", "educate me on", "narrate to me", "depict for me",
            "portray for me", "detail for me", "mention to me", "enumerate for me",
            "elucidate for me", "enumerate for me", "brief me on", "communicate to me",
            "convey to me", "disclose to me", "decipher for me", "unravel for me",
            "unmask for me", "unfold for me"]



app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        user_input = request.form['userInput']
        result = deep_search(user_input)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})


def deep_search(user_input):
    try:
        if user_input in qa_dict:
            result = qa_dict[user_input]
            return result
        elif any(user_input.startswith(keyword) for keyword in keywords):
            result = search(user_input)
            return result
        else:
            result = get_response(user_input)
            return result

    except Exception as e:
        x = print("sorry ! i don't know that")
        return x


if __name__ == '__main__':
    app.run(debug=True)
