import { useState } from "react";
import InputForm from "./components/InputForm";
import ResultCard from "./components/ResultCard";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6">
      
      {/* Header */}
      <h1 className="text-4xl font-bold mb-2">TruthLens 🔍</h1>
      <p className="text-gray-600 mb-6 text-center">
        Offline AI Fake News Verification System
      </p>

      {/* Input */}
      <InputForm setResult={setResult} />

      {/* Result */}
      {result && <ResultCard data={result} />}
      
    </div>
  );
}

export default App;
