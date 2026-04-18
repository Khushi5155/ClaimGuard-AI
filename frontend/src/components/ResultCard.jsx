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
    <div className="bg-gray-900 p-6 mt-6 rounded-2xl shadow-xl border border-gray-800 w-full max-w-2xl">

      {/* Header */}
      <h2 className="text-2xl font-bold mb-4">Analysis Result</h2>

      {/* Score Section */}
      <div className="grid grid-cols-2 gap-4 mb-6">

  <div className="bg-gray-800 p-4 rounded-xl">
    <p className="text-gray-400 text-sm">Truth Score</p>
    <p className="text-2xl font-bold">{score}%</p>
  </div>

  <div className="bg-gray-800 p-4 rounded-xl">
    <p className="text-gray-400 text-sm">Verdict</p>
    <p className={`text-lg font-bold ${getTextColor()}`}>
      {final_result?.verdict}
    </p>
  </div>

</div>

      <div className="mb-6 flex justify-between text-sm">
        <span>Total: {data.claim_summary?.total}</span>
        <span className="text-green-600">
          Real: {data.claim_summary?.real}
        </span>
        <span className="text-red-600">
          Fake: {data.claim_summary?.fake}
        </span>
      </div>

      {/* Verdict */}
      <div className="mb-6">
        <p className="font-semibold text-lg">Verdict:</p>
        <p className={`text-xl font-bold ${getTextColor()}`}>
          {final_result?.verdict}
        </p>
      </div>

      <div className="mb-6">
        <p className="font-semibold mb-2">Claim Analysis</p>

        <div className="space-y-3">
          {data.analysis?.map((item, i) => (
            <div key={i} className="bg-gray-100 p-3 rounded-lg">

              <p className="font-medium">{item.claim}</p>

              <p className="text-sm text-gray-600">
                Match: {item.best_match}
              </p>

              <p className={`text-sm font-semibold ${item.status === "Likely Real"
                ? "text-green-600"
                : item.status === "Uncertain"
                  ? "text-yellow-600"
                  : "text-red-600"
                }`}>
                {item.status} ({(item.similarity_score * 100).toFixed(1)}%)
              </p>

            </div>
          ))}
        </div>
      </div>

      <div className="mb-6">
        <p className="font-semibold mb-2">Evidence (Wikipedia)</p>

        <div className="space-y-3">
          {data.evidence?.map((item, i) => (
            <div key={i} className="bg-gray-50 p-3 rounded-lg">

              <p className="font-medium">{item.claim}</p>

              {item.evidence ? (
                <>
                  <p className="text-sm text-blue-600">
                    {item.evidence.title}
                  </p>
                  <p className="text-sm text-gray-600">
                    {item.evidence.evidence}
                  </p>
                </>
              ) : (
                <p className="text-sm text-red-500">
                  No evidence found
                </p>
              )}

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
