import { useState } from "react";
import { analyzeNews } from "../services/api";

function InputForm({ setResult }) {
  const [text, setText] = useState("");
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    // 🛑 Validation
    if (!text.trim()) {
      alert("Please enter news text");
      return;
    }

    try {
      setLoading(true);

      const data = await analyzeNews({ text, url });

      setResult(data);
    } catch (err) {
      alert("Server error. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-gray-900 p-6 rounded-2xl shadow-lg border border-gray-800 w-full max-w-xl">
      <h2 className="text-xl font-semibold mb-4">Analyze News</h2>

      <textarea
        placeholder="Enter news text..."
        className="w-full p-3 border rounded-lg mb-3 focus:outline-none focus:ring-2 focus:ring-blue-400"
        rows="4"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <input
        type="text"
        placeholder="Enter URL (optional)"
        className="w-full p-3 border rounded-lg mb-3 focus:outline-none focus:ring-2 focus:ring-blue-400"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />

      <button
        onClick={handleSubmit}
        disabled={loading}
        className={`w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white py-2 rounded-lg hover:opacity-90 transition ${
       
          loading
            ? "bg-gray-400 cursor-not-allowed"
            : "bg-blue-600 hover:bg-blue-700"
        }`}
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </div>
  );
}

export default InputForm;
