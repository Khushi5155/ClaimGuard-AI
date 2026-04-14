function ResultCard({ data }) {
  const { claims, final_result, source_info } = data;

  const score = final_result?.truth_score || 0;

  // Color based on score
  const getColor = () => {
    if (score > 75) return "bg-green-500";
    if (score > 50) return "bg-yellow-500";
    return "bg-red-500";
  };

  return (
    <div className="bg-white p-6 mt-6 rounded-2xl shadow-lg w-full max-w-xl">

      {/* Title */}
      <h2 className="text-xl font-semibold mb-4">Analysis Result</h2>

      {/* Score */}
      <div className="mb-4">
        <p className="font-semibold">Truth Score: {score}%</p>
        <div className="w-full bg-gray-200 rounded-full h-4 mt-2">
          <div
            className={`${getColor()} h-4 rounded-full transition-all duration-500`}
            style={{ width: `${score}%` }}
          ></div>
        </div>
      </div>

      {/* Verdict */}
      <p className="mb-3">
        <strong>Verdict:</strong>{" "}
        <span className="font-semibold">
          {final_result?.verdict}
        </span>
      </p>

      {/* Claims */}
      <div className="mb-3">
        <p className="font-semibold">Claims:</p>
        <ul className="list-disc ml-5">
          {claims?.map((c, i) => (
            <li key={i}>{c}</li>
          ))}
        </ul>
      </div>

      {/* Reasons */}
      <div className="mb-3">
        <p className="font-semibold">Reasons:</p>
        <ul className="list-disc ml-5">
          {final_result?.reasons?.map((r, i) => (
            <li key={i}>{r}</li>
          ))}
        </ul>
      </div>

      {/* Source */}
      {source_info?.source && (
        <p className="mt-3">
          <strong>Source:</strong>{" "}
          {source_info.source} ({source_info.source_score})
        </p>
      )}
    </div>
  );
}

export default ResultCard;
