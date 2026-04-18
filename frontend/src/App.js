import { useState } from "react";
import InputForm from "./components/InputForm";
import ResultCard from "./components/ResultCard";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-gray-950 text-white">

      {/* NAVBAR */}
      <nav className="flex justify-between items-center px-8 py-4 border-b border-gray-800">
        <h1 className="text-xl font-bold text-blue-400">
          ClaimGuard AI
        </h1>
        <p className="text-sm text-gray-400">
          Fake News Detection System
        </p>
      </nav>

      {/* MAIN */}
      <div className="flex flex-col items-center px-4 py-10">

        <h2 className="text-4xl font-bold mb-4 text-center">
          Verify News with AI 🔍
        </h2>

        <p className="text-gray-400 mb-8 text-center max-w-xl">
          Analyze claims, check credibility, and get real-world evidence with explainable AI.
        </p>

        <InputForm setResult={setResult} />

        {result && <ResultCard data={result} />}

      </div>
    </div>
  );
}

export default App;
