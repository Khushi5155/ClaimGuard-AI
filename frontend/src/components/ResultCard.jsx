function ResultCard({ data }) {
  const { claims, final_result, source_info } = data;

  const score = final_result?.truth_score || 0;

  // Dynamic color
  const getColor = () => {
    if (score > 75) return "bg-green-500";
    if (score > 50) return "bg-yellow-500";
    return "bg-red-500";
  };

  const getTextColor = () => {
    if (score > 75) return "text-green-600";
    if (score > 50) return "text-yellow-600";
    return "text-red-600";
  };

  return (
    <div className="bg-white p-6 mt-6 rounded-2xl shadow-xl w-full max-w-2xl">

      {/* Header */}
      <h2 className="text-2xl font-bold mb-4">Analysis Result</h2>

      {/* Score Section */}
      <div className="mb-6">
        <div className="flex justify-between items-center">
          <p className="font-semibold">Truth Score</p>
          <p className={`font-bold ${getTextColor()}`}>{score}%</p>
        </div>

        <div className="w-full bg-gray-200 rounded-full h-4 mt-2">
          <div
            className={`${getColor()} h-4 rounded-full transition-all duration-700`}
            style={{ width: `${score}%` }}
          ></div>
        </div>
      </div>

      {/* Verdict */}
      <div className="mb-6">
        <p className="font-semibold text-lg">Verdict:</p>
        <p className={`text-xl font-bold ${getTextColor()}`}>
          {final_result?.verdict}
        </p>
      </div>

      {/* Claims */}
      <div className="mb-6">
        <p className="font-semibold mb-2">Extracted Claims</p>
        <div className="space-y-2">
          {claims?.map((c, i) => (
            <div
              key={i}
              className="bg-gray-100 p-3 rounded-lg text-sm"
            >
              {c}
            </div>
          ))}
        </div>
      </div>

      {/* Reasons */}
      <div className="mb-6">
        <p className="font-semibold mb-2">Why this result?</p>
        <div className="flex flex-wrap gap-2">
          {final_result?.reasons?.map((r, i) => (
            <span
              key={i}
              className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm"
            >
              {r}
            </span>
          ))}
        </div>
      </div>

      {/* Source */}
      {source_info?.source && (
        <div className="mt-4 p-3 bg-gray-50 rounded-lg">
          <p className="font-semibold">Source Info</p>
          <p className="text-sm">
            {source_info.source} → Credibility Score:{" "}
            <span className="font-bold">
              {source_info.source_score}
            </span>
          </p>
        </div>
      )}
    </div>
  );
}

export default ResultCard;
