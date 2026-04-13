import { useState } from "react";
import InputForm from "./components/InputForm";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6">
      <h1 className="text-4xl font-bold mb-2">TruthLens 🔍</h1>
      <p className="text-gray-600 mb-6 text-center">
        Offline AI-based Fake News Verification System
      </p>

      <InputForm setResult={setResult} />

      {result && (
        <pre className="mt-6 bg-black text-green-400 p-4 rounded-lg w-full max-w-xl overflow-x-auto text-sm">
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}

export default App;
